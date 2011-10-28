
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


.. _plugin-messageparser-config:

Configuration
-------------

.. _supybot.plugins.MessageParser.enable:

supybot.plugins.MessageParser.enable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the message parser is enabled. If enabled, will trigger on regexps added to the regexp db.

.. _supybot.plugins.MessageParser.keepRankInfo:

supybot.plugins.MessageParser.keepRankInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether we keep updating the usage count for each regexp, for popularity ranking.

.. _supybot.plugins.MessageParser.listSeparator:

supybot.plugins.MessageParser.listSeparator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: , 

Determines the separator used between regexps when shown by the list command.

.. _supybot.plugins.MessageParser.rankListLength:

supybot.plugins.MessageParser.rankListLength
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 20

Determines the number of regexps returned by the triggerrank command.

.. _supybot.plugins.MessageParser.requireManageCapability:

supybot.plugins.MessageParser.requireManageCapability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: admin; channel,op

Determines the capabilities required (if any) to manage the regexp database, including add, remove, lock, unlock. Use 'channel,capab' for channel-level capabilities. Note that absence of an explicit anticapability means user has capability.

.. _supybot.plugins.MessageParser.requireVacuumCapability:

supybot.plugins.MessageParser.requireVacuumCapability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: admin

Determines the capability required (if any) to vacuum the database.

.. _supybot.plugins.MessageParser.public:

supybot.plugins.MessageParser.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

