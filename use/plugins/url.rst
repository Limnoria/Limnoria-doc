
.. _plugin-url:

The URL plugin
==============

Commands
--------

.. _command-url-stats:

url stats [<channel>]
^^^^^^^^^^^^^^^^^^^^^

Returns the number of URLs in the URL database. *<channel>* is only
required if the message isn't sent in the channel itself.

.. _command-url-last:

url last [<channel>] [--{from,with,without,near,proto} <value>] [--nolimit]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives the last URL matching the given criteria. *--from* is from whom
the URL came; *--proto* is the protocol the URL used; *--with* is something
inside the URL; *--without* is something that should not be in the URL;
*--near* is something in the same message as the URL; If *--nolimit* is
given, returns all the URLs that are found. to just the URL.
*<channel>* is only necessary if the message isn't sent in the channel
itself.



.. _plugin-url-config:

Configuration
-------------

.. _supybot.plugins.URL.nonSnarfingRegexp:

supybot.plugins.URL.nonSnarfingRegexp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: None

Determines what URLs are not to be snarfed and stored in the database for the channel; URLs matching the given regexp will not be snarfed. Give the empty string if you have no URLs that you'd like to exclude from being snarfed.

.. _supybot.plugins.URL.public:

supybot.plugins.URL.public
^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

