# Import the calendar module
import calendar

# Use isleap() to determine the next leap year
from datetime import datetime

for i in range(datetime.today().year + 1, datetime.today().year + 5):
    if calendar.isleap(i):
        print(i)

# Find and use a function in the module calendar to determine how many leap 
# years there will be between years 2000 and 2050, inclusive.
c = 0

for i in range(2000, 2051):
    if calendar.isleap(i):
        c += 1

print(c)

# Find and use a function in module calendar to determine which day of the 
# week July 29, 2016 will be.
print(calendar.day_name[calendar.weekday(2016, calendar.JULY, 29)])
