---
---
[return to all data-structures](data-structures)

[return to concepts](materials)

# Singly-Linked List

## Overview
*   List of nodes of a custom type or object
*   Every node has a pointer to the next node
*   Mutable and iterable structure
*   Maintains head pointer to denote the first node in the list

## *When to use singly linked lists*
*   When you need to insert or delete data 
*   When you need a mutable list
*  When implementing queues
*   When random access is not needed
*   When there is a notion of ordered-relation in that there is significance in neighbor relationships

## Doubly-Linked List

*   Same as before, but each node has a prev and next node
*   The tail points to the head and the head points to the tail
*   Requires extra space, but easier for simple operations because of the ability to backtrack

## Time Complexity
The following table describes time complexity for both singly-linked and doubly-linked lists.

| Operation | Time Complexity |
| :---: | :---: |
| Insertion at index 0 | O(1) |
| Insertion at index _n_ | O(n) |
| Deletion at index 0 | O(1) |
| Deletion at index _n_ | O(n) |
| Search | O(n) |
| Access index _n_ | O(n) |

## Practice Questions
Check out GeeksforGeeks' [compilation](https://www.geeksforgeeks.org/top-20-linked-list-interview-question/) of popular
interview questions related to _linked lists_.

---

[return to all data-structures](data-structures)

[return to concepts](materials)
