
.. _plugin-owner:

The Owner plugin
================

.. _command-load:

load [--deprecated] <plugin>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Loads the plugin *<plugin>* from any of the directories in
conf.supybot.directories.plugins; usually this includes the main
installed directory and 'plugins' in the current directory.
*--deprecated* is necessary if you wish to load deprecated plugins.


.. _command-rename:

rename <plugin> <command> <new name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Renames *<command>* in *<plugin>* to the *<new name>*.


.. _command-enable:

enable [<plugin>] <command>
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enables the command *<command>* for all users.  If *<plugin>*
if given, only enables the *<command>* from *<plugin>*.  This command is
the inverse of disable.


.. _command-defaultcapability:

defaultcapability {add|remove} <capability>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds or removes (according to the first argument) *<capability>* from the
default capabilities given to users (the configuration variable
supybot.capabilities stores these).


.. _command-reloadlocale:

reloadlocale takes no argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reloads the locale of the bot.

.. _command-ircquote:

ircquote <string to be sent to the server>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends the raw string given to the server.


.. _command-disable:

disable [<plugin>] <command>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disables the command *<command>* for all users (including the owners).
If *<plugin>* is given, only disables the *<command>* from *<plugin>*.  If
you want to disable a command for most users but not for yourself, set
a default capability of -plugin.command or -command (if you want to
disable the command in all plugins).


.. _command-upkeep:

upkeep [<level>]
^^^^^^^^^^^^^^^^

Runs the standard upkeep stuff (flushes and gc.collects()).  If given
a level, runs that level of upkeep (currently, the only supported
level is "high", which causes the bot to flush a lot of caches as well
as do normal upkeep stuff.


.. _command-flush:

flush
^^^^^

Runs all the periodic flushers in world.flushers.  This includes
flushing all logs and all configuration changes to disk.


.. _command-unrename:

unrename <plugin>
^^^^^^^^^^^^^^^^^

Removes all renames in *<plugin>*.  The plugin will be reloaded after
this command is run.


.. _command-reset:

reset 
^^^^^^



.. _command-quit:

quit [<text>]
^^^^^^^^^^^^^

Exits the bot with the QUIT message *<text>*.  If *<text>* is not given,
the default quit message (supybot.plugins.Owner.quitMsg) will be used.
If there is no default quitMsg set, your nick will be used.


.. _command-unload:

unload <plugin>
^^^^^^^^^^^^^^^

Unloads the callback by name; use the 'list' command to see a list
of the currently loaded callbacks.  Obviously, the Owner plugin can't
be unloaded.


.. _command-reload:

reload <plugin>
^^^^^^^^^^^^^^^

Unloads and subsequently reloads the plugin by name; use the 'list'
command to see a list of the currently loaded plugins.


.. _command-announce:

announce <text>
^^^^^^^^^^^^^^^

Sends *<text>* to all channels the bot is currently on and not
lobotomized in.


.. _command-defaultplugin:

defaultplugin [--remove] <command> [<plugin>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the default plugin for *<command>* to *<plugin>*.  If *--remove* is
given, removes the current default plugin for *<command>*.  If no plugin
is given, returns the current default plugin set for *<command>*.  See
also, supybot.commands.defaultPlugins.importantPlugins.


.. _command-logmark:

logmark <text>
^^^^^^^^^^^^^^

Logs *<text>* to the global Supybot log at critical priority.  Useful for
marking logfiles for later searching.


