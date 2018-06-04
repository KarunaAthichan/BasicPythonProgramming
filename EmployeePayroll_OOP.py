# create an Employee abstract class
from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, first, last, ssn):
        self.__firstName = first
        self.__lastName = last
        self.__ssn = ssn

    def setFirstName(self, fname):
        self.__firstName = fname

    def getFirstName(self):
        return self.__firstName

    def setLastName(self, lname):
        self.__lastName = lname

    def getLastName(self):
        return self.__lastName

    def setSSN(self, ssn):
        self.__ssn = ssn

    def getSSN(self):
        return self.__ssn

    def checkPositive(self, Value):

        if Value < 0:
            msg = "Attribute value {} must be positive".format(Value)
            raise ValueError(msg)
        else:
            return Value

    def __str__(self):
        return "{} {} Social Security Number: {}".format(self.getFirstName(),
                                                         self.getLastName(),
                                                         self.getSSN())
    @abstractmethod
    def earning(self):pass


class SalariedEmployee(Employee):

    def __init__(self, first, last, ssn, salary):
        super().__init__(first, last, ssn)
        self.__WeeklySalary = self.checkPositive(salary)

    def setWeeklySalary(self, salary):
        self.__WeeklySalary = self.checkPositive(salary)

    def getWeeklySalary(self):
        return self.__WeeklySalary

    def earning(self):
        return self.getWeeklySalary()

    def __str__(self):
        return "Salaried Employee: {} \n{} {:.2f}".format(super().__str__(),
                                                           "Weekly Salary",
                                                           self.getWeeklySalary())

class HourlyEmployee(Employee):

    def __init__(self, first, last, ssn, hourlyWage, hoursWorked):
        super().__init__(first, last, ssn)
        self.__wage = self.setWage(hourlyWage)
        self.__hours = self.setHours(hoursWorked)

    def setWage(self, HourlyWage):
        return self.checkPositive(HourlyWage)

    def getWage(self):
        return self.__wage

    def setHours(self, HoursWorked):

        if HoursWorked >= 0.0 and HoursWorked <= 168.0:
            return HoursWorked
        else:
            raise ValueError("Hourly wage must be >= 0.0")

    def getHours(self):
        return self.__hours

    def earning(self):
        if self.getHours() <= 40:
            return self.getWage() * self.getHours()
        else:
            return 40 * self.getWage() + (self.getHours() - 40) * self.getWage() * 1.5

    def __str__(self):
        return "Hourly Employee: {} \n {}: {:.2f} {}: {:.2f}".format(super().__str__(),
                                                                         "Hourly Wage",
                                                                         self.getWage(),
                                                                         "Hours Worked",
                                                                         self.getHours())

class CommissionEmployee(Employee):

    def __init__(self, first, last, ssn, grossSales, commissionRate):
        super().__init__(first, last, ssn)
        self.__grossSales = self.setGrossSales(grossSales)
        self.__commissionRate = self.setCommissionRate(commissionRate)

    def setCommissionRate(self, rate):
        if rate > 0.0 and rate < 1.0:
            return rate
        else:
            raise ValueError("Rate must be between 0.0 and 1.0")

    def getCommissionRate(self):
        return self.__commissionRate

    def setGrossSales(self, sales):
        return self.checkPositive(sales)

    def getGrossSales(self):
        return self.__grossSales

    def earning(self):
        return self.getCommissionRate() * self.getGrossSales()

    def __str__(self):
        return "Commission Employee: {} \n {}" \
                       "{:.2f} {} {:.2f}".format(super().__str__(),
                                                 "Gross Sales: ",
                                                 self.getGrossSales(),
                                                 "Commission Rate: ",
                                                 self.getCommissionRate())

#Main Program
sEmp = SalariedEmployee("John", "Smith", "111-11-1111",800.00)
hEmp = HourlyEmployee("Karen","Price","222-22-2222", 16.75,40 )
cEmp = CommissionEmployee("Sue","Jones", "333-33-3333", 10000,.06 )

print ("\nsEmp is an Employee's object:", isinstance( sEmp, Employee ))
print ("hEmp is an Employee's object:", isinstance( hEmp, Employee ))
print("CommissionEmployee is subclass of an Employee: ", issubclass(CommissionEmployee,
                                                                  Employee))

print()
print( "Employees processed individually:\n")
print(sEmp, "earned", sEmp.earning())
print(hEmp, "earned", hEmp.earning())
print(cEmp, "earned", cEmp.earning())

#del sEmp tell something about destructor

#create a list of employees
employees = [sEmp, hEmp, cEmp]

for employee in employees:
    print(employee)