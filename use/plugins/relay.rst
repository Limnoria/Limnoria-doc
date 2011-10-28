
.. _plugin-relay:

The Relay plugin
================

.. _command-relay-nicks:

relay nicks [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^

Returns the nicks of the people in the channel on the various networks
the bot is connected to. *<channel>* is only necessary if the message
isn't sent on the channel itself.

.. _command-relay-part:

relay part <channel>
^^^^^^^^^^^^^^^^^^^^

Ceases relaying between the channel *<channel>* on all networks. The bot
will part from the channel on all networks in which it is on the
channel.

.. _command-relay-join:

relay join [<channel>]
^^^^^^^^^^^^^^^^^^^^^^

Starts relaying between the channel *<channel>* on all networks. If on a
network the bot isn't in *<channel>*, he'll join. This commands is
required even if the bot is in the channel on both networks; he won't
relay between those channels unless he's told to join both
channels. If *<channel>* is not given, starts relaying on the channel
the message was sent in.



.. _plugin-relay-config:

Configuration
-------------

.. _supybot.plugins.Relay.color:

supybot.plugins.Relay.color
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will color relayed PRIVMSGs so as to make the messages easier to read.

.. _supybot.plugins.Relay.hostmasks:

supybot.plugins.Relay.hostmasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will relay the hostmask of the person joining or parting the channel when he or she joins or parts.

.. _supybot.plugins.Relay.ignores:

supybot.plugins.Relay.ignores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Determines what hostmasks will not be relayed on a channel.

.. _supybot.plugins.Relay.includeNetwork:

supybot.plugins.Relay.includeNetwork
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will include the network in relayed PRIVMSGs; if you're only relaying between two networks, it's somewhat redundant, and you may wish to save the space.

.. _supybot.plugins.Relay.noticeNonPrivmsgs:

supybot.plugins.Relay.noticeNonPrivmsgs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will used NOTICEs rather than PRIVMSGs for non-PRIVMSG relay messages (i.e., joins, parts, nicks, quits, modes, etc.)

.. _supybot.plugins.Relay.punishOtherRelayBots:

supybot.plugins.Relay.punishOtherRelayBots
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will detect other bots relaying and respond by kickbanning them.

.. _supybot.plugins.Relay.topicSync:

supybot.plugins.Relay.topicSync
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will synchronize topics between networks in the channels it relays.

.. _supybot.plugins.Relay.channels:

supybot.plugins.Relay.channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Determines which channels the bot will relay in.

.. _supybot.plugins.Relay.channels.joinOnAllNetworks:

supybot.plugins.Relay.channels.joinOnAllNetworks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will always join the channel(s) it relays for on all networks the bot is connected to.

.. _supybot.plugins.Relay.public:

supybot.plugins.Relay.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

