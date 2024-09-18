# Reading and Writing File
## File Object


File Object
    - read()
    - write()
    - close()

## Opening a File using With keyword

```python
with open(path, 'r', encoding="utf-8") as f:
    # Do File operations
```

***auto close() file***

Longer way
```python
f = open(path)
try:
    # Do file operations
    pass
finally:
    f.close()
```

# Method for Reading 
## read()
> read() - return whole file as String by Default. Or it will return the specified number of bytes.

## readline()
> `readline()` - return next line of the file as a String

## readlines()
> `readlines() - return list of String of all of lines in the file

## loop to read from a file object

```python
with open(path, 'r', encoding="utf-8") as f:
    for line in f:
        print(line)
```


if use with block, exception may be 

mode:

    - `a`: append
    - 'w': write
    - 'r': read
    - 'w+': read and write
    - '_<b> : read/write binary 
# Working with files

built-in module for handling files:

    - os
    - shutil
    - pathlib

## os module

```python
# add os module
import os 
```

functions:

    - make directories
    - list files
    - move files

### make directories
```python
    import os 

    os.mkdir(absolute_path)
```
### list all entries in a dictionary

```python
import os

folder = '/User/vinhchis/desktop/'
entries = os.scandir(folder)
```

### check if a directory entry or a file or a subdirectory

 - `os.path.isFile(file)` -> check file
 - `os.path.isDir(file)` -> check sub folder

### create a absolute path name

os.path.join(folder_destination, file_name)

***can use '+' two string. But this function check for correct format and is a best practice***

### move file

os.rename(location_original, location_destination)