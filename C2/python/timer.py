import time
import datetime

year = 2016
month = 7#int(input('What month is it?(in numeral, like: jan.=1, Mar=3 etc.) '))
day = 26#int(input('What day is it? '))
hour = 4#int(input('What o\'clock is it? '))
minute = 15#int(input('What minute is it? '))

right_now = datetime.datetime(year, month, day, hour, minute)
print(right_now.now())

