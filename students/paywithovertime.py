hours=input("Enter hours: ")
hours=int(hours)
rate=input("Enter rate: ")
rate=float(rate)
if hours>40:
    overtime=hours-40
    pay=(40*rate)+(overtime*rate*1.5)
else:
    pay=hours*rate
print("Total pay:", pay)
if hours!=int(hours) or rate!=float(rate):
    print("Error. Please enter numeric input.")