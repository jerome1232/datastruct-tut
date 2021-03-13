![Python](images/python-ds)

# Basic Data Structures: An Introduction

## TOC

* [Welcome](index.md)
    * [Assumptions](#assumptions)
    * [Introduction](#introduction)
    * [Data Structures](#data-structures)
    * [Big O Notation](#big-o-notation)
* [Stacks](1-topic.md)
* [Linked lists](2-topic.md)
* [Binary Trees](3-topic.md)

## Assumptions

  The reader has a basic working knowledge of object oriented programming in Python3.

## Introduction
  I am Jeremy Jones, a computer science major at [BYU-I](www.byui.edu).

  This tutorial shall teach the reader about the basic data structures [Stacks](1-topic.md), [Linked Lists](2-topic.md), and [Binary Trees](3-topic.md). There will be example code for some problems for the purposes of demonstration. In addition there will be a programming challenge to be solved with the data structure discussed in each module with an example solution in case the reader gets stuck.

## Data Structures

  Data structures in the field of computer science are collections of data values and their relationships that enables efficient access and use for varying use cases. Depending on what is going to be done with the data, there are different ways of storing, formatting and accessing the data that can be leveraged by using different data structures.

## Big O Notation

  Big O notation is important for talking about the performance of a
  given algorithm.

  Big O notation is a mathematical way of representing how fast a
  given algorithm is as it's data set, or inputs trend towards
  infinity.

  A single operation would be described as *O(1)*.

  ```python
  # O(1) performance
  def add(x, y):
    return x + y
  ```

  The function below will loop through the data set once to find a
  solution. It can be said it would take *O(n)* to complete it's task.

  ```python
  # loops through the entire array once, printing each item
  # O(n) performance
  def print(n):
    for item in n:
        print item
  ```

  For the purposes of Big O notation any constant multiples or
  addends are dropped off. The function below would be *O(2n)* because it loops through the data twice, but we
  drop that constant so it's just *O(n)*.

  ```python
  # loops through the entire array twice, printing each item
  # O(2n), the constant is dropped for O(n) performance
  def printTwice(n):
    for item in n:
      print item
    for item in n:
      print item
  ```

  A nested for-loop is an example of an algorithm that takes *O(n²)* time. This one would print a two dimensional array.

  ```python
  # prints each item in a 2d array.
  # O(n²) performance
  def printMatrix(n):
    for row in n:
      for col in row:
        print(col)
  ```

  A classic example of an algorithm with exponential Big O notation
  is a recursive fibonacci sequence. It has a Big O notation of *O(2ⁿ)*.
  For every call to fib, fib calls itself twice. There will be more
  on recursion later, if you don't understand it now, don't worry
  about it. Just understand this gets slow very quickly.

  ```python
  # This has O(2ⁿ) performance. This is terrible!
  def fib(n):
    if n <= 1 : return n
    return fib(n - 2) + fib(n - 1)
  ```
  For the purposes of big O notation we also drop the least
  significant terms. So if an algorithm took *O(n⁴ + n² + n/2)* time
  we would just say it takes *O(n⁴)* time to complete. As our data
  becomes arbitrarily large those lesser terms become less and less
  significant. A big O notation of *O(log(n))*
  is best, while *O(2ⁿ)* is very poor.

---

  [Back to top](#basic-data-structures-an-introduction)

  [Next module](1-topic.md)
