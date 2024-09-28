from random import random
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
user=int(input("Enter your choice:"))
if user==0:
    print(rock)
elif user==1:
    print(paper)
else:
    print(scissors)
computer = random.randint(0,2)
print(computer)
if computer==0:
    print(rock)
    if user == 0:
        print("Draw")
    elif user == 1:
        print("You win!")
    else:
        print("You loose")
elif computer==1:
    print(paper)
    if user == 0:
        print("You loose")
    elif user == 1:
        print("Draw")
    else:
        print("You win!")
else:
    print(scissors)
    if user == 0:
        print("You Win!")
    elif user == 1:
        print("You Loose")
    else:
        print("Draw")
