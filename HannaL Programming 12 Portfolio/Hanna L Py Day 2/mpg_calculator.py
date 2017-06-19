# Calculate Miles Per Gallon
print("This program calculates mpg.")
 
# Get miles driven from the user
miles_driven = input("Enter miles driven:")
# Convert text entered to a
# floating point number
miles_driven = float(miles_driven)
 
# Get gallons used from the user
gallons_used = input("Enter gallons used:")
# Convert text entered to a
# floating point number
gallons_used = float(gallons_used)
 
# Calculate and print the answer
mpg = miles_driven / gallons_used
print("Miles per gallon:", mpg)

# Calculate Kinetic Energy
 
print("This program calculates the kinetic energy of a moving object.")
m_string = input("Enter the object's mass in kilograms: ")
m = float(m_string)
v_string = input("Enter the object's speed in meters per second: ")
v = float(v_string)
 
e = 0.5 * m * v * v
print("The object has " + str(e) + " joules of energy.")