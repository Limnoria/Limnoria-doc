
.. _plugin-later:

The Later plugin
================

Commands
--------

.. _command-later-notes:

later notes [<nick>]
^^^^^^^^^^^^^^^^^^^^

If *<nick>* is given, replies with what notes are waiting on *<nick>*,
otherwise, replies with the nicks that have notes waiting for them.

.. _command-later-remove:

later remove <nick>
^^^^^^^^^^^^^^^^^^^

Removes the notes waiting on *<nick>*.

.. _command-later-tell:

later tell <nick> <text>
^^^^^^^^^^^^^^^^^^^^^^^^

Tells *<nick>* *<text>* the next time *<nick>* is in seen. *<nick>* can
contain wildcard characters, and the first matching nick will be
given the note.



.. _plugin-later-config:

Configuration
-------------

.. _supybot.plugins.Later.maximum:

supybot.plugins.Later.maximum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 0

Determines the maximum number of messages to be queued for a user. If this value is 0, there is no maximum.

.. _supybot.plugins.Later.messageExpiry:

supybot.plugins.Later.messageExpiry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 30

Determines the maximum number of days that a message will remain queued for a user. After this time elapses, the message will be deleted. If this value is 0, there is no maximum.

.. _supybot.plugins.Later.private:

supybot.plugins.Later.private
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether users will be notified in the first place in which they're seen, or in private.

.. _supybot.plugins.Later.public:

supybot.plugins.Later.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.Later.tellOnJoin:

supybot.plugins.Later.tellOnJoin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether users will be notified upon joining any channel the bot is in, or only upon sending a message.

