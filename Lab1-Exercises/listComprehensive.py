#use list comprehensive for an efficent solution 
# Using a list comprehension to create a list of numbers from 1 to 6
numbers_a = [num for num in range(1, 7)]
numbers_b = [num for num in range(2, 13, 2)]
numbers_c = [num for num in range(4, 80, 15)]
numbers_d = [num for num in range(30, -30, -10)]
numbers_e = [num for num in range(-7, 4, 20)]
numbers_f = [num for num in range(97, 80, 2)]
numbers_g = [num for num in range(-4, 100, 18)]

# Printing the list
print("a:", numbers_a)
print("b:", numbers_b)
print("c:", numbers_c)
print("d:", numbers_d)
print("e:", numbers_e)
print("f:", numbers_f)
print("g:", numbers_g)

def numOfPrint(number_of_line, value_to_print):
    print 