# Take in 5 integers from the user and store them in a list. Then take in another 5 integers and store them in a separate list. 
# Create a third array containing just the common values from both arrays without storing duplicates duplicates. Print out all three lists.

da_first_list = []
da_second_list = []
da_common_list = []

num = 5
other_num = 5

while num > 0:
    x = int(input('Enter a number for the first list: '))
    num -= 1
    da_first_list.append(x)
    
while other_num > 0:
    y = int(input('Enter a number for the second list: '))
    other_num-= 1
    da_second_list.append(y)
    
for i in da_first_list:
    for j in da_second_list:
        if i == j:
            da_common_list.append(j)
da_common_list = list(set(da_common_list))
            

print(f'First List: {da_first_list}')
print(f'Second List: {da_second_list}')
print(f'Common List: {da_common_list}')

