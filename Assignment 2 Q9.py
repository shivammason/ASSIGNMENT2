
def computepay(hours,rate):
    if hours < 40:
        pay = rate * hours
    else:
        times_over = hours // 40 - 1
        overtime = hours % 40
        pay = 40.0 * rate + times_over * rate * (40 * 1.5) + overtime * rate * 1.5
    print('Pay:',pay)

input_hours = input('Enter Hours: ')
try:
    hours = float(input_hours)
except:
    print('Error, please enter numeric input')
    quit()

input_rate = input('Enter Rate: ')
try:
    rate = float(input_rate)
except:
    print('Error, please enter numeric input')
    quit()

computepay(hours,rate)
