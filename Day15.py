#COFFEE VENDING MACHINE

MENU ={
    "espresso":
        {
        "ingredients":
            {
              "water":75,
              "coffee":100, 
              "milk":20 
            },
        "cost":50
        },
     "latte":
        {
        "ingredients":
            {
              "water":150,
              "coffee":50,
              "milk":100
            },
        "cost":75
        },
    "cappucino":
        {
        "ingredients":
            {
              "water":200,
              "coffee":50,
              "milk":75
            },
        "cost":100
        },
}
resources ={
  "water":500,
  "milk":200,
  "coffee":100,
  "cost":1000  
}


def check_resources(ingred):
    """Checks if required resources are available"""
    
    if ingred['water']> resources['water']:
        print("Sorry there is not enough water")
    elif ingred['milk']> resources['milk']:
        print("Sorry there is not enough milk")
    elif ingred['coffee']> resources['coffee']:
        print("Sorry there is not enough coffee")
        
        
def payment(drinks):
    """Payment process"""
    rup1=int(input("Enter number of 1 rupee coins:"))*1
    rup2=int(input("Enter number of 2 rupee coins:"))*2
    rup5=int(input("Enter number of 5 rupee coins:"))*5
    rup10=int(input("Enter number of 10 rupee coins:"))*10
    total=rup1+rup2+rup5+rup10
    sum=drink['cost']
    change=total-sum
    if total< sum:
        print("Sorry that's not enough money. Your money has been refunded.")
    else:
        resources['cost']+=sum
        if change!=0:
            print(f"Here is Rs.{change} rupees in change")
            
            
def make_coffee(ingreds):
    """Balances resources"""
    resources['water']-=ingreds['water']
    resources['milk']-=ingreds['milk']
    resources['coffee']-=ingreds['coffee']
        
is_working=True
while is_working:
    print("Welcome to our Coffee Vending Machine!")
    choice=input("What would you like today?(espresso/latte/cappucino):").lower()
    if choice=='off':
        is_working=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: Rs.{resources['cost']}")
    else:
        drink= MENU[choice]
        drink_ingredients= drink['ingredients']
        check_resources(drink_ingredients)
        total=payment(drink)
        make_coffee(drink_ingredients)
        
        
    
    

