---
---
[return to all data-structures](data-structures)

[return to resources](resources)

# The _Heap_ Data Structure
## Overview
* Resembles a binary tree when drawn.
* Is ordered based on __minimum__ or __maximum__ values.
    * A custom __comparable__ can be used in Java for other comparisons.
    * In the context of _min_ or _max_, either the min or the max respectively is at the root.
* Can be represented as an array as well.
* The tree is near full except for missing nodes in the lowest level on the right-hand side.
* The __height__ of a heap is _log(n)_, where _n_ is the number of the nodes in the tree.
* Relational indices can be calculated for parent nodes and their children.
* Elements can be user-defined data types and structures, or user-defined data structures.

## When to use heaps

*   When you need to sort a list (heap sort)
* 	When using priority [queues](queues).
*   When there is a priority associated with a custom sorting comparable
* 	When the level of a given node is important.
    * This is known as _leveling_.
*   When data is coming in and you want to sort it along the way

## Heapification
_Heapification_ is when a __heap__ is rearranged to maintain the _heap_ property<sup>1</sup>. In the context of a _max heap_, this means that each node is greater than all of its children.

## The _HeapSort_ Algorithm
This algorithm utilizes a _binary head_, or a heap whose nodes each have two children nodes (with the possible exception
of the penultimate level). The steps<sup>2</sup> are as follows:
1. Build a _max heap_ from the input data.
2. Replace the root of the heap (which happens to contain the largest item) with the last item of the heap.
3. Reduce the size of the heap by 1, then _heapify_ the root of the tree.
4. Repeat steps 1-3 as long as the size of the heap is >1.

Once the algorithm breaks, the input data will be sorted!


## Time Complexity

| Operation | Time Complexity |
| :---: | :---: |
| Heapify | O(log(n)) |
| Insert | O(log(n)) |
| Delete | O(log(n)) |
| Building a Heap | Simple Bound: O(n log(n)) |
| Building a Heap | Tight Bound<sup>3</sup> : O(n) |

## _Heap_ Review
Check out GeeksforGeek's [Heap Quiz](https://www.geeksforgeeks.org/data-structure-gq/heap-gq/) to review heap-related properties
and concepts.

### References
1. [NIST: Heapify](https://xlinux.nist.gov/dads/HTML/heapify.html)
2. [GeeksforGeeks: HeapSort](https://www.geeksforgeeks.org/heap-sort/)
3. [GeeksforGeeks: Time Complexity of Building a Heap](https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/)

---
[return to all data-structures](data-structures)

[return to resources](resources)
