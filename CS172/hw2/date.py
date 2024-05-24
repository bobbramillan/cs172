#Bavanan Bramillan bb3323
#date program with overloaded methods, getters, and date changer function

class Date:
    def __init__(self, month=1, day=1, year=1900):
        self.__month = month
        self.__day = day
        self.__year = year

    def getMonth(self):
        return self.__month

    def getDay(self):
        return self.__day

    def getYear(self):
        return self.__year

    def is_leap_year(self):
        return (self.__year % 4 == 0)

    def changeDate(self, days_to_add):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            days_in_month[1] = 29

        self.__day += days_to_add
        while self.__day > days_in_month[self.__month - 1]:
            self.__day -= days_in_month[self.__month - 1]
            self.__month += 1
            if self.__month >= 12:
                self.__month = 1
                self.__year += 1

    def __str__(self):
        return f"{self.__month:02d}/{self.__day:02d}/{self.__year:04d}"

    def __eq__(self, other):
        return (self.__year, self.__month, self.__day) == (other.__year, other.__month, other.__day)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (self.__year, self.__month, self.__day) < (other.__year, other.__month, other.__day)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __gt__(self, other):
        return (self.__year, self.__month, self.__day) > (other.__year, other.__month, other.__day)

    def __ge__(self, other):
        return (self > other) or (self == other)

    def __getitem__(self, index):
        if index == 0:
            return self.__month
        elif index == 1:
            return self.__day
        elif index == 2:
            return self.__year
        else:
            raise IndexError("Index out of Bounds")




