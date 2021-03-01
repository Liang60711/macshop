import random
import string

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

slug=create_ref_code()
print(slug)