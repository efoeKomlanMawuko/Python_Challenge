# Ask the user to type in the first line of a nursery rhyme and display
# the length of the string.
# Ask for a starting number and an ending number and then 
# display just that section of the text (remember Python starts counting from 0 and not 1).

phrase = input("Enter the first line of a nursery rhyme : ")
length = len(phrase)
print("This has",length,"letters in it")
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))
part = (phrase[start:end])
print(part)