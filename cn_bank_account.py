from bank_account import BankAccount
from CTkMessagebox import CTkMessagebox

class CNBankAccount(BankAccount):
    def __init__(self, account_number, account_name, account_type, balance=0.0, pin=1234, birthdate="", status="Active"):
        self.__account_number = str(account_number)
        self.__account_name = str(account_name)
        self.__account_type = str(account_type)
        self.__balance = balance
        self.__pin = int(pin)
        self.__birthdate = str(birthdate)
        self.__status = str(status)
        self.pin_attempts = 0
        
    @property
    def account_number(self):
        return self.__account_number    
    
    @property
    def account_name(self):
        return self.__account_name
    
    @property
    def pin(self):
        return self.__pin

    @property
    def balance(self):
        return self.__balance

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def account_type(self):
        return self.__account_type
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    def check_balance(self):
        CTkMessagebox(title="Balance Inquiry", message=f"Current balance: ₱{self.balance}.", icon="info", sound=True)

    def authenticate(self, entered_pin):
        if int(entered_pin) == self.__pin:
            self.pin_attempts = 0
            return True, 0
        else:
            self.pin_attempts += 1
            if self.pin_attempts < 3:
                CTkMessagebox(title="Incorrect PIN!", message=f"Attempt {self.pin_attempts} of 3.", icon="cancel", sound=True)
                return False, self.pin_attempts
            else:
                CTkMessagebox(title="Failed!", message="Too many incorrect attempts. Back to Main Menu.", icon="cancel", sound=True)
                self.pin_attempts = 0
                return False, 3
            

    def change_pin(self, old_pin, new_pin):
        if int(old_pin) != self.__pin:
            CTkMessagebox(title="Incorrect old PIN", message="Old PIN does not match.", icon="cancel", sound=True)
        elif new_pin == old_pin:
            CTkMessagebox(title="Invalid New PIN", message="Old and new pin cannot be the same.", icon="cancel", sound=True)
        elif len(new_pin) != 4:
            CTkMessagebox(title="Invalid New PIN", message="PIN should be 4 digits.", icon="cancel", sound=True)
        else:
            self.__pin = int(new_pin)
            CTkMessagebox(title="Success!", message="PIN has been successfully changed.", icon="check", sound=True)

    def deposit(self, amount, account_type, source):
        if self.__status == "Active":
            if source == 'atm' and amount > 20000:
                if account_type == "Savings":
                    CTkMessagebox(title="ATM Deposit Limit Exceeded", message="Please transact with a teller for higher amounts", icon="cancel", sound=True)
                else:
                    CTkMessagebox(title="ATM Deposit Limit Exceeded", message="Payroll account is unable to deposit amount higher than Php 20,000.", icon="cancel", sound=True)
            else:
                self.__balance += amount
                CTkMessagebox(title="Deposit successful!", message=f"Amount deposited: ₱{amount}.", icon="check", sound=True)

        else:
            CTkMessagebox(title="Account locked", message="Unable to initiate transaction.", icon="cancel", sound=True)

    def withdraw(self, amount, account_type, source):
        if self.__status == "Active":
            if source == 'atm' and amount > 20000:
                if account_type == "Savings":
                    CTkMessagebox(title="ATM Deposit Limit Exceeded", message="Please transact with a teller for higher amounts", icon="cancel", sound=True)
                else:
                    CTkMessagebox(title="ATM Withdrawal Limit Exceeded", message="Payroll account is unable to withdraw amount higher than Php 20,000.", icon="cancel", sound=True)
            elif self.__balance >= amount:
                self.__balance -= amount
                CTkMessagebox(title="Withdrawal Successful!", message=f"Amount withdrawn: ₱{amount}.", icon="check", sound=True)
            else:
                CTkMessagebox(title="Insufficient Balance", message="Please retry with a lower amount", icon="cancel", sound=True)
        else:
            CTkMessagebox(title="Account locked", message="Unable to initiate transaction.", icon="cancel", sound=True)