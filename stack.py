class Stack(object):
    """
    stack is LIFO (last in, first out)
    Elements are removed from the stack in the reverse order to the order of their addition

    1) push adds an element to the collection;
    2) pop removes the last element that was added.
    3) Additionally, a peek operation may give access to the top of the stack

    """
    def __init__(self):
        self.storage = []

    def peek(self):
        # just show the top of the stack
        print 'top of the stack = {0}'.format(self.storage[0])

    def push(self, p):
        # element enters the top of the stack
        self.storage.insert(0, p)
        print 'stack = ', self.storage

    def pop(self):
        # element removed from the top of the stack only when there is an element available
        if not len(self.storage) == 0:
            print 'popping = {0}'.format(self.storage[0])
            self.storage = self.storage[1:]
            return self.storage
        else:
            raise ValueError('ERROR: Stack is empty, you need to push a value to pop')

if __name__ == "__main__":
    mystack = Stack()
    mystack.push(1)
    mystack.peek()
    mystack.pop()