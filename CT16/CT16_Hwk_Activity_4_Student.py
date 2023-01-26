# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
total = 0
count = 0
step = 0
start = 0
stop = 0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
start = int (input ("Enter a start value: "))
stop = int (input ("Enter a stop value: "))
step = int (input ("Enter a step: "))

for number in range (start, stop, step):
    total = total + number
    count = count + 1

print (count, total)

