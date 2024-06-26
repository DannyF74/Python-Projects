# DATETIME CHALLENGE REQUIREMENTS

# 1. Import the datetime module and any others to aid in time zone calculations.

# 2. Create a script that will find out the current times in the Portland HQ and NYC and London branches. 
# Then, compare that time with each branch's hours to see if they are open or closed.

# 3. Print out to the screen the three branches and whether they are open or closed.


# Imported the datetime and pytz modules. I had to install the pytz 
# module using the following command in the command line:
# pip install pytz
import datetime
import pytz
from pytz import timezone

# Used print(pytz.all_timezones) to find the names of the timezones
# I needed to use and created variables with the full date time
# of the locations required.
now_portland = datetime.datetime.now(timezone('US/Pacific'))
now_nyc = datetime.datetime.now(timezone('US/Eastern'))
now_london = datetime.datetime.now(timezone('Europe/London'))

# Created a new variable to store just the current hours minutes and
# seconds of the time zone. I then printed these so the user can
# clearly see the current time in each location
pdx_time = now_portland.strftime("%X")
nyc_time = now_nyc.strftime("%X")
ldn_time = now_london.strftime("%X")

print("\nThe time in Portland, OR is currently: " + str(pdx_time))
print("The time in New York City, NY is currently: " + str(nyc_time))
print("The time in London, England is currently: " + str(ldn_time))

# Set the open and close times of the offices and showed the user
# the times.
open = datetime.time(9, 00)
close = datetime.time(17, 00)
print("\nOur opening hours are between " + str(open) + " and " + str(close))

# Created a new variable to check current times against the open 
# and close times. Then used an if/else statement to display
# if each location was open or closed.
pdx_time_chk = now_portland.time()
if pdx_time_chk > open and pdx_time_chk < close:
    print("\nOur Portland office is open")
else:
    print("\nOur Portland office is closed")

nyc_time_chk = now_nyc.time()
if nyc_time_chk > open and nyc_time_chk < close:
    print("Our New York office is open")
else:
    print("Our New York office is closed")

ldn_time_chk = now_london.time()
if ldn_time_chk > open and ldn_time_chk < close:
    print("Our London office is open")
else:
    print("Our London office is closed")
