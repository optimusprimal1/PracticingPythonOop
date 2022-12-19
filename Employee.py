from abc import ABC, abstractclassmethod

class Employee(ABC):
    FirstName = ""
    LastName = ""
    SocialSecurityNumber = ""
    def __init__(self,firstName,lastName, sSN) :
        self.FirstName = firstName
        self.LastName = lastName
        self.SocialSecurityNumber = sSN
    
    @abstractclassmethod
    def Earning(self):
        pass












