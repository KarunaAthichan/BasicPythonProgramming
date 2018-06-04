class Date:

    # declaring private variable
    __day = 0
    __month = 0
    __year = 0

    # declaring number of days in a month in tuple
    days_per_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # define an initial function
    def __init__(self, y, m, d):
        self.__day = d
        self.__month = m
        self.__year = y

        # to validate the input
        self.setYear(y)
        self.setMonth(m)
        self.setDay(d)

    # define set day function
    def setDay(self, day):

        # check if the day is in correct range
        if day > 0 and day <= self.days_per_month[self.__month]:
            self.__day = day

        # check for leap year
        elif self.__month == 2 and day == 29 and (self.__year % 400 == 0 or
                                                      (self.__year % 4 == 0 and self.__year % 100 != 0)):

            self.__day = day

        else:
            print("Invalid Day")

    # define set month function
    def setMonth(self, month):
        if month > 0 and month <= 12:
            self.__month = month

        else:
            print("Invalid Month")

    # define set year function
    def setYear(self, year):
        if year >= 1900 and year <= 2020:
            self.__year = year

        else:
            print("Invalid Year")

    def getDay(self):
        return self.__day

    def getMonth(self):
        return self.__month

    def getYear(self):
        return self.__year

    # define string function to print object inputs
    def __str__(self):
        return "{}//{:0>2d}//{:0>2d} ".format(self.getYear(),

                                              self.getMonth(), self.getDay())


bDate = Date(1992, 3, 8)
eDate = Date(2014, 8, 14)

print(bDate)
print(eDate)

print(bDate.getDay())
print(eDate.getDay())

print(bDate.getMonth())
print(eDate.getMonth())

print(bDate.getYear())
print(eDate.getYear())