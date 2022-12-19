from Employee import Employee

class SalariedEmployee(Employee):
    __weeklySalary = 0

    def get_weeklySalary(self):
        return self.__weeklySalary
    
    def set_weeklySalary(self,value):
        if value>=0:
            self.__weeklySalary=value
        else:
            raise ValueError("Salary must be greater then 0")

    def get_PaymentAmount(self):
        return self.get_weeklySalary()
    

