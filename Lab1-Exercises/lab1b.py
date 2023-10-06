#question 1

# Define the number of iterations (number of rows)
num_iterations = 6
border = print("+" + "-" * 4 + "+")


# Top border
border
# Loop to generate the pattern
for i in range(num_iterations):
    if i % 2 == 0:
        print("\\" + " " * 2 + "/" + " " * 2)
    else:
        print("/" + " " * 2 + "\\" + " " * 2)

# Bottom border
border

#question 2
# Define the number of rows and columns
num_rows = 5
num_columns = 10

# Generate and print the pattern using list comprehension
# new_list = [expression for item in iterable if condition]
pattern = ['*' * num_columns for _ in range(num_rows)]
print('\n'.join(pattern))

#an example of a simple list comprehension:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]

#question 3
for num in range(1,7):
    print("a: ", num)

for num in range(2, 7, 2):
    print("b: ", num)

# for num in range(-7, 4, 13):
#     print("b: ", num)

#use list comprehensive for an efficent solution 
# Using a list comprehension to create a list of numbers from 1 to 6
numbers_a = [num for num in range(1, 7)]
numbers_b = [num for num in range(2, 13, 2)]
numbers_c = [num for num in range(4, 80, 15)]
numbers_d = [num for num in range(30, -30, -10)]
numbers_e = [num for num in range(-7, 4, 20)] #not working
numbers_f = [num for num in range(97, 80, 2)]

# Printing the list
print("a:", numbers_a)
print("b:", numbers_b)
print("c:", numbers_c)
print("d:", numbers_d)
print("e:", numbers_e)
print("f:", numbers_f)
