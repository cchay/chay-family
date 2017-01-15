## Christopher Chay, 2016.1.16
##Assignment 2: Make a list of my family and a dictionary of one memeber(name.age,gender)
## Grade: 100%

famList = [ "Chris", "MJ", "Callista", "Christopher", "Caleb", "Emmanuel", "Celesta" ]
print(famList)

famMemDict0 = {"gender": "male", "age": 46, "weight:" :205, "height": "5'8"}
famMemDict0e = {"gender": "female", "age": "~CLASSIFIED~", "weight:" : "~CLASSIFIED~", "height": "~5'5"}
famMemDict1 = { "gender": "female", "age": 16, "weight:" :125, "height": "5'3"}
print('Callista: ', famMemDict1)
famMemDict2 = {"gender": "male", "age": 14, "weight:" :132, "height": "5'7" }
famMemDict3 = {"gender": "male", "age": 12, "weight:" :120, "height": "5'1" }
famMemDict4 = {"gender": "male", "age": 10, "weight:" :120, "height": "5'0" }
famMemDict5 = {"gender": "female", "age": 7, "weight:" :64, "height": "3'10" }

question = input( '''Which family member would you like to see?
"c0"Chris
"c0e"MJ
"c1"Callista
"c2"Christopher
"c3"Caleb
"c4"Emmanuel
"c5"Celesta
''' )

if question == "c0":
   print("Chris:", famMemDict0)
elif question == "c0e":
   print("MJ:", famMemDict0e)
elif question == "c1":
   print("Callista:", famMemDict1)
elif question == "c2":
   print("Christopher:", famMemDict2)
elif question == "c3":
   print("Caleb:", famMemDict3)
elif question == "c4":
   print("Emmanuel:", famMemDict4)
elif question == "c5":
   print("Celesta:", famMemDict5)
