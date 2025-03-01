import re

#1
p1 = re.compile(r'^ab*$')
test_strings1 = ['a', 'ab', 'abb', 'ac', 'b']
for s in test_strings1:
    if p1.fullmatch(s):
        print(f"'{s}' m")
    else:
        print(f"'{s}' does not m")
print()

#2
p2 = re.compile(r'^ab{2,3}$')
test_strings2 = ['ab', 'abb', 'abbb', 'abbbb']
for s in test_strings2:
    if p2.fullmatch(s):
        print(f"'{s}' m")
    else:
        print(f"'{s}' does not m")
print()

#3
p3 = re.compile(r'\b[a-z]+_[a-z]+\b')
text3 = "examples some more here"
m3 = p3.findall(text3)
print("m found:", m3)
print()

#4
p4 = re.compile(r'\b[A-Z][a-z]+\b')
text4 = "Test for ABC BCs"
m4 = p4.findall(text4)
print("m found:", m4)
print()

#5
p5 = re.compile(r'^a.*b$')
test_strings5 = ["acccb", "a123b", "ab", "a", "b", "aXYZb", "a\nb"]
for s in test_strings5:
    if p5.fullmatch(s):
        print(f"'{s}' m")
    else:
        print(f"'{s}' does not m")
print()

#6
text6 = "Hello, Test TEst Test"
result6 = re.sub(r'[ ,\.]', ':', text6)
print("Result:", result6)
print()

#7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

snake_str = "this_is_snake_case"
camel_str = snake_to_camel(snake_str)
print(f"Snake case: {snake_str}")
print(f"Camel case: {camel_str}")
print()

#8
text8 = "SplitSplitSplit"
parts8 = re.split(r'(?=[A-Z])', text8)
parts8 = [part for part in parts8 if part]
print("Parts:", parts8)
print()

#9
text9 = "HellloHellooMEmMemEM"
result9 = re.sub(r'(?<!^)(?=[A-Z])', ' ', text9)
print("Result:", result9)
print()

#10
def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

camel_str2 = "CamelCASe"
snake_str2 = camel_to_snake(camel_str2)
print(f"Camel case: {camel_str2}")
print(f"Snake case: {snake_str2}")
