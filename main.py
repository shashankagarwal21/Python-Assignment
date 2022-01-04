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
