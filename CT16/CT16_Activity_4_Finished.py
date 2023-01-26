# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
nouns = ["cakes", "bicycles", "trees", "pigeons", "houses"]
verbs = ["eat", "ride", "hug", "chase", "draw"]
sentence = ""
userInput = "N"

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
while (userInput == "N"):
    nounIndex = int(input("Enter a noun index: "))
    verbIndex = int(input("Enter a verb index: "))

    sentence = "The children " + verbs[verbIndex] + " " + nouns[nounIndex] + "."
    print(sentence)

    userInput = input("Does this sentence make sense (Y/N)? ")
    userInput = userInput.upper()

print("Goodbye")
