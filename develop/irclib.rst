.. _supybot-irclib:

**************
supybot.irclib
**************

.. _supybot-irclib-irc:

Irc
===

It is usually the `irc` object given to plugin commands.

.. autoclass:: supybot.irclib.Irc
    :members:
    :inherited-members:


.. _supybot-irclib-ircstate:

IrcState
========

Used mainly as the ``state`` attribute of :py:class:`supybot.irclib.Irc` objects.

.. autoclass:: supybot.irclib.IrcState
    :members:
    :inherited-members:



.. _supybot-irclib-ircstatefsm:

IrcStateFsm
===========

Used as the ``fsm`` attribute of :py:class:`supybot.irclib.IrcState` objects

.. autoclass:: supybot.irclib.IrcStateFsm
    :members:
    :inherited-members:


.. _supybot-irclib-channelstate:

ChannelState
============

Used mainly as the ``.state.channels['#chan']`` attribute of
:py:class:`supybot.irclib.Irc` objects.

.. autoclass:: supybot.irclib.ChannelState
    :members:
    :inherited-members:

Other classes
=============

.. automodule:: supybot.irclib
    :members:
    :exclude-members: Irc, IrcState, IrcStateFsm, ChannelState
