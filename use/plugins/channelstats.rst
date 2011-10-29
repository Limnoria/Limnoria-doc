
.. _plugin-channelstats:

The ChannelStats plugin
=======================

Commands
--------

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



.. _plugin-channelstats-config:

Configuration
-------------

.. _supybot.plugins.ChannelStats.frowns:

supybot.plugins.ChannelStats.frowns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: [':\|', ':-/', ':-\\', ':\\', ':/', ':(', ':-(', ":'("]

Determines what words (i.e., pieces of text with no spaces in them ) are considered 'frowns' for the purposes of stats-keeping.

.. _supybot.plugins.ChannelStats.selfStats:

supybot.plugins.ChannelStats.selfStats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will keep channel statistics on itself, possibly skewing the channel stats (especially in cases where the bot is relaying between channels on a network).

.. _supybot.plugins.ChannelStats.smileys:

supybot.plugins.ChannelStats.smileys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: [':)', ';)', ';]', ':-)', ':-D', ':D', ':P', ':p', '(=', '=)']

Determines what words (i.e., pieces of text with no spaces in them) are considered 'smileys' for the purposes of stats-keeping.

.. _supybot.plugins.ChannelStats.public:

supybot.plugins.ChannelStats.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

