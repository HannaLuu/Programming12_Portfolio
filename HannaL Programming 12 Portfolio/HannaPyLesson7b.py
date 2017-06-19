x = "This is a sample string"
#x = "0123456789"
 
print("x=", x)
 
# Accessing a single character
print("x[0]=", x[0])
print("x[1]=", x[1])
 
# Accessing from the right side
print("x[-1]=", x[-1])
 
# Access 0-5
print("x[:6]=", x[:6])
# Access 6
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])



a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))


a = "Hi There"
print(len(a))


months = "JanFebMarAprMayJunJulAugSepOctNovDec"
 
n = int(input("Enter a month number: "))

my_starting_index = (n-1) * 3

my_month_string = []
for i in range (3):
    my_month_string += months[my_starting_index+i]

print (my_month_string)