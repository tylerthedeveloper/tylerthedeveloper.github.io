---
---
[return to resources](resources)

# 1. Arrays
    
*   Immutable Object - Require pre-allocated space

*   An Indexed collection of elements (of the same type)

*   Elements include built-in or custom objects or data-types

## *When to use arrays*

*   When you know the size of the list
*   When the size of the list won't change
*   When the ordering of the list won't change
*   When dealing with matrices (n-dimensional lists)
*   When binary / linear search is needed
*   When direct (indexed) access is needed


# 2. Heaps

*   Resembles a binary tree

*   Has ordering based on a min or max (custom comparable can be implemented)

*   The min or max is at the root

*   Can be represented in an array

*   The tree is near full except there may be missing nodes at the right-most indices in the last level

*   The height is log(n) where n is the number of nodes in the tree

*   Relational Indices can be calculated for parent and children

*   Elements include built-in or custom objects


## *When to use heaps*

*   When you need to sort the list
*   Priority Queue
*   When there is a priority associated with a custom sorting comparable
*   When you need a notion of leveling
*   When data is coming in and you want to sort it along the way

# 3. Linked List

*   List of nodes of a custom type or object

*   Every node has a pointer to the next node

*   Mutable and iterable structure


## *When to use linked lists*
*   When you need to insert or delete data 
*   When you need a mutable list
*   When random access is not needed
*   When there is a notion of ordered-relation in that there is significance in neighbor relationships

## 4. ???

