"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
Estimated time:
Actual time:
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state, or type 'all' to see all: ").upper()
while state_code != "ALL":
    try:
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
    except ValueError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
max_length = max(len(code) for code in list(CODE_TO_NAME.keys()))
for code, state in CODE_TO_NAME.items():
    print(f"{code:{max_length}} is {state}")
