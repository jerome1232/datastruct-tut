class Queue:
    '''
    This represents a queue implemented by a doubly
    linked list.
    '''

    class Node:
        '''
        An individual node inside a linked list
        '''

        def __init__(self, data):
            '''Initialize with provided data and no links.'''
            self.data = data
            self.previous = None
            self.next = None

    def __init__(self):
        '''Initialize an empty linked list.'''
        self.head = None
        self.tail = None

    def enqueue(self, value):
        '''Add a node to the end of the queue'''

        # 1. Create new node
        new_node = Queue.Node(value) # Create a new node

         # 1.5 empty list check
        if self.tail is None:
            # All links are default to None
            # So we just make the node the head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # 2. Link to old tail
            new_node.previous = self.tail
            # 3. Link old tail to new node
            self.tail.next = new_node
            # 4. Make tail the new_node
            self.tail = new_node

    def dequeue(self):
        '''Remove a node from the front of the queue.'''
        pass