#(i)
'''
4 methods available in the STACK =
        -PUSH: addd and item to the stack.
        -POP: remvoe the item that has been in the stack for the shortest time.
        -TOP: report the item that is on top of the stack(been on for shortest time).
        -Length: report how many elements in the stack.
'''
#(ii)***************************************************************************
'''
st.push('d') => st = [d]
st.pop() => st = []
st.push('c') => st = [c]
st.push('l') => st = [l,c]
st.push('o') => st = [o,l,c]
st.pop() => st = [l,c]
st.pop() => st = [c]
st.push('o') => st = [o,c]
st.push('b') => st = [b.o.c]
st.push('h') => st = [h,b,o,c]
st.pop() => st = [b,o,c]
st.pop() => st = [o,c]
st.push('r') => st = [r,o,c]
st.push('r') => st = [r,r,o,c]
st.pop() => st = [r,o,c]
st.push('k') => st = [k,r,o,c]


final_state = [k,r,o,c]

'''
#(iii)**************************************************************************

class Stack:
    def __init__(self):
        self.alist = []


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
stack1 = Stack()
stack1.push(1)
stack1.push(2)

'''
The average time is O(1) which means it is constant time and therefore very efficent.'''