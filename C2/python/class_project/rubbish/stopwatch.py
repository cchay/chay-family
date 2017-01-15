import datetime
import time


today  = datetime.datetime(2016, 9, 22, 8, 23)


def stopWatch():
   print('Press <ENTER> to start a new stop watch.')
   input()
   print('Started')
   start_time = time.time()
   last_time = start_time
   while True:
      try:
         last_time = time.time()
         last_time-= start_time
         time.sleep(1)
         print(round(last_time))
      except KeyboardInterrupt:
         break

   end_time = time.time()
   end_time -= start_time
   print('\nStopped')
   print(round(end_time/60, 2), ' minutes.')
   return timer()



#stopWatch()


def hr_timer():
   print('Type the amount of hours to start a timer.')
   hours = int(input())
   minutes = 60
   seconds = 60
   print('Started')
   for i in range(hours-1, -1, -1):
      for a in range(minutes-1, -1, -1):
         for b in range(seconds, -1, -1):
            time.sleep(1)
            print(str(i) + ':' + str(a) + ':' + str(b))


   return timer()



def mi_timer():
   print('Type the amount of minutes to start a timer.')
   minutes = int(input())
   seconds = 60
   print('Started')
   for a in range(minutes-1, -1, -1):
      for b in range(seconds, -1, -1):
         time.sleep(1)
         print(str(a) + ':' + str(b))


   print('\nStopped')
   return timer()





def showTime(hr, mi, se):
   print(str(hr) + ':' + str(mi) + ':' + str(se))


def navigation(time):
   if time == 'mt':
      return mi_timer()

   elif time == 'ht':
      return hr_timer()

   elif time == 'sw':
      return stopWatch()

   else:
      return timer()

def timer():
   try:
      while True:
         user_input = input('Type:\n"mt"(minute timer)\n"ht"(hour timer)\n"sw"(stopwatch)\n')
         print(navigation(user_input))
         
   except KeyboardInterrupt:
      return timer()

today.now()
timer()
   
'''
while True:
   print('Press <ENTER> to start a new stop watch.')
   input()
   print('Started')
   start_time = time.time()
   last_time = start_time
   
   while True:
      try:
         last_time += time.time()
         time.sleep(0.001)
         print(last_time)
      except KeyboardInterrupt:
         break

   end_time = time.time()
   end_time -= last_time
   print(end_time)
'''
