from Employee import Employee


class HourlyEmployee(Employee):
    __Wage=0
    __Hours = 0
    def __init__(self, wage, hour, firstName, lastName, sSN):
        self.__Wage = wage
        self.__Hours = hour
        self.FirstName = firstName
        self.LastName = lastName
        self.SocialSecurityNumber = sSN

    def get_wage(self):
        return self.__Wage
    
    def set_wage (self, value):
        if value>0:
            self.__Wage = value
        else:
            raise ValueError("Wage must be greater then 0")
    
    def get_hour(self):
        return self.__Hours
    
    def set_hour(self, value):
        if value>=0 and value<= 168:
            self.__Hours = value
        else:
            return ValueError("Hours must be >= 0 and <= 168")

    def Earning(self):
        if self.__Hours<=40:
            return self.__Wage*self.__Hours
        else:
            return (40 *self.__Hours) + ( (self.__Hours-40) * self.__Wage * 1.5) 


hourlyEmployee = HourlyEmployee(50, 45, "Ahmed", " Hassan","12345")
print("Earning of hourly Employee = ", hourlyEmployee.Earning())