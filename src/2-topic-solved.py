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

   def proccess(self, athlete):
      '''Processes an athletes information'''

      place = ""

      if athlete is None:
         return
      elif athlete[1] == 1:
         place = "got Gold"
      elif athlete[1] == 2:
         place = "got Silver"
      elif athlete[1] == 3:
         place = "got Bronze"
      elif athlete[1]  == 4:
         place = "got honorable mention"
      else:
         place = "Did not place"

      print(athlete[0], place, "with score:", athlete[2])

athletes = (('Susan', 1, 100),
         ('Billy', 3, 300),
         ('Jill', 2, 500),
         ('Anthony', 3, 200),
         ('Eric', 4, 30),
         ('Erin', 2, 25),
         ('Elizabeth', 5, 32),
         ('Angela', 1, 22),
         ('Emilee', 3, 89),
         ('Sarah', 6, 999),
         ('Anna', 8, 245))

work = Queue()

work_length = 0
for athlete in athletes:
   work.enqueue(athlete)
   work_length += 1

while work_length > 0:
   work.proccess(work.dequeue())
   work_length -= 1