# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
num1 = 0
num2 = 0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
num1 = int (input ("Enter a number: "))
num2 = int (input ("Enter a second number: "))

if (num1 >= 1):
    if (num1 <= 10):
        if ((num2 >= 11) and (num2 <= 20)):
            print ("Valid")
        else:
            print ("Second number is invalid")
    else:
        print ("First number too high")
else:
    print ("First number too low")
