from art import logo
# import call method from subprocess module
from subprocess import call
import os
 
# import sleep to show output for some time period
from time import sleep
 
# define clear function
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')
aunctioners = []

print(logo)
print("Welcome to the secret auction program.")

def bider_details():
    name = input("what is your name: \n")
    bid = int(input("What's your bid?: $"))
    
    bidder_dict = {}
    bidder_dict["name"] = name
    bidder_dict["bid"] = bid
    aunctioners.append(bidder_dict)

def each_aunctioner():
    highes_value = 0
    for aunctioner in aunctioners:
        bids = aunctioner.get("bid")
    if bids < highes_value:
        highes_value == bids
    print(highes_value)
    
other_biders = "yes" 
while other_biders == "yes":
    bider_details()
    other_biders = input("Are there any other bidders: ") 
    if other_biders == "no":
        other_biders == "no"

each_aunctioner()
# print(aunctioners)