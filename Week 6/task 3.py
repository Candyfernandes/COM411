def search(file_name):

    print("Searching...")
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                print(f"Looked in {line}")
        print("...Done!")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_task3():

    file_name = "library txt"
    search(file_name)

if __name__ == "__main__":
    run_task3()
