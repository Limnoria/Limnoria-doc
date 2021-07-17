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

You should have already read through our install document (if you had to
manually install) before reading any further.  Now we'll give you a whirlwind
tour as to how you can get Limnoria setup and use Limnoria effectively.

Initial Setup
=============

Now that you have Limnoria installed, you'll want to get it running.  The first
thing you'll want to do is run supybot-wizard.  Before running supybot-wizard,
you should be in the directory in which you want your bot-related files to
reside.  The wizard will walk you through setting up a base config file for
your Limnoria.  Once you've completed the wizard, you will have a config file
called botname.conf.  In order to get the bot running, run ``supybot
botname.conf``.

Listing Commands
================

Ok, so let's assume your bot connected to the server and joined the channels
you told it to join.  For now we'll assume you named your bot 'mybot' (you
probably didn't, but it'll make it much clearer in the examples that follow to
assume that you did).  We'll also assume that you told it to join #channel (a
nice generic name for a channel, isn't it? :))  So what do you do with this
bot that you just made to join your channel?  Try this in the channel::

    <user> supybot: list
    <supybot> Admin, Channel, ChannelLogger, Config, Misc, Network, Owner, Plugin, User, and Utilities

Replacing 'supybot' with the actual name you picked for your bot, of course.
Your bot should reply with a list of the plugins it currently has loaded.  At
least `Admin`, `Channel`, `Config`, `Misc`, `Owner`, and `User` should be
there; if you used supybot-wizard to create your configuration file you may
have many more plugins loaded.  The list command can also be used to list the
commands in a given plugin::

    <user> supybot: list Misc
    <supybot> user: apropos, clearmores, completenick, help, last, list, more, noticetell, ping, source, tell, and version

This listed all the commands in the `Misc` plugin.  If you want to see the help
for any command, just use the help command::

    <user> supybot: help help
    <supybot> user: (help [<plugin>] [<command>]) -- This command gives a useful description of what <command> does. <plugin> is only necessary if the command is in more than one plugin. You may also want to use the 'list' command to list all available plugins and commands.
    <user> supybot: help list
    <supybot> user: (list [--unloaded] [<plugin>]) -- Lists the commands available in the given plugin. If no plugin is given, lists the public plugins available. If --unloaded is given, it will list available plugins that are not loaded.
    <user> supybot: help load
    <supybot> user: (load <plugin>) -- Loads the plugin <plugin> from any of the directories in conf.supybot.directories.plugins; usually this includes the main installed directory and 'plugins' in the current directory.

Sometimes more than one plugin will have a given command; for instance, the
"list" command exists in both the Misc and Config plugins (both loaded by
default).  List, in this case, defaults to the Misc plugin, but you may want
to get the help for the list command in the Config plugin.  In that case,
you'll want to give your command like this::

    <user> supybot: help config list
    <supybot> user: (config list <group>) -- Returns the configuration variables available under the given configuration <group>. If a variable has values under it, it is preceded by an '@' sign.

Anytime your bot tells you that a given command is defined in several plugins,
you'll want to use this syntax ("plugin command") to disambiguate which
plugin's command you wish to call.  For instance, if you wanted to call the
Config plugin's list command, then you'd need to say::

    <user> supybot: config list

Rather than just 'list'.

Making Limnoria Recognize You
=============================

For making the bot to identify to services, please see :ref:`identifying to services. <identifying-to-services>`

If you ran the wizard, then it is almost certainly the case that you already
added an owner user for yourself.  If not, however, you can add one via the
handy-dandy 'supybot-adduser' script.  You'll want to run it while the bot is
not running (otherwise it could overwrite supybot-adduser's changes to your
user database before you get a chance to reload them).  Just follow the
prompts, and when it asks if you want to give the user any capabilities, say
yes and then give yourself the 'owner' capability, restart the bot and you'll
be ready to load some plugins!

Now, in order for the bot to recognize you as your owner user, you'll have to
identify with the bot.

Open up a query window in your irc client ('/query'
should do it; if not, just know that you can't identify in a channel because
it requires sending your password to the bot).  Then type this::

    <user> help identify
    <supybot> (identify <name> <password>) -- Identifies the user as <name>. This command (and all other commands that include a password) must be sent to the bot privately, not in a channel.

And follow the instructions; the command you send will probably look like
this, with 'myowneruser' and 'myuserpassword' replaced::

    <user> identify myowneruser myuserpassword
    <supybot> The operation succeeded

The bot told you 'The operation succeeded', meaning that you got the right name
and password.  Now that you're identified, you can do anything that requires
any privilege: that includes all the commands in the Owner and Admin plugins,
which you may want to take a look at (using the list and help commands, of
course).  One command in particular that you might want to use (it's from the
User plugin) is the 'hostmask add' command: it lets you add a hostmask to your
user record so the bot recognizes you by your hostmask instead of requiring
you always to identify with it before it recognizes you.  Use the 'help'
command to see how this command works.  Here's how I often use it::

    <user> hostmask add myuser [hostmask] mypassword
    <supybot> The operation succeeded

You may not have seen that '[hostmask]' syntax before.  Limnoria allows nested
commands, which means that any command's output can be nested as an argument
to another command.  The hostmask command from the User plugin returns the
hostmask of a given nick, but if given no arguments, it returns the hostmask
of the person giving the command. So the command above adds the hostmask I'm
currently using to my user's list of recognized hostmasks.  I'm only required
to give mypassword if I'm not already identified with the bot.

It might often be better to specify the hostmask by yourself instead of 
nesting the hostmask command as the hostmask command gives your exact
hostmask of that moment meaning ``nick!ident@host`` which means that you
will get unidentified if you change your nickname.

I (Mikaela) often specify hostmasks in two other forms depending on the
situation which I go through in next subtopics.

Wildcard nick
^^^^^^^^^^^^^

In case my username and host stay the same or there aren't bots on same
server which could get identified as me to other bots, I use::

    <user> user hostmask add myuser *!myident@myhost
    <supybot> The operation succeeded

I only recommend this if there is ident server configured and the IRC
network checks for it.

Host only
^^^^^^^^^

In case I am the only one who has the same host (cloaks/vhosts on many
networks which have account in them, (for example Libera) or server where
no one else has access and no bots share it either), I use::

    <user> user hostmask add myuser *!*@mycloak
    <supybot> The operation succeeded

Mycloak at Libera is usually in format ``user/accountname``. You
can usually request hostmasks using HostServ, ``/msg HostServ help``, or
asking on help channel of your IRC network, in case of Libera that is
#libera. OFTC is exception to this and uses 
``/msg NickServ set cloak on``, but whatever your network users, you can 
ask it on their help channel.

Limnoria
--------

Limnoria has two additional methods to identify, GPG and NickAuth, each
provided as a plugin that you need to load (with the ``load`` command).

GPG
^^^

First you must associate your GPG key with your Limnoria account. The gpg 
add command takes two arguments, key id and key server.

My key is 0x0C207F07B2F32B67 and it's on keyserver pool.sks-keyservers.net 
so and now I add it to my bot::

    <Mikaela> +gpg add 0x0C207F07B2F32B67 pool.sks-keyservers.net
    <Yvzabevn> 1 key imported, 0 unchanged, 0 not imported.

Now I can get token to sign so I can identify::

    <Guest45020> +gpg gettoken
    <Yvzabevn> Your token is: {03640620-97ea-4fdf-b0c3-ce8fb62f2dc5}. Please sign it with your GPG key, paste it somewhere, and call the 'auth' command with the URL to the (raw) file containing the signature.

Then I follow the instructions and sign my token in terminal::

    echo "{03640620-97ea-4fdf-b0c3-ce8fb62f2dc5}"|gpg --clearsign|curl -F 'sprunge=<-' http://sprunge.us

Note that I sent the output to curl with flags to directly send the 
clearsigned content to sprunge.us pastebin. Curl should be installed on
most of distributions and comes with msysgit. If you remove the curl part,
you get the output to terminal and can pastebin it to any pastebin of 
your choice. Sprunge.us has only plain text and is easy so I used it in
this example.

And last I give the bot link to the plain text signature::

    <Guest45020> +gpg auth http://sprunge.us/DUdd     
    <Yvzabevn> You are now authenticated as Mikaela.

NickAuth
^^^^^^^^

This requires you to load the NickAuth plugin (see next section of this 
page for loading plugins).

NickAuth allows you to identify to the bot using your NickServ account. 
First I add my NickServ account name which I can see with "/whois Mikaela Mikaela" (because my current nick is Mikaela). It gives me something like::

    [Mikaela] is logged in as Mikaela

Now I tell the bot add my NickServ account Mikaela to my bot user on 
Libera. The syntax is [<network>] <bot-username> <NickServ-account>::

    <Mikaela> +nickauth nick add Libera Mikaela Mikaela
    <Yvzabevn> OK.

Next time when I identify to NickServ I will get identified automatically
if the bot sees that I was identified when I joined. This requires server
to support extended-join and WHOX. Most of modern networks support
them, but if your bot is using some bouncer, it might not support them.

Automatic identification doesn't work always even when it's supported, but
when it fails, I can always use the NickAuth Auth command to identify to
the bot::

    <Guest45020> +whoami
    <Yvzabevn> I don't recognize you. You can messsage me either of these two commands: "user identify <username> <password>" to log in or "user register <username> <password>" to register.
    <Guest45020> +nickauth auth
    <Yvzabevn> You are now authenticated as Mikaela.

Loading Plugins
===============

Let's take a look at loading other plugins.  If you didn't use supybot-wizard,
though, you might do well to try it before playing around with loading plugins
yourself: each plugin has its own configure function that the wizard uses to
setup the appropriate registry entries if the plugin requires any.

If you do want to play around with loading plugins, you're going to need to
have the owner capability.

Remember earlier when I told you to try ``help load``?  That's the very command
you'll be using. Basically, if you want to load, say, the Games plugin, then
``load Games``.  Simple, right?  If you need a list of the plugins you can load,
you'll have to list the directory the plugins are in (using whatever command
is appropriate for your operating system, either 'ls' or 'dir').

Understanding the help syntax
=============================

The syntax of a command describes how to run a command.
The syntax is given by the help command.
Some examples:

help [<plugin>] [<command>]
    This is the help of :ref:`command-plugin-help`.

    The chevrons mean you have to replace <plugin> and <command> by a plugin
    name and a command name.

    The brackets mean the argument they wrap is **optional**.

    So, the fellowing commands are correct::
    
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

    This two commands are ok::

        <user> join #limnoria
        <user> join #limnoria MySecretKey

utilities last <text> [<text> ...]
    This is the help for :ref:`command-utilities-last`.
    By the way, there is another ``last`` command in the `Misc` plugin, which
    doesn't do the same thing, that's why you need to give the plugin name.

    You have to give at least one argument, but you can give as many as you
    wish.

Getting More From Your Limnoria
===============================

Another command you might find yourself needing somewhat often is the 'more'
command.  The IRC protocol limits messages to 512 bytes, 60 or so of which
must be devoted to some bookkeeping.  Sometimes, however, Limnoria wants to
send a message that's longer than that.  What it does, then, is break it into
"chunks" and send the first one, following it with ``(X more messages)`` where
X is how many more chunks there are.  To get to these chunks, use the `more`
command.  One way to try is to look at the default value of
`supybot.replies.genericNoCapability` -- it's so long that it'll stretch
across two messages::

    <jemfinch|lambda> $config default
                      supybot.replies.genericNoCapability
    <lambdaman> jemfinch|lambda: You're missing some capability
                you need. This could be because you actually
                possess the anti-capability for the capability
                that's required of you, or because the channel
                provides that anti-capability by default, or
                because the global capabilities include that
                anti-capability. Or, it could be because the
                channel or the global defaultAllow is set to
                False, meaning (1 more message)
    <jemfinch|lambda> $more
    <lambdaman> jemfinch|lambda: that no commands are allowed
                unless explicitly in your capabilities. Either
                way, you can't do what you want to do.

So basically, the bot keeps, for each person it sees, a list of "chunks" which
are "released" one at a time by the `more` command.  In fact, you can even get
the more chunks for another user: if you want to see another chunk in the last
command jemfinch gave, for instance, you would just say `more jemfinch` after
which, his "chunks" now belong to you.  So, you would just need to say `more`
to continue seeing chunks from jemfinch's initial command.

Final Word
==========

You should now have a solid foundation for using Limnoria.  You can use the
`list` command to see what plugins your bot has loaded and what commands are
in those plugins; you can use the 'help' command to see how to use a specific
command, and you can use the 'more' command to continue a long response from
the bot.  With these three commands, you should have a strong basis with which
to discover the rest of the features of Limnoria!

Do be sure to read our other documentation and make use of the resources we
provide for assistance; this website and, of course, #limnoria on
irc.libera.chat if you run into any trouble!
