FLAT_FEE = 2.00
PER_GRAM_FEE = 0.02

weight = 0
cost = 0.0
excess = 0
parcel = "Y"
layout = "{} grams costs £{:4.2f}"

while (parcel == "Y"):
    weight = int (input ("Enter a package weight (grams): "))
    if (weight <= 100):
        cost = FLAT_FEE
    else:
        excess = weight
        cost = FLAT_FEE + (excess * PER_GRAM_FEE)

    print (layout.format (weight, cost))
    parcel = input ("Another parcel (Y/N)? ")
    parcel = parcel.upper()

