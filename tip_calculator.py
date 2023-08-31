print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill?\n"))
num_people = int(input("How many people to split the bill?\n"))
tip_percentage = int(input("What percentage top would you like to give? 10, 12, or 15? "))
a = tip_percentage / 100
b = total_bill + total_bill * a
c = b / num_people
print("Each person should pay: " + str(c))