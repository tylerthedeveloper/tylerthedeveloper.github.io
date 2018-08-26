---
---
[return to all data-structures](data-structures)

[return to resources](resources)

# Hashmap

*   Uses a hash function to map **keys** to **values**

*   Each key is associated with a list of values, which hash to that key by the hash function

*   Implemented with an array of lists, with each key corresponding to a slot in the array containing the list of its values

* Automatically resize themselves to maintain constant average insertion and lookup times


## *When to use hashmaps*
*   Caches/dictionaries
*   Keeping track of the solutions to subproblems in dynamic programming (memoization)
* Keeping track of which nodes have been visited in a depth first search or breadth first search of a graph

## *Time complexity*
* With automatic resizing, a hashmap will have average O(1) time for insertion, lookup, and deletion
* The worst case time for these operations in O(n)

## *Practice questions*
