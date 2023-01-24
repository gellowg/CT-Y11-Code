PER_PERSON = 5.00

numPeople = 0
membership = "N"
charge = 0.0

numPeople = int (input ("Enter number of people in your party: "))
membership = input ("Are you a member (Y/N)? ")
membership = membership.upper()

charge = numPeople * PER_PERSON

if (numPeople >= 4):
    charge = charge + ((charge / 100) * 5)
    if (membership == "Y"):
        charge = charge + ((charge / 100) * 10)

print ("The charge is: ", charge)


