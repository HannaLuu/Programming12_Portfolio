i = 0
while i < 10:
    print(i)
    i = i + 1

i = 1
while i <= 2 ** 32:
    print(i)
    i *= 2

done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True
     
    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        done = True

value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)

