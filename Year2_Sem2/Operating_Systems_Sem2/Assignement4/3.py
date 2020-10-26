import os,sys
pid = os.fork()
#fork and exec together
print("second test")
if pid == 0:            #this is child
    print("This is the child.")
    print("Im going to exec another program now.")
    newprogram = input("Please enter new program to run (testScript.sh)...")
    fullpath = os.getcwd()+"/"+newprogram
#os.getcwd()-/home/nathancrowley/College/Year2/OS 2/Assignments/Lab4_Assignment
    os.execl(fullpath,fullpath,'NULL')  #insert new program here
else:
    print("The child is pid {}.".format(pid))
    os.wait()