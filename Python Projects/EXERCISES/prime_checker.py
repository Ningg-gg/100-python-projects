#Write your code below this line 👇
 #Udemy code

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# My code
# def prime_checker(number):
#     if number == 1:
#         print("It's not a prime number")
#     elif number % 10 == 0:
#         print("It's not a prime number")
#     elif number % 2 == 0 and number != 2:
#         print("It's not a prime number")
#     elif number % 3 == 0 and number != 3:
#         print("It's not a prime number")
#     elif number % 5 == 0 and number != 5:
#         print("It's not a prime number")
#     elif number % 7 == 0 and number != 7:
#         print("It's not a prime number")
#     else: 
#         print("It's a prime number")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
 


