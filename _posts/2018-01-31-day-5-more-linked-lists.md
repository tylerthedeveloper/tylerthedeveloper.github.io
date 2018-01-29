---
layout: post
permalink: /_posts/2018-01-31-day-5-more-linked-lists
title:  "Day 5: More Linked-lists"
date:   2018-01-29 7:15:00 -0000
categories: linkedlists
---

# Introduction
Want to learn more about linked-lists, [click here!](../interview/resources)

<!--

# Warmup Question - Singly Linked List
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


# Warmup Question V2 - Doubly Linked List
**Delete tail:** Given a doubly linked list that is also circular, delete the tail and return the head node that is pointed to by the new tail.

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

    public Node deleteDoublyLinkedTail(Node head) {
        if (head == null || head.prev == head) return null;
        Node tail = head.prev;
        if (tail.prev == head) {
            head.prev = head;
            return head;
        }
        tail = tail.prev; // move back one to delete tail
        tail.next = head;
        head.prev = tail;
        /*
            omitting null checking
            all the above is represented in a one liner below
            head.prev.prev.next = head;
        */
        return head;
    }

```


## Discussion
With a doubly-linked-list, we can do this in constant time!


# First Question
**Reverse Singly Linked List:** Given the head pointer of a singly linked list, return a pointer to the reversed list

**Input:** (Node) 1 -> 2 -> 3 -> 4 

**Output** 1 < - 2 <- 3 <- 4

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

    public Node reverseList(Node head) {
        if ( head == null) return null;
        if ( head.next == null) return head;
        ListNode prev = null;
        while ( head != null) {
            ListNode front = head.next;
            head.next = prev;
            prev = head;
            head = front;
        }
        return prev;
    }


```


## Discussion
This is a classic question that often gets asked. 
It's good to know because pointers can get very confusing! 



# Second Question - linked-list traversal V1
**Nth Node From End:** Given a singly-linked list, return the Nth node from the end of the list. 

**Input:** int end

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

    public Node nthNodeFromEnd(Node head, int end) {
        if (head == null) return null;
        HashMap<Node, Integer> listMap = new HashMap<>();
        int counter = 0;
        while (head != null) {
            listMap.put(head, counter++);
            head = head.next;
        }
        return listMap.get(counter - n);
    }
    
```

## Discussion
Here we take advantage of a hashmap to keep track of nodes and their respective index.
This allows us to very quickly lookup the node at a given index.



# Second Question - linked-list traversal V2
**Nth Node From End:** Given a singly-linked list, return the Nth node from the end of the list. 

**Input:** int end

**Output** Node node

**NEW Constraints:** 
*	do so with constant space
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

    public Node nthNodeFromEnd(Node head, int end) {
        if (head == null || n < 0) return null; //empty or negative index
        int listLen = 0; //need to figure this out 
        Node cur = head;
        while (cur != null) {
            listLen++;
            cur = cur.next;
        }
        if (end > listLen) return null; //out of bounds
        Node ret = head; // reset a node pointer
        int idx = 0; //follow an index
        while (idx != listLen - end) {
            ret = ret.next;
            idx++;
        }
        return ret;
    }
    
```

## Discussion
Here we have to do multiple passes, becasue we cannot keep track of information along the way without extra space. 

-->