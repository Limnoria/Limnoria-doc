
.. _plugin-praise:

The Praise plugin
=================

.. _command-praise-praise:

praise praise [<channel>] [<id>] <who|what> [for <reason>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Praises *<who|what>* (for *<reason>*, if given). If *<id>* is given, uses
that specific praise. *<channel>* is only necessary if the message isn't
sent in the channel itself.



.. _plugin-praise-config:

Configuration
-------------

.. _supybot.plugins.Praise.showIds:

supybot.plugins.Praise.showIds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will show the ids of a praise when the praise is given.

.. _supybot.plugins.Praise.public:

supybot.plugins.Praise.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

