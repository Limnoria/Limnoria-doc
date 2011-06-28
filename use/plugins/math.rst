
.. _plugin-math:

The Math plugin
===============

Conversion
----------

.. _command-math-base:

math base <fromBase> [<toBase>] <number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts *<number>* from base *<fromBase>* to base *<toBase>*.
If *<toBase>* is left out, it converts to decimal.

.. _command-math-convert:

math convert [<number>] <unit> to <other unit>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts from *<unit>* to *<other unit>*. If number isn't given, it
defaults to 1. For unit information, see 'units' command.

Calculation
-----------

.. _command-math-rpn:

math rpn <rpn math expression>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the value of an RPN expression.

.. _command-math-icalc:

math icalc <math expression>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the same as the calc command except that it allows integer
math, and can thus cause the bot to suck up CPU. Hence it requires
the 'trusted' capability to use.

.. _command-math-units:

math units [<type>]
^^^^^^^^^^^^^^^^^^^

With no arguments, returns a list of measurement types, which can be
passed as arguments. When called with a type as an argument, returns
the units of that type.

.. _command-math-calc:

math calc <math expression>
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the value of the evaluated *<math expression>*. The syntax is
Python syntax; the type of arithmetic is floating point. Floating
point arithmetic is used in order to prevent a user from being able to
crash to the bot with something like '10**10**10**10'. One consequence
is that large values such as '10**24' might not be exact.

