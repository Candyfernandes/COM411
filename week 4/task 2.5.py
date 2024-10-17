def main():
    print("Program Started!")
    print("Please enter an ASCII code:")

    try:
        user_input = abs(int(input()))

        if user_input in range(32, 127):
            character = chr(user_input)
            print(f"The character represented by the ASCII code {user_input} is {character}.")
        else:
            print("Error: Please enter a number in the range 32 - 126.")
    except ValueError:
        print("Error: Please enter a valid integer.")

    print("Program Ended!")


if __name__ == "__main__":
    main()
