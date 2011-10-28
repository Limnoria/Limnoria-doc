
.. _plugin-anonymous:

The Anonymous plugin
====================

.. _command-channel-do:

do <channel> <action>
^^^^^^^^^^^^^^^^^^^^^

Performs *<action>* in *<channel>*.

.. _command-channel-say:

say <channel|nick> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^

Sends *<text>* to *<channel|nick>*. Can only send to *<nick>* if
:ref:`supybot.plugins.Anonymous.allowPrivateTarget` is True.



.. _plugin-anonymous-config:

Configuration
-------------

.. _supybot.plugins.Anonymous.requirePresenceInChannel:

supybot.plugins.Anonymous.requirePresenceInChannel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot should require people trying to use this plugin to be in the channel they wish to anonymously send to.

.. _supybot.plugins.Anonymous.allowPrivateTarget:

supybot.plugins.Anonymous.allowPrivateTarget
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will require targets of the "say" command to be public (i.e., channels). If this is True, the bot will allow people to use the "say" command to send private messages to other users.

.. _supybot.plugins.Anonymous.public:

supybot.plugins.Anonymous.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.Anonymous.requireCapability:

supybot.plugins.Anonymous.requireCapability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines what capability (if any) the bot should require people trying to use this plugin to have.

.. _supybot.plugins.Anonymous.requireRegistration:

supybot.plugins.Anonymous.requireRegistration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot should require people trying to use this plugin to be registered.

