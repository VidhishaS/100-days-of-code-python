from random import randint
print("Random number guessing game")
print("Im thinking of a number between 1 and 100")
lvl=input("Choose your level: Easy, Medium, or Hard: ").lower()
def level(lvl):
    if lvl=="easy":
        at=10
    elif lvl=="medium":
        at=8
    else:
        at=5
    return at
        
def game(attempts):
    g=0    
    num=randint(1,100)
    while attempts!=0:
            print(f"You have {attempts} attempts remaining")
            g=int(input("Make your guess: "))
            if g==num:
                print("Congratulations! You have guessed the right number")
                return
            elif g>num:
                print("Too high, try again")
            elif g<num:
                print("Too low, try again")
            attempts-=1
    print(f"You have failed to guess the number({num}), better luck next time!")

attempts=level(lvl)
game(attempts)
        
        
        
    
    



