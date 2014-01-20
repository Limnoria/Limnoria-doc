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

Commands and numerics
=====================

You can catch commands directly with “do-methods”: when the bot receives a
``PRIVMSG``, all ``doPrivmsg`` methods are called; when it gets a ``437``
message, all ``do437`` methods are called, etc.

Those command take two commands: an :ref:`Irc object <supybot-irclib-irc>`
and a :ref:`IrcMsg object <supybot-ircmsgs>`.

To get a list of all possible messages, check IRC RFCs.

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

.. note::
    I wrote this section with the little knowledge I have of the
    commands handling (all I know comes from hacks I made to write
    the Aka plugin), so keep in mind some informations might
    be wrong.
    As for all the documentation, feel free to contact me to
    correct/enhance it.

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
