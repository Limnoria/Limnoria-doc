
.. _plugin-services:

The Services plugin
===================

.. command-disabled:

disabled 
^^^^^^^^^



.. command-identify:

identify
^^^^^^^^

Identifies with NickServ using the current nick.


.. command-nicks:

nicks
^^^^^

Returns the nicks that this plugin is configured to identify and ghost
with.


.. command-unban:

unban [<channel>]
^^^^^^^^^^^^^^^^^

Attempts to get unbanned by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself, but chances
are, if you need this command, you're not sending it in the channel
itself.


.. command-reset:

reset 
^^^^^^



.. command-invite:

invite [<channel>]
^^^^^^^^^^^^^^^^^^

Attempts to get invited by ChanServ to *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself, but chances
are, if you need this command, you're not sending it in the channel
itself.


.. command-password:

password <nick> [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the NickServ password for *<nick>* to *<password>*. If *<password>* is
not given, removes *<nick>* from the configured nicks.


.. command-ghost:

ghost [<nick>]
^^^^^^^^^^^^^^

Ghosts the bot's given nick and takes it. If no nick is given,
ghosts the bot's configured nick and takes it.


.. command-voice:

voice [<channel>]
^^^^^^^^^^^^^^^^^

Attempts to get voiced by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-op:

op [<channel>]
^^^^^^^^^^^^^^

Attempts to get opped by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


