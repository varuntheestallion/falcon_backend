from random import choice
from string import ascii_letters, digits


def create_random_code(size):
    available_chars = ascii_letters + digits
    return "".join([choice(available_chars) for _ in range(size)])
