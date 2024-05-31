#bb3323 Bavanan Bramillan
class Birthday:
        def __init__(self, month=0, day=0, year=0):
                self.__month = month
                self.__day = day
                self.__year = year
        
        def getMonth(self):
                return self.__month
        
        def getDay(self):
                return self.__day
        
        def getYear(self):
                return self.__year

        def __str__(self):
                return f"{self.__month}/{self.__day}/{self.__year}"
        
        def __hash__(self):
                return (self.__day + self.__month + self.__year) % 12
        
        def __eq__(self):
                if self.__month == other.__getMonth() and self.__day == other.__getDay() and self.__year == other.__getYear(): 
                        return True
        
                