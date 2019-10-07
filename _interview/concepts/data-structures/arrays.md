---
---
[return to all data-structures](data-structures)

[return to concepts](materials)

# Arrays

## Overview
*   Immutable Object - Require pre-allocated space
*   An Indexed collection of elements (of the same type)
    * To mix different types, consider using a __list__
* Size can't be changed after initializing the array
    * Can be circumvented with Java's _ArrayList_ struct or Python's _list_ struct


## When to use arrays

*   When you know the size of the list
*   When the size of the list won't change
*   When the ordering of the list won't change
*   When dealing with matrices (n-dimensional lists)
*   When binary / linear search is needed
*   When direct (indexed) access is needed

## Time Complexity

| Operation | Time Complexity |
| :---: | :---: |
| Index | O(1) |
| Search | O(n) |

The worst _space complexity_ of an array is __O(n)__.


* Accessing an element at a certain position: O(1)
* Traversing an array (e.g. looping through an array, linear search): O(n)

---
[return to all data-structures](data-structures)

[return to concepts](materials)
