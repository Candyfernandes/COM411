def observed_items ():
    observations = []
    print ("counting observations ....")
    for _ in range(7):
        item = input("Enter an item: ")
        observations.append(item)
    return observations

def run_task ():
    print("counting observations ......")
    observations = observed_items()
    observation_set = set()


