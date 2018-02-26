---
layout: post
permalink: /_posts/2018-02-07-day-7-more-trees
title:  "Day 7: More Trees"
date:   2018-02-07 7:15:00 -0000
categories: trees
---

# Introduction
Want to learn more about trees, [click here!](../interview/resources)

<!-- 
# Warmup Question
**Node count V2: Full Nodes:** Given an implementation tree comprised of nodes, return the total number of full nodes in a binary tree. A full node is a node which has both children. If there are no full nodes, return 0. 

**Input:** (Node) 
     1
   2  3
  4 5 6 7 

**Output** 3 (1, 2, 3)

**Constraints:** 
*	???
*	??

## Solution:
```java

    class Node {
        int data;
        Node left;
        Node right;

        Node(int data, Node left, Node right) {
            this.data = data;
            this.left = left;
            this.right = right;
        }
    }
    
    public int numberOfFullNodes(TreeNode root) {
        if (root == null) return 0;
        int cur = 0;
        if (root.left != null && root.right != null) cur++;
        return cur + numberOfFullNodes(root.left) + numberOfFullNodes(root.right);
    }

```


## Discussion
This is a simple full traversal of a binary tree, counting the nodes according to the specification above



# Warmup question V2
**Node count V3: Half Nodes:** Given an implementation tree comprised of nodes, return the total number of half nodes in a binary tree. A half node is a node which has exactly one child node. If there are no half nodes, return 0. 

**Input:** (Node) 
    1
   2 3
  4   7 

**Output** 2 (2, 3)

**Constraints:** 
*	???
*	??

## Solution:
```java

    class Node {
        int data;
        Node left;
        Node right;

        Node(int data, Node left, Node right) {
            this.data = data;
            this.left = left;
            this.right = right;
        }
    }
    
    public int numberOfHalfNodes(TreeNode root) { 
        if (root == null) return 0;
        int cur = 0;
        if (root.left == null ^ root.right == null) cur++;
        return cur + numberOfHalfNodes(root.left) + numberOfHalfNodes(root.right);
    }
```

## Discussion
This is a simple full traversal of a binary tree, counting the nodes according to the specification above, with a cool logic trick to make it faster



# First Question - Binary Trees
**Distance of a node from the root** Given an implementation of a BINARY tree comprised of nodes with data values, return the the distance of between the node and the root

**Input:** (Node) 
     4
   2   6
  1 3 5 7  --- > find 7

**Output** 2 (4->6->7)

**Constraints:** 
*	???
*	??

## Solution:
```java

    class Node {
        int data;
        Node left;
        Node right;

        Node(int data, Node left, Node right) {
            this.data = data;
            this.left = left;
            this.right = right;
        }
    }
    
    public int pathLengthFromRoot(TreeNode root, int n1) {
        if (root == null) return 0;
        if (root.data == n1) return 1;
        int l = pathLengthFromRoot(root.left, n1);
        if (l > 0)  return 1 + pathLengthFromRoot(root.left, n1);
        int r = pathLengthFromRoot(root.right, n1);
        if (r > 0) return 1 + pathLengthFromRoot(root.right, n1);
        return 0;
    }
```

## Discussion
Here we explore the benefits of binary trees and ordering. We are able to crawl down the tree in towards the find the final goal.



# Second Question
**Level Order:** Given an implementation of a BINARY tree comprised of nodes with data values, print out the tree in level order


**Input:** (Node) 
     4
   2   6
  1 3 5 7  

**Output** 
4 2 6 1 3 5 7

**Constraints:** 
*	???
*	???

## Solution:
```java
    class Node {
        int data;
        Node next;

        Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }
    }

    public void levelOrderTraversalInLine() {
		if (classTree == null) return;
		Queue<Node> q = new LinkedList<>();
		q.add(classTree);
		while ( !q.isEmpty() ){
			Node cur = q.remove();
			System.out.print(cur.data + " ");
			if (cur.l != null) q.add(cur.l);
			if (cur.r != null) q.add(cur.r);
		}
	}

```

## Discussion
THis is a simple BFS (breadth-first-search) traversal


# Second Question - V2
**Level Order:** Given an implementation of a BINARY tree comprised of nodes with data values,print out the tree in level order, line by line


**Input:** (Node) 
     4
   2   6
  1 3 5 7  

**Output** 
4 
2 6 
1 3 5 7

**Constraints:** 
*	???
*	???

## Solution:
```java
    class Node {
        int data;
        Node next;

        Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }
    }

    public void levelOrderTraversalLineByLine(Node node) {
		if (node == null) return;
		Queue<Node> q = new LinkedList<>();
		Queue<Node> level = new LinkedList<>();
		q.add(node);
		while ( !q.isEmpty() ||  !level.isEmpty() ) {
			while (!q.isEmpty() ) {
				Node cur = q.remove();
				level.add(cur);
			}
			System.out.println(" ");
			while (!level.isEmpty() ) {
				Node cur = level.remove();
				System.out.print(cur.data + " ");
				if (cur.left != null) q.add(cur.lleft);
				if (cur.right != null) q.add(cur.right);
			}
			System.out.println(" ");
		}
	} 

```

## Discussion
Here we needed to use 2n extra space

-->