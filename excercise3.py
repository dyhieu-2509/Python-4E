hours = input("Enter hours: ")
print(hours)
rate = input("Enter rate: ")
print(rate)

if float(hours) < 40:
    pay = float(hours) * float(rate)
    print(float(pay))
else:
    timeabove = float(hours) - 40
    pay = (float(rate) * 40) + (1.5 * float(rate) * float(timeabove))
    print(float(pay)) 