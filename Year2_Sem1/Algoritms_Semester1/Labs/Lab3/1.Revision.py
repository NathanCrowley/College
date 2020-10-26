#(i)
'''
4 methods of a Queue (FIFO):
    1.enqueue - add item to the que.
    2. dequeue - remove and return the item that has been in the queue for longest time.
    3. front - report the item that has been in the queue for longest time.
    4. length - report how many elements are in the queue.
'''


#(ii)
'''
q0.enqueue('p')         Q = [p]
q0.enqueue('a')         Q = [p,a]
q0.dequeue()            Q = [a]
q0.enqueue('r')         Q = [a,r]
q0.dequeue()            Q = [r]
q0.dequeue()            Q = []
q0.enqueue('i')         Q = [i]
q0.enqueue('s')         Q = [i,s]
q0.enqueue('f')         Q = [i,s,f]
q0.enqueue('r')         Q = [i,s,f,r]
q0.enqueue('a')         Q = [i,s,f,r,a]
q0.dequeue()            Q = [s,f,r,a]
q0.enqueue('n')         Q = [s,f,r,a,n]
q0.dequeue()            Q = [f,r,a,n]
q0.enqueue('c')         Q = [f,r,a,n,c]
q0.enqueue('e')         Q = [f,r,a,n,c,e]

Q = [f,r,a,n,c,e]

'''


#(iii)
'''
Wrap-Around implementaion: 
    we need this because since a Queue is FIFO, there can be free space at the start of the  
    queue which could be used instead of extending the list size, which can be costly.
    
    So we use a HEAD and TAIL to determine if each block of the list is full or not,
    it will only extend the list size when the TAIL and HEAD point at the same index.

Each operation will have a O(1).
'''