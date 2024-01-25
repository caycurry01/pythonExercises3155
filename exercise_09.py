def get_valid_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

sum_result = 0
counter = 1
for _ in range(5):
    user_input = get_valid_integer_input(f"Enter an int #{counter}: ")
    sum_result += user_input
    counter += 1

print("\nYour sum is: ", sum_result)
