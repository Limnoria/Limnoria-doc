
.. _plugin-messageparser:

The MessageParser plugin
========================

.. command-show:

show [<channel>] [--id] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Looks up the value of *<regexp>* in the triggers database.
*<channel>* is only necessary if the message isn't sent in the channel
itself.
If option *--id* specified, will retrieve by regexp id, not content.


.. command-lock:

lock [<channel>] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^

Locks the *<regexp>* so that it cannot be
removed or overwritten to. *<channel>* is only necessary if the message isn't
sent in the channel itself.


.. command-rank:

rank [<channel>]
^^^^^^^^^^^^^^^^

Returns a list of top-ranked regexps, sorted by usage count
(rank). The number of regexps returned is set by the
rankListLength registry value. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. command-unlock:

unlock [<channel>] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlocks the entry associated with *<regexp>* so that it can be
removed or overwritten. *<channel>* is only necessary if the message isn't
sent in the channel itself.


.. command-vacuum:

vacuum [<channel>]
^^^^^^^^^^^^^^^^^^

Vacuums the database for *<channel>*.
See SQLite vacuum doc here: http://www.sqlite.org/lang_vacuum.html
*<channel>* is only necessary if the message isn't sent in
the channel itself.
First check if user has the required capability specified in plugin
config requireVacuumCapability.


.. command-info:

info [<channel>] [--id] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Display information about *<regexp>* in the triggers database.
*<channel>* is only necessary if the message isn't sent in the channel
itself.
If option *--id* specified, will retrieve by regexp id, not content.


.. command-list:

list [<channel>]
^^^^^^^^^^^^^^^^

Lists regexps present in the triggers database.
*<channel>* is only necessary if the message isn't sent in the channel
itself. Regexp ID listed in paretheses.


.. command-remove:

remove [<channel>] [--id] <regexp>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the trigger for *<regexp>* from the triggers database.
*<channel>* is only necessary if
the message isn't sent in the channel itself.
If option *--id* specified, will retrieve by regexp id, not content.


.. command-add:

add [<channel>] <regexp> <action>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Associates *<regexp>* with *<action>*. *<channel>* is only
necessary if the message isn't sent on the channel
itself. Action is echoed upon regexp match, with variables $1, $2,
etc. being interpolated from the regexp match groups.

