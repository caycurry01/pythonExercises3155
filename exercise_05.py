# Create a 2D list of space 5x5 filled with zeroes. Take in three coordinates (row and column) from the user. 
# Modify the list to store 1s in the space of the entered coordinates. Print out resulting matrix.

list_of_zeroes = [0, 0, 0, 0, 0]
row0 = int(input('Enter row for foroordiate 0: '))
col0 = int(input('Enter column for coordinate 0: '))
row1 = int(input('Enter row for foroordiate 1: '))
col1 = int(input('Enter column for coordinate 1: '))
row2 = int(input('Enter row for foroordiate 2: '))
col2 = int(input('Enter column for coordinate 2: '))

for row in range(1):
    for col in range(5):
        print(*list_of_zeroes)
    