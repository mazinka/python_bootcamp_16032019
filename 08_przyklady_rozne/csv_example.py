import csv

with open('logs.txt'), open('drugi.csv','w', newline=" "):
    reader = csv.DictReader(logs, delimiter=";")
    writer = csv.writer(f,delimiter=";")
    for row in reader:
        writer.writerow([row['action'], row['time']])


# with open ('drugi.csv', 'w') as f:
#     writer = csv.writer(f,delimiter=";")
#     writer.writerow(['id','login','time'])