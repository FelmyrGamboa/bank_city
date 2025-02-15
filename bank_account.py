from abc import ABC, abstractmethod

class BankAccount(ABC):

    @property
    @abstractmethod
    def account_number(self):
        pass
    
    @property
    @abstractmethod
    def account_name(self):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

    @property
    @abstractmethod
    def birthdate(self):
        pass

    @property
    @abstractmethod
    def account_type(self):
        pass
    
    @property
    @abstractmethod
    def status(self):
        pass

    @status.setter
    @abstractmethod
    def status(self, new_status):
        pass

    @abstractmethod 
    def deposit(self, amount, source='teller'):
        pass
    
    @abstractmethod
    def withdraw(self, amount, source='teller'):
        pass
    
    @property
    @abstractmethod
    def check_balance(self):
        pass
    
    @property
    @abstractmethod
    def pin(self):
        pass
    
    @abstractmethod
    def authenticate(self, entered_pin):
        pass

    @abstractmethod
    def change_pin(self, new_pin):
        pass