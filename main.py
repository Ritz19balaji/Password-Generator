import random
import string

def generate_password(length=12):
    """Generate a strong random password with the given length."""
    if length < 6:
        print("Password length should be at least 6 characters for security.")
        return None

    # Define character pools
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure password contains at least one of each required type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    return "".join(password)

# Take user input for password length
length = int(input("Enter desired password length: "))

# Generate and display the password
password = generate_password(length)
if password:
    print(f"Generated Password: {password}")
