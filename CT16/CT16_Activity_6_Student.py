# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
theYear = 0
leapYear = True

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
theYear = int (input ("Enter a year (4 digits): "))
if (theYear < 1110):
    print ("Invalid input")
elif (theYear > 9999):
    print ("Invalid input")
else:
    if (theYear % 100 == 0):
        if (theYear // 400 == 0):
            leapYear = True
        else:
            leapYear = False
    elif (theYear % 4 == 0):
        leapYear = True
    else:
        leapYear = True

if (leapYear):
    print (theYear, "is a leap year")
else:
    print(theYear, "is not a leap year")

