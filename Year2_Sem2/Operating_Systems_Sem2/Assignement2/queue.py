'''
Nathan Crowley - 118429092
'''


from asn1crypto._ffi import null

class queue():      #each queue object is a list and has a type to clarify if its a READY or BLOCKED queue
    def __init__(self, level, type):
        self.queue = []
        self.__level = level
        self.type = type
        self.__Qtime_slice = 1          #set base time slice to 1

    def __str__(self):
        return "Queue level: {}. Type: {}.|| Time Slice: {}.".format(self.__level,self.type,self.__Qtime_slice)

#Getters and Setters
#******************************
    def get_Qlevel(self):
        return self.__level

    def set_time_slice(self):   #Each queue initialises the time slice to 0 when created and then use the time slice setter to calculate the correct time slice
        i = self.get_Qlevel()
        q = list_of_queues[0].__Qtime_slice         #set q as base time slice
        self.__Qtime_slice = (2**i)*q

    def get_time_slice(self):
        return self.__Qtime_slice

#*****************************
    def isQueueEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    def get_Queue_len(self):
        return len(self.queue)

    def printQueue(self):
        print("-" * 20, "{} QUEUE".format(self.type), "-" * 20)
        if self.isQueueEmpty():
            return "***** THE QUEUE IS EMPTY *****"
        for items in self.queue:
            print(items)

def nextProcess(): #self = list_of_queues
    for level in range(len(list_of_queues)):                #level is an int from 0 to 7
        if list_of_queues[level].get_Queue_len() != 0:      #check each level if its empty or not
            next_pro = list_of_queues[level].queue.pop(0)   #if there is a process in a queue pop it off the top of the queue
            return next_pro

#instances of the Queue class


ready = queue(0,"READY")
ready1 = queue(1,"READY")
ready2 = queue(2,"READY")
ready3 = queue(3,"READY")
ready4 = queue(4,"READY")
ready5 = queue(5,"READY")
ready6 = queue(6,"READY")
ready7 = queue(7,"READY")
blocked = queue(0,"BLOCKED")


#add all queues to the list of queus
list_of_queues = [ready, ready1, ready2, ready3, ready4, ready5, ready6, ready7]

