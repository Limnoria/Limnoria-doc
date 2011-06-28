
.. _plugin-messageparser:

The MessageParser plugin
========================

Administration
--------------

.. _command-messageparser-remove:

messageparser remove [<channel>] [--id] <regexp>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the trigger for *<regexp>* from the triggers database.
*<channel>* is only necessary if
the message isn't sent in the channel itself.
If option *--id* specified, will retrieve by regexp id, not content.

.. _command-messageparser-add:

messageparser add [<channel>] <regexp> <action>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Associates *<regexp>* with *<action>*. *<channel>* is only
necessary if the message isn't sent on the channel
itself. Action is echoed upon regexp match, with variables $1, $2,
etc. being interpolated from the regexp match groups.


.. _command-messageparser-lock:

messageparser lock [<channel>] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Locks the *<regexp>* so that it cannot be
removed or overwritten to. *<channel>* is only necessary if the message isn't
sent in the channel itself.

.. _command-messageparser-unlock:

messageparser unlock [<channel>] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlocks the entry associated with *<regexp>* so that it can be
removed or overwritten. *<channel>* is only necessary if the message isn't
sent in the channel itself.

.. _command-messageparser-vacuum:

messageparser vacuum [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vacuums the database for *<channel>*.
See SQLite vacuum doc here: http://www.sqlite.org/lang_vacuum.html
*<channel>* is only necessary if the message isn't sent in
the channel itself.
First check if user has the required capability specified in plugin
config requireVacuumCapability.

User commands
-------------

.. _command-messageparser-show:

messageparser show [<channel>] [--id] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Looks up the value of *<regexp>* in the triggers database.
*<channel>* is only necessary if the message isn't sent in the channel
itself.
If option *--id* specified, will retrieve by regexp id, not content.

.. _command-messageparser-rank:

messageparser rank [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a list of top-ranked regexps, sorted by usage count
(rank). The number of regexps returned is set by the
rankListLength registry value. *<channel>* is only necessary if the
message isn't sent in the channel itself.

.. _command-messageparser-info:

messageparser info [<channel>] [--id] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Display information about *<regexp>* in the triggers database.
*<channel>* is only necessary if the message isn't sent in the channel
itself.
If option *--id* specified, will retrieve by regexp id, not content.

.. _command-messageparser-list:

messageparser list [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists regexps present in the triggers database.
*<channel>* is only necessary if the message isn't sent in the channel
itself. Regexp ID listed in paretheses.
