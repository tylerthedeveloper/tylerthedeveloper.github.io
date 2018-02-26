---
layout: post
permalink: /_posts/2018-01-29-day-4-fun-with-linked-lists
title:  "Day 4: Fun With Linked-lists"
date:   2018-01-29 7:15:00 -0000
categories: linkedlists
---

# Introduction
Want to learn more about linked-lists, [click here!](../interview/resources)


# Warm-up Question
**List Length, even or odd:** Given a singly-linked list (not built-in), check whether its length is even or odd in a single pass. 

**Input:** Node node

**Output** an integer

**Constraints:** 
*   ??
*   ??

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

    public Boolean isListEven(Node head) {
        if (head == null) return true;
        int i = 1;
        while (head.next != null) {
            i++;
            head = head.next;
        }
        return (i%2 == 0);
    }

```

## Discussion
Obviously we have built in data type of linked list with the size property for this reason, but this is a good example of dealing with simple custom structures you may face.


# First Question
**List Palindrome:** Given a singly-linked list, determine if the list represents a palindrome.

**Input:** Node node

**Output** boolean

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

    public boolean isListPalindrome(Node head) {
        if (head == null || head.next == null) return true;
        StringBuilder sb = new StringBuilder();
        Node cur = head;
        while (cur != null) {
            sb.add(cur.data);
            cur = cur.next;
        }
        int n = sb.size();
        for (int i = 0; i < n/2; i++) 
            if (sb.charAt(i) != sb.charAt(n-i-1)) 
                return false;
        return true;
        
    }

```

## Discussion

*This is a typical palindrome question, with no constraints of extra space, we had no problem, but what if we couldn't use extra space???*

# Second Question
**Remove Duplicates:** Given a singly-linked list, return the head of the list after removing duplicates.

**Input:** Node node

**Output** Node node

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

    public Node removeDups(Node head) {
        if (node == null) return null;
        Set<Integer> set = new HashSet<>();
        Node cur = head, dummy = cur;
        set.add(cur.data);
        while (cur.next != null) {
            if (!set.add(cur.next.data)) {
                cur.next = cur.next.next;
                if (cur == null) break;
            } else {
                cur = cur.next;
            }
        }
        return dummy;
    }

```

## Discussion
Here we are taking advantage of the Set data structure and are accomplishing this goal in a single pass!



# Third Question - Singly Linked List
**Delete tail:** Given a singly linked list that is also circular, delete the tail and return the head node that is pointed to by the new tail.

**Input:** (Node) 1 -> 2 -> 3 -> 4 -> 1

**Output** (Node) 1 -> 2 -> 3 -> 1

**Constraints:** 
*	???
*	??

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

    public Node deleteTail(Node head) {
        if (head == null) return null;
        Node prev = head;
        Node cur = head.next;
        while (cur.next != head) {
            prev = prev.next;    
            cur = prev.next;
        }
        prev.next = prev.next.next;
        cur.next = null;
        return prev.next;
    }

```


## Discussion
This is an improvement on singly linked lists giving us the option to use circularity.
However, keep in mind this is not doubly-linked, therefore we don't have the full benefits yet.
