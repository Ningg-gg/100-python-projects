from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

#add item to auction dictionary
def bidding(name,amount):
  auction[name] = amount

loop = True
auction = {}

while loop:
  bid_name = input("What is your name? ")
  bid_amount = int(input("What's your bid? $"))
  other_name = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  bidding(name=bid_name, amount = bid_amount)
  
  if other_name == 'yes':
    clear()
  elif other_name == 'no':
    highest_bid = 0
    for bid in auction:
      amount = auction[bid]
      if amount > highest_bid:
        highest_bid = amount

    key_list = list(auction.keys())
    val_list = list(auction.values())
    position = val_list.index(highest_bid)
    bidder = key_list[position]
    
    print(f"The winner is {bidder} with a bid of ${highest_bid}.")
    loop = False