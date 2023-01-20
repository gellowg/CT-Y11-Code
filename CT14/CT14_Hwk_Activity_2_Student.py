# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
myList = [10, 20, 30, 40, 50, 60 ,70, 80, 90, 100]

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def backwardTraversal (pList):
    position = 0
    start = 0
    stop = len (pList)
    step = 2

    for position in range (start, stop, step):
        # Print each item in the list
        print (pList[position])

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
backwardTraversal (myList)

