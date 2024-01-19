# Write a script that takes in a grade from 0-100 inclusive (include both 0 and 100 in the range). 
# Assuming a normal 10 point grading scale, print off whether the user got an A, B, C, D, or F.

x = int(input("Enter Grade: "))

if x >= 90 and x <= 100:
    letter_grade = 'A'
elif x >= 80 and x < 90:
    letter_grade = 'B'
elif x >= 70 and x < 80:
    letter_grade = 'C'
elif x >=60 and x < 70:
    letter_grade = 'D'
elif x < 0:
    print('Number must be greater than zero.')
    letter_grade = 'does not exist' 
else:
    letter_grade = 'F'
    
print(f'Your letter grade is {letter_grade}')
    
