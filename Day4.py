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
player=int(input("What do you choose?\nType 0 for rock, 1 for paper and 2 for scissors\n"))
if player==0:
    print(rock)
elif player==1:
    print(paper)
elif player==2:
    print(scissors)
else:
    print("Invalid number")
    exit()
comp=random.randint(0,2)
options=[rock,paper,scissors]
print("Computer:")
ans=options[comp]
print(ans)
if player==comp:
    print("It's a draw!")
elif player<comp:
    print("You lose!")

elif player>comp:
    print("You win!")

