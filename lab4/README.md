## Lab 4 - DFD
### Data Flow Diagram

Transfer of data between processes shown using DFD.

1. Rectangle - External entity
2. Circle - Process
3. Two parallel lines - Database
4. 'sim card' - Output
5. Synchronous and Asynchronous connections

Every level contains 3-7 bubbles only. Inputs/Outputs should be balanced between levels in DFD ie the inputs/outputs of level n should be satisfied in level n+1.

#### Level 0 - Context Level Diagram
* Whole project one process/one bubble
* Users and project interface
* Define external entities
* e.g request/response b/w user and system

#### Level 1 
* External entity not needed to be defined
* System processes and databases shown

#### Level 2
* System proceses may further be decomposed
* Make sure the I/O of this process in Level 1 are only used in Level 2. Maintain consistency.

***
https://en.wikipedia.org/wiki/Data_flow_diagram

