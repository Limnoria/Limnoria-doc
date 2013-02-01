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

    .. attribute:: zombie

        Whether or not this object represents a living IRC connection.

        :type: bool

    .. attribute:: network

        The name of the network this object is connected to.

        :type: str

    .. attribute:: startedAt

        :type: float


.. _supybot-irclib-ircstate:

IrcState
========

Used mainly as the `state` attribute of :py:class:`supybot.irclib.Irc` objects.

.. autoclass:: supybot.irclib.IrcState
    :members:
    :inherited-members:


.. _supybot-irclib-channelstate:

ChannelState
============

Used mainly as the `channels['#chan']` attribute of
:py:class:`supybot.irclib.Irc` objects.

.. autoclass:: supybot.irclib.ChannelState
    :members:
    :inherited-members:

Other classes
=============

.. automodule:: supybot.irclib
    :members:
    :exclude-members: Irc, IrcState, ChannelState
