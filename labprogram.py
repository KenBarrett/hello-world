name = input("enter your name.")
pineapples = input("Do you like pinaples on your pizza? Y or N")
pineapples = pineapples.lower()
if pineapples == 'n':
    print(name + " is a good person and has a good taste for food.")
elif pineapples == 'y':
    print(name + " is a terrible person and has no taste for food.")
else:
    print(name + " cannot properly answer a question.")


