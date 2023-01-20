# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
myList = [150, 153, 163, 198, 200, 210, 212, 217, 251,
          263, 281, 311, 318, 365, 376, 401, 411, 441,
          583, 616, 620, 636, 716, 802, 807, 807, 840,
          841, 877, 896]

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def reverseSearch (inList, inTarget):
    index = 0
    found = False
    passed = False

# -----> Add the code to search the list, only looping until
#        the item is found or the place where it should
#        be located at is passed

    for item in range(len(inList), -1, -1):
        if item == inTarget:
            found = True
        if item < inTarget:
            found = True
            
    if (found):
        print (inTarget, "found at index", index)
    else:
        print (inTarget, "not found")

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
reverseSearch (myList, 636)
reverseSearch (myList, 150)
reverseSearch (myList, 130)

reverseSearch (myList, 896)
reverseSearch (myList, 720)
reverseSearch (myList, 900)
