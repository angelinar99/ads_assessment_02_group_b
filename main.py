
"""
Palindromes
"""
#Task 1
# Provide your solution here
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]



print(is_palindrome("taco cat"))  # True
print(is_palindrome("Step on no cats"))  # True
print(is_palindrome("Never odd or even"))  #True
print(is_palindrome("Me no palindrome"))  #False


"""
Multiplication Table
"""
#Task 2
#Provide your solution here

def print_multiplication(number: int, rows: int) -> None:

    if number <= 0 or rows <= 0:
        print("Error: Number and rows cannot be less than 1.")
        return

    for i in range(1, rows + 1):
        print(f"{number} * {i} = {number * i}")

print_multiplication(6, 3)
print_multiplication(10,2)
print_multiplication(0, 0)
print_multiplication(-10, 2)
print_multiplication(2,-2)


