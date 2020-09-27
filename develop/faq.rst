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

