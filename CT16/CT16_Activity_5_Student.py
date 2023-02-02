# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
nouns = ["cakes", "bicycles", "trees", "pigeons", "houses"]
verbs = ["eat", "ride", "hug", "chase", "draw"]
theVerb = ""
theNoun = ""
sentence = ""
userInput = "N"

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
while (userInput == "N"):
    nounIndex = int (input ("Enter a noun index: "))
    verbIndex = int (input ("Enter a verb index: "))

    theVerb = verbs[verbIndex]
    theNoun = nouns[nounIndex]
    sentence = "The children " + theVerb + " " + theNoun + "."
    print (sentence)

    userInput = input ("Does this sentence make sense (Y/N)? ")
    userInput = userInput.upper()

print ("Goodbye") 