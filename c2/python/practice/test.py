entry_number = 1

file = open('prac.py', 'w')
file.write('Top Scores:\n\nName:\tScore:\nChris\t1234 pts')
file.close()
file = open('prac.py', 'r')
print(file.read())
file.close()
