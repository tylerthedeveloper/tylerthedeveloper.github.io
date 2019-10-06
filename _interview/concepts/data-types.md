---
---
[return to concepts](materials)

# Data Types

## Common Types
Below are some primitive data types<sup>1</sup> that are included in most, if not all, (high-level) languages:

| Type | Description |
| :---: | :---: |
| Integer | Integer number |
| Float | Floating-point number |
| Char | Character |
| Pointer | Memory address referring to another object |

The following types are more sophisticated, but are available in many popular languages:

| Type | Description |
| :---: | :---: |
| String | Array of characters |
| List | List of values, can be resized |

## (Java) Data Types
In C343, you'll be using Java to complete homework. Listed below, courtesy of GeeksforGeeks<sup>2</sup>, are the the primitive data types in Java:

| Type | Size | Description |
| :---: | :---: | :---: |
| byte | 1 byte | Stores whole numbers from -128 to 127 |
| short | 2 bytes | Stores whole numbers from -32,768 to 32,767 |
| int | 4 bytes | Stores whole numbers from -2,147,483,648 to 2,147,483,647 |
| long | 8 bytes | Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| float | 4 bytes | Stores fractional numbers from 3.4e−038 to 3.4e+038. Sufficient for storing 6 to 7 decimal digits |
| double | 8 bytes | Stores fractional numbers from 1.7e−308 to 1.7e+038. Sufficient for storing 15 decimal digits |
| boolean | 1 bit | Stores __TRUE__/__FALSE__ values as a 1 or 0 respectively |
| char | 2 bytes | Stores a single character/letter |

As you can see, there are 6 types dedicated to integer numbers differing only by their size in memory and their range.
Choosing the right data type can reduce the amount of memory the program needs. If you're unsure what to use, __int__ and
__double__ are good choices for those who want to use integers and require some degree of precision respectively.

### References
1. [Wikipedia: Primitive Data Type](https://en.wikipedia.org/wiki/Primitive_data_type)
2. [GeeksforGeeks: Java Data Types](https://www.w3schools.com/java/java_data_types.asp)

---
[return to concepts](materials)
