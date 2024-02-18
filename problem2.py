

# Problem number 2
    



age = float(input("Enter your age:>\t"))
days = input("Enter your days:>\t")
price = 500

if age >= 18 and days=="wednesday":
    price-=50
    print(price)
elif age >=18:
    print(price)
elif age <=18 and days=="wednesday":
    price-=50
    print(price)
else :
    print(price)
    

