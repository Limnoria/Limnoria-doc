
.. _plugin-relay:

The Relay plugin
================

.. _command-nicks:

nicks [<channel>]
^^^^^^^^^^^^^^^^^

Returns the nicks of the people in the channel on the various networks
the bot is connected to. *<channel>* is only necessary if the message
isn't sent on the channel itself.


.. _command-part:

part <channel>
^^^^^^^^^^^^^^

Ceases relaying between the channel *<channel>* on all networks. The bot
will part from the channel on all networks in which it is on the
channel.


.. _command-join:

join [<channel>]
^^^^^^^^^^^^^^^^

Starts relaying between the channel *<channel>* on all networks. If on a
network the bot isn't in *<channel>*, he'll join. This commands is
required even if the bot is in the channel on both networks; he won't
relay between those channels unless he's told to join both
channels. If *<channel>* is not given, starts relaying on the channel
the message was sent in.


