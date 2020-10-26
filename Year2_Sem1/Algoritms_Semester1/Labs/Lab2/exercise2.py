""" Class definition for an array-based implementation of the Stack ADT.

For invalid method calls, does not throw exceptions. Instead, returns
None if a return value is expected, and otherwise ignores the request.

"""


class Stack:
    """ An array-based stack. """

    def __init__(self):
        self._list = []      #Note that this is meant to be private
                             #_list should only be accessed from the
                             #methods defined in this class.

    def __str__(self):
        """ Display a stack as a string, by listing elements in sequence.

            |- denotes the bottom of the stack
            -> denotes the top of the stack.
            So '|-x-y-z-> denotes a stack with 3 elements, and z at the top.
        """
        retstr = '|-'
        for element in self._list:
            retstr = retstr + str(element) + '-'
        retstr = retstr + '->'
        return retstr

    def pop(self):
        """ Remove and return the top element of the stack. """
        if len(self._list) == 0:
            return None
        return self._list.pop()

    def push(self, element):
        """ Place element onto the top of the stack. """
        self._list.append(element)

    def top(self):
        """ Return but don't remove the top element of the stack. """
        if len(self._list) == 0:
            return None
        return self._list[-1]

    def length(self):
        """ Return the number of elements on the stack. """
        return len(self._list)

    def test():
        """ Test the basic functionality of the stack. Class method. """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print('stack should be |-1-2-3-->, and is %s' % stack)
        print('stack.length should be 3, and is %d' % stack.length())
        print('stack.top() should be 3, and is %d' % stack.top())
        print('stack.pop() should be 3, and is %d' % stack.pop())
        print('stack should now be |-1-2-->, and is %s' % stack)
        print('stack.length() should be 2, and is %d' % stack.length())
        stack.pop()
        stack.pop()
        print('popped two more items; length() should be 0, and is %d' % (
                                                     stack.length()))
        print('stack.top() should be None, and is %s' % stack.top())
        print('stack.pop() should be None, and is %s' % stack.top())
        print('stack should be |-->, and is %s' % stack)

x = Stack()
x.push(1)
x.push(2)
x.push(3)
print(x.length())      # = 3
