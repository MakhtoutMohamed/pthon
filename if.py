import os

os.system('clear')

answer = input("do you wanna hear a joke?\n")

affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

#if (answer == "Yes" or answer == "yes") or (answer == "Y" or answer == "y"):
if answer.lower() in affirmative_responses:
    print("I'm a joke hhhhhh")
# elif answer == "No":
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("Whoooooo.")