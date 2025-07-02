import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Combine all types of characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("== Password Generator ==")
    try:
        user_length = int(input("Enter the desired password length: "))
        result = generate_password(user_length)
        print("\nGenerated Password:", result)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
