print("Pentatonix Quiz!")

total_correct = 0


answer_1 = int(input("How many albums have Pentatonix released?"))
if answer_1 == 4:
    print("Correct")
    total_correct = total_correct + 1
else:
    print("Incorrect")


answer_2 = int(input("How many EPs have Pnetatonix released?"))
if answer_2 == 4:
    print("Correct")
    total_correct = total_correct + 1
else:
    print("Incorrect")


print("Time for a math break!")
answer_3 = int(input("What is 4*(3-1)?"))
if answer_3 == 8:
    print("Correct!")
    total_correct = total_correct + 1
else:
    print("Sorry, you're incorrect. :(")


print("Back to questions about Pentatonix")
answer_4 = int(input("How many members are in Pentatonix?\n1. 3\n2. 4\n3. 5\n4. 6\nAnswer:"))
if answer_4 == 3:
    print ("Correct")
    total_correct = total_correct + 1
else:
    print ("Incorrect")


answer_5 = input("What is the abbreviation for Pentatonix?")
if answer_5.lower() == "ptx":
    print("Correct")
    total_correct = total_correct + 1
else:
    print ("Incorrect")

percentage = int(total_correct / 5 * 100)

print("You got", total_correct , "answers right.\nThat is a score of", percentage ,"percent")
