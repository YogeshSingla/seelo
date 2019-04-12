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

#### 4. Indentation error

##### Problem

```
Traceback (most recent call last):
  File "/home/kirito/TODO/seelo/lab9/TAVS/webapp/cgi-bin/rent.py", line 7, in <module>
    import User
  File "/home/kirito/TODO/seelo/lab9/TAVS/webapp/mymodule/User.py", line 4
    self.u_name = ''
       ^
IndentationError: expected an indented block
		
```

##### Solution

Python is space/tab conscious!
Make sure you are consistent with spaces or tabs across all your python scripts.
Use sublime text editors bottom right option to convert tabs/spaces.

#### 5. Calling cross CGI scripts

##### Problem

When the admin login is successful, the server should send the admin.py request instead of a html response from the existing cgi script of authenticate_admin

##### Solution

Import the admin.py within the success case of if condition to call the admin.py cgi script


### List of ERRORS that may be encountered
These are for troubleshooting. During execution to prevent the system from landing in an unconsistent state multiple safety checks are done. Each throws a error cause. They are listed below.

#### Error #1
Trying to book a vehicle that does not exist. Enter allowed vehicles from the form only.

#### Error #2
Trying to book another vehicle before returning the previous vehicle.

#### Error #3
Trying to return without booking first.

#### Error #4
No vehicles added by admin to book for customers.

#### Error #5
Vehicle being trying to be updated is missing

#### Error #6
Vehicle files is missing

#### Error #7 
Admin credentials file missing

#### Error #8
All vehicles of choosen rent type booked