
.. _plugin-automode:

The AutoMode plugin
===================

This plugins enables your bot to automatically voice, halfop, and op people on
your channel, according to their capabilities.

Owners
------

Owners are always opped unless you set :ref:`supybot.plugins.AutoMode.owner`
to False.
With stock Supybot and Gribble, setting this to False will cause no automode
at all for owners. In Limnoria, settings this to False will make automode
work as for normal users (only channel capabilities count).


.. _plugin-automode-config:

Configuration
-------------

.. _supybot.plugins.AutoMode.enable:

supybot.plugins.AutoMode.enable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is enabled.

.. _supybot.plugins.AutoMode.fallthrough:

supybot.plugins.AutoMode.fallthrough
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will "fall through" to halfop/voicing when auto-opping is turned off but auto-halfopping/voicing are turned on.

.. _supybot.plugins.AutoMode.halfop:

supybot.plugins.AutoMode.halfop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will automatically halfop people with the <channel>,halfop capability when they join the channel.

.. _supybot.plugins.AutoMode.op:

supybot.plugins.AutoMode.op
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will automatically op people with the <channel>,op capability when they join the channel.

.. _supybot.plugins.AutoMode.voice:

supybot.plugins.AutoMode.voice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will automatically voice people with the <channel>,voice capability when they join the channel.

.. _supybot.plugins.AutoMode.ban:

supybot.plugins.AutoMode.ban
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will automatically ban people who join the channel and are on the banlist.

.. _supybot.plugins.AutoMode.ban.period:

supybot.plugins.AutoMode.ban.period
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 86400

Determines how many seconds the bot will automatically ban a person when banning.

.. _supybot.plugins.AutoMode.owner:

supybot.plugins.AutoMode.owner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin will automode owners even if they don't have op/halfop/voice/whatever capability.

.. _supybot.plugins.AutoMode.public:

supybot.plugins.AutoMode.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

