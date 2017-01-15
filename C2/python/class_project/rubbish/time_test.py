import time

def countdown(number):
   number = int(number)
   total_time = 60
   for i in range(int(number)-1):
      time.sleep(1)
      print(number)
      number -= 1 

countdown(input('number: '))
