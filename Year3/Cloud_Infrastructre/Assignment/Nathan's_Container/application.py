'''
- TO RUN: 100,10 gives output of 10 times from 0 to 100 in increments of 10.

Create an application, can be simple but must have a measurable execution time, And run this on the HOST,
the VM and the Container.

Compare these execution times and plot on a graph.

Application:
    take in a number (i) from user
    start timer
    iterator this number (i) in a while loop
        do some calcuation each time to slow down the program
        while i > 1:
            i-=1
    end timer
    write timer and index to file
'''
import time


def application(i,file):
    start_time = time.time()
    for iterator in range(i):
        for padding in range(100000):
            empty_variable = padding
    end_time = time.time()
    execution_time = end_time - start_time
    #Limit to 5 decimal place
    execution_time = ("%.5f"%execution_time)
    with open(file,"a") as textfile:
        textfile.write(str(execution_time)+"             "+str(i)+"\n")

''' Test the application funciton - run it a mutliple of times and append each Execution time to file'''


def test(endPoint,interval):
    #write header to the file
    with open("Execution_Times","w") as textfile:
        textfile.write("Execution time"+"   -   "+"Iterators"+"\n"+"-"*30+"\n")
    #run application function
    for x in range(0,endPoint+interval,interval):
        application(x,"Execution_Times")


user_input = (input("Enter data information (EndPoint,intervals) >>>"))
endPoint = user_input.split(",")[0]
interval = user_input.split(",")[1]
test(int(endPoint),int(interval))
