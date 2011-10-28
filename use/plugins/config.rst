
.. _plugin-config:

The Config plugin
=================

Accessing config
----------------

.. _command-config-help:

config help <name>
^^^^^^^^^^^^^^^^^^

Returns the description of the configuration variable *<name>*.

.. _command-config-default:

config default <name>
^^^^^^^^^^^^^^^^^^^^^

Returns the default value of the configuration variable *<name>*.

.. _command-config-list:

config list <group>
^^^^^^^^^^^^^^^^^^^

Returns the configuration variables available under the given
configuration *<group>*. If a variable has values under it, it is
preceded by an '@' sign. If a variable is a 'ChannelValue', that is,
it can be separately configured for each channel using the 'channel'
command in this plugin, it is preceded by an '#' sign.

.. _command-config-search:

config search <word>
^^^^^^^^^^^^^^^^^^^^

Searches for *<word>* in the current configuration variables.

.. _command-config-channel:

config channel [<channel>] <name> [<value>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If *<value>* is given, sets the channel configuration variable for *<name>*
to *<value>* for *<channel>*. Otherwise, returns the current channel
configuration value of *<name>*. *<channel>* is only necessary if the
message isn't sent in the channel itself.

.. _command-config-config:

config config <name> [<value>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If *<value>* is given, sets the value of *<name>* to *<value>*. Otherwise,
returns the current value of *<name>*. You may omit the leading
"supybot." in the name if you so choose.


Maintenance
-----------

.. _command-config-reload:

config reload
^^^^^^^^^^^^^

Reloads the various configuration files (user database, channel
database, registry, etc.).

.. _command-config-export:

config export <filename>
^^^^^^^^^^^^^^^^^^^^^^^^

Exports the public variables of your configuration to *<filename>*.
If you want to show someone your configuration file, but you don't
want that person to be able to see things like passwords, etc., this
command will export a "sanitized" configuration file suitable for
showing publicly.


.. _plugin-config-config:

Configuration
-------------

.. _supybot.plugins.Config.public:

supybot.plugins.Config.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

