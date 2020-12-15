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
        pass

    def dequeue(self):
      '''Remove a node from the front of the queue.'''

      # Check for an empty list
      if self.head is None:
         print("Queue is empty")
         return
      # special case when we hit the last item.
      elif self.head == self.tail:
         node = self.head
         data = node.data
         self.head = None
         self.tail = None
         return data
      else:
         # 1 and 2, store a reference to the node
         # and store the data.
         node = self.head
         data = node.data
         # 3. Make the next node head
         self.head = node.next
         # 4. make nodes next property None
         node.next = None
         # 5. Make heads previous property None
         self.head.previous = None
         # 6. Return data
         return data
