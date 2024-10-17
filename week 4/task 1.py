def main ():
    print ("program started!")
    print("Please enter a standard character:")

user_input = input("Enter a character: ")

if len(user_input) == 1:
    ascii_value = ord(user_input)
    print(f"The ASCII code for {user_input} is {ascii_value}.")
else:
    print("Error: Please enter a single character.")

print("Program Ended!")


