import pickle, time, sys
player_profile = pickle.load(open('/home/iceman/_/chay-family/c2/python/games/rpg-techno-game/data/rpg-techno-game-data.pickle', 'rb'))

empty_starterdict = {'bits': 100, 
'weapons': {'right hand': 0, 'lefthand': 0, 'bothhands': 0}, 
'xp': 0, 
'name': '', 
'maxhp': 75, 
'attributes': {'strength': 1, 'agility': 1}, 
'weapon': 'bitnbyte sword', 
'inventory': [], 
'level': 1, 
'armour': {'legs': {'sprice': 12, 'name': 'bitnbyte pants', 'armour': 3, 'bprice': 15},
           'torso': {'sprice': 100, 'name': 'bitnbyte platemail', 'armour': 4, 'bprice': 125},
           'feet': {'sprice': 0, 'name': 'none', 'armour': 0, 'bprice': 0},
           'head': {'sprice': 0, 'name': 'none', 'armour': 0, 'bprice': 0},
           'hands': {'sprice': 0, 'name': 'none', 'armour': 0, 'bprice': 0}}, 'hp': 75, 'password': '', 'wdamage': 10, 'skills': {'dodge': {'cost': 5, 'level': 1}, 'slash': {'cost': 5, 'level': 1, 'damage': 10}}}






class login():
   def __init__(self):
      self.username = ''
      self.password  = ''   
   
   def welcome(self):
      loginattempts = 0
      print('Welcome to RTG')
      print('Would you like to login or create a new account? (login/create)')
      answer = input('*\: ')
      
      if answer == "login":
         return login().login(loginattempts)
      
      elif answer == "create":
         return login().create()
      
      else:
         return login().welcome()
      
       

   def login(self, loginattempts):
      print('please type in your player name and password')
      username = input('Username*\: ')
      password = input('Password*\: ')
      self.username = username
      self.password = password
      

      
      if self.username in player_profile:
         if self.password == player_profile[self.username]['password']:
            print(self.username)
            print('Welcome, {}.' .format(self.username))
            time.sleep(2)


         
      else:
         if loginattempts >= 3:
            print('Would you like to go back to the welcome page? (yes/no)')
            answer = input('*\: ')
            if answer == "yes":
               return login().welcome()
            else:
               return login().login(loginattempts)
            
         print('Your username or password is incorrect. Please try again.')
         loginattempts += 1
         print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
         return login().login(loginattempts)
      
      
      
   
   def create(self):
      print('Okay, Let\'s create your character.')
      username = input('What is the name of your charcter?(it is the same as your username)*\: ')
      password = input('What is the password? *\: ')
      
      if username in player_profile:
         input('Username already taken. Press ENTER to continue')
         return login().create()
      
      self.username = username
      self.password = password
      
      player_profile[self.username] = empty_starterdict
      player_profile[self.username]['name'] = username
      player_profile[self.username]['password'] = password

