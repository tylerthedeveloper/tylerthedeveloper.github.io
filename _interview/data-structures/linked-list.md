---
---
[return to all data-structures](data-structures)

[return to resources](resources)

# 3. Singly-Linked List

*   List of nodes of a custom type or object

*   Every node has a pointer to the next node

*   Mutable and iterable structure

## *When to use singly linked lists*
*   When you need to insert or delete data 
*   When you need a mutable list
*   When random access is not needed
*   When there is a notion of ordered-relation in that there is significance in neighbor relationships

## 3.1 Doubly-Linked List

*   Same as before, but each node has a prev and next node
*   The tail points to the head and the head points to the tail
*   Requires extra space, but easier for simple operations because of the ability to backtrack