# my-machine-learning-journey
Here I document my journey of Machine Learning!

# Roadmap
To grasp the concepts of machine learning I would choose the path of : 
+ Python Basics
+ `numpy`
+ `pandas`
+ `matplotlib`
+ `sklearn`
+ `scrapy`
+ `bs4`
+ `selenium`

## Python Basics
These is a small python documentation for learning python from scratch!

### Printing
+ This is how you print `Hello world!` in Python : 
#### Code
``` py
print("Hello world!")
```
#### Output
```
Hello world!
```
+ This is how you add something at the end of a string in Python :
#### Code
``` py
print("Hello World", end = "!!")
```
#### Output
```
Hello World!!
```

### Variables
+ This is how you declare variables in Python :
#### Code
``` py
a = 5
b = 10
```

+ This is how you write multiple variables in a single line using semi-colon(;) :
``` py
a = 5; b = 10
```

### Comments
Comments are lines of statements that are ignored by the python interpreter while execution of the program.
There are two ways of writting comments : 
+ `Single line comments` : Using hastags' # ' in the beginning of the line makes a single line comment.
``` py
# This is a single line comment
a = 5 # assigning 5 to the variable a
```

+ `Multi-line comments` : Using triple single quotes or triple double quotes before the starting and at the ending of the statement.
``` py
''' This is a multi-line comment
You can even use Triple double quotes """
for making multi-line comments
'''
```

### Data Types
+ `Integer(int)` : Represents whole numbers without any fractional part, such as 5, -10, 1000, etc.
+ `Float(float)` : Represents real numbers with both integer and fractional parts, such as 3.14, -0.001, 2.0, etc.
+ `String(str)` : Represents sequences of characters enclosed within single quotes (''), double quotes ("") or triple quotes (''''' or """).
+ `Boolean(bool)` : Represents the truth values `True` and `False`, which are used for logical operations.
+ `List` : Represents an ordered collection of items. Lists are mutable, which means you can change their elements after creation.
+ `Tuple` : Similar to lists, but tuples are immutable, meaning you cannot change the elements after creation.
+ `Dictionary(dict)` :  Represents a collection of key-value pairs enclosed within curly braces {}. Keys within a dictionary must be unique.
+ `Set` : Represents an unordered collection of unique items. Sets do not allow duplicate elements.
+ `NoneType(None)` : Represents the absence of a value or a null value.

These are the primary built-in data types in Python. Additionally, Python allows for defining custom data types using classes and objects.

### Operators
There are a few types of operators in Python :
#### Assignment Operator : 
Assignment operator is used to assign values to a variable.
``` py
a = 5
```

#### Arithmatic Operator : 
These are the operators that perform mathematical calculations in python : 
| Operation   | Description                         | Operator | Example            |
|-------------|-------------------------------------|----------|--------------------|
| `sum`       | Add two numbers                     | `+`      | `sum = 5 + 4`      |
| `difference`| Subtract two numbers                | `-`      | `difference = 10 - 4` |
| `product`   | Multiply two numbers                | `*`      | `product = 3 * 4`  |
| `quotient`  | Divide two numbers (get quotient)   | `/`      | `quotient = 10 / 2`|
| `remainder` | Divide two numbers (get remainder)  | `%`      | `remainder = 17 % 3`|
| `exponent`  | Get a number raised to the power of its exponent | `**` | `raised_to_power = 2 ** 5`|


#### Relational Operator : 
This is used to compare two data values : 
| Name              | Sign  | Usage                 | Example             |
|-------------------|-------|-----------------------|---------------------|
| Equal to          | ==    | Equality comparison   | x == y              |
| Not equal to      | !=    | Inequality comparison | x != y              |
| Greater than      | >     | Greater than comparison | x > y              |
| Less than         | <     | Less than comparison  | x < y               |
| Greater than or equal to | >= | Greater than or equal comparison | x >= y     |
| Less than or equal to    | <= | Less than or equal comparison | x <= y          |

#### Logical Operator : 
| Operation    | Description                                | Symbol | Example                  |
|--------------|--------------------------------------------|--------|--------------------------|
| `and`        | Logical AND operator                       | `and`  | `result = True and False`|
| `or`         | Logical OR operator                        | `or`   | `result = True or False` |
| `not`        | Logical NOT operator                       | `not`  | `result = not True`      |

#### Bitwise Operator
| Operation   | Description                           | Symbol | Example                    | Output    |
|-------------|---------------------------------------|--------|----------------------------|-----------|
| `AND`       | Bitwise AND                           | `&`    | `result = 5 & 3`           | `result`  |
| `OR`        | Bitwise OR                            | `|`    | `result = 5 \| 3`          | `result`  |
| `XOR`       | Bitwise XOR                           | `^`    | `result = 5 ^ 3`           | `result`  |
| `NOT`       | Bitwise NOT (One's complement)        | `~`    | `result = ~5`              | `result`  |
| `Left Shift`| Shift left by pushing zeros in         | `<<`   | `result = 5 << 2`          | `result`  |
| `Right Shift`| Shift right by pushing copies in     | `>>`   | `result = 5 >> 2`          | `result`  |

#### Identitiy Operator
| Operator  | Description                          | Symbol | Example                    |
|-----------|--------------------------------------|--------|----------------------------|
| `is`      | Evaluates if both sides are identical objects | `is`   | `result = x is y`          |
| `is not`  | Evaluates if both sides are not identical objects | `is not` | `result = x is not y`   |

### F-strings























