#write a program that prints * 15 times on one line, repeat on 5 lines
#solution 1
# print("*" * 15)
# print("*" * 15)
# print("*" * 15)
# print("*" * 15)
# print("*" * 15)

#refactor to use a loop
#solution 2
# for i in range(5):
#     print("*" * 15)

#Solution 3
#refactor to use most efficient code
solution = ("*" * 15 + "\n") * 5
print(solution)

#write a program that prints 1 once then 2 twice then 3 three times up to 7 seven times
#solution 1
for i in range(1,8):
    print(str(i) * i)

#refactor to use most efficient code
solution = ""
for i in range(1,8):
    solution += str(i) * i + "\n"
print(solution)

#refactor
solution = ""
for i in range(1,8):
    solution += str(i) * i
    if i < 7:
        solution += "\n"
print(solution)

