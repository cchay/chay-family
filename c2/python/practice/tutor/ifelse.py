name = input('Enter a name: ')

while name != "bye":
   name = input('Enter a name: ')
   if name == "bye":
      break
      
   if name == "booboo" or name == "toad":
      print( 'You are wealcome' )
   elif name == "brian" or name == "lotso":
      print( 'Good to see you!!' )
   elif name == "Drago":
      print( 'Get outta here crazy man!!' )
   elif 'harry potter' in name or name == "harmoin" or name == "draygo":
      print( 'Wizads!! Die!!' )
   else:
      print( 'Hi.' )
