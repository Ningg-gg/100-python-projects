# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()
name_merged = lowercase_name1 + lowercase_name2
t = name_merged.count("t")
r = name_merged.count("r")
u = name_merged.count("u")
e = name_merged.count("e")
true = t + r + u + e

l = name_merged.count("l")
o = name_merged.count("o")
v = name_merged.count("v")
e = name_merged.count("e")
love = l + o + v + e

true_love = str(true) + str(love)
true_love_as_int = int(true_love)

if true_love_as_int < 10 or true_love_as_int > 90:
    print(f"Your score is {true_love_as_int}, you go together like coke and mentos.")
elif true_love_as_int >= 40 and true_love_as_int <= 50:
    print(f"Your score is {true_love_as_int}, you are alright together.")
else:
    print(f"Your score is {true_love_as_int}.")


