# Laboratory Exercise #6 and #7: Encapsulation and Abstraction - DELA ROSA, SORIANO

from abc import ABC, abstractmethod

class User(ABC):

    @property
    @abstractmethod
    def fullname(self):
        pass

    @property
    @abstractmethod
    def birthdate(self):
        pass

    @property
    @abstractmethod
    def role(self):
        pass

    @property
    @abstractmethod
    def monthly_salary(self):
        pass

    @property
    @abstractmethod
    def username(self):
        pass

    @property
    @abstractmethod
    def password(self):
        pass