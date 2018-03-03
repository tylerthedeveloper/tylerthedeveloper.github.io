---
layout: post
permalink: /_posts/2018-01-10-day-1-intro-and-arrays
title:  "Day 1: Introduction and Arrays!"
date:   2018-01-10 7:15:00 -0000
categories: arrays 
---

# Introduction

Want to learn more about arrays, [click here!](../interview/resources)

# First Question
**Two-sum:** Given a list of numbers and a target, determine whether a pair exists that sum up to the target value

**Input:** list = {1, 2, 5, 4, 8, 9, 10}, target = 12 

**Constraints:** 
*	a solution exists
*	a number cannot be used twice
*	no negative numbers


## Solution: V1 - Simple/Brute Force Solution
<!-- <details>
    <summary> Click to expand </summary>
<p> -->
```java
public boolean hasTwoSum(int arr[], int target) {
    if (arr == null || arr.length == 0) return false;
    int n = arr.length, temp;
    for (int i = 0; i < n; i++) {
        temp = arr[i];
        for (int j = i+1; j < n; j++) {
            if (temp + arr[j] == target)
                return true;
        }
    }
    return false;
}
```
<!-- </p>
</details> -->


## Discussion
This is is simple - for each element in the list, we go over the subsequent elements in the list.
This is why our runtime is O(n^2).

## Solution: V2 - Based on counting sort --> [read about it here](https://www.geeksforgeeks.org/counting-sort/)
**New constraints and rules:**
*	Has to be better than O(n^2)
*	Can use extra space
*	**Return the indices of the first elements in the solution**
*   (Have to be given max value in list to use this algorithm)

<!-- <details>
  <summary> Click to expand </summary> -->
  ```java
  public static int[] hasTwoSum(int arr[], int target) {
      if (arr == null || arr.length == 0) return null;
      int n = arr.length;
      int temp[] = new int[n*n]; //arbitrary size 
      for (int i = 0; i < n; i++) 
        temp[i] = -1;
      for (int i = 0; i < n; i++) {
        temp[arr[i]] = i; 
        int tempdiff = target - arr[i];
        if (tempdiff-arr[temp[tempdiff]] == 0) 
          return new int[]{temp[tempdiff], i};  
      }
      return null;
  }
  ```


