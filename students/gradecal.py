num = int(input("Enter score: "))
if num > 100 or num < 0:
    print("Invalid score")
elif num >= 80:
    print("A")
elif num >= 70:
    print("B")
elif num >= 60:
    print("C")
elif num >= 50:
    print("D") 
else:
    print("F")

