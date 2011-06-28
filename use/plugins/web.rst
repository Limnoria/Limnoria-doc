
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

