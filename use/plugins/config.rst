
.. _plugin-config:

The Config plugin
=================

.. _command-help:

help <name>
^^^^^^^^^^^

Returns the description of the configuration variable *<name>*.


.. _command-default:

default <name>
^^^^^^^^^^^^^^

Returns the default value of the configuration variable *<name>*.


.. _command-list:

list <group>
^^^^^^^^^^^^

Returns the configuration variables available under the given
configuration *<group>*. If a variable has values under it, it is
preceded by an '@' sign. If a variable is a 'ChannelValue', that is,
it can be separately configured for each channel using the 'channel'
command in this plugin, it is preceded by an '#' sign.


.. _command-search:

search <word>
^^^^^^^^^^^^^

Searches for *<word>* in the current configuration variables.


.. _command-reload:

reload
^^^^^^

Reloads the various configuration files (user database, channel
database, registry, etc.).


.. _command-export:

export <filename>
^^^^^^^^^^^^^^^^^

Exports the public variables of your configuration to *<filename>*.
If you want to show someone your configuration file, but you don't
want that person to be able to see things like passwords, etc., this
command will export a "sanitized" configuration file suitable for
showing publicly.


.. _command-channel:

channel [<channel>] <name> [<value>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If *<value>* is given, sets the channel configuration variable for *<name>*
to *<value>* for *<channel>*. Otherwise, returns the current channel
configuration value of *<name>*. *<channel>* is only necessary if the
message isn't sent in the channel itself.

.. _command-config:

config <name> [<value>]
^^^^^^^^^^^^^^^^^^^^^^^

If *<value>* is given, sets the value of *<name>* to *<value>*. Otherwise,
returns the current value of *<name>*. You may omit the leading
"supybot." in the name if you so choose.


