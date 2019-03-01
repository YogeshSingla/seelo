# Lab 6 - System Design II
## Use Case Diagram

### Difference between extend and include
Extend is used when a use case adds steps to another first-class use case.

For example, imagine "Withdraw Cash" is a use case of an Automated Teller Machine (ATM). "Assess Fee" would extend Withdraw Cash and describe the conditional "extension point" that is instantiated when the ATM user doesn't bank at the ATM's owning institution. Notice that the basic "Withdraw Cash" use case stands on its own, without the extension.
Include is used to extract use case fragments that are duplicated in multiple use cases. The included use case cannot stand alone and the original use case is not complete without the included one. This should be used sparingly and only in cases where the duplication is significant and exists by design (rather than by coincidence).
For example, the flow of events that occurs at the beginning of every ATM use case (when the user puts in their ATM card, enters their PIN, and is shown the main menu) would be a good candidate for an include.


extend : use condition as well

ref: https://stackoverflow.com/questions/1696927/whats-is-the-difference-between-include-and-extend-in-use-case-diagram
https://circle.visual-paradigm.com/docs/uml-and-sysml/use-case-diagram/use-case-diagram-notations-guide/


## Class Diagram	

### aggregation vs composition
 aggregation relationship is often "catalog" containment to distinguish it from composition's "physical" containment.

 aggregation with filled rhombus

ref: https://en.wikipedia.org/wiki/Class_diagram