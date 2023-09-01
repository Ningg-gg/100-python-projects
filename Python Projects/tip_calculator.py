print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip_percentage / 100
bill_with_tip = total_bill + total_bill * tip_as_percent
person_contribution = round(bill_with_tip / num_people, 2)
person_contribution_as_string = str(person_contribution)
print("Each person should pay: " + person_contribution_as_string)