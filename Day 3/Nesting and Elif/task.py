####### Nesting and elifp

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

age = int(input("What is your age?"))
if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")


##### exercise do jeito que fiz #####

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi == 18.5:
    print("normal weight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

##### Solução ######

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")