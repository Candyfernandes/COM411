print("How many bars should be charged?")
num_bars = int(input())
charging_bars = 0

while charging_bars < num_bars:
    charging_bars += 1
    bar = "█" * charging_bars
    print(F"charging {bar}")


print("The battery is fully charged.")
