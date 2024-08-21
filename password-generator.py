import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

#password = ''.join(random.choice(characters) for i in range(8))

def main():
    while True:
        try:
            password_size = int(input("Enter the size of the password you want to generate: "))
            password = generate_password(password_size)
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            break
    print(f"Your generated password is >_ {password}")

def generate_password(size=8):
    password = ""

    for _ in range(size):\
        password += random.choice(characters)
    
    return password

if __name__ == "__main__":
    main()