---
layout: post
permalink: /_posts/2018-03-05-day-13-hashmaps
title:  "Day 13: Hashmaps"
date:   2018-03-03 7:15:00 -0000
categories: hashmaps
---

# Introduction
Want to learn more about hashmaps, [click here!](../interview/resources)


# Warmup Question
**Char Count:** Given a string, print out the number of occurences of each letter in the string

**Input:** list = aaabbc

**Output:** 
a, 3
b, 2
c, 1

**Constraints:** 


```java
    public static void charCount(String str) {
      if (str == null || str.length() == 0) 
        System.out.print("");
      int n = str.length();
      HashMap<Character, Integer> map = new HashMap<>();
      for (int i = 0; i < n; i++) {
            if (map.get(str.charAt(i)) == null)
                map.put(str.charAt(i), 1);        
            else
                map.put(str.charAt(i), map.get(str.charAt(i) + 1);
      }

      for (int i = 0; i < n; i++)
        System.out.print(str.charAt(i) + ": " + map.get(str.charAt(i)));
  }
  ```

## Discussion
This is a simple linear traverseal using O(n) space and O(n) time.


# Question 1
**Two-sum:** Given a list of numbers and a target, determine whether a pair exists that sum up to the target value, return the indices of the elements in the pair

**Input:** list = {1, 2, 5, 4, 8, 9, 10}, target = 12 

**Output:** 3, 4  --> (4, 8)


**Constraints:** 
*	a solution exists
*	a number cannot be used twice
*	no negative numbers


```java
    public static int[] hasTwoSum(int arr[], int target) {
      if (arr == null || arr.length == 0) return null;
      int n = arr.length;
      HashMap<Integer, Integer> map = new HashMap<>();
      for (int i = 0; i < n; i++) {
        map.put(arr[i], i);
        int tempdiff = target - arr[i];
        if (map.get(tempdiff) != null)
          return new int[]{map.get(tempdiff), i};  
      }
      return null;
  }
  ```

## Discussion
This is a simple linear traverseal using O(n) space and O(n) time.



# Question 1 - V2
**three-sum:** Given a list of numbers and a target, determine whether a trio exists that sum up to the target value, and return that trio

**Input:** list = {1, 2, 3, 5, 4, 8, 9, 10}, target = 12 

**Output:** 3, 4, 5

**Constraints:** 
*	a solution exists
*	a number cannot be used twice
*	no negative numbers

```java
    public static int[] threeSum(int arr[], int target) {
      if (arr == null || arr.length == 0) return null;
      int n = arr.length;
      HashMap<Integer, Integer> map = new HashMap<>();
      HashMap<Integer, Integer> map2 = new HashMap<>();
      for (int i = 0; i < n; i++) {
            map.put(arr[i], i);
            for (int j = i+1; j < n; j++) {
                int tempdiff = target - arr[j] - arr[i];
                if (map.get(tempdiff) != null)
                return new int[]{map.get(tempdiff), arr[j], arr[i]};  
      }
      return null;
  }
  ```

## Discussion