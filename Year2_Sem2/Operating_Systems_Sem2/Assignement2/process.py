'''
Nathan Crowley - 118429092
'''


from Year2_semester2.Operating_Systems_Sem2.Assignement2.scheduler import *
from Year2_semester2.Operating_Systems_Sem2.Assignement2.queue import *
import time
import random

class Process:
    def __init__(self,priority,id,quanta,state,in_out,trig_duration):
        #each process object has an id,BurstTime,state,Input_output,Interupt duration and time slice.
        self.__priority = priority
        self.__id = id
        self.__quanta = quanta
        self.__state = state
        self.__in_out = in_out
        self.__trig_duration = trig_duration
        #*****************
        self.__arrivalTime = 0
        #*****************

    def __str__(self):
        return "Process id: {}. Quanta: {}. State: {}. || I/O: {}. Trigger Duration: {}.".format(self.__id,self.__quanta,self.__state,self.__in_out,self.__trig_duration)

#Getters and Setters
    @property
    def id(self):
        return self.__id

    @property
    def quanta(self):
        return self.__quanta
#-------------------------------------------------------------
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self,new_state):
        self.__state = new_state
#--------------------------------------------------------------
    @property
    def in_out(self):
        return self.__in_out
    @in_out.setter
    def in_out(self,new):
        self.__in_out = new
#--------------------------------------------------------------
    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self,new_priority):
        self.__priority = new_priority


#Functions
    def addReadYProcess(self):      #if the processes state is Ready append it to the Queue with matching priority
        if self.state == "READY":
            p = self.priority
            list_of_queues[p].queue.append(self)

    def addBlockedProcess(self):
        self.state = "BLOCKED"            #when I/O triggered suspend the process while the trigger runs
        print("Process: {} is Blocked for {}s.".format(self.id,self.__trig_duration))
        blocked.queue.append(self)          #append to the blocked queue while it is suspended
        time.sleep(self.__trig_duration)    #set off the trigger (interrupt handler)
        self.state = "READY"
        if self.priority >= 0:
            self.priority -= 1           #increase its priority before it is added back
        self.priority = 0
        print("Priority has been increased. New priority = {}.".format(self.priority))
        print("Process: {} State: {}.".format(self.id,self.state))


    def runProcess(self):           #simulate the scheduler
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(self.__quanta,self.priority,print("**** PROCESS {} WAS RAN ******.\n".format(self)))

    def decrease_quanta(self,current_Q):  # decrement the quanta of a process after it has run
        #process = self
        self.__quanta = self.__quanta - current_Q.get_time_slice()
        if self.__quanta < 0:  # if the Burst Time is negative set it as 0 for convenience
            self.__quanta = 0
        print("Process: {} Quanta: {}.".format(self.id, self.__quanta))

    def run_interupt(self):         #when an interupt happens we want to set the state to Suspended and run the interupt handler then set the state back to Ready once the interupt is completed.
        self.state = "SUSPENDED"
        delay = random.randint(1,3)
        print("Process: {} suspended for {} seconds.".format(self.id,delay))
        time.sleep(delay)
        self.state = "READY"
        print("Process: {} State: {}".format(self.id,self.state))
