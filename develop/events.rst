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

* isCommandMethod takes a command name as a string (which may contain
  spaces) and returns a boolean telling if the plugin provides this command.
* listCommands returns a list of command names as strings (which may
  contain spaces)
* getCommand takes a potential command name as a list of strings, and
  returns a truncated list corresponding to the name of a command provided
  by the plugin. If no command match, it returns an empty list.
* getCommandMethod takes a command name as a list of strings and
  returns the corresponding method/function.
