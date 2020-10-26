import os
print("-"*100)
#----------1)Create directories---------------------------------
user = str(input("Please enter directory to create...\t"))
#users chose which directory for file.
if user not in os.listdir('.'):         #check if file not yet created.
    os.mkdir('./{}'.format(user))           #if its new create it.
else:
    print("\n\t**DIRECTORY ALREADY CREATED**\n")
print(os.listdir('.'))              #show the names of files/dir in cwd.

#----------2)Copy existing file to new directory----------------
import shutil
check = True                #only works for files in cwd.
while check:        #check if file in cwd.
    userfile2copy = input("Please enter file to be copied...\t")    #file to be moved.
    if userfile2copy in os.listdir('.'):
        check = False               #no need to stay in while loop.
        destinationDir = input("Please enter file destination directory...\t") #where to put it.
        currentDir = os.getcwd()            #get current PATH.
        newPath = shutil.copy(userfile2copy,currentDir+'/'+destinationDir)
        print("\nNew Path >> ",newPath)     #display new path.
    else:
        print("\n\t**ERROR FILE NOT IN THIS CWD**\n")

#----------3)Read the file--------------------------------------
with open(currentDir+'/'+destinationDir+'/'+userfile2copy,'r') as textfile:
    print("--File Contents--\n",textfile.read())        #display file contents
print("-"*100)