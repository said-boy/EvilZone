print('Challenge: Encoding 1')
print()
number = input('Figure out what this says: ')
a = number.split(' ')
result = ''
for i in a:
    result += chr(int(i))
print(f"Solve Challenge \t : {result}")