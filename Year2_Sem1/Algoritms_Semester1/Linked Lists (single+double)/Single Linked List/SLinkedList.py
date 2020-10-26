class SLLNode:
    def __init__(self,item,nextnode):
        self.element = item                         #item
        self.next = nextnode                        #pointer to next item

class SLinkedList:
    def __int__(self):
        self.first = None                           #an SLLNode
        self.size = 0                               #an integer

    def add_first(self,element):                    #add at front of the list
        node = SLLNode(element,self.first)          #create a node object
        self.first = node                           #set first node as the newly created object
        self.size = self.size + 1                   #increment the size of the list

    def add_last(self,item):                        #add at end of the list
        new_node = SLLNode(element,None)            #create a new node pointing to None to show its the last item
        if self.first == None:                      #if theres nothing as the first node(SLL is empty)
            self.first = new_node                   #set the first node as the new node
        else:
            node = self.first                       #call the first node 'node'
            while node.next:                        #while the next node != None (this is used to find the last element in the SLL)
                node = node.next                    #now node is the next node in the SLL (sets the node as the last node)
            node.next = new_node                    #node = last node ,so  sets the next node after that as the new node
        self.size = self.size + 1                   #increment size

    def get_first(self):                            #report first item in SLL
        if self.size == 0:                          #if the list is empty
            return None
        else:
            return self.first.element               #else return the element of the first node

    def get_last(self):                             #report last element
        pass

    def remove_first(self):                         #remove first element in the SLL
        pass

    def length(self):                               #report the size
        pass


#-----------------------------------------------------------------------------
mylist = SLinkedList()
mylist.add_last("4")
