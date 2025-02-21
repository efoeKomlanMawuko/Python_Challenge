# Ask which direction the user wants to counts (up or down). If they select up, 
# then ask them for the top number and then count from 1 to that number. If they 
# select down, ask them to enter a number below 20 and the count down from 20 to
# that number. If they enter a number which is 10 or higher, display the message
# "I don't understand"
sens = input("Did you want to count (up or down) ? : ")
sens = sens.lower()

if sens == "up":
    top = int(input("Enter the top number : "))
    for i in range(1,top+1):
        print(i)
elif sens == "down":
    below = int(input("Enter a number below 20 : "))
    scale = 20 - below
    for i in range(scale+1): #for i in range(20,num-1, -1)
        resultat = 20 - i #print(i)
        print(resultat)
else:
    print("I don't understand")