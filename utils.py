import string, random

def generate_random_code(length = 7, chars = string.ascii_letters + string.digits):
    return ''.join([random.choice(chars) for _ in range(length)])