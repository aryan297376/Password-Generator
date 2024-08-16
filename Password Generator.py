import random
import string

# Initial greeting
reply = input("Hey there, welcome to the password generator! ").strip().lower()

if reply in ["hey", "hi", "hello"]:
    print("Ok")
else:
    print("Can't understand you... Sorry")
    quit()

# Check if the user needs help with creating a password
reply_2 = input("So, do you need help creating a password? (Yes or No) ").strip().lower()

if reply_2 == "yes":
    print("I'll help you")
elif reply_2 == "no":
    print("Ok then, have a good day")
    quit()
else:
    print("Invalid response")
    quit()

# Asking for the purpose of the password
reply_3 = input("For what purpose do you need a password? ").strip()

# Available character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Asking for the type of password
password_type = input("Which password type do you want? (A = Numeric, B = Alphabetic, C = Alphanumeric): ").strip().upper()

if password_type == "A":
    print("Numeric")
    char_set = num
    filename = "Numeric_Passes.txt"
elif password_type == "B":
    print("Alphabetic")
    char_set = lower + upper
    filename = "Alphabetic_Passes.txt"
elif password_type == "C":
    print("Alphanumeric")
    char_set = lower + upper + num + symbols
    filename = "Alphanumeric_Passes.txt"
else:
    print("Error: Invalid selection")
    quit()

# Password length input
length = int(input("Enter the length of the password: "))

# Generating the password
password = "".join(random.sample(char_set, length))

# Saving password to appropriate file
with open(filename, "a") as f:
    f.write(password + '\n')

# Saving password to a general file
with open("Password.txt", "a") as f:
    f.write(f"Your password for {reply_3} is: {password}\n")

# Displaying the generated password
print(f"Your password for {reply_3} is: {password}")
