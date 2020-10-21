#!usr/bin/python3
#Noel Glamann
#December 10, 2019

'''
I was absent 12/9. This is what they learned. 
This was my "crash course" from Mr. Schmidt.
Notes in notebook under File Handling. 
I also added comments for better understanding.
'''

save_file = open("file.txt", "w")
#Opens a file saved under the name file.txt but refered to as save_file. This 
#file is opened in write mode so it can be written. If you do this to a new file, 
#it will be created, but if it's an old file it will be overwritten. 

save_file.write("stuff")
#This is what adds "stuff" to the file. MUST be a string to be written.

save_file.close()
#You HAVE TO close every file you open before you can change modes.

save_file = open("file.txt", "r")
#Now, opens the save_file in read mode. Read mode is the default mode, so unless
#specified otherwise, files will always be opened in read mode. 

my_text = save_file.read()
#The new variable my_text now has the contents of save_file. It's as if you read
#the file and put everything you read into a new variable. 

save_file.close()
#Be sure to always close the file. 