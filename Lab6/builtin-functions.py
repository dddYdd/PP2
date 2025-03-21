#1
import math
import time

numbers = [2, 3, 4, 5]
result = math.prod(numbers)
print("Product of the list:", result)

#2
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

sample_text = "Hello World"
count_case(sample_text)

#3
def is_palindrome(s):
    return s == s[::-1]

test_string = "madam"
print(f"Is '{test_string}' a palindrome?:", is_palindrome(test_string))

#4
number = 25100
delay_ms = 2123

time.sleep(delay_ms / 1000)
sqrt_result = math.sqrt(number)
print(f"Square root of {number} after {delay_ms} milliseconds is {sqrt_result}")

#5
t = (True, 1, "non-empty", 5)
print("All elements are True?:", all(t))
