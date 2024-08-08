#Nesting a list in a dictionary in a dictionary

# travel_dict={
#     "India":{"states":["Karnataka","Maharashtra","Tamil Nadu","Kerala"], "cities":20,"Metros":2},
#     "Sri Lanka":{"citiesS":["Colombo","Kandy"]}
# }

# #Nesting dictionaries in a list

# travel_dict=[
#     {"Country":"India",
#      "states":["Karnataka","Maharashtra","Tamil Nadu","Kerala"],
#        "cities":20,
#        "Metros":2
#     },
#     {"Country2":"Sri Lanka",
#      "citiesS":["Colombo","Kandy"]
#     }
# ]

#Silent auction
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids={}
i=True

def auction(bid):
    highest_bid=0
    for b in bid:
        money=bid[b]
        if money>highest_bid:
            highest_bid=money
            winner=b
    print(f"{winner} wins the silent auction by bidding ${highest_bid}")
while i==True:
    name=input("Enter your full name: ")
    price=int(input("Enter your bid: $"))
    bids[name]=price
    people=input("Are there more bids you'd like to place? y/n: ")
    if people=="n":
        i=False
    else:
        continue
auction(bids)   


        
        
        
    
    
    


