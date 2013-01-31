.. _supybot-irclib:

**************
supybot.irclib
**************

Most used classes
=================

.. _supybot-irclib-irc:

supybot.irclib.Irc
------------------

It is usually the `irc` object given to plugin commands.

.. autoclass:: supybot.irclib.Irc
    :members:
    :inherited-members:


.. _supybot-irclib-ircstate:

supybot.irclib.IrcState
-----------------------

Used mainly as the `state` attribute of :py:class:`supybot.irclib.Irc` objects.

.. autoclass:: supybot.irclib.IrcState
    :members:
    :inherited-members:


.. _supybot-irclib-channelstate:

supybot.irclib.ChannelState
---------------------------

Used mainly as the `channels['#chan']` attribute of
:py:class:`supybot.irclib.Irc` objects.

.. autoclass:: supybot.irclib.ChannelState
    :members:
    :inherited-members:
