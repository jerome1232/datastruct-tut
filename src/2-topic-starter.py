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
      pass

   def proccess(self, athelete):
      '''Processes an atheletes information'''

      place = ""

      if athelete is None:
         return
      elif athelete[1] == 1:
         place = "got Gold"
      elif athelete[1] == 2:
         place = "got Silver"
      elif athelete[1] == 3:
         place = "got Bronze"
      elif athelete[1]  == 4:
         place = "got honorable mention"
      else:
         place = "Did not place"

      print(athelete[0], place, "with score:", athelete[2])

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
for athelete in athletes:
   work.enqueue(athelete)
   work_length += 1

while work_length > 0:
   work.proccess(work.dequeue())
   work_length -= 1