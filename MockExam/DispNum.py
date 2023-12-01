#The program should prompt the user to enter a positive number and then prints the corresponding output on the screen.
# For example:
# def input_dat(num):
#     input_dat = input("Enter a positive number: ") 
    
#     if input_dat > 0:
#         print("1 2 3 4 5")
#     else:
#         print("Invalid input")

# input_dat = input("Enter a positive number: ")
# if int(input_dat) > 0:
#     for i in range(1, int(input_dat) + 1):
#         print(str(i) * i)
# elif int(input_dat) < 0:
#     print("Invalid input")
# else:
#     print("0")


# solution1 = input("Enter a positive number: ")
# for i in range(1, int(solution1) + 1):
#     print(str(i) * i)


# print(input_dat)
prompt = int(input("Enter a positive number: "))
solution = [str(i) * i for i in range(1, prompt + 1)]
print(solution)