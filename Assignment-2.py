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
