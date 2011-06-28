
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

