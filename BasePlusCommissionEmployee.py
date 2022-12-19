from CommisionEmployee import CommisionEmployee


class BasePlusCommissionEmployee(CommisionEmployee):
    __baseSalary = 0
    def __init__(self, baseSalary, grossSale, commisionRate, firstName, lastName, sSN):
        super().__init__(grossSale, commisionRate, firstName, lastName, sSN)
        self.__baseSalary = baseSalary
    
    def get_BaseSalary(self):
        return self.__baseSalary
