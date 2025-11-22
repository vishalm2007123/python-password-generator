import random
import string

def generate_random_string(length=10):
    alphabet = string.ascii_letters + string.digits+ string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password 
password = generate_random_string(12)
print("Generated Password:", password)