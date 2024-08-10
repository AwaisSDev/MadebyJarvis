# Project Description: prints factorial of 5
# Write code only

def factorial(n):
    """
    Calculate the factorial of a number.

    :param n: The number to calculate the factorial of.
    :return: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    number = 5
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
