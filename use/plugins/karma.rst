
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


.. _plugin-karma-config:

Configuration
-------------

.. _supybot.plugins.Karma.allowSelfRating:

supybot.plugins.Karma.allowSelfRating
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether users can adjust the karma of their nick.

.. _supybot.plugins.Karma.allowUnaddressedKarma:

supybot.plugins.Karma.allowUnaddressedKarma
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will increase/decrease karma without being addressed.

.. _supybot.plugins.Karma.mostDisplay:

supybot.plugins.Karma.mostDisplay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 25

Determines how many karma things are shown when the most command is called.

.. _supybot.plugins.Karma.rankingDisplay:

supybot.plugins.Karma.rankingDisplay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 3

Determines how many highest/lowest karma things are shown when karma is called with no arguments.

.. _supybot.plugins.Karma.response:

supybot.plugins.Karma.response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will reply with a success message when something's karma is increased or decreased.

.. _supybot.plugins.Karma.simpleOutput:

supybot.plugins.Karma.simpleOutput
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will output shorter versions of the karma output when requesting a single thing's karma.

.. _supybot.plugins.Karma.public:

supybot.plugins.Karma.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

