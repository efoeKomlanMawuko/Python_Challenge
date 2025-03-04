# Create a list of six school subjects. Ask the user which of these subjects 
# they don't like. Delete the subject that have chosen from the list before
# you display the list again

subjects = ["Maths","PCT","English","French","History-Geography","Biologie"]
print(subjects)
unlike = input("Enter the subject you don't like : ")
subjects.remove(unlike)
print(subjects)