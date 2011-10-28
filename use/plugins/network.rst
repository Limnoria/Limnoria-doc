
.. _plugin-network:

The Network plugin
==================

Getting status
--------------

.. _command-network-driver:

network driver [<network>]
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current network driver for *<network>*. *<network>* is only
necessary if the message isn't sent on the network to which this
command is to apply.

.. _command-network-networks:

network networks
^^^^^^^^^^^^^^^^

Returns the networks to which the bot is currently connected.

.. _command-network-latency:

network latency [<network>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current latency to *<network>*. *<network>* is only necessary
if the message isn't sent on the network to which this command is to
apply.

Running commands
----------------

.. _command-network-whois:

network whois [<network>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the WHOIS response *<network>* gives for *<nick>*. *<network>* is
only necessary if the network is different than the network the command
is sent on.

.. _command-network-command:

network command <network> <command> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives the bot *<command>* (with its associated *<arg>*s) on *<network>*.

(Dis)connecting
---------------

.. _command-network-connect:

network connect [--ssl] <network> [<host[:port]>] [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connects to another network (which will be represented by the name
provided in *<network>*) at *<host:port>*. If port is not provided, it
defaults to 6667, the default port for IRC. If password is
provided, it will be sent to the server in a PASS command. If *--ssl* is
provided, an SSL connection will be attempted.

.. _command-network-reconnect:

network reconnect [<network>] [<quit message>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disconnects and then reconnects to *<network>*. If no network is given,
disconnects and then reconnects to the network the command was given
on. If no quit message is given, uses the configured one
(:ref:`supybot.plugins.Owner.quitMsg`) or the nick of the person giving the
command.

.. _command-network-disconnect:

network disconnect [<network>] [<quit message>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disconnects from the network represented by the network *<network>*.
If *<quit message>* is given, quits the network with the given quit
message. *<network>* is only necessary if the network is different
from the network the command is sent on.


.. _plugin-network-config:

Configuration
-------------

.. _supybot.plugins.Network.public:

supybot.plugins.Network.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

