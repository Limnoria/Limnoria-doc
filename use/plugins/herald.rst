
.. _plugin-herald:

The Herald plugin
=================

User commands
-------------

.. _command-herald-get:

herald get [<channel>] [<user|nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current herald message for *<user>* (or the user
*<nick|hostmask>* is currently identified or recognized as). If *<user>*
is not given, defaults to the user giving the command. *<channel>*
is only necessary if the message isn't sent in the channel itself.

.. _command-herald-remove:

herald remove [<channel>] [<user|nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the herald message set for *<user>*, or the user
*<nick|hostmask>* is currently identified or recognized as. If *<user>*
is not given, defaults to the user giving the command.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-herald-change:

herald change [<channel>] [<user|nick>] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the herald message for *<user>*, or the user *<nick|hostmask>* is
currently identified or recognized as, according to *<regexp>*. If
*<user>* is not given, defaults to the calling user. *<channel>* is only
necessary if the message isn't sent in the channel itself.

Op commands
-----------

.. _command-herald-default:

herald default [<channel>] [--remove|<msg>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If *<msg>* is given, sets the default herald to *<msg>*. A *<msg>* of ""
will remove the default herald. If *<msg>* is not given, returns the
current default herald. *<channel>* is only necessary if the message
isn't sent in the channel itself.

.. _command-herald-add:

herald add [<channel>] <user|nick> <msg>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the herald message for *<user>* (or the user *<nick|hostmask>* is
currently identified or recognized as) to *<msg>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.



.. _plugin-herald-config:

Configuration
-------------

.. _supybot.plugins.Herald.heralding:

supybot.plugins.Herald.heralding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether messages will be sent to the channel when a recognized user joins; basically enables or disables the plugin.

.. _supybot.plugins.Herald.default:

supybot.plugins.Herald.default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Sets the default herald to use. If a user has a personal herald specified, that will be used instead. If set to the empty string, the default herald will be disabled.

.. _supybot.plugins.Herald.default.notice:

supybot.plugins.Herald.default.notice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the default herald will be sent as a NOTICE instead of a PRIVMSG.

.. _supybot.plugins.Herald.default.public:

supybot.plugins.Herald.default.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the default herald will be sent publicly.

.. _supybot.plugins.Herald.throttle:

supybot.plugins.Herald.throttle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 600

Determines the minimum number of seconds between heralds.

.. _supybot.plugins.Herald.throttle.afterPart:

supybot.plugins.Herald.throttle.afterPart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 0

Determines the minimum number of seconds after parting that the bot will not herald the person when he or she rejoins.

.. _supybot.plugins.Herald.throttle.afterSplit:

supybot.plugins.Herald.throttle.afterSplit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 60

Determines the minimum number of seconds after a netsplit that the bot will not herald the users that split.

.. _supybot.plugins.Herald.public:

supybot.plugins.Herald.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.Herald.requireCapability:

supybot.plugins.Herald.requireCapability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines what capability (if any) is required to add/change/remove the herald of another user.

