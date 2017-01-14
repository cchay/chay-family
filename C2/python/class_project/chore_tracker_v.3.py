import pickle, sys, time

profiles = pickle.load(open('profiles.pickle', 'rb'))

profile = 'none'

class emptyProfile:
   def __init__(self):
      self.name = 'name'
      self.password = 'password'

class Profile:
   def __init__(self, name, password, profiles):
      self.name = name
      self.password = password
      self.tasks = profiles[self.name]['Tasks']

profile = emptyProfile()

class login:
   def opening(self):
      action = input('Welcome to Christopher Chay\'s Chore Tracker\nOptions:\n"1" Sign up\n"2" Log in\n"3" Updates\n"4" Quit\n')
      if action == '1':
         return login().create()
      elif action == '2':
         return login().login()
      elif action == '3':
         print('''New Updates:
2016.12.26-2016.12.27, Chore_Tracker v.3
   * Removed the annoying blocker in the sign up and login page
   * Task Presentation is so much cleaner and nicer to look at
   * Fixed the bug in the Profile section, you can now go back to the chore page without error
   * In the Sign up and Login page, you can type 'b' to go back to the main page at any time
   * Fixed spelling and various bugs
   * Put in some convenient confirmations 

2016.12.25, Chore_Tracker v.3
   * Program now allows you to log out and switch to a different profile
   * Typo's and other errors are more clearly pointed out
   * Re-wrote the instructions and guidelines so that it's much clearer
   * Edited the profile section so that you can change your username and/or password
   * And so much more that I can't remember
''')
         input('Press <ENTER> to return to the Opening page.')
         return login().opening()
        
      elif action == '4':
         with open('profiles.pickle', 'wb') as h:
            pickle.dump(profiles, h) 
         sys.exit()
        
      else:
         return login().opening()
    
   def login(self):
      print('Login Page')
      profile_name = input('Name: ')
      if profile_name == 'b':
         return login().opening()
         
      password = input('Password: ')
      if password == 'b':
         return login().opening()

      for i in profiles:
         if profile_name in profiles:
            if password == profiles[profile_name]['Password']:
               time.sleep(0.5)
               print('\n...Welcome, {profile}...' .format(profile = profile_name))
               time.sleep(1)
               profile.name = profile_name
               profile.password = password
               break
            else:
               print('The name or password was incorrect.')
               print('Type "b" in the password or profile name area if you want to back to the main page.')
               input('Press <ENTER> to continue')
               print('\n\n')
               return login().login()
         
         else:
            print('The name or password was incorrect.')
            print('Type "b" in the password or profile name area if you want to back to the main page.')
            input('Press <ENTER> to continue')
            print('\n\n')
            return login().login()
            


   def create(self):
      print('Sign up Page')
      new_profile = input('New Username: ')
      if new_profile == 'b':
         return login().opening()
      
      new_password = input('New Password: ')
      if new_password == 'b':
         return login().opening()
      

      if new_profile != '' and new_password != '':
         if not new_profile in profiles:
            print('Are you satisfied with Profile name: {}, and Profile password: {} ?' .format(new_profile, new_password))
            confirm = input('(y/n) ')
            if confirm == 'y':
               profiles[new_profile] = {'Password': new_password, 'Tasks': {}}
               profile.name = new_profile
               profile.password = new_password
               print('Profile successfully created! Welcome {}' .format(profile.name))
               input('Press <ENTER> to continue')
            else:
               return login().create()
         else:
            print('ERROR: Profile name already exists!')
            print('Type "b" in the password or profile name area if you want to back to the main page.')
            input('Press <ENTER> to continue')
            print('\n\n')
            return login().create()
      else:
         print('ERROR: You failed to fill out one of the forms.')
         print('Type "b" in the password or profile name area if you want to back to the main page.')
         input('Press <ENTER> to continue')
         print('\n\n')
         return login().create()
         



def editProfile():
   print('\nName: {name}\nPassword: {password}' .format(password = profile.password, name = profile.name))
   print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')    
   action = input('''Options:
    "e" (Edit the profile name and/or the password)
    "d" (Deletes the profile for ever)
    "b" (Goes back to the main chore page)
    "q" (Exits and saves the program)
Input: ''')

   if 'd' in action:
      confirm = input('Are you sure you wish to delete this account? (y/n)')
      if confirm == 'y':
         del profiles[profile.name]
         return login().opening()

      else:
         return editProfile()


   elif 'e' in action:
      action = input('''What would you like to change?
"n" (Change Name)
"p" (Change Password)
''')
      if action == 'n':
         new_profile_name = input('New Profile Name: ')
         if new_profile_name != '':
            profiles[new_profile_name] = profiles[profile.name]
            del profiles[profile.name]
            profile.name = new_profile_name
            print('SYSTEM: Profile Name changed')
            input('Press <ENTER> to continue')
            print('\n\n')
            return editProfile()
         else:
            print('Invalid Username!')
            return editProfile()


      elif action == 'p':
         new_password = input('New Password: ')
         if new_password != '':
            profile.password = new_password
            profiles[profile.name]['Password'] = profile.password
            print('SYSTEM: Profile Password changed')
            input('Press <ENTER> to continue')
            print('\n\n')
            return editProfile()
         else:
            print('Invalid Password!')
            return editProfile()


      else:
         print('ERROR: Typo!')
         return editProfile()


   elif action == 'b':
      return main()


   elif action == 'q':
      with open('profiles.pickle', 'wb') as h:
         pickle.dump(profiles, h) 
      sys.exit()
            
   else:
      print('Oops! You typed something wrong.')
      return editProfile()



    
def main():
   print('\nTasks:')
   for chores in profiles[profile.name]['Tasks']:
      for task in profiles[profile.name]['Tasks'][chores]:
         print('{}: {}' .format(chores, task))

   print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Chore options:
    "a" (add a new chore)
    "c" (change an existing chore)
    "d" (delete an existing chore)
Other Options:
    "p" (view profile settings)
    "l" (Log out and switch to another profile)
    "s" (Saves changes)
    "q" (Saves and exits program)''')
   action = input('Input: ')


   if action == 'c':
      try:
         task_name = input('What is the name of the task? ')
         if task_name in profiles[profile.name]['Tasks']:
            pass
         else:
            print('ERROR: Task does not exist in task list')
            input('Press <ENTER> to continue')
            print('\n\n')
            return main()
            
         new_task = input('What is the new task? ')
         for tasks in profiles[profile.name]:
            if task_name in profiles[profile.name]['Tasks']:
               profiles[profile.name]['Tasks'][task_name] = [new_task]
      except ValueError as e:
         print('ERROR: You typed something wrong')
      except KeyError as e:
         print('ERROR: You typed something wrong')
      
      print('SYSTEM: Task changed')


   elif action == 'd':
      try:
         del_task = input('What is the name of the task you wan to delete? ')
         confirm = input('Are you sure you wish to delete this task? (y/n)')
         if confirm == 'y':
            del profiles[profile.name]['Tasks'][del_task]
            print('SYSTEM: Task deleted')
         else:
            pass
            
      except ValueError as e:
         print('ERROR: Task does not exist in task list')
      except KeyError as e:
         print('ERROR: Task does not exist in task list')    
         

   elif action == 'a':
      try:
         new_task_name = input('What is the new task name? ')
         new_task = input('What is the new task? ')
        
         if new_task != '':
            if not new_task_name in profiles[profile.name]['Tasks']:
               profiles[profile.name]['Tasks'][new_task_name] = [new_task]
               print('SYSTEM: Task created')
            else:
               print('Task already exists.')
         else:
            print('You failed to name the task.')
            input('Press <ENTER> to continue')
            print('\n\n')


      except ValueError as e:
         print('ERROR: You typed something wrong')
      except KeyError as e:
         print('ERROR: You typed something wrong')
     
            
   elif action == 'q':
      with open('profiles.pickle', 'wb') as h:
         pickle.dump(profiles, h)
      print('SYSTEM: Quiting...') 
      sys.exit()
  
  
   elif action == 's':
      with open('profiles.pickle', 'wb') as h:
            pickle.dump(profiles, h)
      print('SYSTEM: All changes saved')
    
    
   elif action == 'p':
      return editProfile()


   elif action == "l":
      with open('profiles.pickle', 'wb') as h:
            pickle.dump(profiles, h)
      return login().opening()


   else:
      print('ERROR: Misspelled something or You didn\'t type anything!')
   
   input('Press <ENTER> to continue')
   print('\n\n')
   return main()
    
def navigation():
   main()
   return navigation()


login().opening()
profile = Profile(profile.name, profile.password, profiles)

print('----------------------------------------------------------------')

while True:
   navigation()
