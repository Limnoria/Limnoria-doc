
.. _plugin-linkrelay:

The LinkRelay plugin
====================

.. _command-linkrelay-nosubstitute:

linkrelay nosubstitute <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Undo a substitution.

.. _command-linkrelay-nicks:

linkrelay nicks [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the nicks of the people in the linked channels.
*<channel>* is only necessary if the message
isn't sent on the channel itself.

.. _command-linkrelay-list:

linkrelay list
^^^^^^^^^^^^^^

Returns all the defined relay links

.. _command-linkrelay-remove:

linkrelay remove [--from <channel>@<network>] [--to <channel>@<network>] [--regexp <regexp>] [--reciprocal]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove a relay from the list. You must give at least *--from* or *--to;* if
one of them is not given, it defaults to the current channel@network.
Only messages matching *<regexp>* will be relayed; if *<regexp>* is not
given, everything is relayed.
If *--reciprocal* is given, another relay will be removed automatically,
in the opposite direction.

.. _command-linkrelay-add:

linkrelay add [--from <channel>@<network>] [--to <channel>@<network>] [--regexp <regexp>] [--reciprocal]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a relay to the list. You must give at least *--from* or *--to;* if
one of them is not given, it defaults to the current channel@network.
Only messages matching *<regexp>* will be relayed; if *<regexp>* is not
given, everything is relayed.
If *--reciprocal* is given, another relay will be added automatically,
in the opposite direction.

.. _command-linkrelay-substitute:

linkrelay substitute <regexp> <replacement>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces all nicks that matches the *<regexp>* by the *<replacement>*
string.



.. _plugin-linkrelay-config:

Configuration
-------------

.. _supybot.plugins.LinkRelay.color:

supybot.plugins.LinkRelay.color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will color Relayed PRIVMSGs so as to make the messages easier to read.

.. _supybot.plugins.LinkRelay.hostmasks:

supybot.plugins.LinkRelay.hostmasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will Relay the hostmask of the person joining or parting the channel when he or she joins or parts.

.. _supybot.plugins.LinkRelay.includeNetwork:

supybot.plugins.LinkRelay.includeNetwork
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will include the network in Relayed PRIVMSGs; if you're only Relaying between two networks, it's somewhat redundant, and you may wish to save the space.

.. _supybot.plugins.LinkRelay.nonPrivmsgs:

supybot.plugins.LinkRelay.nonPrivmsgs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: privmsg

Determines whether the bot will use PRIVMSGs (privmsg), NOTICEs (notice), for non-PRIVMSG Relay messages (i.e., joins, parts, nicks, quits, modes, etc.), or whether it won't relay such messages (nothing)

.. _supybot.plugins.LinkRelay.topicSync:

supybot.plugins.LinkRelay.topicSync
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will synchronize topics between networks in the channels it Relays.

.. _supybot.plugins.LinkRelay.colors:

supybot.plugins.LinkRelay.colors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.LinkRelay.colors.info:

supybot.plugins.LinkRelay.colors.info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 02

Color used for relaying 02.

.. _supybot.plugins.LinkRelay.colors.join:

supybot.plugins.LinkRelay.colors.join
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 14

Color used for relaying 14.

.. _supybot.plugins.LinkRelay.colors.kick:

supybot.plugins.LinkRelay.colors.kick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 14

Color used for relaying 14.

.. _supybot.plugins.LinkRelay.colors.mode:

supybot.plugins.LinkRelay.colors.mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 14

Color used for relaying 14.

.. _supybot.plugins.LinkRelay.colors.nick:

supybot.plugins.LinkRelay.colors.nick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 14

Color used for relaying 14.

.. _supybot.plugins.LinkRelay.colors.part:

supybot.plugins.LinkRelay.colors.part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 14

Color used for relaying 14.

.. _supybot.plugins.LinkRelay.colors.quit:

supybot.plugins.LinkRelay.colors.quit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 14

Color used for relaying 14.

.. _supybot.plugins.LinkRelay.colors.truncated:

supybot.plugins.LinkRelay.colors.truncated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 14

Color used for relaying 14.

.. _supybot.plugins.LinkRelay.public:

supybot.plugins.LinkRelay.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.LinkRelay.relays:

supybot.plugins.LinkRelay.relays
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

You shouldn't edit this configuration variable yourself unless you know what you do. Use @LinkRelay {add|remove} instead.

.. _supybot.plugins.LinkRelay.substitutes:

supybot.plugins.LinkRelay.substitutes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

You shouldn't edit this configuration variable yourself unless you know what you do. Use @LinkRelay (no)substitute instead.

