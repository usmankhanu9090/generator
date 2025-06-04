import random
import strings
import os

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password string

# Main function to prompt the user for password length and generate a password
def main():
    print("Password Generator - Generate a Random Password")
    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        if length <= 0:
            print("Password length must be a positive integer.")
            return
        
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
