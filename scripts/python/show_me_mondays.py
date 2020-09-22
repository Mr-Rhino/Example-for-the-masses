import datetime
import calendar
from sys import argv
script, startmonth, startyear = argv
#
days = []
def calculate():
  oneday = datetime.timedelta(days=1)
  oneweek = datetime.timedelta(days=7)
#
  month = int(startmonth)
  year = int(startyear)
  start = datetime.date(month=month, day=1, year=year)
  while start.weekday() != 0:
    start += oneday
#

  while start.year == year:
    days.append(start)
    start += oneweek
#
calculate()
print (days)
