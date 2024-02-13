.. _events:

***********************************
Special methods and catching events
***********************************

This page is a non-exhaustive list of special plugin method names and
events catchable via those methods (other events include
:ref:`configuration hooks <configuration-hooks>` and
:ref:`HTTP server callbacks <http_plugins>`)

All methods here are defined in ``supybot-callbacks-plugin``. You may
override them if you need, but make sure you call the parent's one
unless you actually don't want to do it.

In case multiple plugins implement the same special methods, the order
they are called depends on the ``callAfter`` and ``callBefore``
(lists of plugin names) attributes of the plugins, if they are set.

Loading and unloading
=====================

The ``__init__`` method gets called with an Irc object as a parameter
when a plugin is loaded (or has just been reloaded).
Make sure you always call the parent's ``__init__``.

When a plugin is unloaded (or is to be reloaded), the ``die``
method is called (with no parameter).
Also make sure you always call the parent's ``die``.

.. _do-method-handlers:

Commands and numerics
=====================

You can catch commands directly with “do-methods”: when the bot receives a
``PRIVMSG``, all ``doPrivmsg`` methods are called; when it gets a ``437``
message, all ``do437`` methods are called, etc.

These methods are called **after** Limnoria updates its internal state;
so for example someone changes their nick from ``foo`` to ``bar`` (ie.
``:foo!~user@example.org NICK bar``), then ``doNick`` is called while
``irc.state.channels.[...].users`` already contains ``bar``.

Those command take two arguments: an :ref:`Irc object <supybot-irclib-irc>`
and a :ref:`IrcMsg object <supybot-ircmsgs>`.

To get a list of all possible messages, check `IRC specifications
<https://modern.ircdocs.horse/>`__.

Filters
=======

The ``inFilter`` and ``outFilter`` methods allow you to “intercept”
messages between the bot and the network and to alter them.

``inFilter`` gets messages just after they are parsed from network;
and its return value is fed to the bot.
``outFilter`` does the opposite: it get any message the bot is about
the send, and returns a message (which may be the same) that will
be sent instead.


.. _commands_handling:

Commands handling
=================

Command dispatching
-------------------

* ``isCommandMethod`` takes a command name as a string (which may contain
  spaces) and returns a boolean telling if the plugin provides this command.
* ``listCommands`` returns a list of command names as strings (which may
  contain spaces)
* ``getCommand`` takes a potential command name as a list of strings, and
  returns a truncated list corresponding to the name of a command provided
  by the plugin. If no command match, it returns an empty list.
* ``getCommandMethod`` takes a command name as a list of strings and
  returns the corresponding method/function.
* ``callCommand`` gets a command name as a list of strings, an irc object,
  an msg object, and extra arguments (with `*args` and `**kwargs`),
  calls ``getCommandMethod`` to get the command method, and calls it
  with the arguments.
  It also calls the functions in ``pre_command_callback``.

Pre-command-call callbacks
--------------------------

.. note::
    Until stock Supybot and Gribble merge this feature, this section
    only applies to Limnoria

If you want a function of your plugin to be called before every command call,
you can add it to the ``pre_command_callback`` attribute of your plugin
(actually, it is a static class attribute, so make sure you *add* it to the
list and don't touch other items of the list).

At every command call, *all* callbacks are called, and if *any* of them
returns ``True``, the command is not called.

Other command-related events
----------------------------

* all ``invalidCommand`` methods get called (with an Irc object, an IrcMsg
  objet, and a list of token) when a user calls a command that no plugin
  provides.


Regular expression triggered events
===================================

The :class:`supybot.callbacks.PluginRegexp` class provides some utilities
for creating plugins that act on regular expression matching.
