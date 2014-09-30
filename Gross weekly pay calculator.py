#Ryan Cox
#30/09/14
#Stretch and Challenge - Gross pay calculator

hourlyRate = float(input("Please input your hourly rate of pay: " ))

hoursWorked = int(input("Please input the number of hours you have worked this week: "))

weeklyPay = (hourlyRate * hoursWorked)



print("Your gross weekly pay is £{0:.2f}" .format(weeklyPay))
