---
layout: post
permalink: /_posts/2018-01-22-day-3-review-and-linkedlists
title:  "Day 3: Quick Recap and LinkedLists!"
date:   2018-01-22 7:15:00 -0000
categories: arrays, linkedlists 
---

## Introduction
Want to learn more about linkedlists, [click here!](../interview/resources)

## Review 
Check out the new outlined [interview structure, tips, and tricks](../interview/structure)

## Warm-up Question - Array Review
**Find the Missing Number** - Given an unordered array of integers, with all numbers inclusive between a given lower bound and upper bound but one, find that missing number

**Input:** arr = {1, 4, 3, 2, 9, 10, 5, 8, 6}, low = 1, high = 10

**Output** 7

**Constraints:** 
*	all numbers are included in the inclusive range but one
*	all numbers are positive integers greater than 0

(fill these in)
*   array size...?
*   low, high?
*   uniqueness?

```java
    public int findMissingNum(int arr[], int low, int high) {
        int n = arr.length;
        int temp[] = new int[high+1]; //why ??? See Discussion-point 1
        for (int i = 0; i < n; i++)
            temp[arr[i]] = arr[i];
        for (int i = low; i <= high; i++) //why these conditions?
            if (temp[i] == 0) return i;
        return -1;
    }
```

## Discussion
In our array session we utilized the properties of array indexing to check visited values.
At first we did not have space or time requirements.
*   DP-1: 
*   DP-2:

## Warm-up Question V2 - Calculus tricks
**Find the Missing Number** - Given an unordered array of integers, with all numbers inclusive between a given lower bound and upper bound but one, find that missing number.

**Input:** arr = {1, 4, 3, 2, 9, 10, 5, 8, 6}, low = 1, high = 10

**Output** 7

**New Constraints:** 
*	Solve this in constant space
*	Solve this in linear time 

## Solution:
```java
    public int findMissingNum(int arr[], int low, int high) {
        int target = (high*(high+1)) / 2;
        for (Integer i : arr)
            target -= i;
        return target;
    }
```

## Discussion
This is an example of a simple question made harder, only by changing the constraints.
We used a simple series calculation: Sum[Min, Max] = (Max*(Max+1)) / 2.

*It is good to keep up to date with common and basic calculus axioms related to log calculations, series, etc.*
        

# Second Question
**Find Duplicates:** 

**Input:** 
**Output** 
**Constraints:** 
*	
*	

## Solution:
```java
    ???
```

## Discussion