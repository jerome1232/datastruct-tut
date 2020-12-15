def matchParens(string):
   # Create an empty stack
   stack = []

   for char in string:
      if char == "(":
         # When we encounter an opening paren
         # add it to the stack.
         stack.append(char)
      elif char == ")":
         # When we encounter a closing paren, check
         # that there's an open parent to close.
         if len(stack) > 0:
            # Since we have something in the stack,
            # we've encountered an opening paren.
            # Pop it off.
            stack.pop()
         else:
            # if our stack is empty, then we have an unmatched
            # closing paren, we know right now parens are unbalanced.
            return False

   if len(stack) > 0:
      # If the stack is bigger than zero,
      # we had unclosed parens.
      return False
   else:
      # If we get here our stack was zero,
      # so we have a paren balanced string!
      return True



# Tests

strings = (
           "This has (matched) parens!",
           "This doesn't (have matched parens",
           "Neither) does this"
           # add more test strings if you want here
           )

for string in strings:
   print(matchParens(string))

# Expected output:
# True
# False
# False