***********************************
Special methods and catching events
***********************************

This page is a non-exhaustive list of special plugin method names and
events catchable via those methods (other events include
:ref:`configuration hooks <configuration-hooks>` and
:ref:`HTTP server callbacks <http_plugins>`)

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
