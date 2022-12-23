from CommisionEmployee import CommisionEmployee


class BasePlusCommissionEmployee(CommisionEmployee):
    __baseSalary = 0
    def __init__(self, baseSalary, grossSale, commisionRate, firstName, lastName, sSN):
        super().__init__(grossSale, commisionRate, firstName, lastName, sSN)
        self.__baseSalary = baseSalary
    
    def get_BaseSalary(self):
        return self.__baseSalary
    
    def get_BaseSalary(self):
        return self.__baseSalary
    
    def set_BaseSalary(abc, value):
        if value>0:
            abc.__baseSalary = value
        else:
            raise ValueError("BaseSalary "+value+" BaseSalary must be greater then 0")
    
    def Earning(self):
        print()
        return self.get_BaseSalary()+ super().Earning()

baseCommissionEmployee = BasePlusCommissionEmployee(30000,4000,0.9,"Ahmed", " Hassan","12345")
# commissionEmployee.set_CommisionRate(0.8)
# commissionEmployee.set_GrossSale(4000)
print('commissionEmployee.Earning() = ',baseCommissionEmployee.Earning())