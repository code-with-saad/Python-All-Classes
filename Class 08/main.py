# play with current date and datetime
from datetime import date, datetime

# ISO (International Organization for Standardization) Date format
# 2023-08-26 10:30:00+05:00
# %Y-%m-%d %H:%M:%S%z

# date
print("date")
current_date = date.today()
print(current_date) # %Y-%m-%d
print(current_date.year)
print(current_date.month)
print(current_date.day)

# date with time -> system local time
print("\ndate with time - local sytem")
current_date_time = datetime.now() # system localtime
print(current_date_time)  # %Y-%m-%d %H:%M:%S.%f

print(current_date_time.year)
print(current_date_time.month)
print(current_date_time.day)
print(current_date_time.hour)
print(current_date_time.minute)
print(current_date_time.second)

# date with time -> UTC datetime without timezone
print("\ndate with time - UTC")
utc_date_time = datetime.utcnow()  # system localtime
print(utc_date_time)  # %Y-%m-%d %H:%M:%S.%f


# ================================================================

# create date and time from string
from datetime import datetime, date


print("create date and time with ISO formatted string date")
date_iso = "2023-08-26"  # ISO 8601
dt_obj = date.fromisoformat(date_iso)
print(dt_obj.year)

datetime_iso = "2023-08-26 20:50:45"  # ISO 8601
dt_obj = datetime.fromisoformat(datetime_iso)
print(dt_obj.year)


# https://strftime.org/
# create date object from string other than is ISO
print("\ncreate date object from string other than ISO")
dt_pakistan_format = "26-08-2023"
dt_united_states_format = "08/26/2023"
dt_iso_format = "2023-08-26"
invalid_dt = "2023/-08--/26"
dt_12_hour_format = "26-08-2023 08:10:00 PM"
dt_named_and_short_form_format = "8-September-23 08:10:00"

dt = datetime.strptime(
    dt_pakistan_format,
    "%d-%m-%Y"
)
print("date obj converted from pak date format:", dt)


dt = datetime.strptime(
    dt_united_states_format,
    "%m/%d/%Y"
)
print("date obj converted from united state date format:", dt)


dt = datetime.strptime(
    dt_iso_format,
    "%Y-%m-%d"
)
print("date obj converted from iso date format:", dt)


dt = datetime.strptime(
    invalid_dt,
    "%Y/-%m--/%d"
)
print("date obj converted from invalid date format:", dt)

dt = datetime.strptime(
    dt_12_hour_format,
    "%d-%m-%Y %I:%M:%S %p"
)
print("date obj converted from 12 hour format:", dt)

dt = datetime.strptime(
    dt_named_and_short_form_format,
    "%d-%B-%y %H:%M:%S"
)
print("date obj converted from dt_named_and_short_form_format:", dt)



# create datetime from ISO date string that is timezone aware
print("create date from tz aware date string")
datetime_iso = "2023-08-26 20:50:45+05:00"  # ISO 8601
dt_obj = datetime.fromisoformat(datetime_iso)
print(dt_obj.year)
print(dt_obj.tzinfo)


# create datetime from NON-ISO date string that is timezone aware
datetime_non_iso = "2023/08/26 20:50:45+05:00"  # non ISO
dt_obj = datetime.strptime(datetime_non_iso, "%Y/%m/%d %H:%M:%S%z")
print(dt_obj.year)
print(dt_obj.tzinfo)

# datetiem containd microseconds
datetime.strptime(
    "2023-01-01 23:59:59.123+02:00",
    "%Y-%m-%d %H:%M:%S.%f%z"
)

print(dt.year)


# ==================================================================


# create date time from integer
from datetime import date, datetime

my_day = 26
my_month = 8
my_year = 2023
d = date(
  day=26, 
  month=8, 
  year=2023
)
print("create datetime from integer")
print(d)
print(d.year)


# create date time from timestamp - number of seconds from 1970-Jan-01
ts = 1693029240 # number of seconds
ts_date = datetime.fromtimestamp(ts)
print("\ncreate datetime from timestamp")
print(ts_date)
print(ts_date.year)



# =================================================================


# pip install python-dateutil
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

# date manipulation using replace method of date object
print("date manipulation using replace method of date object")
dt = "2023-01-01 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print("original_date:", dt_obj)

updated_date = dt_obj.replace(year=2000, month=5, day=10)
print("updated_date:", updated_date)



# ===============================================================


# date manipulation using timedelta
print("\ndate manipulation using timedelta")
dt = "2023-01-01 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print("original_date:", dt_obj)
updated_date = dt_obj - timedelta(days=2)
print("updated_date:", updated_date)


# generate new dates
dt = "2023-01-05 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print(f"\ngenerate past dates from this date:\n{dt_obj}")

for i in range(1, 10):
    change_dt = dt_obj - timedelta(days=i)
    print("loop", change_dt)


# date manipulation using relativedelta to change year, month and day easily
print("\ndate manipulation using relativedelta to change year, month and day easily")
dt_1 = datetime.now()
print(dt_1)

x = dt_1 - relativedelta(months=2, year=1)
print(x)


dt_2 = datetime.now()
x = dt_2 + relativedelta(months=2, hours=2, days=4)
print(x)


# difference between timedelta and relativedelta
"""
timedelta deals with day and smaller units i.e day, hour, minute, second etc
relativedelta deals with units years, months, days.

timedelta arguments are singular
relativedelta arguments are plural
"""


# calculate difference between 2 dates
print("\ncalculate difference between 2 dates")
current_dt = datetime.now()
custom_dt = datetime.now()

custom_dt = custom_dt.replace(day=2)

print(custom_dt)
print(current_dt)

diff = current_dt - custom_dt
print(diff.days)
print(diff.total_seconds())





# ======================================================================


# pip install python-dateutil
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

# date manipulation using replace method of date object
print("date manipulation using replace method of date object")
dt = "2023-01-01 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print("original_date:", dt_obj)

updated_date = dt_obj.replace(year=2000, month=5, day=10)
print("updated_date:", updated_date)



# ======================================================================



# date manipulation using timedelta
print("\ndate manipulation using timedelta")
dt = "2023-01-01 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print("original_date:", dt_obj)
updated_date = dt_obj - timedelta(days=2)
print("updated_date:", updated_date)


# generate new dates
dt = "2023-01-05 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print(f"\ngenerate past dates from this date:\n{dt_obj}")

for i in range(1, 10):
    change_dt = dt_obj - timedelta(days=i)
    print("loop", change_dt)


# date manipulation using relativedelta to change year, month and day easily
print("\ndate manipulation using relativedelta to change year, month and day easily")
dt_1 = datetime.now()
print(dt_1)

x = dt_1 - relativedelta(months=2, year=1)
print(x)


dt_2 = datetime.now()
x = dt_2 + relativedelta(months=2, hours=2, days=4)
print(x)


# difference between timedelta and relativedelta
"""
timedelta deals with day and smaller units i.e day, hour, minute, second etc
relativedelta deals with units years, months, days.

timedelta arguments are singular
relativedelta arguments are plural
"""


# calculate difference between 2 dates
print("\ncalculate difference between 2 dates")
current_dt = datetime.now()
custom_dt = datetime.now()

custom_dt = custom_dt.replace(day=2)

print(custom_dt)
print(current_dt)

diff = current_dt - custom_dt
print(diff.days)
print(diff.total_seconds())



# ===============================================================




# display customized date format
from datetime import datetime, date

print("display customized date format")
date_iso = datetime.now()
print("iso_formatted_date:", date_iso)

pak_formatted_date = datetime.strftime(date_iso, "%d-%m-%Y")
print("pak formatted date:", pak_formatted_date)

us_formatted_date = datetime.strftime(date_iso, "%m/%d/%Y")
print("US formatted date:", us_formatted_date)

date_formatted_12_hour = datetime.strftime(date_iso, "%d-%m-%Y %I:%M:%S %p")
print("display date in 12 hours format:", date_formatted_12_hour)

date_formatted_24_hour = datetime.strftime(date_iso, "%Y-%m-d %H:%M:%S")
print("display date in 24 hours format:", date_formatted_24_hour)

date_formatted_with_weekday_name = datetime.strftime(date_iso, "%Y-%m-d %H:%M:%S %A")
print("display date in 24 hours format:", date_formatted_with_weekday_name)


# https://strftime.org/



# ===============================================================





# pip install pytz
import pytz
from datetime import datetime, timedelta

# display all the timezones in this module
print("display all the timezones in this module")
all_tz = pytz.all_timezones
print("all timezones", all_tz)
print(len(all_tz))

# create date object with timezone detail
print("\ncreate date object with timezone detail")
date_without_tz = datetime.now()
date_with_tz = datetime.now(tz=pytz.timezone("Asia/Karachi"))
print("date_without_tz", date_without_tz)
print("date_with_tz", date_with_tz)


# correct way: add timezone detail in unaware tz date object 
print("\nadd timezone detail in date object")
date_without_tz = datetime.now()
tz_detail = pytz.timezone("Asia/Karachi")
tz_aware_dt = tz_detail.localize(date_without_tz)
print("tz_aware_dt", tz_aware_dt)


# correct way: change timezone detail
print("\nchange timezone detail from KHI to Saudi Arab")
date_without_tz = datetime.now()
tz_detail = pytz.timezone("Asia/Karachi")
tz_aware_dt = tz_detail.localize(date_without_tz)
print("tz_aware_dt", tz_aware_dt)
tz_2_detail = pytz.timezone("Asia/Riyadh")
print("updated_tz_detail", tz_aware_dt.astimezone(tz_2_detail))


# parse date string with timezone detail
print("\nparse date string with timezone detail")
saudi_arab_dt_str = "2023-08-26 15:18:33.983780+03:00"
saudi_arab_dt_obj = datetime.strptime(saudi_arab_dt_str, "%Y-%m-%d %H:%M:%S.%f%z")
print(saudi_arab_dt_obj.tzinfo)



# wrong way of adding timezone detail
dt_str = "2023-08-15 15:50:00" # US/Pacific
dt_obj = datetime.fromisoformat(dt_str)
dt_obj = dt_obj.replace(tzinfo=pytz.timezone("Asia/Karachi"))


# wrong way of updating timezone detail
dt_obj = datetime.utcnow() # timezone 00:00
dt_obj_tz_aware = dt_obj.astimezone(pytz.timezone("Asia/Riyadh")) # this will assume UTC date as localtime
print("utcnow converted to tz aware date object")
print(dt_obj) # UTC
print(dt_obj_tz_aware) # wrong tz converted hour. it should add 3 hours in utc date and not subtract 2 hours


# changing date using replace/timedelta will not aware of the changing DST
print("\nchanging date using replace/timedelta will not aware of the changing DST")
tz_detail = pytz.timezone("US/Pacific")
dt_str = "2020-03-07 15:00:00"  # US/Pacific
dt_obj = datetime.fromisoformat(dt_str)
tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt, "before DST Activation")


print(tz_aware_dt.replace(day=9), "DST Activated on this day but our date obj doesn't know")
print(tz_aware_dt + timedelta(days=2), "DST Activated on this day but our date obj doesn't know")


tz_detail = pytz.timezone("US/Pacific")
dt_str = "2020-03-09 15:00:00"  # US/Pacific
dt_obj = datetime.fromisoformat(dt_str)
tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt, "DST Activated on this day and date obj is aware")



# ===============================================================


# get last day of the month
import calendar

month_r = calendar.monthrange(
    2023, 1
)
print("last day of the month jan 2023 is:", month_r[1])

month_r = calendar.monthrange(
    2023, 2
)
print("last day of the month feb 2023 is:", month_r[1])


month_r = calendar.monthrange(
    2023, 3
)
print("last day of the month mar 2023 is:", month_r[1])

month_r = calendar.monthrange(
    2023, 4
)
print("last day of the month apr 2023 is:", month_r[1])




























