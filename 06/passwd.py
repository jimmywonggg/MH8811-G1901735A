import random
import re

# create string that have a mix of lowercase letters, uppercase letters, numbers, and symbols
strs = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def genPassword(n):
    global strs
    if n < 4:
	    n = 4
    # loop
    while True:
        # create password
        password = ''.join(random.choices(strs, k=n))
        if re.search(r'[0-9]', password) and re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', password):
            return password


if __name__ == '__main__':
    p = genPassword(12)
    print(p)