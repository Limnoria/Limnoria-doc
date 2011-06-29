
.. _plugin-twitter:

The Twitter plugin
==================

This plugin provides access to the Twitter API, using OAuth authentication.
You can set a Twitter account for the whole bot, and an account per channel.

This plugin may work with identica/statusnet Twitter-compatible API, but has
not been tested yet.

.. include:: unofficial.inc

.. _command-twitter-friendslist:

twitter friendslist [<channel>] [<user>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with the friends (i.e. people who one subscribes to) of the
*<user>*. If *<user>* is not given, it defaults to the *<channel>*'s account.
If *<channel>* is not given, it defaults to the current channel.

.. _command-twitter-timeline:

twitter timeline [<channel>|<user>] [--since <oldest>] [--max <newest>] [--count <number>] [--noretweet]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with the timeline of the *<user>*.
If *<user>* is not given, it defaults to the account associated with the
*<channel>*.
If *<channel>* is not given, it defaults to the current channel.
If given, *--since* and *--max* take tweet IDs, used as boundaries.
If given, *--count* takes an integer, that stands for the number of
tweets to display.
If *--noretweet* is given, only native user's tweet will be displayed.

.. _command-twitter-post:

twitter post [<channel>] <message>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates the status of the account associated with the given *<channel>*
to the *<message>*. If *<channel>* is not given, it defaults to the
current channel.

