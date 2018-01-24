---
layout: post
permalink: /_posts/2018-01-29-day-4-fun-with-linked-lists
title:  "Day 4: Fun With Linked-lists"
date:   2018-01-29 7:15:00 -0000
categories: linkedlists
---

# Introduction
Want to learn more about linkedlists, [click here!](../interview/resources)

# Review 
Check out the new outlined [interview structure, tips, and tricks](../interview/structure)

# Warm-up Question(s) - Array Review
## Arrays and Duplicates - V1 

**Find Number of Duplicates:** Return the number of elements that have a duplicate in an array of integers.

**Constraints:** 
*	There are no more than 2 instances of an element
*	Not every element has a duplicate

**Input:** arr = {1, 4, 3, 2, 2, 4, 1}

**Output:** 3 because [1, 2, 4] all have duplicates

## First Solution:
```java
    public int findNumOfDups(int arr[]) {
        int dups = 0, temp;
        for (int i = 0; i < n; i++) {
            temp = arr[i];
            for (int j = i+1; j < n; j++) {
                if (temp == arr[j]) dups++;
                break;
            }
        }
        return dups;
    }
```

## DISCUSSION:
This is a very naive solution running in O(n^2) time, but does the job. Let's improve it below.

## Arrays, Sets, and Duplicates - V2
Now return the total number of duplicate elements, i.e. only count distinct elements

**New Constraints:** 
*   There can be more than more than 2 elements with the same value (not just pairs)

**Input:** arr = {1, 4, 3, 2, 2, 2, 4, 1, 5, 5, 5, 5}

**Output:** 7 because {1, 4, 3, 2, 2, 2, 4, 1, 5, 5, 5, 5}  --> {1, 4, 3, 2, 5} and 12 - 5 = 7

## Second Solution:
```java
    import java.util.HashSet;
    import java.util.Set;
    public int findNumOfDups(int arr[]) {
        int n = arr.length;
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i<n; i++) 
            set.add(arr[i]);	
        return (n - set.size());
    }
```

## DISCUSSION:
This is much cleaner solution and solves a harder question. 
It is O(N) space and O(N) time, which is an improvement from the last question.