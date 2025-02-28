# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input number
num = int(input("Enter a number to calculate its factorial: "))

# Call the factorial function
result = factorial(num)

# Output the result
print(f"The factorial of {num} is {result}")
