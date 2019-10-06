---
---
[return to all data-structures](data-structures)

[return to concepts](materials)

# The _Stack_ Data Structure
## Overview
* A __stack__ is a _collection_ data type that is best visualized as a "tower" of elements.
* It can be described as _LIFO_ (Last in, First out).
* Differs from _queues_ in how objects are removed (in _stacks_, the __last__ entry is removed).

## Stack Operations
There are four basic operations<sup>1</sup> that can be done on a stack:
* __push()__: adds an element to the top of the stack.
      * Depending on your implementation of __stack__, you may need to check if the stack is not full first.
* __pop()__: removes an element from the top of the stack if the stack is not empty.
* __peek()__: Return the top element of the stack, but don't remove it.
* __isEmpty()__: return __TRUE__ if the stack is empty and __FALSE__ otherwise.

## When to Use Stacks
* When LIFO processing order matters.
* When data needs to be processed immediately after being added to the stack.
* Keeping track of changes in a file. For example, in Microsoft Word.
    * Edits are stored as entries in a stack for easy retrieval (just pop the stack)


## Time Complexity

| Operation   | Time Complexity |
|--------|------|
| Push   | O(1) |
| Pop    | O(1) |


## Practice Problems
Check out HackerEarth's [Basics of Stacks](https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/)
page for more practice problems.

* Given a word (string), print the word backwards


### References
1. [GeeksforGeeks: Stack Data Structure (Introduction and Program)](https://www.geeksforgeeks.org/stack-data-structure-introduction-program/)


---
[return to all data-structures](data-structures)

[return to concepts](materials)
