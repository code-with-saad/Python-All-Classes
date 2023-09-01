# ================================ Exercises ================================


# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".

from datetime import date, time, datetime, timedelta
import calendar

# current_date = date.today()
# print(current_date)



# ----------------------------------------------------------------


# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

# ----------------------------------------------------------------

# dt = "8/31/2023"
# print(dt)

# dt = datetime.strptime(
#     dt, "%m/%d/%Y"
# )

# print(dt) # Showing result with Time
# print(dt.year, dt.month, dt.day, sep="-") # Showing result without Time

# ----------------------------------------------------------------

# Write a program that takes a birth year as input and calculates the age of a person.

# ----------------------------------------------------------------

# birth_date = int(input("Enter your birth year: "))
# today  = date.today()
# age =  today.year - birth_date
# print(age)

# ----------------------------------------------------------------

# Create a program that calculates and prints the number of days remaining until a person's next birthday.

# ----------------------------------------------------------------

# birth = date(2007, 11, 21)
# today = date.today()

# if ( today.month == birth.month and today.day >= birth.day or today.month > birth.month ) : 
#     next_Birthday_Year = today.year + 1
# else:
#     next_Birthday_Year = today.year


# next_Birthday = date(
#     next_Birthday_Year, birth.month, birth.day
# )

# print("Next birthday:", next_Birthday)

# diff = next_Birthday - today

# print("Days left for next birthday:",diff.days)

# ----------------------------------------------------------------

# Write a program that calculates and displays the number of days between two given dates.

# ----------------------------------------------------------------

# def number_of_days(date_1, date_2):  
#     return (date_2 - date_1).days  


# date_1 = date(2023, 9, 10)  
# date_2 = date(2024, 2, 4)  
# print ("Number of Days between the given Dates are:", number_of_days(date_1, date_2), "days")  

# ----------------------------------------------------------------

# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).

# ----------------------------------------------------------------

# dt = "29-8-2023"
# dt1 = datetime.strptime(dt, "%d-%m-%Y").weekday()
# d1 = calendar.day_name[dt1]
# print(d1)

# ----------------------------------------------------------------

# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

# ----------------------------------------------------------------

# month = 8
# year = 2023
    
# if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
#     print("Number of days is 29")

# elif(month==2) :
#     print("Number of days is 28")

# elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
#     print("Number of days is 31")

# else :
#     print("Number of days is 30")

# ----------------------------------------------------------------


# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.

# ----------------------------------------------------------------



# ----------------------------------------------------------------


# Write a Python program that uses the datetime module to print the current date and time.

# ----------------------------------------------------------------

# current_datetime = datetime.now()
# print(current_datetime)

# ----------------------------------------------------------------

# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

# ----------------------------------------------------------------

# dt = "8/31/2023"

# dt = datetime.strptime(
#     dt, "%m/%d/%Y"
# )
# print(dt)

# ----------------------------------------------------------------

# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".

# ----------------------------------------------------------------

# def date_conversion(date):
#     print(date)
#     dt = datetime.strptime(
#         date, "%m/%d/%Y %H:%M:%S"
#     )
#     print(dt)

# date_conversion("9/1/2023 3:5:25")

# ----------------------------------------------------------------

# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.

# ----------------------------------------------------------------

# # start time and end time
# start_time = datetime.strptime("2:13:57", "%H:%M:%S")
# end_time = datetime.strptime("4:46:38", "%H:%M:%S")

# # get difference
# delta = end_time - start_time


# # get difference in seconds
# sec = delta.total_seconds()
# print('difference in seconds:', sec)


# # get difference in minutes
# min = sec // 60
# print('difference in minutes:', min)


# # get difference in hours
# hours = sec // 3600
# print('difference in hours:', hours)

# ----------------------------------------------------------------

# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.

# ----------------------------------------------------------------

# def dateconversion(date):
#     hour = int(input("Enter a number of hours: "))
#     dt = str(date + timedelta(hours=hour))
#     print(dt)

# dateconversion(datetime.now())

# ----------------------------------------------------------------

# Write a program that takes a date string in the format "MM-DD-YYYY" as input and converts it to a datetime object using strptime().

# ----------------------------------------------------------------

# date_input = input("Enter a date in this format => (MM-DD-YYYY): ")
# datetime_obj = datetime.strptime(date_input, "%m-%d-%Y")
# print(datetime_obj.date())

# ----------------------------------------------------------------

# Create a function that takes a datetime object as input and formats it as "Month Day, Year" (e.g., "August 25, 2023") using strftime().

# ----------------------------------------------------------------

# def datetime_obj():
#     datetime_obj1 = input("Enter a date in this format => ( DD-MM-YYY ): ")
#     datetime_obj1 = datetime.strptime(datetime_obj1, "%d-%m-%Y")
#     format_datetimeobj = datetime_obj1.strftime("%B-%d-%Y")
#     print(format_datetimeobj)

# datetime_obj()
    
# ----------------------------------------------------------------

# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().

# ----------------------------------------------------------------

# def datetime_obj():
#     datetime_obj1 = input("Enter a date in this format => ( DD-MM-YYY ): ")
#     datetime_obj1 = datetime.strptime(datetime_obj1, "%d-%m-%Y")
#     format_datetimeobj = datetime_obj1.strftime("%d-%B-%Y")
#     print(format_datetimeobj)

# datetime_obj()

# ----------------------------------------------------------------

# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00" 
# hint: https://strftime.org/

# ----------------------------------------------------------------

# date1 = "26-08-2023 15:18:33.983780-07:00"
# new_datetime = datetime.strptime(date1, "%d-%m-%Y %H:%M:%S.%f%z")
# print(new_datetime)

# ----------------------------------------------------------------

# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/

# ----------------------------------------------------------------

# date1 = "08-26-2023 08:10:00 PM"
# format = "%m-%d-%Y %I:%M:%S %p"
# new_datetime = datetime.strptime(date1, format)
# formation = new_datetime.strftime(format)
# print(formation)

# ----------------------------------------------------------------






















































































































































































































































































































































































