import random
import string


def get_random_string(count):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=count))

def get_random_username(count_of_letters):
    return ''.join(random.choices(string.ascii_letters, k=count_of_letters))
