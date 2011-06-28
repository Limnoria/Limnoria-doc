
.. _plugin-web:

The Web plugin
==============

.. _command-urlunquote:

urlunquote <text>
^^^^^^^^^^^^^^^^^

Returns the text un-URL quoted.


.. _command-netcraft:

netcraft <hostname|ip>
^^^^^^^^^^^^^^^^^^^^^^

Returns Netcraft.com's determination of what operating system and
webserver is running on the host given.


.. _command-urlquote:

urlquote <text>
^^^^^^^^^^^^^^^

Returns the URL quoted form of the text.


.. _command-size:

size <url>
^^^^^^^^^^

Returns the Content-Length header of *<url>*. Only HTTP urls are valid,
of course.


.. _command-title:

title <url>
^^^^^^^^^^^

Returns the HTML *<title>*...*</title>* of a URL.


.. _command-doctype:

doctype <url>
^^^^^^^^^^^^^

Returns the DOCTYPE string of *<url>*. Only HTTP urls are valid, of
course.


.. _command-headers:

headers <url>
^^^^^^^^^^^^^

Returns the HTTP headers of *<url>*. Only HTTP urls are valid, of
course.


.. _command-fetch:

fetch <url>
^^^^^^^^^^^

Returns the contents of *<url>*, or as much as is configured in
supybot.plugins.Web.fetch.maximum. If that configuration variable is
set to 0, this command will be effectively disabled.


