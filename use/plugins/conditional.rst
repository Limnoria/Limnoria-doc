
.. _plugin-conditional:

The Conditional plugin
======================

Numeric comparison
------------------

.. _command-conditional-nlt:

conditional nlt <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a numeric comparison on *<item1>* and *<item2>*.
Returns true if *<item1>* is less than *<item2>*.

.. _command-conditional-nne:

conditional nne <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a numeric comparison on *<item1>* and *<item2>*.
Returns true if they are not equal.

.. _command-conditional-nle:

conditional nle <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a numeric comparison on *<item1>* and *<item2>*.
Returns true if *<item1>* is less than or equal to *<item2>*.

.. _command-conditional-nge:

conditional nge <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a numeric comparison on *<item1>* and *<item2>*.
Returns true if *<item1>* is greater than or equal to *<item2>*.

.. _command-conditional-nceq:

conditional nceq <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a numeric comparison on *<item1>* and *<item2>*.
Returns true if they are equal.

.. _command-conditional-ngt:

conditional ngt <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a numeric comparison on *<item1>* and *<item2>*.
Returns true if they *<item1>* is greater than *<item2>*.

String comparison
-----------------

.. _command-conditional-le:

conditional le <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a string comparison on *<item1>* and *<item2>*.
Returns true if *<item1>* is less than or equal to *<item2>*.

.. _command-conditional-ceq:

conditional ceq <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a string comparison on *<item1>* and *<item2>*.
Returns true if they are equal.

.. _command-conditional-gt:

conditional gt <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a string comparison on *<item1>* and *<item2>*.
Returns true if *<item1>* is greater than *<item2>*.

.. _command-conditional-ge:

conditional ge <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a string comparison on *<item1>* and *<item2>*.
Returns true if *<item1>* is greater than or equal to *<item2>*.

.. _command-conditional-ne:

conditional ne <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a string comparison on *<item1>* and *<item2>*.
Returns true if they are not equal.

.. _command-conditional-lt:

conditional lt <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a string comparison on *<item1>* and *<item2>*.
Returns true if *<item1>* is less than *<item2>*.

.. _command-conditional-match:

conditional match <item1> <item2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Determines if *<item1>* is a substring of *<item2>*.
Returns true if *<item1>* is contained in *<item2>*.

Logical operators
-----------------

.. _command-conditional-cand:

conditional cand <cond1> [<cond2> ... <condN>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns true if all conditions supplied evaluate to true.

.. _command-conditional-cxor:

conditional cxor <cond1> [<cond2> ... <condN>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns true if only one of conditions supplied evaluates to true.

.. _command-conditional-cor:

conditional cor <cond1> [<cond2> ... <condN>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns true if any one of conditions supplied evaluates to true.

.. _command-conditional-cif:

conditional cif <condition> <ifcommand> <elsecommand>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Runs *<ifcommand>* if *<condition>* evaluates to true, runs *<elsecommand>*
if it evaluates to false.

Use other logical operators defined in this plugin and command nesting
to your advantage here.

