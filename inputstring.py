#!/usr/bin/python3
#Noel & KJ
# 09 October 2019

'''Create a loop that takes user input and adds that input to an existing string that starts out empty.
   Keep doing this until the user enters a period - then print the string.'''

#Creates empty string variable
my_string = ""
user_input = input("Type some text. '.' to quit:")
punctuation = (".", "?", "!")

while user_input not in punctuation:
    
    my_string += user_input + " "
    user_input = input("Type some text. '.' to quit:")
    
my_string = my_string[:-1]
print(my_string + user_input)

    
