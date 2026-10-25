try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except ValueError:
    print("Error. Please enter numeric input.")
    exit()

if hours > 40:
    overtime = hours - 40
    pay = (40 * rate) + (overtime * rate * 1.5)
else:
    pay = hours * rate

    print("Total pay:", pay)