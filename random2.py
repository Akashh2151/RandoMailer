# random2.py

import random
import string

def generate_random_email():
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    domain = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    extension = random.choice(['com', 'net', 'org', 'edu'])
    return f'{username}@{domain}.{extension}'
