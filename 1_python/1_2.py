print(" *** Wind classification ***")

wind = float(input("Enter wind speed (km/h) : "))



if wind < 52:
    ans = "Breeze"
elif wind < 56:
    ans = "Depression"
elif wind < 102:
    ans = "Tropical Storm"
elif wind < 209:
    ans = "Typhoon"
else:
    ans = "Super Typhoon"

print("Wind classification is " + ans + ".")