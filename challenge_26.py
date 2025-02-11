# Pig Latin takes the first consonant of a word, moves it to the end of the word and
# adds on an "ay". If a word begins with a vowel you just add "way" to the end. For
# example, pig becomes igpay, babana becomes ananabay, and aadvark becomes aadwarkway. 
# Create a program that will ask the user to enter a word and change it into Pig Latin.
# Make sur the new word is displayed in lower case.

word = input("Enter a word : ")
if word[0] in ["a","o","u","i","e","y"]:
    PigLatin = word+"way"
else:
    length = len(word)
    PigLatin = word[1:length] + word[0] + "ay"

print(PigLatin.lower())