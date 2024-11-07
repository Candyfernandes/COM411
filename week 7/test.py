def observed_items():
    observations = []
    print("Please enter 7 items (some duplicates are fine):")
    for _ in range(7):
        item = input("Enter an item: ")
        observations.append(item)
    return observations

def run_task2():
    print("Counting observations...")
    observations = observed_items()
    observation_set = set()
    for item in observations:
        observation_set.add((item, observations.count(item)))
    print("Observations count:", observation_set)

run_task2()
