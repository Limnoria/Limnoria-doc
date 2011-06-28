
.. _plugin-moobotfactoids:

The MoobotFactoids plugin
=========================

.. _command-lock:

lock [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Locks the factoid with the given factoid key. Requires that the user
be registered and have created the factoid originally. *<channel>* is
only necessary if the message isn't sent in the channel itself.


.. _command-listauth:

listauth [<channel>] <author name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the keys of the factoids with the given author. Note that if an
author has an integer name, you'll have to use that author's id to use
this function (so don't use integer usernames!). *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. _command-random:

random [<channel>]
^^^^^^^^^^^^^^^^^^

Displays a random factoid (along with its key) from the database.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. _command-unlock:

unlock [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlocks the factoid with the given factoid key. Requires that the
user be registered and have locked the factoid. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. _command-literal:

literal [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the literal factoid for the given factoid key. No parsing of
the factoid value is done as it is with normal retrieval. *<channel>*
is only necessary if the message isn't sent in the channel itself.


.. _command-listvalues:

listvalues [<channel>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the keys of the factoids whose value contains the provided text.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. _command-reset:

reset 
^^^^^^



.. _command-factinfo:

factinfo [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the various bits of info on the factoid for the given key.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. _command-most:

most [<channel>] {popular|authored|recent}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the most {popular|authored|recent} factoids. "popular" lists the
most frequently requested factoids. "authored" lists the author with
the most factoids. "recent" lists the most recently created factoids.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. _command-die:

die 
^^^^



.. _command-remove:

remove [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletes the factoid with the given key. *<channel>* is only necessary
if the message isn't sent in the channel itself.


.. _command-listkeys:

listkeys [<channel>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the keys of the factoids whose key contains the provided text.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


