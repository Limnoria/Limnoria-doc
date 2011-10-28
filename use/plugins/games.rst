
.. _plugin-games:

The Games plugin
================

Random
------

.. _command-games-dice:

games dice <dice>d<sides>
^^^^^^^^^^^^^^^^^^^^^^^^^

Rolls a die with *<sides>* number of sides *<dice>* times.
For example, 2d6 will roll 2 six-sided dice; 10d10 will roll 10
ten-sided dice.

.. _command-games-roulette:

games roulette [spin]
^^^^^^^^^^^^^^^^^^^^^

Fires the revolver. If the bullet was in the chamber, you're dead.
Tell me to spin the chambers and I will.

.. _command-games-eightball:

games eightball [<question>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ask a question and the answer shall be provided.

.. _command-games-coin:

games coin
^^^^^^^^^^

Flips a coin and returns the result.

Miscellaneous
-------------

.. _command-games-monologue:

games monologue [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of consecutive lines you've sent in *<channel>*
without being interrupted by someone else (i.e. how long your current
'monologue' is). *<channel>* is only necessary if the message isn't sent
in the channel itself.


.. _plugin-games-config:

Configuration
-------------

.. _supybot.plugins.Games.public:

supybot.plugins.Games.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

