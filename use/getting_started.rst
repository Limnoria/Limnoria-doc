.. _getting-started:

*************************************
Getting Started with Limnoria/Supybot
*************************************

.. highlight:: irc

Introduction
============

Ok, so you've decided to try out Limnoria.  That's great!  The more people who
use Limnoria, the more people can submit bugs and help us to make it the best
IRC bot in the world :)

At this point, we assume you've already followed the steps to
:ref:`install and configure <use-install>` Limnoria, and that the bot has
connected to the network you specified.

When the bot is in a channel, it will respond by default to messages prefixed by
its nick (e.g. ``supybot: echo hi``), or any prefixes you configured inside the
wizard (e.g. ``@echo hi``). If you haven't told it to join any channels,
you can also send it direct messages, in which case no prefix is required.

Finding the bot's commands
==========================

Limnoria uses a two tier system for its commands, where each command is
registered under a plugin. The first step to navigating Limnoria is to run
``list``, which will show you all the plugins loaded::

    <user> supybot: list
    <supybot> Admin, Channel, ChannelLogger, Config, Misc, Network, Owner, Plugin, User, and Utilities

Replacing 'supybot' with the actual name you picked for your bot, of course.
At least `Admin`, `Channel`, `Config`, `Misc`, `Owner`, and `User` should be
there; if you used ``supybot-wizard`` to create your configuration file you may
have many more plugins loaded.  The ``list`` command can then be used to list the
commands in a given plugin::

    <user> supybot: list Misc
    <supybot> user: apropos, clearmores, completenick, help, last, list, more, noticetell, ping, source, tell, and version

This lists all the commands in the `Misc` plugin.  If you want to see the help
for a specific command, you can then use the help command::

    <user> supybot: help help
    <supybot> user: (help [<plugin>] [<command>]) -- This command gives a useful description of what <command> does. <plugin> is only necessary if the command is in more than one plugin. You may also want to use the 'list' command to list all available plugins and commands.
    <user> supybot: help list
    <supybot> user: (list [--unloaded] [<plugin>]) -- Lists the commands available in the given plugin. If no plugin is given, lists the public plugins available. If --unloaded is given, it will list available plugins that are not loaded.
    <user> supybot: help load
    <supybot> user: (load <plugin>) -- Loads the plugin <plugin> from any of the directories in conf.supybot.directories.plugins; usually this includes the main installed directory and 'plugins' in the current directory.

Sometimes more than one plugin will register a given command; for instance, the
``list`` command exists in both the Misc and Config plugins (both loaded by
default).  ``list``, in this case, defaults to the Misc plugin, but you may want
to get the help for the list command in the Config plugin.  In that case,
you can prefix your command with the name of the plugin::

    <user> supybot: help config list
    <supybot> user: (config list <group>) -- Returns the configuration variables available under the given configuration <group>. If a variable has values under it, it is preceded by an '@' sign.

Anytime your bot tells you that a given command is defined in several plugins,
you'll need to use this "plugin command" syntax to choose which
plugin's command you wish to call.  For instance, if you wanted to call the
Config plugin's ``list`` command, then you'd need to run::

    <user> supybot: config list

Rather than just ``list``.

.. _login-to-bot:

Logging in to Limnoria
======================

.. note::
    For making the bot to identify to services, please see
    :ref:`identifying to services. <identifying-to-services>`

Most administrative tasks in Limnoria (loading plugins, adding networks) require
you to be logged in to the bot as an ``owner`` user. If you used
``supybot-wizard`` to configure the bot, you have probably added an owner user
already. If not, shut off the bot and run the ``supybot-adduser`` script to
create a user, and give yourself the ``owner`` capability when it prompts you
to do so.

To log in to the bot, use the ``identify`` command. This must be sent in a
private message (i.e. ``/query``) to the bot, to avoid leaking your password
to a channel::

    <user> help identify
    <supybot> (identify <name> <password>) -- Identifies the user as <name>. This command (and all other commands that include a password) must be sent to the bot privately, not in a channel.

Replacing "myowneruser" and "myuserpassword" with your login details, you should
run::

    <user> identify myowneruser myuserpassword
    <supybot> The operation succeeded.

Once you are logged in as an owner user, you can run commands that require
privileges. Many such administrative commands are located in the *Owner* and
*Admin* plugins.

Automatic login (optional)
--------------------------

If you wish to make managing the bot easier, there are a few ways to log in to
the bot automatically.

Automatic login using network services (NickAuth)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On IRC networks that provide a modern NickServ implementation,
Limnoria supports associating your bot account with a services account. This is
often the easiest method, as it does not involve configuring hostmasks.

To use this, you first need to load the **NickAuth** plugin (see the
:ref:`loading plugins <loading-plugins>` section for details on how to do that).

To find your NickServ account name, run ``/whois <yournick>``, and you should see
some output like this::

    [Mikaela] is logged in as Mikaela

NickAuth logins are managed using the ``nickauth nick add`` and ``nickauth nick remove``
commands. For clarity, ``<user>`` refers to your bot user, and ``<nick>`` refers
to your NickServ account name::

    <user> @help nickauth nick add
    <Limnoria> (nick add [<network>] <user> <nick>) -- Add <nick> to the list of nicks owned by the <user> on the <network>. You have to register this nick to the network services to be authenticated. <network> defaults to the current network.

To add the NickServ account "Mikaela" to a bot account of the same name::

    <Mikaela> @nickauth nick add Mikaela Mikaela
    <Limnoria> OK.

On most networks, NickAuth will automatically activate when you log in to your
services account or join a channel the bot is in. Note that this requires the
`extended-join <https://ircv3.net/specs/extensions/extended-join>`_ and
`WHOX <https://ircv3.net/specs/extensions/whox>`_ IRCv3 features to be supported
by the IRC network.

In places where this does not work, you can manually trigger a login
attempt using the ``nickauth auth`` command::

    <Guest45020> @whoami
    <Limnoria> I don't recognize you. You can messsage me either of these two commands: "user identify <username> <password>" to log in or "user register <username> <password>" to register.
    <Guest45020> @nickauth auth
    <Limnoria> You are now authenticated as Mikaela.

Automatic login using a hostmask
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An alternative to NickAuth that works everywhere is automatic login using your
IRC hostmask (``nick!user@host``). This may be more work to set up as there is
no one-size-fits-all hostmask to match someone; the best approach depends
on the network you're on and the type of host you are connecting from.

Hostmask login is configured using the ``user hostmask add`` and
``user hostmask remove`` commands::

    <user> @help hostmask add
    <Limnoria> (hostmask add [<name>] [<hostmask>] [<password>]) -- Adds the hostmask <hostmask> to the user specified by <name>. The <password> may only be required if the user is not recognized by hostmask. <password> is also not required if an owner user is giving the command on behalf of some other user. If <hostmask> is not given, it defaults to your current hostmask. If <name> is not given, it defaults to your currently identified name. This message must be sent to the bot privately (not on a channel) since it may contain a password.

.. warning::
    Before adding a hostmask, double check that it is specific enough to only
    match *you*. Giving permissions to wide hostmasks (e.g. ``nick!user@*``) is
    a security risk, and could allow others to hijack your bot.

If you're on a network that provides unique :ref:`cloaks/vhosts <cloak-examples>`
based on your username, or have an otherwise dedicated static IP
(e.g. on a server not shared with other people), you can use the "host" part of
your hostmask for logging in::

    <user> user hostmask add myuser *!*@mycloak
    <Limnoria> The operation succeeded.

On shared hosts that implement the `IDENT protocol <https://en.wikipedia.org/wiki/Ident_protocol>`_,
you may want to add the username / ident field to the hostmask as well.
Note that this only works well if the network also implements IDENT checking;
otherwise, anyone can connect with anything in the username field::

    <user> user hostmask add myuser *!myident@myhost
    <Limnoria> The operation succeeded

.. _cloak-examples:

*mycloak* at Libera.chat, for instance, is usually in the format ``user/accountname``.
On other networks, you may be able to request cloaks using HostServ (``/msg HostServ help``)
or by asking a network operator. Note: OFTC is exception, and uses
``/msg NickServ set cloak on`` instead.

.. _loading-plugins:

Loading Plugins
===============

.. note::
    To load plugins, you first need to be :ref:`logged in to the bot as an owner user <login-to-bot>`.

Loading plugins is done with the ``load`` command::

    <user> @help load
    <Limnoria> user: (load <plugin>) -- Loads the plugin <plugin> from any of the directories in conf.supybot.directories.plugins; usually this includes the main installed directory and 'plugins' in the current directory.

For example, to load the *Games* plugin, run::

    <user> @load Games
    <Limnoria> The operation succeeded.

To unload a plugin, there is a corresponding ``unload`` command::

    <user> @unload Games
    <Limnoria> The operation succeeded.

To find plugins to load, consult the :ref:`Built-in plugins reference <builtin-plugins-reference>`
or the Plugins list on `limnoria.net <https://limnoria.net/plugins.xhtml>`_.

.. _help-syntax:
Understanding the help syntax
=============================

This section further explains the help syntax given by the ``help`` command.

Some examples:

help [<plugin>] [<command>]
    This is the help of :ref:`command-plugin-help`.

    The chevrons mean you have to replace <plugin> and <command> by a plugin
    name and a command name.

    The square brackets mean the arguments they wrap are **optional**.

    So, the following commands are correct::

        <user> help
        <user> help PluginName
        <user> help PluginName CommandName
        <user> help CommandName

ping takes no arguments
    This is the help for :ref:`command-misc-ping`.

    I think it is clear enough.

join <channel> [<key>]
    This is the help for :ref:`command-admin-join`.

    It requires a channel name, and the channel key is optional.

    These two commands are ok::

        <user> join #limnoria
        <user> join #limnoria MySecretKey

utilities last <text> [<text> ...]
    This is the help for :ref:`command-utilities-last`.
    By the way, there is another ``last`` command in the `Misc` plugin, which
    doesn't do the same thing, that's why you need to give the plugin name.

    You have to give at least one argument, but you can give as many as you
    wish.

Pagination: Getting More From Your Limnoria
===========================================

Limnoria automatically splits messages that are too long for IRC into multiple
chunks (aka "mores"). By default, it will send only the first chunk, followed by
``(X more messages)``. To view the remaining parts of a response, run the
``more`` command, repeating it as necessary.

Example::

    <jemfinch> $config default supybot.replies.genericNoCapability
    <Limnoria> jemfinch: You're missing some capability you need. This could be because you actually possess the anti-capability for the capability that's required of you, or because the channel provides that anti-capability by default, or because the global capabilities include that anti-capability. Or, it could be because the channel or the global defaultAllow is set to False, meaning (1 more message)
    <jemfinch> $more
    <Limnoria> jemfinch: that no commands are allowed unless explicitly in your capabilities. Either way, you can't do what you want to do.

Chunked messages are stored by user, and you can view "mores" directed at
some else by specifying their nick in the command, e.g. ``more jemfinch``.
After doing this, any further responses are redirected to you, so they can be
displayed via ``more`` (without any extra argument).

If you want the bot to display more pages automatically, you can also
:ref:`configure <configuration-guide>` the following option::

    <jlu5> @config help reply.mores.instant
    <Limnoria> Determines how many mores will be sent instantly (i.e., without the use of the more command, immediately when they are formed). Defaults to 1, which means that a more command will be required for all but the first chunk.  (Current value: 5)

Final Word
==========

You should now have a solid foundation for using Limnoria! In summary, use the
``list`` command to see what plugins your bot has loaded and what commands are
in those plugins, the ``help`` command to see how to use a command, and
the ``more`` command to continue a long response from the bot.

Do be sure to read the rest of the documentation, and visit #limnoria on
irc.libera.chat if you run into any trouble!
