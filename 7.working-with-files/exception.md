## Syntax Error vs Exception

syntax error
key error

tracking down errors


## The format of a try/except Block

```python
try:
    # code that might cause an exception
except:
    # raise an error message
finally:
    # always executed
# continue code as usual
```

## Flow of Control - Catching an Exception in Our Program

> `finally` - will be executed no matter if `try` block raise an error or not

***use finally block to close/clean resources***

## Where Do Exceptions Come From ?

> `raise` keyword -

Exception Class 

```python
    a = 10
    b = 0
    if(b == 0):
        raise ZeroDivisionError
        # raise Exception('B can't be zero')
    else
        result = a // b
```