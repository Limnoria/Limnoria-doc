
.. _plugin-web:

The Web plugin
==============

HTTP
----

.. _command-web-urlunquote:

web urlunquote <text>
^^^^^^^^^^^^^^^^^^^^^

Returns the text un-URL quoted.

.. _command-web-urlquote:

web urlquote <text>
^^^^^^^^^^^^^^^^^^^

Returns the URL quoted form of the text.

.. _command-web-size:

web size <url>
^^^^^^^^^^^^^^

Returns the Content-Length header of *<url>*. Only HTTP urls are valid,
of course.

HTML
----

.. _command-web-title:

web title <url>
^^^^^^^^^^^^^^^

Returns the HTML *<title>*...*</title>* of a URL.

.. _command-web-doctype:

web doctype <url>
^^^^^^^^^^^^^^^^^

Returns the DOCTYPE string of *<url>*. Only HTTP urls are valid, of
course.

.. _command-web-headers:

web headers <url>
^^^^^^^^^^^^^^^^^

Returns the HTTP headers of *<url>*. Only HTTP urls are valid, of
course.

Others
------

.. _command-web-netcraft:

web netcraft <hostname|ip>
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns Netcraft.com's determination of what operating system and
webserver is running on the host given.

.. _command-web-fetch:

web fetch <url>
^^^^^^^^^^^^^^^

Returns the contents of *<url>*, or as much as is configured in
:ref:`supybot.plugins.Web.fetch.maximum.` If that configuration variable is
set to 0, this command will be effectively disabled.



.. _plugin-web-config:

Configuration
-------------

.. _supybot.plugins.Web.nonSnarfingRegexp:

supybot.plugins.Web.nonSnarfingRegexp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: None

Determines what URLs are to be snarfed and stored in the database in the channel; URLs matching the regexp given will not be snarfed. Give the empty string if you have no URLs that you'd like to exclude from being snarfed.

.. _supybot.plugins.Web.titleSnarfer:

supybot.plugins.Web.titleSnarfer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will output the HTML title of URLs it sees in the channel.

.. _supybot.plugins.Web.fetch:

supybot.plugins.Web.fetch
^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Web.fetch.maximum:

supybot.plugins.Web.fetch.maximum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 0

Determines the maximum number of bytes the bot will download via the 'fetch' command in this plugin.

.. _supybot.plugins.Web.public:

supybot.plugins.Web.public
^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

