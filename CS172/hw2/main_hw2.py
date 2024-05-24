#Bavanan Bramillan bb3323
#date changer program utilizes getters, setters from date.py

from inputroutines import intInRange
from date import Date

def main():

    print("Enter the year: ")
    year = intInRange(0, 9999)

    print("Enter the month: ")
    month = intInRange(1, 12)

    if month in [4, 6, 9, 11]:
        print("Enter the day: ")
        day = intInRange(1, 30)
    elif month == 2 and year % 4 == 0:
        print("Enter the day: ")
        day = intInRange(1, 29)
    elif month == 2:
        print("Enter the day: ")
        day = intInRange(1, 28)
    else:
        print("Enter the day: ")
        day = intInRange(1, 31)

    date1 = Date(month, day, year)
    print("\nYour entered Date:", date1)
   #getters
    print("Month:", date1.getMonth())
    print("Day:", date1.getDay())
    print("Year:", date1.getYear())

   #setter demo
    choice = input("\nDo you want to change the Date? (yes/no): ")
    if choice == "yes":
        days_to_add = int(input("Enter the number of days to add: "))
        date1.changeDate(days_to_add)
        print(f"\nNew Date after adding {days_to_add} days: {date1}")
    
    date2 = Date(5, 22, 2004)

    print(f'\nDate comparisons with Date 2: {date2}')
    print("Dates equal? :", date1 == date2)
    print("Dates inequal? :", date1 != date2)
    print("Your Date 1 less than D2? :", date1 < date2)
    print("Your Date 1 <= D2? :", date1 <= date2)
    print("Date1 > D2? :", date1 > date2)
    print("Date1 >= D2? :", date1 >= date2)


    #get item
    print("\nMonth:", date1[0])
    print("Day:", date1[1])
    print("Year:", date1[2])

if __name__ == "__main__":
    main()





