
def __in__(self, data):
   """
   Checks if data is in the BST.  This function
   supports the ability to use the 'in' keyword:

   if 5 in my_bst:
      ("5 is in the bst")

   """
   return self._contains(data, self.root)  # Start at the root

def _contains(self, data, node):
   """
   This function will search for a node that contains
   'data'.  The current sub-tree being search is
   represented by 'node'.  This function is intended
   to be called the first time by the __in__ function.
   """
   # We hit an empty node
   if node is None : return False
   # We found our data!
   if data is node.data : return True
   # Recurse to the left
   if data < node.data:
      return self._contains(data, node.left)
   # Recurse to the right
   else:
      return self._contains(data, node.right)