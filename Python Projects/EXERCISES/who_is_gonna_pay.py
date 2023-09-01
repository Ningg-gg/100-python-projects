# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_names = len(names)
random_num = random.randint(0, num_names - 1)
lucky = names[random_num]
print(f"{lucky} is going to buy the meal today!")

