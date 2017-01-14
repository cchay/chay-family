import datetime
import time

now = datetime.datetime(2016, 7, 2, 5, 17)
alarm1 = datetime.datetime(2016, 7, 2, 5, 18)
print(now)
print(alarm1)

while now != alarm1:
   time.sleep(1)
else:
   print('Timezzz up!!')
