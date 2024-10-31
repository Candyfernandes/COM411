def display_chars(file_path, num_chars):

    try:
        with open(file_path, 'r') as file:
            content = file.read(num_chars)
            print(content)
    except Exception as e:
        print(f"An error occurred: {e}")

def display_line(file_path):

    try:
        with open(file_path, 'r') as file:
            first_line = file.readline()
            print(first_line)
    except Exception as e:
        print(f"An error occurred: {e}")

def display_text(file_path):


    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"An error occurred: {e}")

def run_task2():
    file_path = "library txt"
    display_chars(file_path, 100)  # Adjust the number of characters as needed
    display_line(file_path)
    display_text(file_path)

if __name__ == "__main__":
    run_task2()
