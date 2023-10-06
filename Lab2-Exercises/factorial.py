# Function to calculate the factorial of an integer
def factorial(n):
    # Initialize the result to 1
    result = 1

    # Handle the case for n = 0 (0! = 1)
    if n == 0:
        return result

    # Use a loop to multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i

    return result

# Input: Ask the user for an integer
n = int(input("Enter an integer to calculate its factorial: "))

# Calculate and display the factorial
if n < 0:
    print("Factorial is undefined for negative integers.")
else:
    result = factorial(n)
    print(f"{n}! = {result}")
