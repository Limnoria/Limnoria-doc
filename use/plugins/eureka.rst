
.. _plugin-eureka:

The Eureka plugin
=================

.. _command-eureka-adjust:

eureka adjust [<channel>] <nick> <number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Increase or decrease the score of *<nick>* on the *<channel>*.
If *<channel>* is not given, it defaults to the current channel.

.. _command-eureka-resume:

eureka resume [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^

Resume the Eureka on the given *<channel>*. If *<channel>* is not given,
it defaults to the current channel.

.. _command-eureka-skip:

eureka skip [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^

Give up with this question, and switch to the next one.

.. _command-eureka-stop:

eureka stop [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^

Stop the Eureka on the given *<channel>*. If *<channel>* is not given,
it defaults to the current channel.

.. _command-eureka-clue:

eureka clue [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^

Give the next clue.

.. _command-eureka-scores:

eureka scores [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^

Return the scores on the *<channel>*. If *<channel>* is not given, it
defaults to the current channel.

.. _command-eureka-pause:

eureka pause [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^

Pause the Eureka on the given *<channel>*. If *<channel>* is not given,
it defaults to the current channel.

.. _command-eureka-start:

eureka start [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^

Start the Eureka on the given *<channel>*. If *<channel>* is not given,
it defaults to the current channel.

.. _command-eureka-score:

eureka score [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return the score of *<nick>* on the *<channel>*. If *<channel>* is not
given, it defaults to the current channel.



.. _plugin-eureka-config:

Configuration
-------------

.. _supybot.plugins.Eureka.format:

supybot.plugins.Eureka.format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Eureka.format.score:

supybot.plugins.Eureka.format.score
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: $nick ($score)

Determines the format used by the bot to display the score of a user.

.. _supybot.plugins.Eureka.format.separator:

supybot.plugins.Eureka.format.separator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value:  // 

Determines the string between two user scores.

.. _supybot.plugins.Eureka.public:

supybot.plugins.Eureka.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

