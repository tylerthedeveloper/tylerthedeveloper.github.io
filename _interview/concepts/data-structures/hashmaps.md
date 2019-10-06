---
---
[return to all data-structures](data-structures)

[return to concepts](materials)

# The _HashMap_ Data Structure
## Overview
* Use a _hash_ function to map __keys__ to __values__.
* Each __keys__ is associated with a list of values
    * These values, when hashed, give the key
* Implemented with an array of lists
    * Each key corresponds to a slot in the array containing the list of its values
* Automatically resize themselves to maintain constant average _insertion_ and _lookup_ times

## When to Use HashMaps
* When caching data
* When creating a dictionary of terms/values
* Keeping track of which nodes have been visited in a depth-first or breadth-first search of a [graph](../graphs).

## Time Complexity & Space Complexity

| Operation | Average Time Complexity
| :---: | :---: |
| Indexing | N/A |
| Search | O(1) |
| Insertion | O(1) |
| Deletion | O(1) |

The worst _space complexity_ of a HashMap is __O(n)__.

## HashMap Concept Review
A useful summary of HashMap concepts to review can be found [here](https://javaconceptoftheday.com/java-hashmap-programs-and-examples/).

---
[return to all data-structures](data-structures)

[return to concepts](materials)
