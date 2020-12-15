def insert(self, data):
   """
   Insert 'data' into the BST.  If the BST
   is empty, then set the root equal to the new
   node.  Otherwise, use _insert to recursively
   find the location to insert.
   """
   if self.root is None:
      self.root = BST.Node(data)
   else:
      self._insert(data, self.root)  # Start at the root

def _insert(self, data, node):
   """
   This function will look for a place to insert a node
   with 'data' inside of it.  The current sub-tree is
   represented by 'node'.  This function is intended to be
   called the first time by the insert function.
   """
   # bust out of the function if data exists in the tree
   if data is node.data:
      return
   if data < node.data:
      # The data belongs on the left side.
      if node.left is None:
            # We found an empty spot
            node.left = BST.Node(data)
      else:
            # Need to keep looking.  Call _insert
            # recursively on the left sub-tree.
            self._insert(data, node.left)
   elif data >= node.data:
      # The data belongs on the right side.
      if node.right is None:
            # We found an empty spot
            node.right = BST.Node(data)
      else:
            # Need to keep looking.  Call _insert
            # recursively on the right sub-tree.
            self._insert(data, node.right)