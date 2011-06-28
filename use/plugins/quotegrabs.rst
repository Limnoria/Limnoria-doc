
.. _plugin-quotegrabs:

The QuoteGrabs plugin
=====================

.. _command-ungrab:

ungrab [<channel>] <number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the grab *<number>* (the last by default) on *<channel>*.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. _command-get:

get [<channel>] <id>
^^^^^^^^^^^^^^^^^^^^

Return the quotegrab with the given *<id>*. *<channel>* is only necessary
if the message isn't sent in the channel itself.


.. _command-quote:

quote [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<nick>*'s latest quote grab in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. _command-random:

random [<channel>] [<nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a randomly grabbed quote, optionally choosing only from those
quotes grabbed for *<nick>*. *<channel>* is only necessary if the message
isn't sent in the channel itself.


.. _command-list:

list [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^

Returns a list of shortened quotes that have been grabbed for *<nick>*
as well as the id of each quote. These ids can be used to get the
full quote. *<channel>* is only necessary if the message isn't sent in
the channel itself.


.. _command-search:

search [<channel>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^

Searches for *<text>* in a quote. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. _command-grab:

grab [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^

Grabs a quote from *<channel>* by *<nick>* for the quotegrabs table.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


