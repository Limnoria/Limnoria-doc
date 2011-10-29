
.. _plugin-attackprotector:

The AttackProtector plugin
==========================


.. include:: unofficial.inc


.. _plugin-attackprotector-config:

Configuration
-------------

.. _supybot.plugins.AttackProtector.groupjoin:

supybot.plugins.AttackProtector.groupjoin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.AttackProtector.groupjoin.detection:

supybot.plugins.AttackProtector.groupjoin.detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 20p10

In the format XpY, where X is the number of groupjoin per Y seconds that triggers the punishment.

.. _supybot.plugins.AttackProtector.groupjoin.punishment:

supybot.plugins.AttackProtector.groupjoin.punishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: mode+i

Determines the pushiment applyed when a groupjoin flood is detected.

.. _supybot.plugins.AttackProtector.groupmessage:

supybot.plugins.AttackProtector.groupmessage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.AttackProtector.groupmessage.detection:

supybot.plugins.AttackProtector.groupmessage.detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 100p10

In the format XpY, where X is the number of groupmessage per Y seconds that triggers the punishment.

.. _supybot.plugins.AttackProtector.groupmessage.punishment:

supybot.plugins.AttackProtector.groupmessage.punishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: mode+m

Determines the pushiment applyed when a groupmessage flood is detected.

.. _supybot.plugins.AttackProtector.groupnick:

supybot.plugins.AttackProtector.groupnick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.AttackProtector.groupnick.detection:

supybot.plugins.AttackProtector.groupnick.detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 20p10

In the format XpY, where X is the number of groupnick per Y seconds that triggers the punishment.

.. _supybot.plugins.AttackProtector.groupnick.punishment:

supybot.plugins.AttackProtector.groupnick.punishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: mode+N

Determines the pushiment applyed when a groupnick flood is detected.

.. _supybot.plugins.AttackProtector.grouppart:

supybot.plugins.AttackProtector.grouppart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.AttackProtector.grouppart.detection:

supybot.plugins.AttackProtector.grouppart.detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 20p10

In the format XpY, where X is the number of grouppart per Y seconds that triggers the punishment.

.. _supybot.plugins.AttackProtector.grouppart.punishment:

supybot.plugins.AttackProtector.grouppart.punishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: mode+i

Determines the pushiment applyed when a grouppart flood is detected.

.. _supybot.plugins.AttackProtector.join:

supybot.plugins.AttackProtector.join
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.AttackProtector.join.detection:

supybot.plugins.AttackProtector.join.detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 5p10

In the format XpY, where X is the number of join per Y seconds that triggers the punishment.

.. _supybot.plugins.AttackProtector.join.punishment:

supybot.plugins.AttackProtector.join.punishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: ban

Determines the pushiment applyed when a join flood is detected.

.. _supybot.plugins.AttackProtector.message:

supybot.plugins.AttackProtector.message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.AttackProtector.message.detection:

supybot.plugins.AttackProtector.message.detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 10p20

In the format XpY, where X is the number of message per Y seconds that triggers the punishment.

.. _supybot.plugins.AttackProtector.message.punishment:

supybot.plugins.AttackProtector.message.punishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: kick

Determines the pushiment applyed when a message flood is detected.

.. _supybot.plugins.AttackProtector.nick:

supybot.plugins.AttackProtector.nick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.AttackProtector.nick.detection:

supybot.plugins.AttackProtector.nick.detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 7p300

In the format XpY, where X is the number of nick per Y seconds that triggers the punishment.

.. _supybot.plugins.AttackProtector.nick.punishment:

supybot.plugins.AttackProtector.nick.punishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: ban

Determines the pushiment applyed when a nick flood is detected.

.. _supybot.plugins.AttackProtector.part:

supybot.plugins.AttackProtector.part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.AttackProtector.part.detection:

supybot.plugins.AttackProtector.part.detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 4p5

In the format XpY, where X is the number of part per Y seconds that triggers the punishment.

.. _supybot.plugins.AttackProtector.part.punishment:

supybot.plugins.AttackProtector.part.punishment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: ban

Determines the pushiment applyed when a part flood is detected.

.. _supybot.plugins.AttackProtector.delay:

supybot.plugins.AttackProtector.delay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 10

Determines how long (in seconds) the plugin will wait before being enabled. A too low value makes the bot believe that its incoming messages 'flood' on connection is an attack.

.. _supybot.plugins.AttackProtector.exempt:

supybot.plugins.AttackProtector.exempt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: nopunish

If a user has this capability, he won't be punished by AttackProtector

.. _supybot.plugins.AttackProtector.public:

supybot.plugins.AttackProtector.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

