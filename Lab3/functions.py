#1
def grams_to_ounces(grams):
    return 28.3495231 * grams

#2
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return (rabbits, chickens)
    return "No solution"

#4
def filter_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]

#5
import itertools
def string_permutations():
    user_input = input("Enter a string: ")
    permutations = itertools.permutations(user_input)
    for perm in permutations:
        print("".join(perm))

#6
def reverse_words_in_sentence():
    user_input = input("Enter a sentence: ")
    words = user_input.split()
    reversed_sentence = " ".join(reversed(words))
    print(reversed_sentence)

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i:i + 3] == [0, 0, 7]:
            return True
    return False

#9
import math
def volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

#10
def unique_elements(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return result

#11
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

