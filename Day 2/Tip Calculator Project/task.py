print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? (type just numbers) "))
people = int(input("How many people to split the bill? "))
total = ((bill / people) * (tip / 100 + 1) )
print(f"Each person should pay: ${round(total, 2)} ")

# teste

