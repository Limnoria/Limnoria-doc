
.. _plugin-channellogger:

The ChannelLogger plugin
========================



.. _plugin-channellogger-config:

Configuration
-------------

.. _supybot.plugins.ChannelLogger.enable:

supybot.plugins.ChannelLogger.enable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether logging is enabled.

.. _supybot.plugins.ChannelLogger.filenameTimestamp:

supybot.plugins.ChannelLogger.filenameTimestamp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: %Y-%m-%d

Determines how to represent the timestamp used for the filename in rotated logs. When this timestamp changes, the old logfiles will be closed and a new one started. The format characters for the timestamp are in the time.strftime docs at python.org. In order for your logs to be rotated, you'll also have to enable supybot.plugins.ChannelLogger.rotateLogs.

.. _supybot.plugins.ChannelLogger.noLogPrefix:

supybot.plugins.ChannelLogger.noLogPrefix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: [nolog]

Determines what string a message should be prefixed with in order not to be logged. If you don't want any such prefix, just set it to the empty string.

.. _supybot.plugins.ChannelLogger.rotateLogs:

supybot.plugins.ChannelLogger.rotateLogs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will automatically rotate the logs for this channel. The bot will rotate logs when the timestamp for the log changes. The timestamp is set according to the 'filenameTimestamp' configuration variable.

.. _supybot.plugins.ChannelLogger.stripFormatting:

supybot.plugins.ChannelLogger.stripFormatting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether formatting characters (such as bolding, color, etc.) are removed when writing the logs to disk.

.. _supybot.plugins.ChannelLogger.timestamp:

supybot.plugins.ChannelLogger.timestamp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the logs for this channel are timestamped with the timestamp in supybot.log.timestampFormat.

.. _supybot.plugins.ChannelLogger.directories:

supybot.plugins.ChannelLogger.directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will partition its channel logs into separate directories based on different criteria.

.. _supybot.plugins.ChannelLogger.directories.timestamp:

supybot.plugins.ChannelLogger.directories.timestamp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will use a timestamp (determined by supybot.plugins.ChannelLogger.directories.timestamp.format) if using directories.

.. _supybot.plugins.ChannelLogger.directories.timestamp.format:

supybot.plugins.ChannelLogger.directories.timestamp.format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: %B

Determines what timestamp format will be used in the directory structure for channel logs if supybot.plugins.ChannelLogger.directories.timestamp is True.

.. _supybot.plugins.ChannelLogger.directories.channel:

supybot.plugins.ChannelLogger.directories.channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will use a channel directory if using directories.

.. _supybot.plugins.ChannelLogger.directories.network:

supybot.plugins.ChannelLogger.directories.network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will use a network directory if using directories.

.. _supybot.plugins.ChannelLogger.flushImmediately:

supybot.plugins.ChannelLogger.flushImmediately
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether channel logfiles will be flushed anytime they're written to, rather than being buffered by the operating system.

.. _supybot.plugins.ChannelLogger.public:

supybot.plugins.ChannelLogger.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

