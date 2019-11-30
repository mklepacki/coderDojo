import random

def random_int():
    return random.randint(1, 10000)

def random_int2():
    return random.randint(1,100)

def add_randoms():
    print(random_int() + random_int2())

print('To jest nazwa pliku coder_random.py:', __name__)
if __name__ == "__main__":
    print('To sie wydarzy poniewaz jestem w pliku coder_random')
    add_randoms()