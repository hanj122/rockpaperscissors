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
  elif xchoice = 3:
    picture = paper
  return(picture)


scissor = '\u270C'
rock = '\u270A'
paper = '\u270B'
ggs = "Thank you for playing!"


you = input("What is your name? ")
print("Hello " + you + "\U0001F914")
print("Let us play Bato Bato Pick")
print()

while True:
    print ('''Select one \U0001F914: 
    1 for scissor \u270C
    2 for rock \u270A
    3 for paper \u270B''')
    print(' ')

    # get a selection from the user
    while True:
        try:
            player_choice = int(input("Enter your pick: "))
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")
            continue
        my_choice = random.randint(1, 3)
        
        # if player choice chose a number higher than 3 
        if player_choice > 3: 
            print("You typed a number above 1, 2, and 3. Retry")
            continue
  
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
        while True:
            ans = input("Another round? yes or no?")
            if ans.lower() == 'yes':
            break
            elif ans == 'no':
                print(" ")
            elif ans.lower != "yes" or "no":
                print("You typed an input I can't read. Please type yes or no only!")
                continue
            while True:
                ans2 = input("Another player? yes or no?")
                if ans2.lower() == 'yes':
                    cls = lambda: print('\n"*100)
                    cls()
                    restart_program()
                elif ans2.lower() == "no":
                    print(ggs)
                    exit()
                else:
                    print("You typed an input I can't read. Please type yes or no only!")
                    continue
break            
