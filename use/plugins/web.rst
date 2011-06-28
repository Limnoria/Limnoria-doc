
.. _plugin-web:

The Web plugin
==============

.. command-urlunquote:

urlunquote <text>
^^^^^^^^^^^^^^^^^

Returns the text un-URL quoted.


.. command-netcraft:

netcraft <hostname|ip>
^^^^^^^^^^^^^^^^^^^^^^

Returns Netcraft.com's determination of what operating system and
webserver is running on the host given.


.. command-urlquote:

urlquote <text>
^^^^^^^^^^^^^^^

Returns the URL quoted form of the text.


.. command-size:

size <url>
^^^^^^^^^^

Returns the Content-Length header of *<url>*. Only HTTP urls are valid,
of course.


.. command-title:

title <url>
^^^^^^^^^^^

Returns the HTML *<title>*...*</title>* of a URL.


.. command-doctype:

doctype <url>
^^^^^^^^^^^^^

Returns the DOCTYPE string of *<url>*. Only HTTP urls are valid, of
course.


.. command-headers:

headers <url>
^^^^^^^^^^^^^

Returns the HTTP headers of *<url>*. Only HTTP urls are valid, of
course.


.. command-fetch:

fetch <url>
^^^^^^^^^^^

Returns the contents of *<url>*, or as much as is configured in
supybot.plugins.Web.fetch.maximum. If that configuration variable is
set to 0, this command will be effectively disabled.


