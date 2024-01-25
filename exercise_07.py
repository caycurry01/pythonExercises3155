# Take in a string from the user and split it into an array of single characters. Split the list of characters into a list of lists where each inner list has 3 elements. 
# Notice that the last inner array may have fewer than 3 elements.

string = str(input('Enter string: '))
list = []
list_bits = []

for i in string:
    list.append(i)

for i in range(0, len(list), 3):
    list_bits.append(list[i:i+3])

print(list_bits)
