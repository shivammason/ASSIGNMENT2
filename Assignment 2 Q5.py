
input_hours = input('Enter Hours: ')
input_rate = input('Enter Rate: ')
hours = float(input_hours)
rate = float(input_rate)
if hours < 40:
    pay = rate * hours
else:
    times_over = hours // 40 - 1
    overtime = hours % 40
    pay = 40.0 * rate + times_over * rate * (40 * 1.5) + overtime * rate * 1.5
print('Pay:',pay)
