---
layout: post
permalink: /_posts/2018-03-01-day-10-last-of-trees
title:  "Day 10: Last of Trees"
date:   2018-03-01 7:15:00 -0000
categories: trees
---

# Introduction
Want to learn more about trees, [click here!](../interview/resources)



<!--


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








<!--
# Warmup Question (follow up from last lesson)

**Level Order:** Given an implementation of a BINARY tree comprised of nodes with data values, print out the tree in level order, line by line

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
Here we needed to use 2n extra space, is there anything else to note??


# First Question - 
**Mirror Tree** Convert a binary tree into its mirror image and return the root node of the result.

**Input:** (Node) 
     4
   2   6
  1 3 5 7  

**Output** 

4

6   2

7 5 3 1   

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

    public Node mirror(Node root) {
        if (root == null) return null;
        mirrorHelper(root);
        return root;
    }

    public void mirrorHelper(Node root) {
        if (root == null) return;
        Node left = root.left;
        root.left = root.right;
        root.right = left;
        mirrorHelper(root.right);
        mirrorHelper(root.left);
        
    }    

```

## Discussion



# Second Question
**Tree Longest Sequence:** Given a tree, return the length of the longest increasing sequence such that the child data value is +1 of the parent. The tree is a binary tree, but not necessarily a binary search tree.


**Input:** (Node) 
     4
   2   5
  1 3   6  

**Output** 3: (4 -> 5 -> 6)

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

    public static int findLenLongestSequence(Node node) {
        if (node == null) return 0;
        return findLenLongestSequence(node, 1, 1, node.data);
    }


    private static int findLenLongestSequence(Node node, int curLen, int curMax, int preVal) {
        if (node == null) return 0;
        if (node.data == preVal) {
            curMax++;
            curLen++;
        }
        else curMax = 1;
        if (curMax > curLen)
            curLen = curMax;
        findLenLongestSequence(node.left, curLen, curMax, node.data);
        findLenLongestSequence(node.right, curLen, curMax, node.data);
        return curLen;
    }

```

## Discussion

-->