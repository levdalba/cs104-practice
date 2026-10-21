try :
  age = int(input("Age: "))
  seat = str(input("Seat (normal/premium): "))
  weekend = str(input("Weekend? (yes/no): "))
  student = str(input("Student card? (yes/no): "))

  if seat == "normal" :
    price = float(220)
  elif seat == "premium" :
    price = float(350)
  else :
    print('Unknown seat type')

  if age < 12 or age >= 60 :
    price = price/2
  elif age > 120 or age < 1 :
    print('Please enter a valid age') 
    
  if student == "yes" and weekend == "no":
    price = price*0.8
  elif weekend == "yes" :
    price += 30

  print("Ticket price: ", price, " baht")
except ValueError :
  print('Please enter a valid value.')
