# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
age_left = 90 - age_as_int
days_left = age_left * 365
weeks_left = age_left * 52
months_left = age_left * 12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
