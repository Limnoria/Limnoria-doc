*********************
Software architecture
*********************

Limnoria abstracts its internal architecture away from plugins through
its plugin API, which is enough most of the time.
However, you may need want to understand its internal architecture, either
to debug complex problems, provide advanced features that hook into
the internals, contribute to the core, or simply out of curiosity.

This guide will try to walk you through this, assuming you are already
familiar with using the bot and writing plugins (if not, see the
:ref:`capabilities` documentation, the :ref:`plugin-tutorial`,
and :ref:`events`,

You should also be somewhat familiar with the
`IRC protocol <https://modern.ircdocs.horse/>`.

.. note::

   This document is a work in progress and is still incomplete.
   As usual, feel free to ask any questions in #limnoria @ Libera.

Main loop and drivers
=====================

The main event loop is a very classic synchronous loop.
It is defined in :file:`scripts/supybot`, and essentially just this::

    while world.ircs:
        try:
            drivers.run()
        except KeyboardInterrupt:
            # Handle Ctrl-C (trigger shutdown)
        except:
            # Handle other unhandled errors

Where :func:`drivers.run` does this::

    for (name, driver) in _drivers.items():
         if name not in _deadDrivers:
             driver.run()
    for name in _deadDrivers:
         # Remove the driver
    while _newDrivers:
         (name, driver) = _newDrivers.pop()
         # add the new driver

Drivers are the sources of events in the main thread. In a normal Limnoria
setup, there are two types of drivers: the Socket driver (which connects
synchronously to IRC) and the :ref:`schedule driver <supybot-schedule>`
(which runs functions periodically, like cron).
Historically, there was an alternative driver to connect to IRC,
based on Twisted. It was deprecated, then removed in 2019, because
Python's ``socket`` module became as powerful as Twisted as it gained
support for ``select()`` and TLS.

Network drivers have a reference to a :class:`irclib.Irc` object, and
do three things in their ``run()`` method:

1. check the connection is still alive (and schedule a reconnect if not)
2. get new messages from their :class:`irclib.Irc` instance (using
   :meth:`irclib.Irc.takeMsg`) and send them to the network
3. get new messages from the network and pass them to their :class:`irclib.Irc`
   (using :meth:`irclib.Irc.feedMsg`)

The actual implementation of the current ``Socket`` driver is actually
a little more complex than this, as all ``Socket`` driver instances cooperate
to use ``select()`` together, but this is the rough idea.
See :file:`src/drivers/Socket.py` for details.

irclib
======

As we saw above, network drivers pass their messages to a class defined in
:mod:`irclib`, which is where most of the IRC protocol implementation is.

Unlike most event-driven software (especially IRC implementation), Limnoria
does not have hooks that are registered to call a function when a specific
event/IRC command is received.
Instead, event listeners receive all events, and inherit on
:class:`supybot.irclib.IrcCommandDispatcher`, which calls a specific method
based on the IRC command name. For example, it calls the ``doTopic`` method
when receiving a ``TOPIC`` message.

This dispatching is used both in the main IRC handling
(:class:`supybot.irclib.Irc`) and plugins (via
:class:`supybot.callbacks.PluginMixin`, which inherits
:class:`supybot.irclib.IrcCommandDispatcher`).

We saw above that the :class:`supybot.irclib.Irc` object receives messages
directly from the driver. It's also in charge of keeping track of other
callbacks (ie. plugins) via :meth:`supybot.irclib.Irc.addCallback` and passing
every message to their ``__call__`` method (which then does the dispatching
on its own again, as it inherits :class:`supybot.irclib.IrcCommandDispatcher`).

As there are few callbacks (under a hundred plugins),
this simple architecture is efficient enough.

Additionally, when receiving a message and before sending one, it iterates
through the list of plugins and calls their ``inFilter`` and ``outFilter``
methods (respectively), if any.

If you look at the code of :class:`supybot.irclib.Irc` and
:class:`supybot.irclib.IrcState`, you see they are mostly made of ``doXxx``
methods, which exhaustively implement every known IRC command, update some
state, and optionally react to it by queuing messages.

Commands
========

Next is the callbacks system, mostly implemented in :mod:``supybot.callbacks``.
This is where all the magic happens to make plugins so easy to write;
it's also the most complex part of Limnoria and the hardest to understand,
because everything is tightly interleaved.

TODO

Registry
========

TODO

Auto-documentation
==================

TODO
