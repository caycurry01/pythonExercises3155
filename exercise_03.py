# Take in a number, n, from the user. Then, take in n integers from the user and store them in a list. For instance, if the user enters 4, then the user will have to enter 4 numbers. 
# Print the list and the median of the list.

num = int(input('Enter a number: '))
da_list = []
counter = 1

while num > 0:
    number = int(input(f'Enter number {counter}: ' ))
    da_list.append(number)
    counter+=1
    num -=1

da_list.sort()
mid = len(da_list)//2
res = (da_list[mid]+ da_list[~mid])/2
print(da_list)
print("Median of list is : " + str(res)) 
