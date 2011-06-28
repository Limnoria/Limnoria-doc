
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

