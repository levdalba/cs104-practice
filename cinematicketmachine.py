
age = int(input("Age: "))
seat = input("Seat (normal/premium): ").lower()
weekend = input("Weekend? (yes/no): ").lower()
student = input("Student card? (yes/no): ").lower()

if age < 0:
    print("Please enter a valid age")
elif seat != "normal" and seat != "premium":
    print("Unknown seat type")
else:
    if seat == "normal":
        price = 220
    else:
        price = 350

    if age < 12 or age >= 60:
        price = price / 2

    elif student == "yes" and weekend == "no":
        price = price * 0.8

    if weekend == "yes":
        price = price + 30

    print(f"Ticket price: {price:.2f} baht")
