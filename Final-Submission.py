# Question 1 starts here

# declare variable to store input from user and mean of those input
num_1 = 0
num_2 = 0
num_3 = 0
mean = 0

# take input from user
num_1 = float(input("Enter First number "))
num_2 = float(input("Enter Second number "))
num_3 = float(input("Enter Third number "))

# calculate the average of those 3 numbers
mean = (num_1 + num_2 + num_3)/3

# print the calculated average of the numbers
print("Average of " + str(num_1) + ", " + str(num_2) + ", " + str(num_3) + " is " + str(mean))

# End





# Question 2 starts here

gross_inc = 0  # Variable to store income of gross income entered by user
dependency = 0  # variable to store dependency entered by user
tax_inc = 0  # Variable to store Taxable income
net_inc = 0  # Variable to store the net income
tax_rate = 20  # Defining tax rate
std_deduction = 10000  # Defining standard deduction
add_deduction = 3000  # Defining additional deduction

# take input form user for gross income and number of dependencies
gross_inc = float(input("Please enter your gross income "))
dependency = float(input("Please enter your dependency "))

# calculating the taxable income
tax_inc = (gross_inc * tax_rate) / 100 - std_deduction - (add_deduction * dependency)
net_inc = gross_inc - tax_inc

# Printing the Gross income of user
print("Your gross income is " + str(gross_inc) + "$")
print("Your net income is " + str(net_inc) + "$")

# If taxable income comes out to be negative then user don't have to pay tax, so taxable income = 0$
if tax_inc < 0:
    print("Taxable income = 0$")
else:
    print("Taxable income = " + str(tax_inc) + "$")

# End





# Question 3 starts here

# Create a list named student
student = []  # Student [SID, Name, Gender, Course Name, CGPA

student.append(int(input("Enter your SID ")))  # add SID as integer to first index
student.append(input("Enter your Name "))   # add name as string to second index
student.append(input("Enter your Gender (M/F/U) "))  # add gender as string to third index
student.append(input("Enter your Course Name "))  # add course name as string to fourth index
student.append(float(input("Enter your CGPA ")))  # add CGPA as float to fifth index

print("Hello! " + student[1])  # print the name
print("Your SID is " + str(student[0]))  # print SID
print("You gender is " + student[2])  # print gender
print("You are enrolled in " + student[3] + " Course")  # print course name
print("You scored " + str(student[4]) + " CGPA")  # print CGPA

# End





# Question 4 starts here

i = 0  # variable for the 'for loop'
student = []  # Create a list named student to store marks

# Using a for loop to get input of marks of 5 student
for i in range(5):
    student.append(float(input("Enter marks of Student " + str(i + 1) + " ")))

student.sort()  # Sorting the entered marks

print(student)  # Print the sorted marks

# End






# Question 5 starts here

# a part

color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]  # Create a list named color

color.pop(3)  # Remove 4 th element from list

print(color)  # print the modified list





# b part

color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]  # Recreate the list named color

# find the index of element containing "Black" and "Pink" and replace it with "Purple"
color[color.index("Black")] , color[color.index("Pink")] = "Purple", "Purple"

print(color)  # Print the modified list

# End