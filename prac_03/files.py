"""
CP1404 - Practical
Methods of file reading
"""
# 1.
name = input("Enter name: ")
out_file = open(f"{name}.txt", "w")
print(name.title(), file=out_file)
out_file.close()

# 2.
in_file = open(f"{name}.txt")
text = in_file.read().strip()
in_file.close()
print("Your name is", text)

# 3.
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)


