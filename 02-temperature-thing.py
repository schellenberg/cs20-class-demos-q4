temperature = input("What's the temperature? ")

#convert data type
temperature = int(temperature)

if temperature > 15:
    print("wear shorts")
elif temperature > 0:
    print("wear a t-shirt")
elif temperature > -15:
    print("wear a sweater")
else:
    print("wear a parka")