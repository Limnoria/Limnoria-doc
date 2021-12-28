.. _developer-faq:

**************************
Frequently Asked Questions
**************************

This section tries to cover all questions you may have as a plugin developer.
(If you are a user, check out the :ref:`User FAQ <user-faq>` instead.)


Where can I find the user who called a command?
===============================================

The ``msg`` object passed to all event method as well as command methods is an
:py:class:`supybot.ircmsgs.IrcMsg` object, which stores the content of the
message, the nick and hostname of its author, etc. Check the documentation of
:py:class:`supybot.ircmsgs.IrcMsg` to see all available attributes.:w


Where can I find the hostname from a user's nick?
=================================================

The ``irc`` object passed to all event method as well as command methods is an
:py:class:`supybot.irclib.Irc` object, use
:py:meth:`irc.state.nickToHostmask <supybot.irclib.IrcState.nickToHostmask>`

How do I get channel modes when writing a plugin?
=================================================

  I want to know who's an op in a certain channel, or who's voiced, or
  what the modes on the channel are.  How do I do that?

  Everything you need is kept in a `ChannelState` object in an
  `IrcState` object in the `Irc` object your plugin is given.  To see
  the ops in a given channel, for instance, you would do this::

    irc.state.channels['#channel'].ops

  To see a dictionary mapping mode chars to values (if any), you would
  do this::

    irc.state.channels['#channel'].modes

  From there, things should be self-evident.
