
.. _plugin-conditional:

The Conditional plugin
======================

.. command-gt:

gt <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if <item1> is greater than <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-nlt:

nlt <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if <item1> is less than <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-nne:

nne <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if they are not equal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-ge:

ge <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if <item1> is greater than or equal to <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-cor:

cor <cond1> [<cond2> ... <condN>]
 
 Returns true if any one of conditions supplied evaluates to true.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-nle:

nle <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if <item1> is less than or equal to <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-ceq:

ceq <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if they are equal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-nge:

nge <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if <item1> is greater than or equal to <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-cxor:

cxor <cond1> [<cond2> ... <condN>]
 
 Returns true if only one of conditions supplied evaluates to true.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-le:

le <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if <item1> is less than or equal to <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-cif:

cif <condition> <ifcommand> <elsecommand>
 
 Runs <ifcommand> if <condition> evaluates to true, runs <elsecommand>
 if it evaluates to false.
 
 Use other logical operators defined in this plugin and command nesting
 to your advantage here.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-ne:

ne <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if they are not equal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-cand:

cand <cond1> [<cond2> ... <condN>]
 
 Returns true if all conditions supplied evaluate to true.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-nceq:

nceq <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if they are equal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-ngt:

ngt <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if they <item1> is greater than <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-lt:

lt <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if <item1> is less than <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. command-match:

match <item1> <item2>
 
 Determines if <item1> is a substring of <item2>. 
 Returns true if <item1> is contained in <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



