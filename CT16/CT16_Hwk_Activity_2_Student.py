# ----------------- Import libraries -------------------------
import random
# ----------------- Global Variables -------------------------
animals = ["fish", "hedgehog", "cat", "rabbit", "guinea pig", "mouse"]
choice = 0
found = False
index = 1
# ----------------- Main program -----------------------------
print (animals)
choice = int (input ("Enter a number: "))
while ((not found) and (index < len (animals))):
    if (len (animals[index]) == choice):
        found = True
        print ("The pet for you is a " + animals[index])
    else:
        index = index + 1
if (not found):
    print ("Sorry, I could not find a pet for you.")

