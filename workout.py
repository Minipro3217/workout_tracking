import csv
import datetime

date = datetime.date.today()
fields = ['Weighted_squats', 'Pullups', 'Pushups', 'Plank', 'Lunges', 'Crunches', 'Hold','Curls']
values = []

for field in fields:
    value = input(f"{field}: ")
    try:
        value = int(value)
    except ValueError:
        value = str(value)+"="+str(eval(value))
    values.append(value)

with open('workout_log.csv', mode='a', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONE)
    writer.writerow([date] + values)