
.. _plugin-karma:

The Karma plugin
================

Main commands
-------------

.. _command-karma-clear:

karma clear [<channel>] <name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resets the karma of *<name>* to 0.

.. _command-karma-most:

karma most [<channel>] {increased,decreased,active}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the most increased, the most decreased, or the most active
(the sum of increased and decreased) karma things. *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-karma-karma:

karma karma [<channel>] [<thing> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the karma of *<thing>*. If *<thing>* is not given, returns the top
N karmas, where N is determined by the config variable
:ref:`supybot.plugins.Karma.rankingDisplay.` If one *<thing>* is given, returns
the details of its karma; if more than one *<thing>* is given, returns
the total karma of each of the the things. *<channel>* is only necessary
if the message isn't sent on the channel itself.


Maintenance
-----------

.. _command-karma-load:

karma load [<channel>] <filename>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Loads the Karma database for *<channel>* from *<filename>* in the bot's
data directory. *<channel>* is only necessary if the message isn't sent
in the channel itself.

.. _command-karma-dump:

karma dump [<channel>] <filename>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dumps the Karma database for *<channel>* to *<filename>* in the bot's
data directory. *<channel>* is only necessary if the message isn't sent
in the channel itself.
