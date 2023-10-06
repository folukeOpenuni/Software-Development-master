import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant (D)
    D = b**2 - 4*a*c

    # Check if D is non-negative for real roots
    if D >= 0:
        # Calculate the two real roots
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        return root1, root2
    else:
        return None  # No real roots exist

# Example usage:
a = 2
b = -5
c = 3
roots = solve_quadratic(a, b, c)

if roots is not None:
    print("Real Roots:")
    print(f"Root 1: {roots[0]}")
    print(f"Root 2: {roots[1]}")
else:
    print("No real roots exist because the discriminant is negative.")
