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
---'    ____)____
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

options = [rock , paper, scissors]

choice = input("Please select 0 for rock 1 for paper and 2 for scissor")

opChoice = options[random.randint(0, 2)]
ourChoice = options[choice]

if ourChoice == 0 and opChoice ==2:
    print("u win") #usendim kalani amele isi



