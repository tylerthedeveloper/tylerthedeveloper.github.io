---
---
[return to all data-structures](data-structures)

[return to resources](resources)

# The _Queue_ Data Structure
## Overview
* A __queue__ is a _collection_ data type that is best visualized as a "line" of elements.
* It can be described as _FIFO_ (First in, First out).
* Differs from _stacks_ in how objects are removed (in _queues_, the __front__ entry is removed).

## Queue Operations
There are four basic operations<sup>1</sup> that can be done on a queue:
* __enqueue()__: adds an element to the left of the queue if the queue is not full.
* __dequeue()__: remove the rightmost element of the queue if the queue is not empty.
* __front()__: return the front item from the queue.
* __rear()__: return the last item from the queue.

If the queue is finite, the following operation is necessary:
* __size()__: returns the size of the queue; useful for checking if it is full.

## When to Use Queues
* When FIFO processing order matters.
* When data doesn't need to be processed immediately after being added to the queue<sup>1</sup>.

## Time Complexity

| Operation   | Time Complexity |
|---------|------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Size    | O(n) |

## Practice Problems
Check out HackerEarth's [Basics of Queues](https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/)
page for queue-related practice problems.

### References
1. [GeeksforGeeks: Queue Introduction and Array Implementation](https://www.geeksforgeeks.org/queue-set-1introduction-and-array-implementation/)

---
[return to all data-structures](data-structures)

[return to resources](resources)
