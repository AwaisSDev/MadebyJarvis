"""
factorial of 5 numbers i input prints it too
"""

def factorial(n):
    """
    Calculate the factorial of a number.

    :param n: The number to calculate the factorial of.
    :return: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Prompt the user to input five numbers
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Print the factorial of each number
for num in numbers:
    print(f"The factorial of {num} is {factorial(num)}")