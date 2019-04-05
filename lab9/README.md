## Lab 9  - Coding

### Learning Material

* https://www.python.org/dev/peps/pep-0333/
* https://www.tutorialspoint.com/python/python_cgi_programming.htm

### Addendum 1 : Problems faced during coding and resolutions

#### 1. Error with python path for cgi scripts

##### Problem

The default path in cgi python scripts was:
```
#! /usr/local/bin/python3
```
There was no python module at this path and the server failed to execute the requested scripts.

##### Solution

Update all the scripts header to:
```
#!/usr/bin/python3
```

#### 2. CGI Python scripts not executing

##### Problem
The scripts are not authorized for execution

##### Solution
Update permissions of the files in cgi-bin
```
cd cgi-bin
sudo chmod 775 *.py
```
#### 3. Custom modules import error

##### Problem
```
Traceback (most recent call last):
  File "TAVS/webapp/cgi-bin/rent.py", line 8, in <module>
    import Admin
ModuleNotFoundError: No module named 'Admin'

```
##### Solution 
This is not advised for deployment.
```
import sys
sys.path.insert(0, '/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/')

```
Add this to files which need to import the mymodule