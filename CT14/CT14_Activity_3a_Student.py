# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
myList = [
    150, 153, 163, 198, 200, 210, 212, 217, 251, 263, 281, 311, 318, 365, 376,
    401, 411, 441, 583, 616, 620, 636, 716, 802, 807, 807, 840, 841, 877, 896
]


# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def forwardTraversal(inList):
    index = 0

    # -----> Add a 'for' loop here to traverse forward
    for item in inList:
        # Print first and last item only
        if (index == 0):
            print(inList[index])
        if (index == len(inList) - 1):
            print(inList[index])
        index = index + 1


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
forwardTraversal(myList)
