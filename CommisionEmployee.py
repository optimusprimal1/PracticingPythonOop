from Employee import Employee


class CommisionEmployee(Employee):
    __grossSale = 0
    __commisionRate = 0
    def __init__(self, grossSale, commisionRate, firstName, lastName, sSN):
        super().__init__(firstName, lastName, sSN)
        self.__grossSale = grossSale
        self.__commisionRate = commisionRate
    
    def get_GrossSale(self):
        return self.__grossSale

    def set_GrossSale(self, value):
        if(value>0):
            self.__grossSale = value
        else:
            raise ValueError("GrossSales "+ value + "GrossSales must be >=0.")






    def get_CommisionRate(self):
        return       self.__commisionRate

    def set_CommisionRate(self,value):
        if(value>0 and value < 1):
            self.__commisionRate = value
        else:
            raise ValueError("CommissionRate "+ value + " CommissionRate must be > 0 and < 1.")
    
    def Earning(self):
        # print('self.get_CommisionRate() = ',self.get_CommisionRate())
        # print('get_GrossSale() = ',self.get_GrossSale())
        return self.get_CommisionRate()*self.get_GrossSale()

# commissionEmployee = CommisionEmployee(2000,0.9,"Ahmed", " Hassan","12345")
# # commissionEmployee.set_CommisionRate(0.8)
# # commissionEmployee.set_GrossSale(4000)
# print('commissionEmployee.Earning() = ',commissionEmployee.Earning())