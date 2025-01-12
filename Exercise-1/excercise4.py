hours = input('Enter Hours: ')
try:
    hours = float(hours)         
    print(hours)
except ValueError:
    print('Error, please enter numeric input')

rate = input('Enter Rate: ')
try:
    rate = float(rate)               
    print(rate)
except ValueError:
    print('Error, please enter numeric input')