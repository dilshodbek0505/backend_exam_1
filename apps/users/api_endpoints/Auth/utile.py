import random
import string


def generate_code():
    return ''.join(random.choice(string.digits, k=6))
