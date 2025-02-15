from bank_customer import BankCustomer
from bank_teller import BankTeller
from bank_manager import BankManager
from user import User
from cn_bank_account import CNBankAccount
from formatbirthdate import validate_and_format_birthdate
from manager_processes import ManagerProcesses
from customer_processes import CustomerProccesses
from teller_processes import TellerProcesses
from CTkMessagebox import CTkMessagebox

class BankSystem():

    def __init__(self):
        self.logged_in_user = None

    def transfer_loan_amount(self,user, account):
        self.logged_in_user = user
        customers = BankCustomer.get_usernames()
        if account in customers:
            customer = customers[account]
            teller = BankTeller.get_tellers()[self.logged_in_user.username]
            amount = customer.requested_loan_amount
            teller.transfer_loan(customer, amount)
        else:
            CTkMessagebox(title="Error!", message="Customer not found.", icon="cancel", sound=True)


    def managerpov_transfer_loan_amount(self, user, account):
        self.logged_in_user = user
        customers = BankCustomer.get_usernames()
        if account in customers:
            customer = customers[account]
            teller = BankManager.get_managers()[self.logged_in_user.username]
            amount = customer.requested_loan_amount
            teller.transfer_loan(customer, amount)
        else:
            CTkMessagebox(title="Error!", message="Customer not found.", icon="cancel", sound=True)


    def managerpov_process_lock_acc(self, user):
        self.logged_in_user= user
        return ManagerProcesses.process_to_lock_account(self.logged_in_user.username)
    
    def managerpov_process_unlock_acc(self, user):
        self.logged_in_user= user
        return ManagerProcesses.process_to_unlock_account(self.logged_in_user.username)
    
    def managerpov_process_acc(self, user):
        self.logged_in_user= user
        self.processed_user= ManagerProcesses.process_account_requests(self.logged_in_user.username)
        return self.processed_user
    
    def managerpov_request_account_deactivation(self, user, customer):
        self.logged_in_user = user
        self.logged_in_user.deactivate_account(customer)

    def process_lock_acc(self, user):
        self.logged_in_user = user
        return TellerProcesses.process_to_lock_account(self.logged_in_user.username)

    def process_unlock_acc(self, user):
        self.logged_in_user = user
        return TellerProcesses.process_to_unlock_account(self.logged_in_user.username)
    
    def request_account_deactivation(self, user, customer):
        self.logged_in_user = user
        self.logged_in_user.deactivate_account(customer)

    def request_bank(self, user):
        self.logged_in_user = user
        self.logged_in_user.request_account()

    def account_request_status(self, user):
        self.logged_in_user = user
        CustomerProccesses.check_account_request_status(self.logged_in_user)

    def lock_or_unlock_account(self, user):
        self.logged_in_user = user
        CustomerProccesses.request_lock_or_unlock(self.logged_in_user)
    
    def entered_loan_for_request(self, user, amount):
        self.logged_in_user = user
        if self.logged_in_user.bank_account:
            if self.logged_in_user.bank_account.status == "Active":
                self.logged_in_user.request_loan(amount)
            else:
                CTkMessagebox(title="Loan Request Failed!", message="Account is locked. Unable to request a loan at this time.", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="Loan Transfer Failed!", message="Kindly request for a bank accouunt first.", icon="cancel", sound=True)

    def approve_lock_account(self, user):
        self.logged_in_user = user
        approve_lock_acc = ManagerProcesses.approve_to_lock_account(self.logged_in_user.username)
        return approve_lock_acc
    
    def unlock_account(self, user, account):
        self.logged_in_user = user
        self.logged_in_user.unlock_account(account)

    def lock_account(self, user, account):
        self.logged_in_user = user
        self.logged_in_user.lock_account(account)


    def approve_unlock_account(self, user):
        self.logged_in_user = user
        approve_unlock_acc = ManagerProcesses.approve_to_unlock_account(self.logged_in_user.username)
        return approve_unlock_acc
    
    def approve_loan(self, user, customer_username):
        self.logged_in_user = user
        self.logged_in_user.approve_loan(customer_username)

    def approve_account_deactivation(self, user, user_teller, customer_fullname):
        self.logged_in_user = user
        self.logged_in_user.approve_account_deactivation(user_teller, customer_fullname)

    def loan_application_status(self, user):
        self.logged_in_user = user
        CustomerProccesses.check_loan_application_status(self.logged_in_user)

    def process_acc(self, user):
        self.logged_in_user = user
        self.processed_user = TellerProcesses.process_account_requests(self.logged_in_user.username)
        return self.processed_user
    
    def approve_account(self, user):
        self.logged_in_user = user
        self.approved_user = ManagerProcesses.approve_account_requests(self.logged_in_user.username)
        return self.approved_user

    def atm_transactions(self, user, action, amount):
        self.logged_in_user = user
        if isinstance(self.logged_in_user, BankCustomer):
            self.logged_in_user.use_atm(amount, action)
        elif isinstance(self.logged_in_user, BankManager):
            ManagerProcesses.use_atm(amount, action)
        elif isinstance(self.logged_in_user, BankTeller):
            TellerProcesses.use_atm(amount, action)
        
    
    def atm_change_pin(self, user, old, new):
        self.logged_in_user = user
        if isinstance(self.logged_in_user, BankCustomer):
            self.logged_in_user.atm_change_pin(old, new)
        elif isinstance(self.logged_in_user, BankManager):
            ManagerProcesses.atm_change_pin(old, new)
        elif isinstance(self.logged_in_user, BankTeller):
            TellerProcesses.atm_change_pin(old, new)
        
    def transact_with_telller(self, user, birthday, amount, action):
        self.logged_in_user = user
        formatted_birthdate = validate_and_format_birthdate(birthday)
        if action == "Deposit" or action == "Withdraw":
            if amount.isdigit() and formatted_birthdate:
                self.logged_in_user.transact_with_admin(BankTeller, self.logged_in_user.bank_account, formatted_birthdate, float(amount), action)
            elif not amount.isdigit():
                CTkMessagebox(title="Invalid input", message="Amount input is invalid", icon="cancel", sound=True)
        else:
            self.logged_in_user.transact_with_admin(BankTeller, self.logged_in_user.bank_account, formatted_birthdate, amount, action)
        
    def transact_with_customer(self, user, birthday, amount, action, username):
        self.logged_in_user = user
        formatted_birthdate = validate_and_format_birthdate(birthday)
        customers = BankCustomer.get_usernames()
        if username in customers:
            customer = customers[username]
            if action == "Deposit" or action == "Withdraw":
                if amount.isdigit() and formatted_birthdate:
                        if isinstance(self.logged_in_user, BankTeller):
                            customer.transact_with_admin(BankTeller, customer.bank_account, formatted_birthdate, float(amount), action)
                        elif isinstance(self.logged_in_user, BankManager):
                            customer.transact_with_admin(BankManager, customer.bank_account, formatted_birthdate, float(amount), action)
                elif not amount.isdigit():
                        CTkMessagebox(title="Invalid input", message="Amount input is invalid", icon="cancel", sound=True)
            else:
                if isinstance(self.logged_in_user, BankTeller):
                    customer.transact_with_admin(BankTeller, customer.bank_account, formatted_birthdate, amount, action)
                elif isinstance(self.logged_in_user, BankManager):
                    customer.transact_with_admin(BankManager, customer.bank_account, formatted_birthdate, amount, action)

    def check_account(self, username):
        customers = BankCustomer.get_usernames()
        if username in customers:
            customer = customers[username]
            if customer.bank_account:
                if customer.bank_account.status == "Active":
                    return True
                elif self.logged_in_user.bank_account.status == "Locked":
                    CTkMessagebox(title="Locked Bank Account", message="Unable to perform transactions if account is locked..", icon="cancel", sound=True)
            else:
                CTkMessagebox(title="No Bank Account", message="Unable to perform transactions without a bank account.", icon="cancel", sound=True)

    def atm_check_pin(self, user, entered_pin):
        self.logged_in_user = user
        if isinstance (self.logged_in_user, BankCustomer):
            checked_pin = self.logged_in_user.atm_check_pin(entered_pin)
            if checked_pin == "Success":
                return "Success"
            elif checked_pin == "Failed":
                return "Failed"
            else:
                return "Retry"
        elif isinstance(self.logged_in_user, BankManager):
            checked_pin = ManagerProcesses.atm_check_pin(entered_pin)
            if checked_pin == "Success":
                return "Success"
            elif checked_pin == "Failed":
                return "Failed"
            else:
                return "Retry"
        elif isinstance(self.logged_in_user, BankTeller):
            checked_pin = TellerProcesses.atm_check_pin(entered_pin)
            if checked_pin == "Success":
                return "Success"
            elif checked_pin == "Failed":
                return "Failed"
            else:
                return "Retry"

    
    def verify_customer(self, user, username, account_number):
        self.logged_in_user = user
        customers = BankCustomer.get_usernames()
        if username in customers:
            customer = customers[username]
            if customer.bank_account:
                if customer.bank_account.account_number == account_number:
                    return True
                else:
                    CTkMessagebox(title="Error", message="Incorrect account number. Please try again.", icon="cancel", sound=True) 
            else:
                CTkMessagebox(title="Error", message="Incorrect account number. Please try again.", icon="cancel", sound=True) 
        else:
            CTkMessagebox(title="Customer not found", message="Customer does not exist or username is incorrect.", icon="cancel", sound=True) 
            
    def register_user(self, first_name, middle_name, last_name, birthdate, monthly_salary, username, password):
        while True:
            if first_name == "" or last_name == "" or birthdate == "" or monthly_salary == "" or username == "" or password == "":
                CTkMessagebox(title="Error", message="Please enter a valid input.", icon="cancel", sound=True)
                return False
            else:
                break
        
        while True:
            if not all(part.isalpha() for part in first_name.split()):
                CTkMessagebox(title="Error", message="First name can only contain letters and may have two parts.", icon="cancel", sound=True)
                return False
            else:
                break
            
        while True:
            if middle_name and not middle_name.isalpha():
                CTkMessagebox(title="Error", message="Middle name can only contain letters.", icon="cancel", sound=True)
                return False
            else:
                break
            
        while True:
            if not all(part.isalpha() for part in last_name.split()):
                CTkMessagebox(title="Error", message="Last name can only contain letters and may have two parts.", icon="cancel", sound=True)
                return False
            else:
                break

        while True:
            fullname = f"{first_name.title()} {middle_name.title() if middle_name else ''} {last_name.title()}".strip()
            if BankCustomer.user_exists(fullname):
                CTkMessagebox(title="Notice", message="User already registered.", icon="info", sound=True)
                break
            elif not first_name or not last_name:
                CTkMessagebox(title="Error", message="First and last name cannot be empty.", icon="cancel", sound=True)
                return False
            else:
                while True:
                    birthdate = self.get_valid_birthdate(birthdate)
                    if birthdate == None:
                        return False
                    else:
                        break
                    
                role = "Customer"
                while True:
                    monthly_salary = self.get_valid_salary(monthly_salary)
                    if monthly_salary:
                        break
                    else:
                        return False
                
                while True:
                    username = self.get_unique_username(username)
                    if username == None:
                        return False
                    else: 
                        break

                while True:
                    password = self.get_valid_password(password)
                    if password == None:
                        return False
                    else:
                        break
                BankCustomer.update_users_list(fullname)
                BankCustomer.get_users()[fullname] = BankCustomer(fullname, username, password, birthdate, role, monthly_salary)
                CTkMessagebox(title="Registration Successful!", message=f"Welcome! Thank you for choosing Bank City.", icon="check", sound=True)
                return True

    def get_unique_username(self, username):
        while True:
            if not username:
                CTkMessagebox(title="Error", message="Username cannot be empty.", icon="cancel", sound=True)
                return False
            else:
                if username not in BankCustomer.get_usernames():
                    return username
                else:
                    CTkMessagebox(title="Error", message="Username already taken. Please choose a different username.", icon="cancel", sound=True)
                    return False

    def get_valid_password(self, password):
        while True:
            if not password:
                CTkMessagebox(title="Error", message="Password cannot be empty.", icon="cancel", sound=True)
                return False
            else:
                return password

    def get_valid_birthdate(self, birthdate):
        while True:
            formatted_birthdate = validate_and_format_birthdate(birthdate)
            if formatted_birthdate:
                return formatted_birthdate
            else:
                break

    def get_valid_salary(self, monthly_salary):
        while True:

            if monthly_salary.replace('.', '', 1).isdigit():
                monthly_salary_formatted = float(monthly_salary)

                if round(monthly_salary_formatted, 2) != monthly_salary_formatted:
                    CTkMessagebox(title="Error", message="Please enter a number with up to 2 decimal places.", icon="cancel", sound=True)
                    return False


                if monthly_salary.startswith('0') and not monthly_salary.startswith('0.'):
                    CTkMessagebox(title="Error", message="Salary starting with '0' is invalid.", icon="cancel", sound=True)
                    return False

                return monthly_salary_formatted

            else:
                CTkMessagebox(title="Error", message="Please enter a valid number.", icon="cancel", sound=True)
                return False
            
    def login(self, user_type, username, password):
        while True:
            if user_type == 'customer':
                customers_usernames = BankCustomer.get_usernames()
                customers_passwords = BankCustomer.get_passwords()

                if username in customers_usernames and password in customers_passwords:
                    self.logged_in_user = customers_usernames[username]
                    CTkMessagebox(title="Welcome!", message=f"Welcome! {BankCustomer.get_usernames()[username].fullname}", icon="check", sound=True)
                    return True
                else:
                    CTkMessagebox(title="Error", message="Invalid username or password for customer or user not registered.", icon="cancel", sound=True)
                    return False

            elif user_type == 'teller':
                if username in BankTeller.get_tellers() and BankTeller.get_tellers()[username].authenticate(password):
                    self.logged_in_user = BankTeller.get_tellers()[username]
                    CTkMessagebox(title="Success!", message=f"Welcome! {BankTeller.get_tellers()[username].fullname}", icon="check", sound=True)
                    return True
                else:
                    CTkMessagebox(title="Error", message="Invalid username or password for teller.", icon="cancel", sound=True)
                    return False

            elif user_type == 'manager':
                if username in BankManager.get_managers() and BankManager.get_managers()[username].authenticate(password):
                    self.logged_in_user = BankManager.get_managers()[username]
                    CTkMessagebox(title="Success!", message=f"Welcome! {BankManager.get_tellers()[username].fullname}", icon="check", sound=True)
                    return True
                else:
                    CTkMessagebox(title="Error", message="Invalid username or password for manager.", icon="cancel", sound=True)
                    return False
            return self.logged_in_user