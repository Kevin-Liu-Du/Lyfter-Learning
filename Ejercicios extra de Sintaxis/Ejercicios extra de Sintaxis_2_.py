# Create pseudocode that asks the user for a time in seconds and calculates whether it is less than or greater than 10 minutes.
# If it is less, display how many seconds are needed to reach 10 minutes. If it is greater, display "Greater than".
# If it is exactly equal, display "Equal".


sec = int(input("Enter a random time in seconds:: "))
sec_min = 600
if (sec < sec_min):
    needed = sec_min - sec
    print(f"The time needed to reach 10 minutes is {needed} seconds.")
elif (sec == sec):
    print("The time entered is equal to 10 min.")
else:
    print("The time entered is greater than 10 min.")