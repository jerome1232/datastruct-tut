![Python](images/python-ds)

# Stacks

## TOC

* [Welcome](welcome.md)
* [Stacks](1-topic.md)
  * [Introduction](#Introduction-to-Stacks)
  * [Use Cases](#Common-use-cases)
  * [Example](#Example)
  * [Anti-Example](#Anti-example)
  * [Coding Challenge](#Coding-Challenge)
* [Linked lists](2-topic.md)
* [Binary Trees](3-topic.md)

# Introduction to Stacks

  Stacks are a data structure which can be thought of as a stack of pancakes. When cooking them we add them to a physical stack of pancakes on a plate. We always add pancakes to the top of our stack, and we always remove pancakes from the top. To do anything else will involve shuffling a lot of pancakes and wouldn't be very efficient. With stacks when we add a pancake, or data item we call this **push**ing. When we remove a pancake or data item this is called **pop**ping. In python a stack can be represented using a dynamic array.

  In python using a dynamic array to implement a stack data structure is efficient because both the **pop** and **push** operations are *O(1)* performance operations.

  ```python
    # creating an empty list.
    stack = []

    # push operation
    #
    # adds the data value 1 to the end of the list
    # or top of the stack.
    stack.append(1)

    # pop operation
    #
    # removes whatever is at the end of the list
    # or top of the stack and assigns it to a variable.
    item = stack.pop()
  ```

  # Common use cases

  Some very common uses cases where a stack would be used is to evaluate expressions or parse syntax. Anytime you need to backtrack or undo operations a stack can be useful (like operations in a word editor, or solving a maze when you need to backtrace your steps after running into a dead-end).

  # Example

  One thing stacks are very good at, is reversing things. If I wanted to quickly and efficiently reverse a string I could use a stack like the example *reverse()* function below. This is fairly straight forward, by simply adding items to the stack and then removing them, they are reversed.

  The *reverse()* function will have a performance of *O(n)*.

  ```python
  def reverse(string):
    # create an empty list to use as a stack
    stack = []

    # loop over the string, adding each character to the stack
    for char in string:
      # This is a push operation
      stack.append(char)

    # loop until the stack is exhausted, popping off each
    # item and printing it
    while len(stack) > 0:
      # This is a pop operation, remember this actually
      # removes items off of the stack, so our stack is decreasing
      # in length each iteration.
      print(stack.pop())
  ```
# Anti-Example

An instance where a stack would be a bad choice is if you needed to regularly remove items from the front of the stack, or even the middle. For example you were trying to perform operations on a First in First out basis, like a line for a grocery store. Every time you take an item from the front of the stack, due to the way dynamic arrays work all items have to be shuffled forward and would take *O(n)* time. There's another data structure we will discuss that would be handy for this situation.

# Coding Challenge

Create a function called *matchParens()* that accepts a string, scans it for opening and closing parens and will return true if all opening parens are closed, and there are no unmatched parens. There is some code with tests to get you started.

***BONUS*** - Match brackets, parens, and curly braces.

```python
def matchParens(string):
  # Create an empty stack
  stack = []

  # replace with your code
  pass


# Tests - Not exhaustive.

strings = (
           "This has (matched) parens!",
           "This doesn't (have matched parens",
           "Neither) does this"
           # add more test strings if you want here (I'd advise it)
           )

for string in strings:
  print(matchParens(string))

# Expected output:
# True
# False
# False
```

If you get stuck there is a completed version [here](src/1-topic.py)

  ---

[Back to top](#stacks)

[Previous Module](welcome.md)

[Next Module](2-topic.md)