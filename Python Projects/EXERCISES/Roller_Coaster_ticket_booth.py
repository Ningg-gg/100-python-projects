#Roller Coaster ticket booth
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  if age > 18:
    print("You have to pay $12.")
  elif age >= 12:
    print("You have to pay $7.")
  else:
    print("You have to pay $5.")

else:
  print("Sorry, you have to grow taller before you can ride")

