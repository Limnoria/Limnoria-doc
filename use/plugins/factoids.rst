
.. _plugin-factoids:

The Factoids plugin
===================

Reading factoids
----------------

.. _command-factoids-info:

factoids info [<channel>] <key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives information about the factoid(s) associated with *<key>*.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-factoids-random:

factoids random [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a random factoid from the database for *<channel>*. *<channel>*
is only necessary if the message isn't sent in the channel itself.

.. _command-factoids-search:

factoids search [<channel>] [--values] [--{regexp} <value>] [<glob> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches the keyspace for keys matching *<glob>*. If *--regexp* is given,
it associated value is taken as a regexp and matched against the keys.
If *--values* is given, search the value space instead of the keyspace.

.. _command-factoids-whatis:

factoids whatis [<channel>] [--raw] <key> [<number>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Looks up the value of *<key>* in the factoid database. If given a
number, will return only that exact factoid. If '*--raw'* option is
given, no variable substitution will take place on the factoid.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-factoids-rank:

factoids rank [<channel>] [--plain] [--alpha] [<number>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a list of top-ranked factoid keys, sorted by usage count
(rank). If *<number>* is not provided, the default number of factoid keys
returned is set by the rankListLength registry value.

If *--plain* option is given, rank numbers and usage counts are not
included in output.

If *--alpha* option is given in addition to *--plain,* keys are sorted
alphabetically, instead of by rank.

*<channel>* is only necessary if the message isn't sent in the channel
itself.

Administration
--------------

.. _command-factoids-learn:

factoids learn [<channel>] <key> WORD <value>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Associates *<key>* with *<value>*.  *<channel>* is only
necessary if the message isn't sent on the channel
itself.  The WORD (defined in :ref:`supybot.plugins.Factoids.learnSeparator`)
is necessary to separate the
key from the value.  It can be changed to another word
via the :ref:`supybot.plugins.Factoids.learnSeparator` registry value.

.. _command-factoids-forget:

factoids forget [<channel>] <key> [<number>|*]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a key-fact relationship for key *<key>* from the factoids
database. If there is more than one such relationship for this key,
a number is necessary to determine which one should be removed.
A * can be used to remove all relationships for *<key>*.

If as a result, the key (factoid) remains without any relationships to
a factoid (key), it shall be removed from the database.

*<channel>* is only necessary if
the message isn't sent in the channel itself.

.. _command-factoids-unlock:

factoids unlock [<channel>] <key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlocks the factoid(s) associated with *<key>* so that they can be
removed or added to. *<channel>* is only necessary if the message isn't
sent in the channel itself.

.. _command-factoids-alias:

factoids alias [<channel>] <oldkey> <newkey> [<number>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a new key *<newkey>* for factoid associated with *<oldkey>*.
*<number>* is only necessary if there's more than one factoid associated
with *<oldkey>*.

The same action can be accomplished by using the 'learn' function with
a new key but an existing (verbatim) factoid content.

.. _command-factoids-change:

factoids change [<channel>] <key> <number> <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the factoid #*<number>* associated with *<key>* according to
*<regexp>*.

.. _command-factoids-lock:

factoids lock [<channel>] <key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Locks the factoid(s) associated with *<key>* so that they cannot be
removed or added to. *<channel>* is only necessary if the message isn't
sent in the channel itself.



.. _plugin-factoids-config:

Configuration
-------------

.. _supybot.plugins.Factoids.format:

supybot.plugins.Factoids.format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: $key could be $value.

Determines the format of the response given when a factoid's value is requested. All the standard substitutes apply, in addition to "$key" for the factoid's key and "$value" for the factoid's value.

.. _supybot.plugins.Factoids.keepRankInfo:

supybot.plugins.Factoids.keepRankInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether we keep updating the usage count for each factoid, for popularity ranking.

.. _supybot.plugins.Factoids.learnSeparator:

supybot.plugins.Factoids.learnSeparator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: as

Determines what separator must be used in the learn command. Defaults to 'as' -- learn <key> as <value>. Users might feel more comfortable with 'is' or something else, so it's configurable.

.. _supybot.plugins.Factoids.rankListLength:

supybot.plugins.Factoids.rankListLength
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 20

Determines the number of factoid keys returned by the factrank command.

.. _supybot.plugins.Factoids.replyApproximateSearchKeys:

supybot.plugins.Factoids.replyApproximateSearchKeys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

If you try to look up a nonexistent factoid, this setting make the bot try to find some possible matching keys through several approximate matching algorithms and return a list of matching keys, before giving up.

.. _supybot.plugins.Factoids.replyWhenInvalidCommand:

supybot.plugins.Factoids.replyWhenInvalidCommand
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will reply to invalid commands by searching for a factoid; basically making the whatis unnecessary when you want all factoids for a given key.

.. _supybot.plugins.Factoids.showFactoidIfOnlyOneMatch:

supybot.plugins.Factoids.showFactoidIfOnlyOneMatch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will reply with the single matching factoid if only one factoid matches when using the search command.

.. _supybot.plugins.Factoids.public:

supybot.plugins.Factoids.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

