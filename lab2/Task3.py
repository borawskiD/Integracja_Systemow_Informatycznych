import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    elements = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(elements) for i in range(length))
    return result_str


print(get_random_string(8))

with open('passwords.txt', 'w') as f:
    for i in range(999):
        f.write(get_random_string(6))
        f.write("\n")
