
.. _plugin-admin:

The Admin plugin
================

Capabilities
------------

.. _command-admin-capability-add:

capability add <name|hostmask> <capability>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives the user specified by *<name>* (or the user to whom *<hostmask>*
currently maps) the specified capability *<capability>*

.. _command-admin-capability-remove:

capability remove <name|hostmask> <capability>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Takes from the user specified by *<name>* (or the user to whom
*<hostmask>* currently maps) the specified capability *<capability>*

Channels
--------

.. _command-admin-channels:

channels
^^^^^^^^

Returns the channels the bot is on. Must be given in private, in order
to protect the secrecy of secret channels.

.. _command-admin-join:

join <channel> [<key>]
^^^^^^^^^^^^^^^^^^^^^^

Tell the bot to join the given channel. If *<key>* is given, it is used
when attempting to join the channel.

.. _command-admin-part:

part [<channel>] [<reason>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tells the bot to part the list of channels you give it. *<channel>* is
only necessary if you want the bot to part a channel other than the
current channel. If *<reason>* is specified, use it as the part
message.

Ignores
-------

.. _command-admin-ignore-list:

ignore list
^^^^^^^^^^^

Lists the hostmasks that the bot is ignoring.

.. _command-admin-ignore-remove:

ignore remove <hostmask|nick>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This will remove the persistent ignore on *<hostmask>* or the
hostmask currently associated with *<nick>*.

.. _command-admin-ignore-add:

ignore add <hostmask|nick> [<expires>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This will set a persistent ignore on *<hostmask>* or the hostmask
currently associated with *<nick>*. *<expires>* is an optional argument
specifying when (in "seconds from now") the ignore will expire; if
it isn't given, the ignore will never automatically expire.

Miscellaneous
-------------

.. _command-admin-nick:

nick [<nick>]
^^^^^^^^^^^^^

Changes the bot's nick to *<nick>*. If no nick is given, returns the
bot's current nick.



.. _plugin-admin-config:

Configuration
-------------

.. _supybot.plugins.Admin.public:

supybot.plugins.Admin.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

