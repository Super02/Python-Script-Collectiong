gender = input("Er du en mand eller kvinde: (m/k) ")
weight = int(input("Hvad vejer du i KG: "))
height = int(input("Hvor høj er du i CM: "))
age = int(input("Hvor gammel er du: "))

bmr = 10 * (weight) + 6.25 * (height) - 5 * (age)

if gender == "m":
    bmr = bmr + 5
elif gender == "k":
    bmr = bmr - 161
else:
    print("Ugyldigt svar, prøv igen")

print("-----------")
print("Dit BMR er (helt passiv):", bmr)
print("Dit BMR er (lidt aktiv):", 1.53*bmr)
print("Dit BMR er (meget aktiv):", 1.76*bmr)
print("Dit BMR er (super aktiv):", 2.25*bmr)
print("-----------")
