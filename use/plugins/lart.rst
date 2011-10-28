
.. _plugin-lart:

The Lart plugin
===============

.. _command-lart-lart:

lart lart [<channel>] [<id>] <who|what> [for <reason>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Uses the Luser Attitude Readjustment Tool on *<who|what>* (for *<reason>*,
if given). If *<id>* is given, uses that specific lart. *<channel>* is
only necessary if the message isn't sent in the channel itself.



.. _plugin-lart-config:

Configuration
-------------

.. _supybot.plugins.Lart.showIds:

supybot.plugins.Lart.showIds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will show the ids of a lart when the lart is given.

.. _supybot.plugins.Lart.public:

supybot.plugins.Lart.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

