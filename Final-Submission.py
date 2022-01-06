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
student = []  # Student [SID, Name, Gender, Course Name, CGPA]

student.append(int(input("Enter your SID ")))  # add SID as integer to first
student.append(input("Enter your Name "))   # add name as string to second
student.append(input("Enter your Gender (M/F/U) "))  # add gender as string to third
student.append(input("Enter your Course Name "))  # add course name as string to fourth
student.append(float(input("Enter your CGPA ")))  # add CGPA as float to fifth

print("Hello! " + student[1])  # print the name
print("Your SID is " + str(student[0]))  # print sid
print("You gender is " + student[2])  # print gender
print("You are enrolled in " + student[3] + " Course")  # print course name
print("You scored " + str(student[4]) + " CGPA")  # print CGPA

# End
