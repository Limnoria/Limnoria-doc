
.. _plugin-news:

The News plugin
===============

.. command-old:

old [<channel>] [<id>]
^^^^^^^^^^^^^^^^^^^^^^

Returns the old news item for *<channel>* with *<id>*. If no number is
given, returns all the old news items in reverse order. *<channel>* is
only necessary if the message isn't sent in the channel itself.


.. command-die:

die 
^^^^



.. command-remove:

remove [<channel>] <id>
^^^^^^^^^^^^^^^^^^^^^^^

Removes the news item with *<id>* from *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-add:

add [<channel>] <expires> <subject>: <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a given news item of *<text>* to a channel with the given *<subject>*.
If *<expires>* isn't 0, that news item will expire *<expires>* seconds from
now. *<channel>* is only necessary if the message isn't sent in the
channel itself.


.. command-news:

news [<channel>] [<id>]
^^^^^^^^^^^^^^^^^^^^^^^

Display the news items for *<channel>* in the format of '(#id) subject'.
If *<id>* is given, retrieve only that news item; otherwise retrieve all
news items. *<channel>* is only necessary if the message isn't sent in
the channel itself.


.. command-change:

change [<channel>] <id> <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the news item with *<id>* from *<channel>* according to the
regular expression *<regexp>*. *<regexp>* should be of the form
s/text/replacement/flags. *<channel>* is only necessary if the message
isn't sent on the channel itself.


