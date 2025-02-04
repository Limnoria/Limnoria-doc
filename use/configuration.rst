=============
Configuration
=============

Introduction
------------

Much of Limnoria's behaviour, as well as those of its plugins, is configurable.

Limnoria provides a hierarchical configuration system, which is usually managed
via IRC using the `Config` plugin. By default, it will write back its configuration
periodically to the same ``botname.conf`` that the bot was started with.
(In most cases, this will be the ``.conf`` file created by ``supybot-wizard``.)

The main commands to interact with the config system are ``config``,
``config list``, and ``config help``, which are described in the following
sections.

Navigating the Configuration Registry
-------------------------------------

The root of Limnoria's config registry is named ``supybot``. At this level you
can find a few config variables (e.g. ``nick``, which sets the bot's nick), as
well as many more options nested within groups. This hierarchy allows config
options to be grouped naturally, and provides each plugin with a dedicated space
to declare its settings.

You can list the options in any group with the ``config list`` command::

    <Mikaela> @config list supybot
    <Limnoria> #alwaysJoinOnInvite, @abuse, @capabilities, @commands, @databases, @debug, @directories, @drivers, @log, @networks, @nick, @plugins, @protocols, @replies, @reply, @servers, defaultIgnore, defaultSocketTimeout, externalIP, flush, followIdentificationThroughNickChanges, ident, language, pidFile, snarfThrottle, upkeepInterval, and user

Some of the most common config groups include:

- `supybot.directories`: contains options on where to store log files, search for plugins, etc.
- `supybot.networks`: contains the configuration for all known IRC networks
- `supybot.log`: contains options relating to Limnoria's logs, such as verbosity
- `supybot.plugins.<plugin name>`: contains the configuration for each plugin
- `supybot.replies`: contains options for Limnoria's standard replies
- `supybot.reply`: contains options on how Limnoria should format its command output


Configuration Option Types
---------------------------

Inside ``config list``, the type of each configuration entry is labeled with a
symbol:

- **@** indicates that a config variable contains a group. (i.e. you can
  ``config list`` it as well). Note that some groups like ``supybot.nick`` are
  also configuration options themselves as well.
- **:** indicates that a config variable can be set per-network.
- **#** indicates that a config variable can be set per-channel. Most
  per-channel options can be set per-network as well, so you will often see them
  marked as **#:**
- Everything else is an option that can only be set globally.

The next section will focus on setting variables globally. Changing network and
channel-specific configuration is described
:ref:`later on <channel-specific-configuration>`.

Getting / Setting Configuration Values
--------------------------------------

To access a config option, you need to first construct its full path. An option's
path reflects the groups that you traversed in order to find it:
e.g. ``supybot.nick`` or ``supybot.reply.whenAddressedBy.chars``.

Then, you can run ``config help`` on an option to see how to use it.
For example, to see what ``supybot.snarfThrottle`` means, run::

  <jemfinch> @config help supybot.snarfThrottle
  <supybot> jemfinch: A floating point number of seconds to
            throttle snarfed URLs, in order to prevent loops between two
            bots snarfing the same URLs and having the snarfed URL in
            the output of the snarf message.  (Current value: 10.0)

To fetch the current value of a configuration variable, run the ``config``
command with just the name of the variable, e.g. ::

  <jemfinch> @config supybot.reply.whenAddressedBy.chars
  <supybot> jemfinch: '@'

To set a variable, add the new value after the name. This command sets the
bot's prefix character to either `@` or `$`::

  <jemfinch> @config supybot.reply.whenAddressedBy.chars @$
  <supybot> jemfinch: The operation succeeded.

  <jemfinch> $config supybot.reply.whenAddressedBy.chars
  <supybot> jemfinch: '@$'

To revert this change::

  <jemfinch> $config supybot.reply.whenAddressedBy.chars @
  <supybot> jemfinch: The operation succeeded.
  <jemfinch> $note that this makes no response.

By default, Limnoria writes its config to disk periodically
(see ``supybot.flush`` and ``supybot.upkeepInterval`` options), as well as when
shutting off the bot. This can also be manually triggered by running the
``flush`` command.

Default Values
--------------
To find the default value for a given configuration variable, use the
``config default`` command::

  <jemfinch> @config default supybot.reply.whenAddressedBy.chars
  <supybot> jemfinch: ''

To reset a configuration variable to its default value, use ``config setdefault``::

  <jemfinch> @config setdefault supybot.reply.whenAddressedBy.chars
  <supybot> jemfinch: The operation succeeded.
  <jemfinch> @note that this does nothing

Searching the Registry
----------------------

Limnoria allows searching for configuration variables by name, using the
``config search`` command::

    <Mikaela> @config search op
    <Limnoria> supybot.plugins.AutoMode.op, supybot.plugins.AutoMode.halfop, supybot.plugins.ChannelStatus.topic, supybot.plugins.LinkRelay.topicSync, supybot.plugins.NoLatin1.operator, supybot.plugins.Services.ChanServ.op, supybot.plugins.Services.ChanServ.halfop, supybot.plugins.Topic, supybot.plugins.Topic.public, supybot.plugins.Topic.separator, supybot.plugins.Topic.format, (1 more message)
    <Mikaela> @more
    <@Limnoria> supybot.plugins.Topic.recognizeTopiclen, supybot.plugins.Topic.default, supybot.plugins.Topic.alwaysSetOnJoin, supybot.plugins.Topic.undo, supybot.plugins.Topic.undo.max, and supybot.plugins.Topic.requireManageCapability

Do note that you can only see configuration variables for plugins that are
currently loaded or that you loaded in the past; if you've never loaded a plugin,
there's no way for the bot to know what configuration variables it registers.

.. _channel-specific-configuration:

Network- and Channel-Specific Configuration
-------------------------------------------

Many configuration variables can be set on a per-channel or per-network basis
via the ``config channel`` and ``config network`` commands. For example, to
set the bot's prefix character for the current channel, run::

  <jemfinch> @config channel supybot.reply.whenAddressedBy.chars !
  <supybot> jemfinch: The operation succeeded.

If you are not in a channel, or want to set the option for another channel, you
can also do so with the extended syntax: ``config channel [<network>] [<channel>]
<name> [<value>]``

To set the default prefix character for all channels on the current network,
run::

  <jemfinch> @config network supybot.reply.whenAddressedBy.chars !
  <supybot> jemfinch: The operation succeeded.

Note that channel-specific settings take precedence over network-specific ones.

Finally, you can also unset any channel-specific or network-specific variables
with the ``config reset channel`` and ``config reset network`` commands.

Editing the Config Manually
---------------------------

.. note::
    We don't recommend this; you should normally do everything with the commands
    in the Config plugin.

Before editing the config manually, you should either stop the bot or
set the ``supybot.flush`` option to ``false`` to prevent Limnoria from
writing its config out and overwriting your changes.

Once you have made your changes, use the ``config reload`` command to reload
Limnoria's configuration from disk.
This will refresh the bot's main configuration as well as any user/channel/ignore
databases, which are stored by default in separate files under the ``conf/``
directory.

If you cannot access the bot on IRC and your bot is running on a POSIX
system, you can also send it a SIGHUP signal; it is exactly the same
as ``config reload`` (note that the Config plugin has to be loaded for this
to work).
