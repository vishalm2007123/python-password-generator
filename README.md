# 🔐 Python Password Generator

This is a simple **random password generator** written in Python.  
It generates strong passwords using **letters, digits, and special characters**.

This is my **first project as a first-year Cybersecurity student**, created to practice Python and basic security concepts.

---

## 🚀 Features
- Generates completely random passwords  
- Uses uppercase, lowercase, digits, and punctuation  
- Default password length = 12  
- Easy to modify for any length  

---

## 🧠 How It Works
The script uses:
- `string` for character sets
- `random` to pick characters randomly

```python
import random
import string

def generate_random_string(length=10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password 

password = generate_random_string(12)
print("Generated Password:", password)
