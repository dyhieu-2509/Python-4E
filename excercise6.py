num = 0
count = 0
total = 0
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try :
        num1 = float(number)
    except:
        print('Invailed Input')
        continue
    count += 1
    total = total + num1
print (int(total), count, total/count)