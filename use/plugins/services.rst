
.. _plugin-services:

The Services plugin
===================

NickServ
--------

.. _command-services-identify:

services identify
^^^^^^^^^^^^^^^^^

Identifies with NickServ using the current nick.

.. _command-services-nicks:

services nicks
^^^^^^^^^^^^^^

Returns the nicks that this plugin is configured to identify and ghost
with.

.. _command-services-password:

services password <nick> [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the NickServ password for *<nick>* to *<password>*. If *<password>* is
not given, removes *<nick>* from the configured nicks.

.. _command-services-ghost:

services ghost [<nick>]
^^^^^^^^^^^^^^^^^^^^^^^

Ghosts the bot's given nick and takes it. If no nick is given,
ghosts the bot's configured nick and takes it.

ChanServ
--------

.. _command-services-unban:

services unban [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^

Attempts to get unbanned by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself, but chances
are, if you need this command, you're not sending it in the channel
itself.

.. _command-services-invite:

services invite [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attempts to get invited by ChanServ to *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself, but chances
are, if you need this command, you're not sending it in the channel
itself.

.. _command-services-voice:

services voice [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^

Attempts to get voiced by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-services-op:

services op [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^

Attempts to get opped by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.

