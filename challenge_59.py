# Display five colours and ask the user to pick one. If they pick 
# the same as the program has chosen, say "Well done", otherwise display 
# a witty answer which involves the correct colour, 
# e.g. "I bet you are GREEN with right now". Ask them to guess again; if they 
# have still not got it right, keep giving them the same clue and ask the user to enter a colour
# until they guess it correctly. 
import random

colors  = ["BLUE","GREEN","RED","BLACK","YELLOW","WHITE"]

comp_color = random.choice(colors)

answer = False
while answer == False:
    print("BLUE,GREEN,RED,BLACK,YELLOW,WHITE")
    print()
    choix = input("Enter a Colour : ")
    if choix == comp_color:
        print("I bet you are",comp_color,"with rigth now")
        answer = True