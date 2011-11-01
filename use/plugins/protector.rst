
.. _plugin-protector:

The Protector plugin
====================

Enforces channel capabilities (op/voice).


.. _plugin-protector-config:

Configuration
-------------

.. _supybot.plugins.Protector.enable:

supybot.plugins.Protector.enable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is enabled in a given channel.

.. _supybot.plugins.Protector.immune:

supybot.plugins.Protector.immune
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Determines what nicks the bot will consider to be immune from enforcement. These nicks will not even have their actions watched by this plugin. In general, only the ChanServ for this network will be in this list.

.. _supybot.plugins.Protector.public:

supybot.plugins.Protector.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

