print("Look at this calculator, lets start with addition")
try:
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))
    Answer = x + y
    print("You're welcome buddy, the answer is:")
    print(Answer)
    print(":P learn how to add on your own though.")
except ValueError:
    print("THAT ISN'T A NUMBER, DUMBASS...if you can't follow simple instructions, do it yourself >:(")