#For this exercise, accept a string input from the user and pass that input to a function. That function should count the lowercased letters
# of the string in a dictionary and then return that dictionary.

def count_lowercase(input_string):
    letter_count = {}

    for char in input_string:
        if char.isalpha():
            # Convert the letter to lowercase
            char = char.lower()
            # Update the letter count in the dictionary
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

user_input = input("Enter a string: ")
result_dict = count_lowercase(user_input)

print("\nResulting Dictionary:")
print(result_dict)
