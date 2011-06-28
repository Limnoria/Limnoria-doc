
.. _plugin-quotegrabs:

The QuoteGrabs plugin
=====================

Getting quotes
--------------

.. _command-quotegrabs-get:

quotegrabs get [<channel>] <id>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return the quotegrab with the given *<id>*. *<channel>* is only necessary
if the message isn't sent in the channel itself.

.. _command-quotegrabs-quote:

quotegrabs quote [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<nick>*'s latest quote grab in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-quotegrabs-random:

quotegrabs random [<channel>] [<nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a randomly grabbed quote, optionally choosing only from those
quotes grabbed for *<nick>*. *<channel>* is only necessary if the message
isn't sent in the channel itself.

.. _command-quotegrabs-list:

quotegrabs list [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a list of shortened quotes that have been grabbed for *<nick>*
as well as the id of each quote. These ids can be used to get the
full quote. *<channel>* is only necessary if the message isn't sent in
the channel itself.

.. _command-quotegrabs-search:

quotegrabs search [<channel>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches for *<text>* in a quote. *<channel>* is only necessary if the
message isn't sent in the channel itself.

(Un)quoting
-----------

.. _command-quotegrabs-ungrab:

quotegrabs ungrab [<channel>] <number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the grab *<number>* (the last by default) on *<channel>*.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-quotegrabs-grab:

quotegrabs grab [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Grabs a quote from *<channel>* by *<nick>* for the quotegrabs table.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

