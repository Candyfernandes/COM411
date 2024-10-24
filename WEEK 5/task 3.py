def directions ():
    steps = ["Move forward", "Turn left", "Turn right"]
    return steps
def menu():
    print("please select a direction")
    steps= directions()
    for index, direction in enumerate(steps):
        print(f"{index}: {direction}")

def run_task3():
    menu()


run_task3()