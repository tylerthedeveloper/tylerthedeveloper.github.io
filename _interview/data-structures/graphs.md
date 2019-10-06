---
---
[return to all data-structures](data-structures)

[return to resources](resources)

# The _Graph_ Data Structure

## Overview
Graphs come in many forms, all of which share the following properties:
* A __graph__ is made up of two sets called the _vertices_ and _edges_.
* The _vertices_ of a graph are typed. The set may be finite or infinite.
    * Not all vertices are necessarily connected by an edge; these outliers are aptly named '_islands_'.
* Each element of the _edge_ set is a pair consisting of two elements from the _vertices_ set.
    * Edges may or may not be completely connected to every vertex.
    * Edges can have weights and a direction, though neither is required.

## When to Use Graphs
* When establishing 'many-to-many' relationships.
    * i.e. more than _one-to-one_.
* When direction is important.
* When neighbors are important.
* When order is important.
* When the relationship between objects resembles family [trees](../trees).
* When dealing with maps.

## Types of Graphs
* Undirected Graphs: E(1,2) == E(2,1)
    * When traversing these graphs, you do __NOT__ have to keep direction in mind.
* Directed Graphs: E(1,2) != E(2,1)
    * There is a direction that must be respected when traversing this graph.
* Vertex Labeled Graphs
    * There is an order that must be followed when traversing these graphs.
* Cyclic Graph
    * There is at least one cycle (i.e. return to the previous node) in this graph (hence the name).
* Edge-labeled Graphs
    * There is a notion of labeling edges that has meaning.
* Weighted Graphs
    * Edges have weights in this type of graph.
* Directed-Cyclic Graphs
    * In addition to there being at _least_ one cycle in this graph, there is a direction that must be followed.
* Disconnected Graphs
    * This type of graph allows for _islands_ (vertices that are not connected by an edge).

## Graph Representations
* __Adjacency List__: an array of lists, each of which contain all the vertices that are adjacent to vertex _i_<sup>1</sup>.
* __Adjacency Matrix__: a square matrix whose elements indicate whether pairs of vertices are adjacent or not<sup>2</sup>.
* __Incidence Matrix__: a matrix with a row for each _vertex_ and a column for each _edge_<sup>3</sup>. 1's indicate a connection between the
                        vertex and edge.

## Graph Traversal
* __Depth-first Search__ (DFS): Visit child vertices before sibling vertices (i.e. start from the bottom of the graph)
    * In a __tree__, DFS can be visualized by starting at the _leaves_ of a tree and moving up to the mother node once all
    leaves have been visited
* __Breadth-first Search__ (BFS): Visit sibling vertices before child vertices
    * Useful for finding the shortest path between two vertices
    * In a __tree__, BFS can be visualized by starting at the left-most daughter node of the root node and moving left-to-right.
    Once the right-most daughter node is visited, move down to the left-most daughter node's daughter.

## Time Complexity
In the following table, _V_ and _E_ refer to the lengths of the _vertices_ and _edges_ sets respectively. In mathematical
notation, these values would be referred to by |V| and |E|.

| Graph Representation | Operation | Time Complexity |
| :---: | :---: | :---: |
| Adjacency List | Store Graph | O(V + E) |
| | Add Vertex | O(1) |
| | Add Edge | O(1) |
| | Remove Vertex | O(E) |
| | Remove Edge | O(V) | 
| | Check Vertex Adjacency | O(V) |
| Adjacency Matrix | Store Graph | O(V<sup>2</sup>) |
| | Add Vertex | O(V<sup>2</sup>) |
| | Add Edge | O(1) |
| | Remove Vertex | O(V<sup>2</sup>) |
| | Remove Edge | O(1) | 
| | Check Vertex Adjacency | O(1) |
| Incidence Matrix | Store Graph | O(V * E) |
| | Add Vertex | O(V * E) |
| | Add Edge | O(V * E) |
| | Remove Vertex | O(V * E) |
| | Remove Edge | O(V * E) | 
| | Check Vertex Adjacency | O(E) |

<img src="../graph-tc.png">


As you can see, different graph representations have different strengths. Make sure to choose the appropriate representation
based off which operations you'll be performing the most!

## Practice Questions
Check out [Graph Data Structure Interview Questions and Practice Problems](https://medium.com/@codingfreak/graph-data-structure-interview-questions-and-practice-problems-22d5cd488855) 
by Medium user _Coding Freak_ for a compliation of common graph-related problems.

### References
1. [HackerEarth: Graph Representation](https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/tutorial/)
2. [Wikipedia: Adjacency list](https://en.wikipedia.org/wiki/Adjacency_matrix)
3. [Wolfram MathWorld: Incidence Matrix](http://mathworld.wolfram.com/IncidenceMatrix.html)

---
[return to all data-structures](data-structures)

[return to resources](resources)

