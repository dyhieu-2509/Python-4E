def computepay(hours, rate):
    if float(hours) < 40.0:
        return float(hours) * float(rate)
    
    abovetime = float(hours) - 40.0
    return (float(rate) * 40.0) + (1.5 * float(rate) * float(abovetime))

hours = input('Enter Hours: ')

rate = input('Enter Rate: ')

pay = computepay(hours, rate)
print('Pay: ', pay)