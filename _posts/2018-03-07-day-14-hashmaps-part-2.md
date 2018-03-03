---
layout: post
permalink: /_posts/2018-03-07-day-14-hashmaps-part-2
title:  "Day 14: Hashmaps Part 2"
date:   2018-03-03 7:15:00 -0000
categories: hashmaps
---

# Introduction
Want to learn more about hashmaps, [click here!](../interview/resources)


# Warmup Question
**Fibonacci:** Return the fibonacci value using the least amount of stack space 

**Input:** 5

**Output:** 8

**Constraints:** 


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


# Question 1

**Input:** list = {8, 8, 1, 2, 2, 5, 4, 8, 9, 10, 3}

**Output:** 1, 2, 3, 4, 5, 8, 9, 10

**Constraints:** 


```java
      public static String duplicate(int[] numbers){

          // very bad -> O(n^2)!!!
          Collections.sort(numbers);
          ///

          ArrayList<Integer> lis = new ArrayList<>();
          boolean dup = false;
          for (int i = 0; i < numbers.length; i++) {
              for (int j = i+1; j < numbers.length; j++) {
                  if (numbers[i] == numbers[j])
                      dup = true;
              if (!dup)
                  lis.add(numbers[i]);
              dup = false;
          }

          for (Integer i : lis) 
              System.out.print(i);
      }
  ```

## Discussion


# Question 1 - V2

**Input:** list = {8, 8, 1, 2, 2, 5, 4, 8, 9, 10, 3}

**Output:** 1, 2, 3, 4, 5, 8, 9, 10

**Constraints:** 


```java
      public static String duplicate(int[] numbers){

          Map<Integer, Integer> map = new HashMap<>();
          for (int i = 0; i < numbers.length; i++) {
              Integer x = map.get(numbers[i]);
              if (x == null) map.put(x, x);
          }

          ArrayList<Integer> lis = new ArrayList<>();
          for (Integer i : map.values()) 
              lis.add(map.get(i));
          
          // very bad -> O(n^2)!!!
          Collections.sort(lis);
          ///

          for (Integer i : lis) 
              System.out.print(i);
              
      }
  ```

## Discussion


# Question 1 - V3

**Array Duplicates:** Given an array with duplicates, print the array sorted without duplictates, but now do it in linear time.

**Input:** list = {8, 8, 1, 2, 2, 5, 4, 8, 9, 10, 3}

**Output:** 1, 2, 3, 4, 5, 8, 9, 10

**Constraints:** 


```java
      public static void duplicate(int[] numbers){
          ArrayList<Integer> lis = new ArrayList<>();
          Map<Integer, Integer> map = new HashMap<>();
          Map<Integer, Integer> treeMap = new TreeMap<>();
          for (int i = 0; i < numbers.length; i++) {
              int x = numbers[i];
              Integer m = map.get(x);
              if (m == null) map.put(x, x);
              else treeMap.put(x, x);
          }
          for (Integer i : treeMap.values()) 
              System.out.print(i);
      }
  ```

## Discussion


