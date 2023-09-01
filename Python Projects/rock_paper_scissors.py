import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if player == "0":
  print(f"{rock}")
elif player == "1":
  print(f"{paper}")
elif player == "2":
  print(f"{scissors}")

print("Computer chose:")
computer = str(random.randint(0,2))

if computer == "0":
  print(f"{rock}")
elif computer == "1":
  print(f"{paper}")
elif computer == "2":
  print(f"{scissors}")


if player == "0" and computer == "0":
 print("Draw")
elif player == "0" and computer == "1":
  print("You lose.")
elif player == "0" and computer == "2":
  print("You win.")
elif player == "1" and computer == "0":
  print("You win.")
elif player == "1" and computer == "1":
  print("Draw")
elif player == "1" and computer == "2":
  print("You lose.")
elif player == "2" and computer == "0":
  print("You lose.")
elif player == "2" and computer == "1":
  print("You win.")
elif player == "2" and computer == "2":
  print("Draw")