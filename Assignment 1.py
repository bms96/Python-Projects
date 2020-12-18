# Prompt the user for the number of hours worked for that week and weekly sales
# Save inputs in variables
hoursWorked = float(input("How many hours did you work this week? "))
salesForWeek = float(input("How much in total sales? "))

#compute the total pay as the sum of the pay based on the number of hours worked times the hourly rate plus the commission

# 5% commission on sales
commission = round(0.05 * salesForWeek, 2)
# Pay is $20/hr
hourlyPay = 20
# Base pay is the product of the hourly rate and hours worked plus commission
weeklyBasePay = round(hourlyPay * hoursWorked, 2)
totalWeekCompensation = round(weeklyBasePay + commission, 2)

# Printing out the results
print(f"\nBase pay for the week is {weeklyBasePay}")
print(f"Commision for the week is {commission}")
print(f"\nThis week your paycheck will be ${totalWeekCompensation}")
