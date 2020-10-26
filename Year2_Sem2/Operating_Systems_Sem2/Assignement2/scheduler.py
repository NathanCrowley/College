'''
Nathan Crowley - 118429092
'''



from Year2_semester2.Operating_Systems_Sem2.Assignement2.process import *
from Year2_semester2.Operating_Systems_Sem2.Assignement2.queue import *
import random
import sched


def main():
#create the hard coded Processes
    #      priority,id,quanta,state,I/O,trig_Duration
    p1 = Process(1, "P1", 10, "READY", False, 1)#A
    p2 = Process(1, "P2", 5, "READY", False, 3)#B
    p3 = Process(2, "P3", 12, "READY", True, 2)#C
    p4 = Process(3, "P4", 3, "READY", False, 4)#D
    p5 = Process(4, "P5", 9, "READY", True, 2)#E
    p6 = Process(4, "P6", 20, "READY", True, 3)#F

    list_of_processes = [p1, p2, p3, p4, p5, p6]

#place all Process objects into the list of Queues at the correct levels
    for objects in list_of_processes:
        objects.addReadYProcess()
    '''for level in range(len(list_of_queues)):
        print(list_of_queues[level]) gives each queue'''
#set the new time slices for each level
    for level in list_of_queues:
        level.set_time_slice()

    for pro in list_of_processes:
        while pro.quanta >= 0:                                  #while there is processes to execute
            for level in range(len(list_of_queues)):            #level is integer from 0 to 1
                current_queue = list_of_queues[level]           #current queue
                if current_queue.get_Queue_len() != 0:
                    process = current_queue.queue.pop(0)        #first process taken off queue
    #this is where you main code goes
                    rand_trig = random.randint(0, 5)            # have the interrupts happen at random if the variable matches a quota
                    if rand_trig == 0:
                        process.run_interupt()                  # put CPU to sleep for a set time and once completed we continue on
                        continue
                    if process.in_out:
                        process.addBlockedProcess()             #block process and when complete add back to higher priority
                        process.addReadYProcess()
                        process = nextProcess()                 #move onto next process
                    if process.quanta > 0 and process.state == "READY":
                        process.runProcess()
                        process.decrease_quanta(current_queue)
                        if process.quanta > 0:                  #if there is still quanta left for a process after the time slice lower its priority and add back into the list of queues
                            if process.priority >= 7:           #check if the priority is already the lowest priority level
                                process.priority = 7
                            process.priority += 1               #if not at the lowest level then lower the priority
                            process.addReadYProcess()           #add it back at new priority


    print("ALL PROCESSES ARE TERMINATED\n -----------------IDLE-------------")


if __name__ == '__main__':
    main()
