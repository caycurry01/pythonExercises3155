# Write a script that takes in two strings from the user. If one string is the suffix of the other string, print the suffix, otherwise, print "No suffix found".

first_string = str(input('Enter first String: '))
second_string = str(input('Enter second String: '))


if second_string in first_string:
    print(second_string)
else:
    print('Suffix not found')

    
    

