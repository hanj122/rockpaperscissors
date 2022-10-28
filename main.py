import random
import sys 
import os 


#restart function
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# symbol maker
def symbol_maker(xchoice):
  if xchoice == 1:
    picture = scissor  
  elif xchoice == 2:
    picture = rock
  else:
   picture = paper
  return(picture)


scissor = '\u270C'
rock = '\u270A'
paper = '\u270B'
ggs = "gg"


you = input("What is your name? ")
print("Hello " + you + "\U0001F914")
print("Let us play Bato Bato Pick")
print()
print ('''Select one \U0001F914: 
  1 for scissor \u270C
  2 for rock \u270A
  3 for paper \u270B''')
print(' ')

# get a selection from the user
while True:
  player_choice = int(input("Enter your pick: ")) 
  my_choice = random.randint(1, 3)
  
  # determine and print the symbol of each user
  your_picture = symbol_maker(player_choice)
  my_picture = symbol_maker(my_choice)
  print("You: " + your_picture + "   Me:  "+ my_picture)
  
  # determine the winneR
  
  if player_choice == my_choice:
    print("It is a tie") 
  elif player_choice == 1 and my_choice == 3:
    print("You win...") 
  elif player_choice == 2 and my_choice == 1:
    print("You win...") 
  elif player_choice == 3 and my_choice == 2:
    print("You win...") 
  else:
    print("I win")

# asking if player wants another round/new player
  ans = input("Another round? yes or no?")
  if ans.lower() == 'yes':
    continue
  else:
    ans2 = input("Another player?: yes or no?")
    if ans2.lower() == 'yes':
       restart_program()
    else: 
      print(ggs)
      break