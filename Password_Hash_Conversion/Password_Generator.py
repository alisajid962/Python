import hashlib
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = generate_password()
print("Generated Password:", password)

stored_hash = hash_password(password)
print("Stored Hash:", stored_hash)

user_input = input("Enter your password: ")
if hash_password(user_input) == stored_hash:
    print("Password is correct! ")
    print("You are now Logged in. ")
else:
    print("Incorrect password.")
