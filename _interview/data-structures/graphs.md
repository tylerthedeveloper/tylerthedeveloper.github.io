---
---
[return to all data-structures](data-structures)

[return to resources](resources)

# Graph
Graphs come in many shapes and structures which share the following properties:

* A graph is made up of two sets called Vertices and Edges.   

* The Verticies are typed and the set may be finite or infinite.

* Not all vertices are necessarily connected by an edge; these are called islands

* Edges may or may not be completely connected to every vertex

* Each element of the Edge set is a pair consisting of two elements from the Vertices set

* Edges can have weights and have a direction or no direction at all


## *Graph Types*

*   Undirected Graphs: E(1,2) == E(2,1)
    > When traversing you do NOT have to keep direction in mind

*   Directed Graphs: E(1,2) != E(2,1)
    > When traversing you have to keep direction in mind

*   Vertex Labeled Graphs
    > There is a notion of ordering

*   Cyclic Graphs
    > There is at LEAST one CYCLE in the graph (i.e. return to where you start)

*   Edge-labeled Graphs
    > There is a notion of labeling edges that has meaning

*   Weighted-Graphs
    > There is a notion of weight on edges 

*   Directed-Cyclic Graphs
    > There is at LEAST one CYCLE in the graph AND there is direction

*   Disconnected-Graphs
    > There are allowed to be islands (vertices that are not connected by an edge)


## *When to use graphs*

*   When establishing many-to-many relationships
*   When there is a notion of directionality or traversal
*   When there is signficance or different values on relationships
*   When there is a notion of neighbors or ordering
*   When there relationships resemble "Family Trees"
*   When dealing with maps 


## *Time complexity*

<img src="../graph-tc.png">


## *Practice questions*
