def movements():
    path = ["Move forward",10, "Move backwards" , 5, "move Left", 3 , "move Right" , "move Up" , 1]
    return path


def run_task2():
    print("Moving....")
    path = movements()
    for i in range(0, len(path), 2):
        direction = path[i]
        steps = path[i + 1]
        print(f"{direction} for {steps} steps")


if __name__ == "__main__":
    run_task2()


