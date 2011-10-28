
.. _plugin-status:

The Status plugin
=================

.. _command-status-status:

status status
^^^^^^^^^^^^^

Returns the status of the bot.

.. _command-status-cmd:

status cmd
^^^^^^^^^^

Returns some interesting command-related statistics.

.. _command-status-commands:

status commands
^^^^^^^^^^^^^^^

Returns a list of the commands offered by the bot.

.. _command-status-uptime:

status uptime
^^^^^^^^^^^^^

Returns the amount of time the bot has been running.

.. _command-status-threads:

status threads
^^^^^^^^^^^^^^

Returns the current threads that are active.

.. _command-status-net:

status net
^^^^^^^^^^

Returns some interesting network-related statistics.

.. _command-status-server:

status server
^^^^^^^^^^^^^

Returns the server the bot is on.

.. _command-status-cpu:

status cpu
^^^^^^^^^^

Returns some interesting CPU-related statistics on the bot.



.. _plugin-status-config:

Configuration
-------------

.. _supybot.plugins.Status.cpu:

supybot.plugins.Status.cpu
^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Status.cpu.children:

supybot.plugins.Status.cpu.children
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the cpu command will list the time taken by children as well as the bot's process.

.. _supybot.plugins.Status.cpu.memory:

supybot.plugins.Status.cpu.memory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the cpu command will report the amount of memory being used by the bot.

.. _supybot.plugins.Status.cpu.threads:

supybot.plugins.Status.cpu.threads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the cpu command will provide the number of threads spawned and active.

.. _supybot.plugins.Status.public:

supybot.plugins.Status.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

