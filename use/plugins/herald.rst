
.. _plugin-herald:

The Herald plugin
=================

.. command-get:

get [<channel>] [<user|nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current herald message for *<user>* (or the user
*<nick|hostmask>* is currently identified or recognized as). If *<user>*
is not given, defaults to the user giving the command. *<channel>*
is only necessary if the message isn't sent in the channel itself.


.. command-die:

die 
^^^^



.. command-remove:

remove [<channel>] [<user|nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the herald message set for *<user>*, or the user
*<nick|hostmask>* is currently identified or recognized as. If *<user>*
is not given, defaults to the user giving the command.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-default:

default [<channel>] [--remove|<msg>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If *<msg>* is given, sets the default herald to *<msg>*. A *<msg>* of ""
will remove the default herald. If *<msg>* is not given, returns the
current default herald. *<channel>* is only necessary if the message
isn't sent in the channel itself.


.. command-add:

add [<channel>] <user|nick> <msg>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the herald message for *<user>* (or the user *<nick|hostmask>* is
currently identified or recognized as) to *<msg>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-change:

change [<channel>] [<user|nick>] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the herald message for *<user>*, or the user *<nick|hostmask>* is
currently identified or recognized as, according to *<regexp>*. If
*<user>* is not given, defaults to the calling user. *<channel>* is only
necessary if the message isn't sent in the channel itself.


