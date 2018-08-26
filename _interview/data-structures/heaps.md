---
---
[return to all data-structures](data-structures)

[return to resources](resources)

# Heaps

*   Resembles a binary tree

*   Has ordering based on a min or max (custom comparable can be implemented)

*   The min or max is at the root

*   Can be represented in an array

*   The tree is near full except there may be missing nodes at the right-most indices in the last level

*   The height is log(n) where n is the number of nodes in the tree

*   Relational Indices can be calculated for parent and children

*   Elements include built-in or custom objects


## *When to use heaps*

*   When you need to sort a list (heap sort)
*   Priority Queue
*   When there is a priority associated with a custom sorting comparable
*   When you need a notion of leveling
*   When data is coming in and you want to sort it along the way

## *Time complexity*

* heapify (restoring ordering property of a heap): O(log n)
* insertion: O(log n)
* deletion: O(log n)
* building a heap:
	* simple bound: n insertions/n calls to heapify = O(n log n)
	* tight bound: O(n) - see proof https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/

## *Practice questions*
