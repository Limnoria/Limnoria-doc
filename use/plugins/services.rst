
.. _plugin-services:

The Services plugin
===================

.. _command-disabled:

disabled 
^^^^^^^^^



.. _command-identify:

identify
^^^^^^^^

Identifies with NickServ using the current nick.


.. _command-nicks:

nicks
^^^^^

Returns the nicks that this plugin is configured to identify and ghost
with.


.. _command-unban:

unban [<channel>]
^^^^^^^^^^^^^^^^^

Attempts to get unbanned by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself, but chances
are, if you need this command, you're not sending it in the channel
itself.


.. _command-reset:

reset 
^^^^^^



.. _command-invite:

invite [<channel>]
^^^^^^^^^^^^^^^^^^

Attempts to get invited by ChanServ to *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself, but chances
are, if you need this command, you're not sending it in the channel
itself.


.. _command-password:

password <nick> [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the NickServ password for *<nick>* to *<password>*. If *<password>* is
not given, removes *<nick>* from the configured nicks.


.. _command-ghost:

ghost [<nick>]
^^^^^^^^^^^^^^

Ghosts the bot's given nick and takes it. If no nick is given,
ghosts the bot's configured nick and takes it.


.. _command-voice:

voice [<channel>]
^^^^^^^^^^^^^^^^^

Attempts to get voiced by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. _command-op:

op [<channel>]
^^^^^^^^^^^^^^

Attempts to get opped by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


