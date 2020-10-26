class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:               #if list is empty(no head node)
            new_node = Node(data)           #create a new node
            new_node.prev = None            #set its previous as null.
            self.head = new_node            #make new_node the head now
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:                 #while next isnt None
                cur = cur.next
            cur.next = new_node             #points next to new node since now new node is the final node
            new_node.prev = cur             #makes a new node and sets its prev to the current node
            new_node.next = None


    def prepend(self,data):
        if self.head == None:               #for when the list is empty at the start.
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node            #move head to the new node since now its first in list.
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(0)

dllist.print_list()