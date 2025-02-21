def generate_squares(n):
    for i in range(n + 1):
        yield i ** 2

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = 5
for square in generate_squares(n):
    print(square)

n = int(input())
print(",".join(str(num) for num in even_numbers(n)))

n = 50
for num in divisible_by_3_and_4(n):
    print(num)

a, b = 3, 7
for square in squares(a, b):
    print(square)

n = 10
for num in countdown(n):
    print(num)
