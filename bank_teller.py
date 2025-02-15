import uuid 
from user import User
from cn_bank_account import CNBankAccount 
from formatbirthdate import validate_and_format_birthdate
from bank_customer import BankCustomer      
from CTkMessagebox import CTkMessagebox

class BankTeller(User):
    __tellers = {}  
    __teller_count = 0
    
    @classmethod
    def get_tellers(cls):
        return cls.__tellers

    def __init__(self, fullname, username, password, birthdate, role, monthly_salary, is_admin=False, bank_account=None):
        self.__fullname = str(fullname)
        self.__birthdate = birthdate
        self.__role = str(role)
        self.__monthly_salary = float(monthly_salary)
        self.__username = username
        self.__password = password
        self.__is_admin = is_admin
        self.__bank_account = bank_account
        BankTeller.__teller_count += 1
        self.__teller_id = BankTeller.__teller_count
        BankTeller.get_tellers()[username] = self

    @property
    def bank_account(self):
        return self.__bank_account
    
    @bank_account.setter
    def bank_account(self, account):
        self.__bank_account = account
    
    @property
    def fullname(self):
        return self.__fullname
    
    @property
    def birthdate(self):
        return self.__birthdate
    
    @property
    def monthly_salary(self):
        return self.__monthly_salary
    
    @property
    def is_admin(self):
        return self.__is_admin
    
    @property
    def username(self):
        return self.__username

    @property
    def teller_id(self):
        return self.__teller_id
    
    @property
    def password(self):
        return self.__password
    
    @property
    def role(self):
        return self.__role

    def authenticate(self, password): 
        return self.__password == password
        
    def create_bank_account(self, customer):
        account_number = (str(uuid.uuid4())[:8]).upper()
        account_name = f"{customer.fullname}'s Savings Account"
        account_type = "Savings"

        if not customer.bank_account:
            if isinstance(customer, BankCustomer):
                customer.bank_account = CNBankAccount(account_number, account_name, account_type, birthdate=customer.birthdate, status="pending")
            else:
                CTkMessagebox(title="Failed!", message="Invalid account type for this user.", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="Failed!", message="User already has an account", icon="cancel", sound=True)

    def deactivate_account(self, account):
        customers = BankCustomer.get_users()
        if account in customers:
            customer = customers[account]
            if self.__is_admin:
                if customer.bank_account.balance > 0:
                    CTkMessagebox(title="Failed", message="Unable to deactivate account. Please zero out balance first before requesting deactivation", icon="cancel", sound=True)
                else:
                    customer.bank_account.status = "Pending_deactivation"
                    CTkMessagebox(title="Success", message="Account deactivation requested. Waiting for Bank Manager's approval.", icon="check", sound=True)
            else:
                CTkMessagebox(title="Failed", message="Only admin tellers can request account deactivation.", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="Failed", message="Account not found.", icon="cancel", sound=True)
    
    def customer_deposit(self, customer, amount):
        customer.deposit(amount, account_type="Savings", source='teller')

    def customer_withdraw(self, customer, amount):
        customer.withdraw(amount, account_type="Savings", source='teller')

    def customer_check_balance(self, customer):
        customer.check_balance()

    def verify_birthdate(self, customer, birthdate):
        if customer.birthdate == birthdate:
            return True
        else:
            return False
        
    def transfer_loan(self, customer, amount):
        if customer.bank_account:
            if customer.loan_status == "Approved":
                if customer.bank_account.account_type == "Savings": 
                    CTkMessagebox(title="Loan Transfer Succesful!", message="Loan amount transferred to {}'s account.".format(customer.fullname), icon="check", sound=True)
                    customer.bank_account.deposit(amount, account_type = "Savings", source="teller")
                    customer.loan_status = None
                else:
                    CTkMessagebox(title="Loan Transfer Failed!", message="Customer does not have a savings account", icon="cancel", sound=True)
            elif customer.loan_status == "Pending":
                CTkMessagebox(title="Pending Loan Request", message="Kindly wait for Bank Manager's approval.", icon="cancel", sound=True)
            elif customer.loan_status == "Denied":
               CTkMessagebox(title="Loan Transfer Failed!", message="Loan request has been denied. Unable to transfer loan amoount.", icon="cancel", sound=True)
            else:
                CTkMessagebox(title="No Request Found", message="Customer does not have any loan request.", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="No Request Found", message="Customer does not have a bank account.", icon="cancel", sound=True)