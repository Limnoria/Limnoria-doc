
.. _plugin-moobotfactoids:

The MoobotFactoids plugin
=========================

Reading factoids
----------------

.. _command-moobotfactoids-listauth:

moobotfactoids listauth [<channel>] <author name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the keys of the factoids with the given author. Note that if an
author has an integer name, you'll have to use that author's id to use
this function (so don't use integer usernames!). *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-moobotfactoids-random:

moobotfactoids random [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Displays a random factoid (along with its key) from the database.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-moobotfactoids-literal:

moobotfactoids literal [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the literal factoid for the given factoid key. No parsing of
the factoid value is done as it is with normal retrieval. *<channel>*
is only necessary if the message isn't sent in the channel itself.

.. _command-moobotfactoids-listvalues:

moobotfactoids listvalues [<channel>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the keys of the factoids whose value contains the provided text.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-moobotfactoids-factinfo:

moobotfactoids factinfo [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the various bits of info on the factoid for the given key.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-moobotfactoids-most:

moobotfactoids most [<channel>] {popular|authored|recent}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the most *{popular|authored|recent}* factoids. "popular" lists the
most frequently requested factoids. "authored" lists the author with
the most factoids. "recent" lists the most recently created factoids.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-moobotfactoids-listkeys:

moobotfactoids listkeys [<channel>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the keys of the factoids whose key contains the provided text.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

Administration
--------------

.. _command-moobotfactoids-lock:

moobotfactoids lock [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Locks the factoid with the given factoid key. Requires that the user
be registered and have created the factoid originally. *<channel>* is
only necessary if the message isn't sent in the channel itself.

.. _command-moobotfactoids-unlock:

moobotfactoids unlock [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlocks the factoid with the given factoid key. Requires that the
user be registered and have locked the factoid. *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-moobotfactoids-remove:

moobotfactoids remove [<channel>] <factoid key>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletes the factoid with the given key. *<channel>* is only necessary
if the message isn't sent in the channel itself.



.. _plugin-moobotfactoids-config:

Configuration
-------------

.. _supybot.plugins.MoobotFactoids.mostCount:

supybot.plugins.MoobotFactoids.mostCount
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 10

Determines how many items are shown when the 'most' command is called.

.. _supybot.plugins.MoobotFactoids.showFactoidIfOnlyOneMatch:

supybot.plugins.MoobotFactoids.showFactoidIfOnlyOneMatch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether or not the factoid value will be shown when a listkeys search returns only one factoid key.

.. _supybot.plugins.MoobotFactoids.public:

supybot.plugins.MoobotFactoids.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

