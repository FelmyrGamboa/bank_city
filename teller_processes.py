from bank_teller import BankTeller
from bank_customer import BankCustomer
from manager_processes import ManagerProcesses
from cn_bank_account import CNBankAccount

# Bank Teller Existing Accounts 
bank_teller = BankTeller("Teller", "teller_username", "teller_password", "March 21, 1990", "Teller", 10000.00, is_admin=True)
teller_monthly_salary = 10000.00  
teller_account = CNBankAccount("J5K2L8M3", "Teller", "Payroll", teller_monthly_salary)
bank_teller.bank_account = teller_account

class TellerProcesses():
    
    @staticmethod
    def use_atm(amount, action):
        if action == "deposit":
            bank_teller.bank_account.deposit(amount, account_type = "Payroll", source ='atm')
        elif action == "withdraw":
            bank_teller.bank_account.withdraw(amount, account_type = "Payroll", source ='atm')
        elif action == "check balance":
            bank_teller.bank_account.check_balance()
    
    def atm_change_pin(old, new):
        bank_teller.bank_account.change_pin(old, new)

    def atm_check_pin(entered_pin):
        check_pin = bank_teller.bank_account.authenticate(entered_pin)
        if check_pin == (True, 0):
            return "Success"
        elif check_pin == (False, 3):
            return "Failed"
        else:
            return "Retry"
        
    @staticmethod
    def process_to_unlock_account(teller):
        teller_username = teller
        if teller_username in BankTeller.get_tellers():
            bank_teller = BankTeller.get_tellers()[teller_username]
            customers = list(BankCustomer.get_usernames().values())

            locked_customers = [customer for customer in customers if customer.bank_account.status == "Locked" and customer.has_requested_unlock == "Requested"]

            if not locked_customers:
                return "No unlock account requests\n to process at this time."
            else:
                result = []
                for i, customer in enumerate(locked_customers):
                    result.append(f"{i}. {customer.fullname}")

                customer_index = int(input("Select customer by number: "))
                customer = locked_customers[customer_index]
                result.append(f"Unlock account request for {customer.fullname} has been processed. Kindly wait for approval.")
                customer.update_unlock_request_status("Processed")
                return "\n".join(result)
        else:
            return "Teller not found."
    
    @staticmethod
    def process_account_requests(teller): 
        teller_username= teller
        if teller_username in BankTeller.get_tellers():
            bank_teller = BankTeller.get_tellers()[teller_username]
            account_request_exists = False 
            for customer_name, customer in BankCustomer.get_usernames().items():
                if not customer.bank_account:
                    bank_teller.create_bank_account(customer)
                    customer.update_account_request_status("Processed")
                    account_request_exists = True
                    return f"Processing account request \n for {customer.fullname}"
            if not account_request_exists:
                return "No account creation requests \nto be processed at this time."
    
    @staticmethod
    def process_to_lock_account(teller):
        teller_username = teller
        if teller_username in BankTeller.get_tellers():
            bank_teller = BankTeller.get_tellers()[teller]
            customers = list(BankCustomer.get_usernames().values())
            active_customers = [customer for customer in customers if customer.bank_account.status == "Active" and customer.has_requested_lock == "Requested"]

            if not active_customers:
                return "No lock account requests\n to process at this time."
            else:
                result = []
                for i, customer in enumerate(active_customers):
                    result.append(f"{i}. {customer.fullname}")

                result.append(f"Lock account request for {customer.fullname} has been processed. Kindly wait for approval.")
                customer.update_lock_request_status("Processed")
                return "\n".join(result)
        else:
            return "Teller not found."