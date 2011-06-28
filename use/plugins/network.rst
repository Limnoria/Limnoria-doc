
.. _plugin-network:

The Network plugin
==================

.. _command-driver:

driver [<network>]
^^^^^^^^^^^^^^^^^^

Returns the current network driver for *<network>*. *<network>* is only
necessary if the message isn't sent on the network to which this
command is to apply.


.. _command-connect:

connect [--ssl] <network> [<host[:port]>] [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connects to another network (which will be represented by the name
provided in *<network>*) at *<host:port>*. If port is not provided, it
defaults to 6667, the default port for IRC. If password is
provided, it will be sent to the server in a PASS command. If *--ssl* is
provided, an SSL connection will be attempted.


.. _command-reconnect:

reconnect [<network>] [<quit message>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disconnects and then reconnects to *<network>*. If no network is given,
disconnects and then reconnects to the network the command was given
on. If no quit message is given, uses the configured one
(supybot.plugins.Owner.quitMsg) or the nick of the person giving the
command.


.. _command-networks:

networks
^^^^^^^^

Returns the networks to which the bot is currently connected.


.. _command-latency:

latency [<network>]
^^^^^^^^^^^^^^^^^^^

Returns the current latency to *<network>*. *<network>* is only necessary
if the message isn't sent on the network to which this command is to
apply.


.. _command-disconnect:

disconnect [<network>] [<quit message>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disconnects from the network represented by the network *<network>*.
If *<quit message>* is given, quits the network with the given quit
message. *<network>* is only necessary if the network is different
from the network the command is sent on.


.. _command-whois:

whois [<network>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^

Returns the WHOIS response *<network>* gives for *<nick>*. *<network>* is
only necessary if the network is different than the network the command
is sent on.


.. _command-command:

command <network> <command> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives the bot *<command>* (with its associated *<arg>*s) on *<network>*.


