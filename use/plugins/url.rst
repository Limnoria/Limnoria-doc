
.. _plugin-url:

The URL plugin
==============

.. _command-stats:

stats [<channel>]
^^^^^^^^^^^^^^^^^

Returns the number of URLs in the URL database. *<channel>* is only
required if the message isn't sent in the channel itself.


.. _command-last:

last [<channel>] [--{from,with,without,near,proto} <value>] [--nolimit]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives the last URL matching the given criteria. *--from* is from whom
the URL came; *--proto* is the protocol the URL used; *--with* is something
inside the URL; *--without* is something that should not be in the URL;
*--near* is something in the same message as the URL; If *--nolimit* is
given, returns all the URLs that are found. to just the URL.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


