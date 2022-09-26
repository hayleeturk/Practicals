
def main():
    """Program to verify password length"""
    minimum = 10
    password_attempt = input("Enter password: ")
    while len(password_attempt) < minimum:
        print("Password must be at least 10 characters")
        password_attempt = input("Enter password: ")
    for i in range(len(password_attempt)):
        print("*", end="")


main()
