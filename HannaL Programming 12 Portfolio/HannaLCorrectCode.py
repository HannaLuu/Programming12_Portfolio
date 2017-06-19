def sum(a, b, c):
    print(a + b + c)
sum(10, 11, 12)

def increase(x):
    return x + 1
x = 10
print("X is", x, " I will now increase x." )
print("X is now", increase(x))

def print_hello():
    print("Hello")
print_hello()

def count_to_ten():
    for i in range(11):
        print(i)
count_to_ten()

def sum_list(list):
    for i in list:
        sum = i
        return sum
list = [45, 2, 10, -5, 100]
print(sum_list(list))

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * -1]
        return result
text = "Programming is the coolest thing ever."
print(reverse(text))

def get_user_choice():
    while True:
        command = input("Command: ")
        if command = f or command = m or command = s or command = d or command = q:
            return command
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
user_command = get_user_choice()
print("You entered:", user_command)