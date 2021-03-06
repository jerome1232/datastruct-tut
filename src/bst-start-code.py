class BST:
   '''A Binary Search Tree.'''

   class Node:
      '''An individual node within a BST.'''

      def __init__(self, data):
         '''Initialize a node with no known links.'''

         self.data = data
         self.left = None
         self.right = None

   def __init__(self):
      '''Initialize an empty BST.'''

      self.root = None

   def __iter__(self):
      '''Teach python how to iterate over our data structure'''

      yield from self._traverse_forward(self.root)

   def _traverse_forward(self, node):
      '''
      If a node is none do nothing, otherwise travel down
      the left side then the right side
      '''

      if node is not None:
         # travel down the left, this will stop when it hits a node
         # with no left node
         yield from self._traverse_forward(node.left)
         yield node.data
         # Do the same on the right
         yield from self._traverse_forward(node.right)

   def get_height(self):
      '''Determine the height of a BST.'''

      # If it's an empty tree our height is zero
      if self.root is None:
         return 0
      else:
         return self._get_height(self.root)

   def _get_height(self, node):
      '''
      The height of any subtree is 1 plus the height of either the left
      or right subtree, whichever is greater.
      '''

      # This is the base case, we are at a Node that is None
      if node is None:
         return 0
      else:
         # A lot like __iter__, we just go down one side at a time.
         # Adding up their heights
         sum_right = 1 + self._get_height(node.right)
         sum_left = 1 + self._get_height(node.left)
         # We return whichever sum is greatest.
         return sum_right if sum_right > sum_left else sum_left

   def __in__(self, data):
      """
      Checks if data is in the BST.  This function
      supports the ability to use the 'in' keyword:

      if 5 in my_bst:
         ("5 is in the bst")

      """
      pass

   def _contains(self, data, node):
      """
      This function will search for a node that contains
      'data'.  The current sub-tree being search is
      represented by 'node'.  This function is intended
      to be called the first time by the __in__ function.
      """
      pass

   def insert(self, data):
      """
      Insert 'data' into the BST.  If the BST
      is empty, then set the root equal to the new
      node.  Otherwise, use _insert to recursively
      find the location to insert.
      """
      pass

   def _insert(self, data, node):
      """
      This function will look for a place to insert a node
      with 'data' inside of it.  The current sub-tree is
      represented by 'node'.  This function is intended to be
      called the first time by the insert function.
      """
      pass

def build_bst(state_list):
   '''
   This will take a sorted list and build
   a balanced BST with it. You'll want to find the
   middle of the list and call a recursive version
   called _build_bst which will do the actual building
   '''
   bst = BST()
   _build_bst(state_list, 0, len(state_list) - 1, bst)
   return bst

def _build_bst(state_list, first, last, bst):
   '''
   Write build_bst, it will insert the middle item into
   into the BST. It will be given the first and last
   indices. You can determine the middle element given
   these.

   After the middle value is inserted you should make
   recursive calls sending the upper and lower half of
   the lists. If you do it write you will get a balanced
   bst.
   '''
   pass

zombie_states = (
   'Alabama', 'Arizona', 'California',
   'Colorado', 'Connecticut', 'Delaware',
   'Florida', 'Georgia', 'Kentucky',
   'Louisiana', 'Maine', 'Maryland',
   'Massachusetts', 'Montana', 'Nebraska',
   'Nevada', 'New Hampshire', 'New Mexico',
   'New York', 'North Carolina', 'Pennsylvania',
   'Rhode Island', 'South Carolina', 'Utah',
   'Vermont', 'Virginia'
)

def interactive_menu(bst):
   '''
   An interactive menu to ask the user which
   state to visit.
   '''

   print("What state would you like to visit?")
   print("")
   state = input(":$ ")
   if state in bst:
      print("This state has been overrun by Zombies!")
      print("Avoid it all costs!")
   else:
      print("This state is safe to visit. Enjoy!")
   print("")
   data = input("Check another state (y/n)? ")
   if data == "y" or data == "Y":
      return True
   else:
      return False

# This will build your BST
bst = build_bst(zombie_states)

# Loops until user quits checking states.
#while interactive_menu(bst):
#   continue

# Implement testing below