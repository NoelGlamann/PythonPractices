#!usr/bin/python3
#Noel 

# a213_password_analyzer.py
import sys
import time
import a213pwalgorithms as pwa

# one-word password analysis
def analyze(password):
    print("Analyzing a one-word password ...")
    time_start = time.time()
    # attempt to find password
    found, num_guesses = pwa.one_word(password)
    time_end = time.time()
    # report results
    if (found):
        print("T")
        #print(password, "found in", num_guesses, "guesses")
    else: 
        print("F")
        #print(password, "NOT found in", num_guesses, "guesses!")
    #print("Time:", format((time_end-time_start), ".8f"))    

# usage 
print("yep")
if len(sys.argv) != 2:
    print("Please supply a passphrase")
    password = input("Password: ").split()
    #sys.exit(0)
# store user password
#password = sys.argv[1]

for i in range(len(password)):
    print(analyze(password[i]))


