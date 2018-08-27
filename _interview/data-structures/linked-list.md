---
---
[return to all data-structures](data-structures)

[return to resources](resources)

# Singly-Linked List

*   List of nodes of a custom type or object

*   Every node has a pointer to the next node

*   Mutable and iterable structure
* Maintains head pointer to denote the first node in the list

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

## *Time complexity for both singly and doubly linked lists*

* Insertion at front of list: O(1)
* Deletion at front of list: O(1)
* Insertion at specified index: O(n)
* Deletion at specified index: O(n)
* Search: O(n)
* Accessing at specified index: O(n)

## *Practice questions*
