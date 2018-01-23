---
layout: post
permalink: /_posts/2018-01-17-day-2-fun-with-heaps
title:  "Day 2: Fun With Heaps!"
date:   2018-01-17 7:15:00 -0000
categories: heaps 
---

# Introduction
Want to learn more about heaps, [click here!](../interview/resources)

# Warm-up Question
**Merge Substrings** - Given two strings, return a string which is the result of interleaving the characters from both strings

**Input:** "data", "structure"

**Output** "dsattraucture"

**Constraints:** 
*	a string can be the empty string
*	the first string can be longer than the second
*	the second string can be longer than the first
*   the strings can be the same size

## Solution:

```java
    public String mergeStrings(String a, String b) {
        int n1 = a.length(), n2 = b.length();
        StringBuffer ss = new StringBuffer();
        int min = Math.min(n1, n2);
        for (int i = 0; i < min; i++) {
            ss.append(a.charAt(i));
            ss.append(b.charAt(i));
        }
        if (n1 == n2) return ss.toString();
        if (min == n1) ss.append(b.substring(min));
        else ss.append(a.substring(min));
        return ss.toString();
    }
```

## Discussion
This is is simple, we identify the longer of the two strings, and traverse until 
we reach the length of the first. We then just dump the rest of the longer string
onto our growing string.
We also use a StringBuilder here, which was designed specifically for strings that are to be mutated.


# First Question
**In-order Traversal:** Given an array representing an in-order binary tree, using heap properties and calculations, print out an in-order walk of the tree.

**Input:** arr = {5, 3, 9, 2, 4, 7, 11 };

**Output** "2, 3, 4, 5, 7, 9, 11"

**Constraints:** 
*	the array is not empty
*	the array represents a binary tree

## Solution:
```java
    public static void inOrderTraversal(int arr[]) {
        inOrderTraversal(arr, 0, arr.length - 1);
    }

    public static void inOrderTraversal(int arr[], int curIndex, int end) {
        if ( curIndex > end) return; 
        inOrderTraversal(arr, curIndex*2 + 1, end);
        System.out.println(arr[curIndex]);
        inOrderTraversal(arr, curIndex*2 + 2, end);
    }
```


## Discussion
This is a recursive solution to a very common problem. It works as follows:

    *   Go all the way left until you cannot (are out of bounds based on heap left-sibling calculation)
        =>   This yields the smallest element in the current subtree

    *   Print that element

    *   Come back up to your parent
        =>   This yields the next element in the current sequence

    *   Go right, then all the way left until you cannot (based on same calculation from above)
        =>   This yields the next element in the current sequence after the root

Along the way, the recursive stack is built, and on the way back up, the values are printed.

        


# Second Question
**Level-order Traversal:** Given an array representing a binary tree, using heap and binary tree properties, print out a level order walk of the tree, with each level on a new line.

**Input:** arr = {5, 3, 9, 2, 4, 7, 11 };

**Output** 
   "5"
  "3 9"
"2 4 7 11"

**Constraints:** 
*	the array is not empty
*	the array represents a tree

## Solution:
```java
    public static void levelOrderTraversal(int arr[]) {
        int n = arr.length;
        int curCount = 0, curLevel = 0;
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
            curCount++;
            if (curCount == (int)(Math.pow(2,curLevel))) {
                System.out.print("\n");                
                curLevel++;
                curCount = 0;
            }   
        }
    }
```


## Discussion
This question is seemingly simple, requiring a simple traversal of the array, but keeping track of values along the way.

With a binary tree, we can calulate how many keys should be on each level, which is 2^(level) elements.

Knowing this, we can track how many elements we have seen so far and when to start a new line.