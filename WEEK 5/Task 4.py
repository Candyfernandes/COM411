def direction ():
    steps = ["Move forward", "move backwards", "Turn left", "Turn right"]
    return steps

def menu_and_input():
    print("please select a direction")
    steps = direction()

    for index, output in enumerate(steps):
        print(f"{index}: {output}")
    choice = int(input("Enter the number of your choice: "))
    return steps[choice]


def run_task4():
    route=[]
    print("working out escape route .......")
    for i in range(5):
        route.append(menu_and_input())
        print(f"Escape route: {route}")


run_task4()



