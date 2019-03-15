## Lab 8

###Activity
* One important point should be clearly understood that an activity diagram cannot be exactly matched with the code
* Partitions provide a constrained view on the behaviors invoked in activities. Constraints could be selected according to the type of the element that the partition represents. The following constraints are normative (standard) in UML 2.4:
	* classifier
	* instance
	* part
	* attribute and value

###State chart
A state chart diagram is normally used to model how the state of an
object changes in its life time. State chart diagrams are good at
describing how the behaviour of an object changes across several use
case executions. However, if we are interested in modelling some
behaviour that involves several objects collaborating with each other,
state chart diagram is not appropriate. We have already seen that such
behaviour is better modelled using sequence or collaboration diagrams.
State chart diagrams are based on the finite state machine (FSM)
formalism.

###Package
Package is a namespace used to group together elements that are semantically related and might change together. It is a general purpose mechanism to organize elements into groups to provide better structure for system model.