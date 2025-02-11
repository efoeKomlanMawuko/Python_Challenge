# Ask how many slices of pizza the user started with and ask
# how many slices that have been eaten. Work out how many slices they
# have left and display the answer in a user-friendly format.

start = int(input("Start number of Pizza : "))
eaten = int(input("number of Pizza eaten : "))

result = start - eaten
print("You have now" , result , "Pizza")