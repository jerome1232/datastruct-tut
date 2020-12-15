class Stack:
    '''
    This represents a stack implemented by a singly
    linked list.
    '''

    class Node:
        '''
        An individual node inside a linked list
        '''

        def __init__(self, data):
            '''Initialize with provided data and no links.'''
            self.data = data
            self.next = None

    def __init__(self):
        '''Initialize an empty linked list.'''
        self.head = None
    def push(self, value):
       '''Adds a node to the top of the stack.'''

       new_node = Stack.Node(value) # Create a new node

       # This is that check for an empty list.
       if self.head is None:
          self.head = new_node
       else:
          new_node.next = self.head # This connects the new node to the old
          self.head = new_node # This sets the new node as the new head

    def pop(self):
       '''Removes a node from the top of a stack, and returns it's data'''

       if self.head is None:
          print("Can't pop an empty list")
          return
       else:
          node = self.head # Temporarily store the node so we don't lose it when head is reassigned
          data = node.data # Get the data from the node
          self.head = node.next # Set head to the next item down
          node.next = None # Set the node.next being popped to None, python will garbage collect it.
          return data

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def __str__(self):
        output = "stack["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

# Sample tests
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)

# Example of attempted pop on empty linked list
stack = Stack()
stack.pop()
