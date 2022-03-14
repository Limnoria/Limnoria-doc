.. _user-faq:

**************************
Frequently Asked Questions
**************************

This section tries to cover all questions you may have as a Limnoria user or
administrator.
(For questions about plugin development, check out the
:ref:`Developer FAQ <user-faq>` instead.)

.. _user-faq-multi-servers:

How do I make my Supybot connect to multiple servers?
=====================================================

  Just use the `connect` command in the `Network` plugin.

.. _user-faq-recognize-owner:

Why does my bot not recognize me or tell me that I don't have the 'owner' capability?
=====================================================================================

  Because you've not given it anything to recognize you from!

  You'll need to identify to the bot (``help identify`` to see how
  that works) or add your hostmask to your user record (``help hostmask
  add`` to see how that works) for it to know that you're you.

  You may wish to note that ``hostmask add`` can accept a password; rather
  than identify, you can send the command::

    hostmask add myOwnerUser [hostmask] myOwnerUserPassword

  and the bot will add your current hostmask to your owner user (of
  course, you should change myOwnerUser and myOwnerUserPassword
  appropriately for your bot).

  For additional ways to identify to your bot, you may want to see
  :ref:`getting-started`.

.. _user-faq-hostmask:

What is a hostmask?
===================

  Each user on IRC is uniquely identified by a string which we call a
  `hostmask`. The IRC RFC refers to it as a prefix. Either way, it
  consists of a nick, a user, and a host, in the form
  ``nick!user@host``.  If your Supybot complains that something you've
  given to it isn't a hostmask, make sure that you have those three
  components and that they're joined in the appropriate manner.

.. _user-faq-bracket-nicks:

My bot can't handle nicks with brackets in them!
================================================

  It always complains about something not being a valid command, or
  about spurious or missing right brackets, etc.

  You should quote arguments (using double quotes, like this:
  ``"foo[bar]"``) that have brackets in them that you don't wish to be
  evaluated as nested commands. Alternatively, you can turn off nested
  commands by setting `supybot.commands.nested` to False, or change the
  brackets that nest commands by setting
  `supybot.commands.nested.brackets` to some other value (like ``<>``,
  which can't occur in IRC nicks).

.. _user-faq-create-command:

How do I create a command?
==========================

  You can create simple commands with the Aka plugin, like this::

    <admin> @aka add "rules" "echo Here are the rules of the channel."
    <bot> Ok.
    [...]
    <user> @rules
    <bot> Here are the rules of the channel.

  You can also make the bot reply on arbitrary words, MessageParser::

    <admin> @messageparser add "some words" "echo Blah blah"
    <bot> Ok
    [...]
    <user> I am saying some words.
    <bot> Blah blah

  Both these examples assume you have the Utilities plugin loaded
  (it provides the ``echo`` command).

  See the help of ``aka add``, ``messageparser add``, and ``echo``
  to see more advanced uses of these commands
  (command arguments, regular expressions, variables, etc.)

  While powerful, Aka and MessageParser cannot do everything.
  For the most advanced commands, you will need to
  :ref:`write your own plugin in Python <develop-plugins>`.

.. _user-faq-migrate-to-aka:

I loaded Alias before, how do I move to Aka?
============================================

  First load both of the plugins, Aka and Alias. Then run
  ``aka importaliasdatabase`` and ``unload Alias``. Now all your aliases
  should be imported to the Aka plugin.

.. _user-faq-aka-unquoted:

I added an aka, but it doesn't work!
====================================

  Take a look at ``aka show <aka you added>``. If the aka the bot has
  listed doesn't match what you're giving it, chances are you need to
  quote your aka in order for the brackets not to be evaluated. For
  instance, if you're adding an aka to give you a link to your
  homepage, you need to say::

    aka add mylink "format concat https://example.com/ [urlquote $1]"

  and not::

    aka add mylink format concat https://example.com/ [urlquote $1]

  The first version works; the second version will always return the
  same url.

.. _user-faq-lobotomized:

What does 'lobotomized' mean?
=============================

  I see this word in commands and in my `channels.conf`, but I don't
  know what it means. What does Supybot mean when it says lobotomized?

  A lobotomy is an operation that removes the frontal lobe of the brain,
  the part that does most of a person's thinking. To lobotomize a bot
  is to tell it to stop thinking--thus, a lobotomized bot will not
  respond to anything said by anyone other than its owner in whichever
  channels it is lobotomized.

  The term is certainly suboptimal, but remains in use because it was
  historically used by certain other IRC bots, and we wanted to ease the
  transition to Supybot from those bots by reusing as much terminology
  as possible.

.. _user-faq-load-all-plugins:

Is there a way to load all the plugins Supybot has?
===================================================

  No, there isn't. Even if there were, some plugins conflict with other
  plugins, so it wouldn't make much sense to load them. For instance,
  what would a bot do with `Factoids`, `MoobotFactoids`, and `Infobot`
  all loaded? Probably just annoy people :)

  You can also install user-contributed plugins using the PluginDownloader
  plugin (``load PluginDownloader``). The ``repolist`` command can list
  repositories and their contents, and the ``install`` command installs
  plugins.

.. _user-faq-list-required-capabilities:

Is there a command that can tell me what capability another command requires?
=============================================================================

  No, there isn't, and there probably never will be.

  Commands have the flexibility to check any capabilities they wish to
  check; while this flexibility is useful, it also makes it hard to
  guess what capability a certain command requires. We could make a
  solution that would work in a large majority of cases, but it wouldn't
  (and couldn't!) be absolutely correct in all circumstances, and since
  we're anal and we hate doing things halfway, we probably won't ever
  add this partial solution.

.. _user-faq-karma-not-working:

Why doesn't `Karma` seem to work for me?
========================================

  `Karma`, by default, doesn't acknowledge karma updates. If you check
  the karma of whatever you increased/decreased, you'll note that your
  increment or decrement still took place. If you'd rather `Karma`
  acknowledge karma updates, change the `supybot.plugins.Karma.response`
  configuration variable to "True".

.. _user-faq-ignore-private-message:

Why won't Supybot respond to private messages?
==============================================

  The most likely cause is that your bot has a mode blocking messages
  from unregistered users. Around Sept. 2005, for example, Freenode added
  a user mode where registered users could set ``+R``, which `blocks`_
  private messages from unregistered users. So, the reason you aren't
  seeing a response from your Supybot is likely:

  * Your Supybot is not registered with NickServ, you are registered,
    and you have set the +R user mode for yourself.

  * or: you have registered your Supybot with NickServ, you aren't
    registered, and your Supybot has the +R user mode set.

.. _user-faq-admin-change-config:

Can users with the admin capability change the configuration?
=============================================================

  Currently, no.  Feel free to make your case to us as to why a certain
  configuration variable should only require the `admin` capability
  instead of the `owner` capability, and if we agree with you, we'll
  change it for the next release.

.. _user-faq-log-channel:

How can I make my Supybot log my IRC channel?
=============================================

  To log all the channels your Supybot is in, simply load the
  `ChannelLogger` plugin, which is included in the main distribution.

.. _user-faq-irc-proxy:

Can Supybot connect through a proxy server?
===========================================

  Limnoria can connect to specific network using socks proxy, simply set 
  the configuration variable `supybot.networks.<network>.socksproxy`. For
  specifying proxy which is used for HTTP requests, set the configuration
  variable `supybot.protocols.http.proxy`.
  
  Supybot also works with transparent proxy server helpers like tsocks_ 
  that are designed to proxy-enable all network applications, and Supybot
  does work with these.

.. _user-faq-cannot-find-plugin:

Why can't Supybot find the plugin I want to load?
=================================================

  Why does my bot say that 'No plugin "foo" exists.' when I try to load
  the foo plugin?

  First, make sure you are typing the plugin name correctly.  ``@load
  foo`` may not be the same as ``@load Foo`` depending on your Supybot
  version  [#plugindir]_.  If that is not the problem, 

.. [#plugindir] Yes, it used to be the same, but then we moved to using
   directories for plugins instead of a single file.  Apparently, that
   makes a difference to Python.

.. _user-faq-report-bug:

I've found a bug, what do I do?
===============================

  Submit your bug at our `issue tracker`_.

.. _user-faq-python-installed:

Is Python installed?
====================

  I run Windows, and I'm not sure if Python is installed on my computer.
  How can I find out for sure?

  Python isn't commonly installed by default on Windows computers.  If
  you don't see it in your start menu somewhere, it's probably not
  installed.

  The easiest way to find out if Python is installed is simply to
  `download it`_ and try to install it.  If the installer complains, you
  probably already have it installed.  If it doesn't, well, now you have
  Python installed.

.. _user-faq-snarf-titles:

How can I make the bot announce titles of URLs (links) posted in channels
=========================================================================

This is called the "title snarfer". You can enable it with::

    load Web
    config supybot.plugins.Web.titleSnarfer True

If you only want it for some channels but not all, use this instead of the last command::

    config channel #channel supybot.plugins.Web.titleSnarfer True

.. _user-faq-title-snarfer-ignoring-website:

Why doesn't the title snarfer announce links from a particular website (eg. Youtube)?
=====================================================================================

Limnoria needs to fetch pages to get their title. But in order to avoid being
overloaded by users, it only fetches the beginning (the first 8kB if I recall
correctly). That's enough to find the title of most pages, but in the last years
Youtube has become so bloated it isn't.

If you are ok with Limnoria fetching more data when users post URLs, you can use::

    config supybot.protocols.http.peekSize 300000

This will make it fetch 300kB from every link, instead of the default 8kB.
This should be enough for Youtube for now. If not enough for other websites,
try increasing it further.

.. _user-faq-make-silent:

Can I make Supybot silent, but still working on channel (as titlesnarfer or something)?
=======================================================================================

With lobotomy, the bot stops doing everything on the channel. If you want
it to not reply to commands, but still work as titlesnarfer or similar, you
can configure it to not respond to anything.

Globally::

    config supybot.reply.whenAddressedBy.chars ""
    config supybot.reply.whenAddressedBy.nicks ""
    config supybot.reply.whenAddressedBy.strings ""
    config supybot.reply.whenAddressedBy.nick False
    config supybot.reply.whenAddressedBy.nick.atEnd False

Or just for one channel::

    config channel #channel supybot.reply.whenAddressedBy.chars ""
    config channel #channel supybot.reply.whenAddressedBy.nicks ""
    config channel #channel supybot.reply.whenAddressedBy.strings ""
    config channel #channel supybot.reply.whenAddressedBy.nick False
    config channel #channel supybot.reply.whenAddressedBy.nick.atEnd False

.. _user-faq-make-connection-secure:
.. _how-to-make-a-connection-secure:

How to make a connection secure?
================================

First, you should make the bot use SSL for each network::

    config supybot.networks.<NETWORK>.ssl on

Then, you must update the server port for the network the bot connects to (this is
usually 6697, but some networks use a different one)::

    config supybot.networks.<NETWORK>.servers irc.network.com:6697

In the previous command, you must of course replace `irc.network.com` with the
hostname of a server of the network. You could either check out the network's
website, or get the current one, with this command::

    config supybot.networks.<NETWORK>.servers


.. _blocks: https://libera.chat/guides/usermodes#main
.. _tsocks: http://tsocks.sourceforge.net
.. _issue tracker: https://github.com/ProgVal/Limnoria/issues
.. _download it: https://python.org/download/
