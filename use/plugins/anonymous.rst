
.. _plugin-anonymous:

The Anonymous plugin
====================

.. _command-do:

do <channel> <action>
^^^^^^^^^^^^^^^^^^^^^

Performs *<action>* in *<channel>*.


.. _command-say:

say <channel|nick> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^

Sends *<text>* to *<channel|nick>*. Can only send to *<nick>* if
supybot.plugins.Anonymous.allowPrivateTarget is True.


