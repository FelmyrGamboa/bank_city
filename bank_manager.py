import uuid
from bank_teller import BankTeller
from bank_account import BankAccount
from bank_customer import BankCustomer
from formatbirthdate import validate_and_format_birthdate
from cn_bank_account import CNBankAccount
from CTkMessagebox import CTkMessagebox

class BankManager(BankTeller):
    __managers = {}  

    @classmethod
    def get_managers(cls):
        return cls.__managers

    def __init__(self, fullname, username, password, birthdate, role, monthly_salary, is_admin=True):
        super().__init__(fullname, username, password, birthdate, role, monthly_salary, is_admin=True, bank_account=None)
        self.__username = username
        self.__password = password 
        self.__is_admin = is_admin  
        BankManager.get_managers()[username] = self  

    @property
    def is_admin(self):
        return self.__is_admin
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    def authenticate(self, password):  
        return self.__password == password
    
    def approve_account_deactivation(self, teller_username, customer_fullname):
        tellers = BankTeller.get_tellers()
        if teller_username in tellers:
            teller = tellers[teller_username]
            if teller.is_admin:
                customers = BankCustomer.get_users()
                if customer_fullname in customers:
                    customer = customers[customer_fullname]
                    if customer.bank_account.status == "Pending_deactivation":
                        BankCustomer.remove_user(customer.fullname)
                        CTkMessagebox(title="Approved", message="Account deactivation request has been approved.", icon="check", sound=True)
                    else:
                        CTkMessagebox(title="No Request Found", message="No pending deactivation requests to be approved at this time", icon="info", sound=True)
                else:
                    CTkMessagebox(title="Error!", message="Account not found!", icon="cancel", sound=True)
            else:
                CTkMessagebox(title="Failed!", message="Teller is not an admin.", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="Error!", message="Teller not found", icon="cancel", sound=True)
            
    def unlock_account(self, account):
        customers = BankCustomer.get_usernames()
        if account in customers:
            customer = customers[account]
            customer.bank_account.status = "Active"
            CTkMessagebox(title="Success!", message=f"Account {customer.bank_account.account_number} unlocked successfully.", icon="check", sound=True)
        else:
            CTkMessagebox(title="Error!", message="Customer not found", icon="cancel", sound=True)
            
    def lock_account(self, account):
        customers = BankCustomer.get_usernames()
        if account in customers:
            customer = customers[account]
            customer.bank_account.status = "Locked"
            CTkMessagebox(title="Success!", message=f"Account {customer.bank_account.account_number} locked successfully.", icon="check", sound=True)
        else:
            CTkMessagebox(title="Error!", message="Customer not found", icon="cancel", sound=True)

    def approve_loan(self, customer_username):
        customers = BankCustomer.get_usernames()
        if customer_username in customers:
            customer = customers[customer_username]
            if customer.loan_status == "Pending":
                amount = float(customer.requested_loan_amount)
                if amount <= customer.monthly_salary * 4 and not customer.has_existing_loan:
                    CTkMessagebox(title="Success!", message="Loan application has been approved.", icon="check", sound=True)
                    customer.has_existing_loan = True
                    customer.loan_status = "Approved"
                    return True
                else:
                    if amount > customer.monthly_salary * 4:
                        CTkMessagebox(title="Failed!", message="Requested amount exceeds 400% of customer's monthly salary.", icon="cancel", sound=True)
                        customer.loan_status = "Denied"
                    elif customer.has_existing_loan:
                        CTkMessagebox(title="Failed!", message="Customer already has an existing loan", icon="cancel", sound=True)
                        customer.loan_status = "Denied"
                    return False
            else:
                CTkMessagebox(title="No Request Found", message="No loan application to approve at this time.", icon="info", sound=True)
        else:
            CTkMessagebox(title="Error!", message="Customer not found", icon="cancel", sound=True)
            return False
    
    def create_bank_account(self, customer):
        account_number = (str(uuid.uuid4())[:8]).upper()
        account_name = f"{customer.fullname}'s Savings Account"
        account_type = "Savings"

        if not customer.bank_account:
            if isinstance(customer, BankCustomer):
                customer.bank_account = CNBankAccount(account_number, account_name, account_type, birthdate=customer.birthdate, status="Active")
            else:
                CTkMessagebox(title="Error!", message="Invalid account type for this user", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="Error!", message="Customer already has an account", icon="info", sound=True)

    def deactivate_account(self, customer):
        customers = BankCustomer.get_users()
        if customer in customers:
            account = customers[customer]
            if self.__is_admin:
                if account.bank_account.balance > 0:
                    CTkMessagebox(title="Error!", message="Unable to deactivate account. Please zero out balance first before requesting deactivation.", icon="cancel", sound=True)
                else:
                    BankCustomer.remove_user(account.fullname)
                    CTkMessagebox(title="Success!", message="Account deactivation has been approved.", icon="check", sound=True)
            else:
                CTkMessagebox(title="Error!", message="Only admin can request deactivation.", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="Error!", message="Customer not found or bank account does not exist. Unable to initiate deactivation process", icon="cancel", sound=True)

    def customer_deposit(self, customer, amount):
        customer.deposit(amount, account_type="Savings", source='manager')

    def customer_withdraw(self, customer, amount):
        customer.withdraw(amount, account_type="Savings", source='manager')

    def customer_check_balance(self, customer):
        customer.check_balance()

    def verify_birthdate(self, customer, birthdate):
        if customer.birthdate == birthdate:
            return True
        else:
            return False
    def approve_account_creation(self, customer):
        if isinstance(customer.bank_account, BankAccount):
            customer.bank_account.status = "Active"

    def transfer_loan(self, customer, amount):
        if customer.bank_account:
            if customer.loan_status == "Pending":
                if customer.bank_account.account_type == "Savings": 
                    CTkMessagebox(title="Loan Transfer Succesful!", message="Loan amount transferred to {}'s account.".format(customer.fullname), icon="check", sound=True)
                    customer.bank_account.deposit(amount, account_type = "Savings", source="manager")
                    customer.loan_status = None
                else:
                    CTkMessagebox(title="Loan Transfer Failed!", message="Customer does not have a savings account", icon="cancel", sound=True)
            elif customer.loan_status == "Denied":
                CTkMessagebox(title="Loan Transfer Failed!", message="Loan request has been denied. Unable to transfer loan amoount.", icon="cancel", sound=True)
            else:
                CTkMessagebox(title="No Request Found", message="Customer does not have any loan request.", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="Loan Transfer Failed!", message="Customer does not have a bank account.", icon="cancel", sound=True)

    
    
    
    
    