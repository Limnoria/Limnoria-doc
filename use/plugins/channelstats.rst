
.. _plugin-channelstats:

The ChannelStats plugin
=======================

.. _command-channelstats-stats:

channelstats stats [<channel>] [<name>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the statistics for *<name>* on *<channel>*. *<channel>* is only
necessary if the message isn't sent on the channel itself. If *<name>*
isn't given, it defaults to the user sending the command.

.. _command-channelstats-rank:

channelstats rank [<channel>] <stat expression>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the ranking of users according to the given stat expression.
Valid variables in the stat expression include 'msgs', 'chars',
'words', 'smileys', 'frowns', 'actions', 'joins', 'parts', 'quits',
'kicks', 'kicked', 'topics', and 'modes'. Any simple mathematical
expression involving those variables is permitted.

.. _command-channelstats-channelstats:

channelstats channelstats [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the statistics for *<channel>*. *<channel>* is only necessary if
the message isn't sent on the channel itself.

