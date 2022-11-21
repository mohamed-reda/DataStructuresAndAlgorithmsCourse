last_num = 0
a = 71
b = 3
m = 7

# It will generate all the numbers before repeating if:
# B, M are relatively prime
# A - 1 is divisible by prime factors of M
# A - 1 is multiple of 4 if M is
print(17 ** (1 / 2))
for i in range(9):
    x = (last_num * a + b) % m
    print(f'try numb {i + 1} is: {x}')
    last_num = x

# the output:
"""
try numb 1 is: 3
try numb 2 is: 6
try numb 3 is: 2
try numb 4 is: 5
try numb 5 is: 1
try numb 6 is: 4
try numb 7 is: 0
try numb 8 is: 3
try numb 9 is: 6
"""
