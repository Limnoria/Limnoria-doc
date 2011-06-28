
.. _plugin-factoids:

The Factoids plugin
===================

.. command-info:

info [<channel>] <key>
^^^^^^^^^^^^^^^^^^^^^^

Gives information about the factoid(s) associated with *<key>*.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-learn:

learn 
^^^^^^



.. command-forget:

forget [<channel>] <key> [<number>|*]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a key-fact relationship for key *<key>* from the factoids
database. If there is more than one such relationship for this key,
a number is necessary to determine which one should be removed.
A * can be used to remove all relationships for *<key>*.

If as a result, the key (factoid) remains without any relationships to
a factoid (key), it shall be removed from the database.

*<channel>* is only necessary if
the message isn't sent in the channel itself.


.. command-random:

random [<channel>]
^^^^^^^^^^^^^^^^^^

Returns a random factoid from the database for *<channel>*. *<channel>*
is only necessary if the message isn't sent in the channel itself.


.. command-rank:

rank [<channel>] [--plain] [--alpha] [<number>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a list of top-ranked factoid keys, sorted by usage count
(rank). If *<number>* is not provided, the default number of factoid keys
returned is set by the rankListLength registry value.

If *--plain* option is given, rank numbers and usage counts are not
included in output.

If *--alpha* option is given in addition to *--plain,* keys are sorted
alphabetically, instead of by rank.

*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-unlock:

unlock [<channel>] <key>
^^^^^^^^^^^^^^^^^^^^^^^^

Unlocks the factoid(s) associated with *<key>* so that they can be
removed or added to. *<channel>* is only necessary if the message isn't
sent in the channel itself.


.. command-search:

search [<channel>] [--values] [--{regexp} <value>] [<glob> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches the keyspace for keys matching *<glob>*. If *--regexp* is given,
it associated value is taken as a regexp and matched against the keys.
If *--values* is given, search the value space instead of the keyspace.


.. command-whatis:

whatis [<channel>] [--raw] <key> [<number>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Looks up the value of *<key>* in the factoid database. If given a
number, will return only that exact factoid. If '*--raw'* option is
given, no variable substitution will take place on the factoid.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-alias:

alias [<channel>] <oldkey> <newkey> [<number>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a new key *<newkey>* for factoid associated with *<oldkey>*.
*<number>* is only necessary if there's more than one factoid associated
with *<oldkey>*.

The same action can be accomplished by using the 'learn' function with
a new key but an existing (verbatim) factoid content.


.. command-change:

change [<channel>] <key> <number> <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the factoid #*<number>* associated with *<key>* according to
*<regexp>*.


.. command-lock:

lock [<channel>] <key>
^^^^^^^^^^^^^^^^^^^^^^

Locks the factoid(s) associated with *<key>* so that they cannot be
removed or added to. *<channel>* is only necessary if the message isn't
sent in the channel itself.


