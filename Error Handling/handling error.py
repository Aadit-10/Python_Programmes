try:
   with open('input.txt','r') as myinputfile:
       print("hoow u doing")
       for line in myinputfile:
           print(line)
except FileNotFoundError:
    print("No file exist")
finally:
    print('I show up after every exception')
print("mahnnnn")