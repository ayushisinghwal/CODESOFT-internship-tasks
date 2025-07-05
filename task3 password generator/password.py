import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for _ in range(length):
        password += random.choice(characters)

    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password should be at least 4 characters long.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
