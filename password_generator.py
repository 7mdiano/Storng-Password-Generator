
import string
import random

def generate_password(pwd_length):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    nums = list(string.digits)
    punc = list(string.punctuation)

    random.shuffle(lower)
    random.shuffle(upper)
    random.shuffle(nums)
    random.shuffle(punc)

    part1 = round(pwd_length*30/100)
    part2 = round(pwd_length*20/100)

    password = []

    for i in range(part1):
        password.append(lower[i])
        password.append(upper[i])

    for i in range(part2):
        password.append(nums[i])
        password.append(punc[i])

    random.shuffle(password)
    password = "".join(password[0:])

    return password


length = input("Password Length: ")

while True:
    try:
        length = int(length)
        if length < 6:
            print("you need at least 6 characters")
            length = input("Password Length: ")
        else:
            break
    except ValueError:
        print("Please enter Integer only!")
        length = input("Password Length: ")

generate_password(length)
