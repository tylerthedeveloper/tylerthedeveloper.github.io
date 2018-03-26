---
layout: post
permalink: /_posts/2018-03-12-day-16-Stacks-Continued
title:  "Day 16: Stacks Continued"
date:   2018-03-12 7:15:00 -0000
categories: stacks
---

# Introduction
Want to learn more about stacks, [click here!](../interview/resources)


# Question 1
**Balancing:** use a stack to check for balanced parentheses in an expression

**Input:** ((({{[]}})))


**Output:** yes

**Constraints:** 
*	???
*	??

```java

    boolean isPair(char c1, char c2)
    {
        switch(c1) {        
            case '(': 
                return (c2 == ')');
            case '{': 
                return (c2 == '}');
            case '[': 
                return (c2 == ']');
            default:
                return false;
        }
        return false;
    }

    public boolean isBalanced(String exp) {
          Stack<Character> stack = new Stack<>();
          char arr[] = exp.toCharArray();
          int n = arr.length;
          for (int i = 0; i < n; i++) {
            if (arr[i] == '{' || arr[i] == '(' || arr[i] == '[')
                stack.push(arr[i]);
            else if (arr[i] == '}' || arr[i] == ')' || arr[i] == ']') 
                if (stack.isEmpty() || (!isPair(stack.pop(), arr[i])))
                    return false;
          }
          return stack.isEmpty();
      }

  ```

## Discussion



# Question 2

**Prefix notation:** evaluate the expression

**Input:** +9*26

**Output:** 21 
(6 * 2) = 12
12 + 9 = 21

**Constraints:** 
*	???
*	??

```java

      // a number or non-operator 
        boolean isOperand(char c)
        {
            return (c >= 48 && c <= 57)
        }  

        //why do we start at end??
        double evalPrfixNotation(String mathExprsn)
        {
            Stack<Double> stack = new Stack<Double>();

            int n = mathExprsn.length();
            for (int j = n - 1; j >= 0; j--) {
          
                // ASCII conversion
                // a number, for all intents and purposes
                if (isOperand(mathExprsn.charAt(j))) 
                    stack.push((double)(mathExprsn.charAt(j) - 48)); 
                  
                else {
          
                     double o1 = stack.pop(),o2 = stack.pop();
         
                    switch (mathExprsn.charAt(j)) {
                    case '+':
                        stack.push(o1 + o2);
                        break;
                    case '-':
                        stack.push(o1 - o2);
                        break;
                    case '*':
                        stack.push(o1 * o2);
                        break;
                    case '/':
                        stack.push(o1 / o2);
                        break;
                    }
                }
            }
          
            return stack.peek();
        }

  ```

## Discussion

