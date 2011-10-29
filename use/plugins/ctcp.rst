
.. _plugin-ctcp:

The Ctcp plugin
===============

Command
-------

.. _command-ctcp-version:

ctcp version [<channel>] [--nicks]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a CTCP VERSION to *<channel>*, returning the various
version strings returned. It waits for 10 seconds before returning
the versions received at that point. If *--nicks* is given, nicks are
associated with the version strings; otherwise, only the version
strings are given.



.. _plugin-ctcp-config:

Configuration
-------------

.. _supybot.plugins.Ctcp.public:

supybot.plugins.Ctcp.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.Ctcp.versionWait:

supybot.plugins.Ctcp.versionWait
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 10

Determines how many seconds the bot will wait after getting a version command (not a CTCP VERSION, but an actual call of the command in this plugin named "version") before replying with the results it has collected.

