---
layout: post
permalink: /_posts/2018-03-20-day-17-Fun-with-DP
title:  "Day 17: Fun With DP"
date:   2018-03-20 7:15:00 -0000
categories: DP
---


# Question 1
**Memoized Fibonacci:** Calculate fibonacci more efficiently by using extra space

**Input:** 5

**Output:** 8

**Constraints:** 
*	???
*	??

```java
    static Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    public static int betterFibonacci(int n) {
        
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;   
        if (map.containsKey(n)) return map.get(n);
        else {
            int cache = betterFibonacci(n-2) + betterFibonacci(n-1);
            map.put(n, cache);
            return cache;
        }
    }
  ```

## Discussion
This is a great example of memoization!


# Question 2

**N-Step/stair Problem:** Count the number of different ways a person can reach the n-th stair, given that he or she can climb either 1 step or 2 steps at a time.

**Input:** 4 

**Output:** 5 (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)


**Constraints:** 
*	???
*	??

```java
    static Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    public static int betterFibonacci(int n) {
        
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;   
        if (map.containsKey(n)) return map.get(n);
        else {
            int cache = betterFibonacci(n-2) + betterFibonacci(n-1);
            map.put(n, cache);
            return cache;
        }
    } 
  ```

## Discussion
This is an abstraction of fibonacci puzzles.
