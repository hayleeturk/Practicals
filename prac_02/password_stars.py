"""CP1404 Practical
Password verification program with functions
"""

MINIMUM = 10


def main():
    """Verify password length."""
    password_attempt = get_password(MINIMUM)
    print_asterisks(password_attempt)


def get_password(minimum):
    password_attempt = input("Enter password: ")
    while len(password_attempt) < minimum:
        print("Password must be at least 10 characters")
        password_attempt = input("Enter password: ")
    return password_attempt


def print_asterisks(password_attempt):
    for i in range(len(password_attempt)):
        print("*", end="")


main()
