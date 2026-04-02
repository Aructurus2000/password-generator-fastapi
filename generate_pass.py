import string
from random import choice, shuffle

chars1 = [c for c in string.ascii_uppercase if c not in 'OI']
chars2 = [c for c in string.ascii_lowercase if c not in 'ol']
chars3 = list(string.digits[2:])
chars = chars1 + chars2 + chars3

def generate_password(length):
    res = [choice(i) for i in (chars1, chars2, chars3)] + [choice(chars) for _ in range(3, length)]
    shuffle(res)
    return ''.join(res)

def generate_passwords(count, length):
    res = set()
    while len(res) < count:
        res.add(generate_password(length))
    return list(res)

for i in generate_passwords(int(input()), int(input())):
    print(i)