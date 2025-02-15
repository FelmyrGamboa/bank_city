from bank_manager import BankManager
from bank_customer import BankCustomer
from cn_bank_account import CNBankAccount
from CTkMessagebox import CTkMessagebox

# Bank Manager Existing Accounts 
bank_manager = BankManager("Manager", "manager_username", "manager_password", "January 20, 1980", "Manager", 15000.00)
manager_monthly_salary = 15000.00
manager_account = CNBankAccount("A7G9T4H2", "Manager", "Payroll", manager_monthly_salary)
bank_manager.bank_account = manager_account

class ManagerProcesses():

    @staticmethod
    def use_atm(amount, action):
        if action == "deposit":
            bank_manager.bank_account.deposit(amount, account_type = "Payroll", source ='atm')
        elif action == "withdraw":
            bank_manager.bank_account.withdraw(amount, account_type = "Payroll", source ='atm')
        elif action == "check balance":
            bank_manager.bank_account.check_balance()
    
    def atm_change_pin(old, new):
        bank_manager.bank_account.change_pin(old, new)
    
    def atm_check_pin(entered_pin):
        check_pin = bank_manager.bank_account.authenticate(entered_pin)
        if check_pin == (True, 0):
            return "Success"
        elif check_pin == (False, 3):
            return "Failed"
        else:
            return "Retry"
    
    @staticmethod
    def approve_to_lock_account(manager):
        manager_username = manager
        if manager_username in BankManager.get_managers():
            bank_manager = BankManager.get_managers()[manager_username]
            customers = list(BankCustomer.get_usernames().values())
            active_customers = [customer for customer in customers if customer.has_requested_lock == "Processed"]

            for customer in enumerate(active_customers):
                bank_manager.lock_account(customer.bank_account)
                customer.update_lock_request_status("Approved")
                return f"Account for {customer.fullname} has been locked."

            if not active_customers:
                return "No requests to be approved at this time."
    
    @staticmethod
    def approve_to_unlock_account(manager):
        manager_username = manager
        if manager_username in BankManager.get_managers():
            bank_manager = BankManager.get_managers()[manager_username]
            customers = list(BankCustomer.get_usernames().values())
            active_customers = [customer for customer in customers if customer.has_requested_lock == "Processed"]

            for customer in enumerate(active_customers):
                bank_manager.unlock_account(customer.bank_account)
                customer.update_unlock_request_status("Approved")
                return f"Account for {customer.fullname} has been unlocked."

            if not active_customers:
                return "No requests to be approved at this time."

    @staticmethod
    def approve_account_requests(manager):
        manager_username = manager
        if manager_username in BankManager.get_managers():
            bank_manager = BankManager.get_managers()[manager_username]
            customer_list = BankCustomer.get_pending_requests()
            for i, customer in enumerate(customer_list):
                bank_manager.approve_account_creation(customer)
                customer.update_account_request_status("Processed")
                customer.update_account_request_status("Approved")
                BankCustomer.remove_pending_request(customer)
                return f"Account creation approved \n for {customer.fullname}"
            if not customer_list:
                return "No account request to \n approve at this time."
        
    @staticmethod
    def process_account_requests(manager):
        manager_username = manager
        if manager_username in BankManager.get_managers():
            bank_manager = BankManager.get_managers()[manager_username]
            account_request_exists = False
            for customer_name, customer in BankCustomer.get_usernames().items():
                if not customer.bank_account:
                    bank_manager.create_bank_account(customer)
                    customer.update_account_request_status("Approved")
                    account_request_exists = True
                    return f"Account request approved \n for {customer.fullname}"
            if not account_request_exists:
                return "No account creation requests \n to be processed at this time."

    
    @staticmethod
    def process_to_lock_account(manager):
        manager_username = manager
        if manager_username in BankManager.get_managers():
            bank_manager = BankManager.get_managers()[manager_username]
            customers = list(BankCustomer.get_usernames().values())
            active_customers = [customer for customer in customers if customer.bank_account.status == "Active" and customer.has_requested_lock == "Requested"]

            if not active_customers:
                return "No lock account requests \nto process at this time."

            else:
                result= []
                for i, customer in enumerate(active_customers):
                    result.append(f"{i}. {customer.fullname}")

                customer_index = int(input("Select customer by number: "))
                customer = active_customers[customer_index]
                bank_manager.lock_account(customer.bank_account)
                CTkMessagebox(title="Success!", message=f"Account for {customer.fullname} has been locked.", icon="check", sound=True)
                customer.update_lock_request_status("Approved")
                return "\n".join(result)
        else:
            return "Teller not found."
    
    @staticmethod
    def process_to_unlock_account(manager):
        manager_username = manager
        if manager_username in BankManager.get_managers():
            bank_manager = BankManager.get_managers()[manager_username]
            customers = list(BankCustomer.get_usernames().values())

            locked_customers = [customer for customer in customers if customer.bank_account.status == "Locked" and customer.has_requested_unlock == "Requested"]

            if not locked_customers:
                return  "No unlock account requests\n to process at this time."

            else:
                result= []
                for i, customer in enumerate(locked_customers):
                    result.append(f"{i}. {customer.fullname}")

                customer_index = int(input("Select customer by number: "))
                customer = locked_customers[customer_index]
                bank_manager.unlock_account(customer.bank_account)
                CTkMessagebox(title="Success!", message=f"Account for {customer.fullname} has been unlocked.", icon="cancel", sound=True)
                customer.update_unlock_request_status("Approved")
                return "\n".join(result)
        else:
            return "Teller not found."
