class Stack:
    def __init__(self):
        self.alist = []
    def __str__(self):
        retstr = '|-'
        for element in self.alist:
            retstr = retstr + str(element) + '-'
        retstr = retstr + '->'
        return retstr

    def push(self,element):                 #O(1)
        self.alist.append(element)

    def pop(self):                          #O(1)
        if len(self.alist) == 0:
            return None
        return self.alist.pop()

    def top(self):                          #O(1)
        if len(self.alist) == 0:
            return None
        return self.alist[-1]

    def length(self):                       #O(1)
        return len(self.alist)

new_list = []

