---
layout: post
permalink: /_posts/2018-01-22-day-3-recap-and-arrays-and-intro-to-sets
title:  "Day 3: Recap, Arrays and Intro to Sets"
date:   2018-01-22 7:15:00 -0000
categories: arrays, sets
---

# Introduction
Want to learn more about arrays, [click here!](../interview/resources)

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

# Arrays, Sets, and Duplicates - V2
Now return the total number of duplicate elements, i.e. only count distinct elements

**New Constraints:** 
*   There can be more than more than 2 elements with the same value (not just pairs)

**Input:** arr = {1, 4, 3, 2, 2, 2, 4, 1, 5, 5, 5, 5}

**Output:** 7 because {1, 4, 3, 2, 2, 2, 4, 1, 5, 5, 5, 5}  -> {1, 4, 3, 2, 5} and 12 - 5 = 7

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


## Arrays, Sets, and Duplicates - V2.1
Given an array of integers, return a new array of size=(n-d) where n is the original array size and d is the number of the duplicates, implying that there are n-d duplicates. Let's use what we just learned.

**Input:** arr = {1, 4, 3, 2, 2, 2, 4, 1, 5, 5, 5, 5}

**Output** newArr = {1, 2, 3, 4, 5}

## Solution:
```java
    import java.util.HashSet;
    import java.util.Set;
    public int[] findUniqueSet(int arr[]) {
        int n = arr.length;
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i<n; i++) 
            set.add(arr[i]);
        return set.toArray();
    }
```

## Discussion
Based on what we learned in the previos solution, we recognize the power of sets.

# Second Question - V1
**Find the Missing Number** - Given an unordered array of integers, with all numbers inclusive between a given lower bound and upper bound but one, find that missing number

**Input:** arr = {1, 4, 3, 2, 9, 10, 5, 8, 6}, low = 1, high = 10

**Output** 7

**Constraints:** 
*	all numbers are included in the inclusive range but one
*	all numbers are positive integers greater than 0

(These are good edge case questions)
*   is low < high? 
*   can low == high? 
*   Uniqueness: are there duplicates?

## Solution:
```java
    public int findMissingNum(int arr[], int low, int high) {
        if (arr == null) return -1; 
        int n = arr.length;
        int temp[] = new int[high+1]; //why ??? See Discussion-point 1
        for (int i = 0; i < n; i++)
            temp[arr[i]] = arr[i];
        for (int i = low+1; i < high; i++) //why these conditions? // low + 1 and high + 1
            if (temp[i] == 0) return i;
        return -1;
    }
```

## Discussion
In our array session we utilized the properties of array indexing to check visited values.
At first we did not have space or time requirements.
*   DP-1: Arrays are length n starting at 0, we need to include our highest number which is at high+1
*   DP-2: We don't need to worry about indices in our array less than low, so we'll start there

### Followup Thoughts:
*This could be made more difficult if negatives are included, what changes would we have to make?*

# Second Question V2 - Calculus tricks
**Find the Missing Number *(same as before)*:**  Given an unordered array of integers, with all numbers inclusive between a given lower bound and upper bound but one, find that missing number.

**Input *(same as before)*:** arr = {1, 4, 3, 2, 9, 10, 5, 8, 6}, low = 1, high = 10

**Output *(same as before)*** 7

**New Constraints:** 
*	Solve this in constant space
*	Solve this in linear time 

## Solution:
```java
    public int findMissingNum(int arr[], int low, int high) {
        int target = (high*(high+1)) / 2;
        for (Integer i : arr)
            target -= i;
        if (low != 1) target = target - (low*(low+1))/2;
        return target;
    }
```

## Discussion
This is an example of a simple question made harder, only by changing the constraints.
We used a simple series calculation: Sum[Min, Max] = (Max*(Max+1)) / 2.

*It is good to keep up to date with common and basic calculus axioms related to log calculations, series, etc.*







