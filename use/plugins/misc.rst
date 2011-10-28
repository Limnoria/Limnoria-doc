
.. _plugin-misc:

The Misc plugin
===============

Main commands
-------------

.. _command-misc-help:

misc help [<plugin>] [<command>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command gives a useful description of what *<command>* does.
*<plugin>* is only necessary if the command is in more than one plugin.

.. _command-misc-list:

misc list [--private] [<plugin>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lists the commands available in the given plugin. If no plugin is
given, lists the public plugins available. If *--private* is given,
lists the private plugins.

.. _command-misc-more:

misc more [<nick>]
^^^^^^^^^^^^^^^^^^

If the last command was truncated due to IRC message length
limitations, returns the next chunk of the result of the last command.
If *<nick>* is given, it takes the continuation of the last command from
*<nick>* instead of the person sending this message.

Utilities
---------

.. _command-misc-last:

misc last [--{from,in,on,with,without,regexp} <value>] [--nolimit]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the last message matching the given criteria. *--from* requires
a nick from whom the message came; *--in* requires a channel the message
was sent to; *--on* requires a network the message was sent on; *--with
requires* some string that had to be in the message; *--regexp* requires
a regular expression the message must match; *--nolimit* returns all
the messages that can be found. By default, the channel this command is
given in is searched.

.. _command-misc-ping:

misc ping
^^^^^^^^^

Checks to see if the bot is alive.

.. _command-misc-tell:

misc tell <nick> <text>
^^^^^^^^^^^^^^^^^^^^^^^

Tells the *<nick>* whatever *<text>* is. Use nested commands to your
benefit here.

Getting informations about the bot
----------------------------------

.. _command-misc-source:

misc source
^^^^^^^^^^^

Returns a URL saying where to get Supybot.

.. _command-misc-version:

misc version
^^^^^^^^^^^^

Returns the version of the current bot.

.. _command-misc-apropos:

misc apropos <string>
^^^^^^^^^^^^^^^^^^^^^

Searches for *<string>* in the commands currently offered by the bot,
returning a list of the commands containing that string.


.. _plugin-misc-config:

Configuration
-------------

.. _supybot.plugins.Misc.last:

supybot.plugins.Misc.last
^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Misc.last.nested:

supybot.plugins.Misc.last.nested
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Misc.last.nested.includeNick:

supybot.plugins.Misc.last.nested.includeNick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether or not the nick will be included in the output of last when it is part of a nested command

.. _supybot.plugins.Misc.last.nested.includeTimestamp:

supybot.plugins.Misc.last.nested.includeTimestamp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether or not the timestamp will be included in the output of last when it is part of a nested command

.. _supybot.plugins.Misc.listPrivatePlugins:

supybot.plugins.Misc.listPrivatePlugins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will list private plugins with the list command if given the --private switch. If this is disabled, non-owner users should be unable to see what private plugins are loaded.

.. _supybot.plugins.Misc.listUnloadedPlugins:

supybot.plugins.Misc.listUnloadedPlugins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will list unloaded plugins with the list command if given the --unloaded switch. If this is disabled, non-owner users should be unable to see what unloaded plugins are available.

.. _supybot.plugins.Misc.public:

supybot.plugins.Misc.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.Misc.timestampFormat:

supybot.plugins.Misc.timestampFormat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: [%H:%M:%S]

Determines the format string for timestamps in the Misc.last command. Refer to the Python documentation for the time module to see what formats are accepted. If you set this variable to the empty string, the timestamp will not be shown.

