import random
class Process:
    def __init__(self,p_id,size):       #each process has an id and size required
        self.id = p_id
        self.sizeKB = size

    def __str__(self):
        return "Process{}: Size {} KB.".format(self.id,self.sizeKB)

class Block:
    def __init__(self,Bid):         #each Block in memory has an id,number of pages, state (if used or not) and size in KB
        self.id = Bid
        x = random.randint(1,7)
        self.pages = (2**x)
        self.pageSize = 4
        self.state = 0
        self.Bsize = self.pages*self.pageSize
        self.status = "FREE"
        self.remainKB = self.pages

    def __str__(self):
        #return "*"+"\t"+"Block {} Pages {} BlockState {} BlockSize {}KB *Status = {}*: ".format(self.id,self.pages,self.state,self.Bsize,self.status)+"["+("^"*self.pages)+("|"*self.remainKB)+"]"
        return "BLOCK-{} (Number of Pages {}. BlockState {} .Block Size {}KB.| *Status = {}*".format(self.id,self.pages,self.state,self.Bsize,self.status)

class SLLNode:
    def __init__(self,item,nextnode):
        self.element = item
        self.next = nextnode

class SLinkedList:
    def __init__(self,size):
        self.first = SLLNode(None,None)
        self.__sizeKB = size
        self.size = 0

    def __str__(self):                              #prints a representation of memory and its blocks
        list = "*"*75+"|Main Memory |"+"*"*75+"\n"
        l = len(list)
        node = self.first.next
        if node is not None:
            list += str(node.element)
            list += "\n"+("-"*120)+"\n"
            while node.next:
                list += "\t"+str(node.element)
                list += "\n"+("-"*120)+"\n"
                node = node.next
            list += "*"*l
        else:
            node = node.next
        return list

    def add_block(self):
        #block = Block(0)
        #self.add_first(block)
        sum = 0
        x = 0
        while sum < self.get_sizeKB():
            block = Block(x)
            if sum + block.Bsize > self.get_sizeKB():
                continue
            self.add_last(block)
            sum += block.Bsize
            x += 1

    def add_first(self,item):
        node = SLLNode(item,self.first)
        self.first = node
        self.size += 1

    def add_last(self,item):
        newnode = SLLNode(item,None)
        if self.first is None:
            self.first = newnode
        else:
            node = self.first
            while node.next:
                node = node.next
            node.next = newnode
        self.size += 1

    def get_first(self):
        if self.size == 0:
            return None
        return self.first.element

    def get_last(self):
        if self.size == 0:
            return None
        node = self.first
        while node.next:
            node = node.next
        return node.element

    def get_sizeKB(self):
        return self.__sizeKB

    def remove_first(self):
        if self.size == 0:
            return None
        item = self.first.element
        self.first = self.first.next
        self.size -= 1
        return item

    def length(self):
        return self.size

#----------------------------------------
free_memory = []
for num in range(0,20):
    rand_KB = random.randint(10,100)
    process = Process(num,rand_KB)
    free_memory.append(process)
for ps in free_memory:
    print(ps)
#print("-"*50)
#--------------------------------------------
main_memory = SLinkedList(4000)
main_memory.add_block()

#print(main_memory)
#print("*"*100)
#print(main_memory.get_sizeKB(),"KB")


