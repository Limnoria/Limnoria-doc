
.. _plugin-conditional:

The Conditional plugin
======================

.. _command-gt:

gt <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if <item1> is greater than <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-nlt:

nlt <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if <item1> is less than <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-nne:

nne <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if they are not equal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-ge:

ge <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if <item1> is greater than or equal to <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-cor:

cor <cond1> [<cond2> ... <condN>]
 
 Returns true if any one of conditions supplied evaluates to true.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-nle:

nle <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if <item1> is less than or equal to <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-ceq:

ceq <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if they are equal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-nge:

nge <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if <item1> is greater than or equal to <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-cxor:

cxor <cond1> [<cond2> ... <condN>]
 
 Returns true if only one of conditions supplied evaluates to true.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-le:

le <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if <item1> is less than or equal to <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-cif:

cif <condition> <ifcommand> <elsecommand>
 
 Runs <ifcommand> if <condition> evaluates to true, runs <elsecommand>
 if it evaluates to false.
 
 Use other logical operators defined in this plugin and command nesting
 to your advantage here.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-ne:

ne <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if they are not equal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-cand:

cand <cond1> [<cond2> ... <condN>]
 
 Returns true if all conditions supplied evaluate to true.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-nceq:

nceq <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if they are equal.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-ngt:

ngt <item1> <item2>
 
 Does a numeric comparison on <item1> and <item2>. 
 Returns true if they <item1> is greater than <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-lt:

lt <item1> <item2>
 
 Does a string comparison on <item1> and <item2>. 
 Returns true if <item1> is less than <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-match:

match <item1> <item2>
 
 Determines if <item1> is a substring of <item2>. 
 Returns true if <item1> is contained in <item2>.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



