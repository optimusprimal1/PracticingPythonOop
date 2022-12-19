from abc import ABC, abstractclassmethod


class IPayable(ABC):
    @abstractclassmethod
    def get_PaymentAmount(self):
        pass


class Invoice(IPayable):
    __quantity=0
    __pricePerItem=0
    PartNumber = ""
    PartsDescription = ""
    def __init__(self, part, description, count, price) :
       self.PartNumber = part
       self.PartNumber = description
       self.set_quantity(count)
       self.set_pricePerItem(price) 

    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self,value):
        if value>0:
            self.__quantity=value
        else:
            raise ValueError("Value should be greater then 0.")
    
    def get_pricePerItem(self):
        return self.__pricePerItem

    def set_pricePerItem(self,value):
        if value>0:
            self.__pricePerItem = value
        else:
            raise ValueError("Value should be greater then 0.")
    
    def get_PaymentAmount(self):
        return float(self.get_quantity()) * self.get_pricePerItem()

invoice = Invoice("swrfsdfdfwerf","Description", 10,100.00)
print("Total Get Payment Amount = ",invoice.get_PaymentAmount())




# 727 + 761 = 1488
# 450 + 981 = 1431 total 1468.92
# 950 + 500 = 1450













# https://clutch.co/developers
# https://clutch.co/developers/blockchain
# https://clutch.co/agencies/digital-marketing
