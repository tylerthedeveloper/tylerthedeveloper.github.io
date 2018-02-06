---
layout: post
permalink: /_posts/2018-02-05-day-6-intro-to-trees
title:  "Day 6: Intro to Trees"
date:   2018-02-05 7:15:00 -0000
categories: trees
---

# Introduction
Want to learn more about trees, [click here!](../interview/resources)


# Warmup Question
**Node count:** Given an implementation tree comprised of nodes, return the number of nodes in the tree

**Input:** (Node) 
    1
   2 3
  4 5 6 7 

**Output** 7

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
    
    public static int nodeCount(Node head) {
        if (head == null) return 0;
        if (head.left == null && head.right == null) return 1;
        return nodeCountHelper(head);
    }

    private static int nodeCountHelper(Node head) {
        if (head == null) return 0;
        return 1 + nodeCountHelper(head.left)
                 + nodeCountHelper(head.right);
    }

    
    
    //cleanest
    public static int nodeCount(Node head) {
        if (head == null) return 0;
        if (head.left == null && head.right == null) return 1;
        return 1 + nodeCount(head.left) + nodeCount(head.right);
    }

```


## Discussion
This is a simple full traversal of a binary tree


# Warmup question V2
**Tree Sum:** Given an implementation tree comprised of nodes with data values, return the sum of the node's keys

**Input:** (Node) 
    1
   2 3
  4 5 6 7 

**Output** 28

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
    
    public static int nodeSum(Node head) {
        if (head == null) return 0;
        if (head.left == null && head.right == null) return head.data;
        return nodeSumHelper(head);
    }

    private static int nodeSumHelper(Node head) {
        if (head == null) return 0;
        return head.data + nodeSumHelper(head.left)
                 + nodeSumHelper(head.right);
    }

```

## Discussion
We followed the exact same traversal as before, with very little changes to the code


# Warmup question V3 - Binary Trees
**Tree Min/Max:** Given an implementation of a BINARY tree comprised of nodes with data values, return the value of the smallest node in the tree

**Input:** (Node) 
     4
   2   6
  1 3 5 7 

**Output** Min = 1, Max = 7

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
    
    public static int minNode(Node head) {
        if (head == null) return -1;
        if (head.left == null) return head.data;
        int min = 0;
        while (head != null) {
            min = head.data;
            head = head.left;
        }
        return min;
    }

    public static int maxNode(Node head) {
        if (head == null) return -1;
        if (head.left == null) return head.data;
        int min = 0;
        while (head != null) {
            min = head.data;
            head = head.right;
        }
        return min;
    }


    /*
        // recursive version, also works for min, max
        public static int maxNode(Node head) {
            if (head == null) return null;
            if (head.right == null) return root;
            return maxNode(head.right);
        }
    */
```

## Discussion
Here we explore the benefits of binary trees and ordering. The min and max caculations are simple traversals down the respective side for min, left or max, right.



# First Question - Binary Search
**Find special index:** Given an array of integers in increasing order, find the index of a special indexed element, in that the value at a[i] = i.

**Input:** arr = {1, 2, 2, 3, 4, 5} 

**Output** 2 because a[2] = 2

**Constraints:** 
*	???
*	??

## Solution:
```java

    
    public static int specialIndex(int arr[], int start, int end) {
        if(start >= end)
        {   
            int mid = (low + high)/2;  
            if(mid == arr[mid]) return mid;
            if(mid > arr[mid]) return binarySearch(arr, (mid + 1), high);
            else return binarySearch(arr, low, (mid -1));
        }
        return -1;
    }
```

## Discussion
This is a great implementation of a binary search algorithm, performing O(log n) time.
