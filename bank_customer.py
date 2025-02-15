from user import User
from cn_bank_account import CNBankAccount
from formatbirthdate import validate_and_format_birthdate
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class BankCustomer(User):
    __users= {} 
    __usernames = {}
    __passwords ={}
    __pending_requests = []

    @classmethod
    def get_users(cls):
        return cls.__users
    
    @classmethod
    def update_users_list(cls, name):
        cls.__users[name] = name  

    @classmethod
    def remove_user(cls,name):
        if name in cls.__users:
            removed_user = cls.__users.pop(name)
            del cls.__usernames[removed_user.username]
            del cls.__passwords[removed_user.password]

    @classmethod
    def user_exists(cls, name):
        return name in cls.__users

    @classmethod
    def get_usernames(cls):
        return cls.__usernames  
    
    @classmethod
    def get_passwords(cls):
        return cls.__passwords
    
    @classmethod
    def get_pending_requests(cls):
        return cls.__pending_requests

    @classmethod
    def remove_pending_request(cls, customer):
        if customer in cls.__pending_requests:
            cls.__pending_requests.remove(customer)
    

    def __init__(self, fullname, username, password, birthdate, role, monthly_salary):
        self.__fullname = str(fullname)
        self.__birthdate = birthdate
        self.__role = str(role)
        self.__monthly_salary = float(monthly_salary)
        self.__bank_account = None
        self.__has_existing_loan = False
        self.__username = username
        self.__password = password
        BankCustomer.get_usernames()[username] = self 
        BankCustomer.get_passwords()[password] = self 
        self.requested_loan_amount = None 
        self.__status = None  
        self.loan_status = None
        self.check_request_account_status = None
        BankCustomer.__pending_requests.append(self)
        self.has_requested_lock = None
        self.has_requested_unlock = None

    @property
    def fullname(self):
        return self.__fullname
    
    @fullname.setter
    def fullname(self):
        pass
    
    @property
    def birthdate(self):
        return self.__birthdate
    
    @birthdate.setter
    def birthdate(self):
        pass
    
    @property
    def monthly_salary(self):
        return self.__monthly_salary
    
    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def bank_account(self):
        return self.__bank_account
    
    @bank_account.setter
    def bank_account(self, account):
        self.__bank_account = account

    @property
    def has_existing_loan(self):
        return self.__has_existing_loan

    @has_existing_loan.setter
    def has_existing_loan(self, value):
        self.__has_existing_loan = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self):
        pass

    def transact_with_admin(self, admin, bank_account, birthdate, amount, action):
        verified = admin.verify_birthdate(admin, bank_account, birthdate)
        if verified:
            if action == "Deposit":
                admin.customer_deposit(admin, self.bank_account, amount)
            elif action == "Withdraw":
                admin.customer_withdraw(admin, self.bank_account, amount)
            elif action == "Check Balance":
                admin.customer_check_balance(admin, self.bank_account)
        if not verified:
            CTkMessagebox(title="Verification Failed", message="Provided birthdate is incorrect.", icon="cancel", sound=True)

    def use_atm(self,amount, action):
        if action == "deposit":
            self.bank_account.deposit(amount, account_type = "Savings", source ='atm')
        elif action == "withdraw":
            self.bank_account.withdraw(amount, account_type = "Savings", source ='atm')
        elif action == "check balance":
            self.bank_account.check_balance()
    
    def atm_change_pin(self, old, new):
        self.bank_account.change_pin(old, new)
    
    def atm_check_pin(self, entered_pin):
        check_pin = self.bank_account.authenticate(entered_pin)
        if check_pin == (True, 0):
            return "Success"
        elif check_pin == (False, 3):
            return "Failed"
        else:
            return "Retry"

    def display_account_details(self):
        if self.bank_account:
            if self.bank_account.status == "Active":
                display_details = f"""
\nACCOUNT DETAILS:\n
Account Number: {self.bank_account.account_number}
Account Name: {self.bank_account._CNBankAccount__account_name}
Account Type: {self.bank_account._CNBankAccount__account_type}
Account Balance: {self.bank_account._CNBankAccount__balance}
Account PIN: {self.bank_account._CNBankAccount__pin}
Account Birthdate: {self.bank_account.birthdate}
Account Status: {self.bank_account.status}
"""
                CTkMessagebox(title="Account Approved!", message=display_details, icon="check", sound=True)
            else:
                CTkMessagebox(title="Account locked", message="Bank account details cannot be accessed at this time.", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="No Bank Account", message="No bank account details can be shown.", icon="cancel", sound=True)

    def update_account_request_status(self, status): 
            self.check_request_account_status = status

    def update_lock_request_status(self,status):
            self.has_requested_lock = status

    def update_unlock_request_status(self,status):
            self.has_requested_unlock = status
    
    def update_loan_application_status(self, status):
        self.loan_status = status

    def request_account(self):
        if not self.bank_account:
            CTkMessagebox(title="Success!", message="Account request made. \n\nPlease wait for the Bank Teller to process your account.", icon="check", sound=True)
            self.update_account_request_status("Pending") 
        else:
            CTkMessagebox(title="Error!", message="You already have a bank account.", icon="cancel", sound=True)

    def request_loan(self, amount):
        if self.__has_existing_loan:
            CTkMessagebox(title="Loan Application Status: Denied", message="You already have an existing loan.", icon="error", sound=True)
        elif self.loan_status == "Pending":
            CTkMessagebox(title="Loan Application Status: Pending", message="Loan application was successful. Kindly wait for the Bank Manager's approval.", icon="info", sound=True)
        else:
            self.requested_loan_amount = amount
            self.loan_status = "Pending"
            CTkMessagebox(title="Loan Application Status: Pending", message="Loan application was successful. Kindly wait for the Bank Manager's approval.", icon="info", sound=True)
            return self.requested_loan_amount