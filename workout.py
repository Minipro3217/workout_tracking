import csv
import datetime
import os

filename = "workout_log.csv"
if not os.path.exists(filename):
    field_names_list = []
    print("""Enter the name of exercises (put a space after each exercise) you want to add (type "close" to end): """)
    while True:
        field_names=input()
        if field_names=="close":
            break
        else:
            fields = field_names.split()
            field_names_list.extend(fields)
    with open(filename, mode="a") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE)
        writer.writerow(field_names_list)

with open(filename, "r") as file:
    firstline_file=file.readline()

date = datetime.date.today()
fields = firstline_file.split(',')
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
