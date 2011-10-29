
.. _plugin-twitter:

The Twitter plugin
==================

.. _command-twitter-friendslist:

twitter friendslist [<channel>] [<user>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with the friends (i.e. people who one subscribes to) of the
*<user>*. If *<user>* is not given, it defaults to the *<channel>*'s account.
If *<channel>* is not given, it defaults to the current channel.

.. _command-twitter-unfollow:

twitter unfollow [<channel>] <user>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unfollow a specified *<user>*
If *<channel>* is not given, it defaults to the current channel.

.. _command-twitter-replies:

twitter replies [<channel>] [--since <oldest>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with the replies timeline.
If *<channel>* is not given, it defaults to the current channel.
If given, *--since* takes a tweet ID, used as a boundary

.. _command-twitter-timeline:

twitter timeline [<channel>] [<user>] [--since <oldest>] [--max <newest>] [--count <number>] [--noretweet] [--with-id]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with the timeline of the *<user>*.
If *<user>* is not given, it defaults to the account associated with the
*<channel>*.
If *<channel>* is not given, it defaults to the current channel.
If given, *--since* and *--max* take tweet IDs, used as boundaries.
If given, *--count* takes an integer, that stands for the number of
tweets to display.
If *--noretweet* is given, only native user's tweet will be displayed.

.. _command-twitter-follow:

twitter follow [<channel>] <user>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow a specified *<user>*
If *<channel>* is not given, it defaults to the current channel.

.. _command-twitter-post:

twitter post [<channel>] <message>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates the status of the account associated with the given *<channel>*
to the *<message>*. If *<channel>* is not given, it defaults to the
current channel.

.. _command-twitter-public:

twitter public [<channel>] [--since <oldest>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with the public timeline.
If *<channel>* is not given, it defaults to the current channel.
If given, *--since* takes a tweet ID, used as a boundary

.. _command-twitter-delete:

twitter delete [<channel>] <id>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a specified status with id *<id>*
If *<channel>* is not given, it defaults to the current channel.



.. _plugin-twitter-config:

Configuration
-------------

.. _supybot.plugins.Twitter.accounts:

supybot.plugins.Twitter.accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Twitter.accounts.bot:

supybot.plugins.Twitter.accounts.bot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Twitter.accounts.bot.api:

supybot.plugins.Twitter.accounts.bot.api
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: https://api.twitter.com/1

The URL to the base API URL (by default, it is Twitter.com, but you can use it for twitter-compatible services, such as identica/statusnet.

.. _supybot.plugins.Twitter.accounts.bot.key:

supybot.plugins.Twitter.accounts.bot.key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

The Twitter Access Token key for the bot's account (running get_access_token.py is a way to get it)

.. _supybot.plugins.Twitter.accounts.bot.secret:

supybot.plugins.Twitter.accounts.bot.secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

The Twitter Access Token secret for the bot's account (running get_access_token.py is a way to get it)

.. _supybot.plugins.Twitter.accounts.channel:

supybot.plugins.Twitter.accounts.channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Twitter.accounts.channel.key:

supybot.plugins.Twitter.accounts.channel.key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

The Twitter Access Token key for this channel's account (running get_access_token.py is a way to get it)

.. _supybot.plugins.Twitter.accounts.channel.secret:

supybot.plugins.Twitter.accounts.channel.secret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

The Twitter Access Token secret for this channel's account (running get_access_token.py is a way to get it)

.. _supybot.plugins.Twitter.accounts.channel.api:

supybot.plugins.Twitter.accounts.channel.api
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: https://api.twitter.com/1

The URL to the base API URL (by default, it is Twitter.com, but you can use it for twitter-compatible services, such as identica/statusnet.

.. _supybot.plugins.Twitter.public:

supybot.plugins.Twitter.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

