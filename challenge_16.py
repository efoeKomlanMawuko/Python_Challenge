# Ask the user if it is rainning and convert their answer to lower case so it doesn't matter
# what case they type it in. If they answer "yes", ask if it is wondy, if they answer "yes" to the second 
# question, display the answer "It is too windy for an umbrella", otherwise display the message
# "Take an unbrella". If they did not answer yes to the first question, display the answer
# "Enjoy your day" 

answer1 = input("Is it rainning ? Yes or No : ")
low_answer1 = str.lower(answer1)
if low_answer1=="yes":
    answer2= input("Is it wondy ? Yes or No : ")
    low_answer2=str.lower(answer2)
    if low_answer2=="yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an unbrella")
else:
    print("Enjoy your day" )


