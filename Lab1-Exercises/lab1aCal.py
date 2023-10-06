def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '//':#ineger dividion returns value with no floating num
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':#exponetial
        return num1 ** num2
    else:
        return "Invalid operator"

# Examples of using the calculate function:
result1 = calculate(-9, 5, '/')
result2 = calculate(695, 20, '%')
result3 = calculate(7, 6 * 5, '+')
result4 = calculate(7 * 6, 5, '+')
result5 = calculate(248 % 100, 5, '/')
result6 = calculate(6 * 3, 9 / 4, '-')
result7 = calculate((5 - 7) * 4, None, None)
result8 = calculate(6, 18 % (17 - 12), '+')
result9 = calculate(20, 10, '**')

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
