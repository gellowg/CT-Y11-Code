# ------------------------------------------------------------
# Global variables
myList = [150, 153, 163, 198, 200, 210, 212, 217, 251,
          263, 281, 311, 318, 365, 376, 401, 411, 441,
          583, 616, 620, 636, 716, 802, 807, 807, 840,
          841, 877, 896]

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def reverseTraversal (inList):
    index = 0

# -----> Add a 'for in range' loop here to traverse in reverse

        # Print first and last item only
        if (index == len (inList) - 1):
            print (inList[index])
        if (index == 0):
            print (inList[index])

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
reverseTraversal (myList)

