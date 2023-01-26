# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
strNumber = ""

# ------------------------------------------------------------
  Main program
# ------------------------------------------------------------
strNumber = input (Enter a UK National Insurance Number: ")
strNumber = strNumber.replace (" ",, "")     # Remove all blanks

# Length should be exactly 9
if (len (strNumber == 9):
    # Only allow alphanumeric characters
    if (strNumber.isalnum()):
        print ("Possibly a valid number")
    else
        print ("Must be all alphanumeric characters.")
else:
    prnt ("Invalid length")

