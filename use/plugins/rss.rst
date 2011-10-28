
.. _plugin-rss:

The RSS plugin
==============

Reading
-------

.. _command-rss-info:

rss info <url|feed>
^^^^^^^^^^^^^^^^^^^

Returns information from the given RSS feed, namely the title,
URL, description, and last update date, if available.

.. _command-rss-announce-list:

rss announce list [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the list of feeds announced in *<channel>*. *<channel>* is
only necessary if the message isn't sent in the channel itself.

.. _command-rss-rss:

rss rss <url> [<number of headlines>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the title components of the given RSS feed.
If *<number of headlines>* is given, return only that many headlines.

Administration
--------------

.. _command-rss-remove:

rss remove <name>
^^^^^^^^^^^^^^^^^

Removes the command for looking up RSS feeds at *<name>* from
this plugin.

.. _command-rss-add:

rss add <name> <url>
^^^^^^^^^^^^^^^^^^^^

Adds a command to this plugin that will look up the RSS feed at the
given URL.

.. _command-rss-announce-remove:

rss announce remove [<channel>] <name|url> [<name|url> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the list of feeds from the current list of announced feeds
in *<channel>*. Valid feeds include the names of registered feeds as
well as URLs for RSS feeds. *<channel>* is only necessary if the
message isn't sent in the channel itself.

.. _command-rss-announce-add:

rss announce add [<channel>] <name|url> [<name|url> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds the list of feeds to the current list of announced feeds in
*<channel>*. Valid feeds include the names of registered feeds as
well as URLs for RSS feeds. *<channel>* is only necessary if the
message isn't sent in the channel itself.



.. _plugin-rss-config:

Configuration
-------------

.. _supybot.plugins.RSS.announcementPrefix:

supybot.plugins.RSS.announcementPrefix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: New news from 

Determines what prefix is prepended (if any) to the new news item announcements made in the channel.

.. _supybot.plugins.RSS.bold:

supybot.plugins.RSS.bold
^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will bold the title of the feed when it announces new news.

.. _supybot.plugins.RSS.headlineSeparator:

supybot.plugins.RSS.headlineSeparator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value:  || 

Determines what string is used to separate headlines in new feeds.

.. _supybot.plugins.RSS.initialAnnounceHeadlines:

supybot.plugins.RSS.initialAnnounceHeadlines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 5

Indicates how many headlines an rss feed will output when it is first added to announce for a channel.

.. _supybot.plugins.RSS.keywordBlacklist:

supybot.plugins.RSS.keywordBlacklist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Space separated list of strings, lets you filter headlines to those not containing any items in this blacklist.

.. _supybot.plugins.RSS.keywordWhitelist:

supybot.plugins.RSS.keywordWhitelist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Space separated list of strings, lets you filter headlines to those containing one or more items in this whitelist.

.. _supybot.plugins.RSS.showLinks:

supybot.plugins.RSS.showLinks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will list the link along with the title of the feed when the rss command is called. supybot.plugins.RSS.announce.showLinks affects whether links will be listed when a feed is automatically announced.

.. _supybot.plugins.RSS.announce:

supybot.plugins.RSS.announce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Determines which RSS feeds should be announced in the channel; valid input is a list of strings (either registered RSS feeds or RSS feed URLs) separated by spaces.

.. _supybot.plugins.RSS.announce.showLinks:

supybot.plugins.RSS.announce.showLinks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will list the link along with the title of the feed when a feed is automatically announced.

.. _supybot.plugins.RSS.defaultNumberOfHeadlines:

supybot.plugins.RSS.defaultNumberOfHeadlines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 1

Indicates how many headlines an rss feed will output by default, if no number is provided.

.. _supybot.plugins.RSS.feeds:

supybot.plugins.RSS.feeds
^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Determines what feeds should be accessible as commands.

.. _supybot.plugins.RSS.public:

supybot.plugins.RSS.public
^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.RSS.waitPeriod:

supybot.plugins.RSS.waitPeriod
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 1800

Indicates how many seconds the bot will wait between retrieving RSS feeds; requests made within this period will return cached results.

