# Write a programme that will ask the number of days and then will show how many
# hours, minutes and seconds are in that number of days.

numberOfDays = int(input("Number of days : "))
hours = numberOfDays * 24
minutes = hours * 60
seconds = minutes * 60

print(f"In {numberOfDays} days, we have:\n{hours} hours\n{minutes} minutes\n{seconds} seconds.")
