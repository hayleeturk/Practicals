"""
CP1404 Practical
Program for email to name dictionary
"""


def main():
    """Make emails to name dictionary"""
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        name = get_name_from_email(email)
        name_check = input(f"Is your name {name}? (Y/n): ").upper()
        if name_check != "Y" and name_check != "":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Take name from email input"""
    section = email.split("@")[0]
    parts = section.split(".")
    name = " ". join(parts). title()
    return name


main()
