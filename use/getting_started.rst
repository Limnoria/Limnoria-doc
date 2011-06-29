.. highlight:: none

.. _getting-started:

****************************
Getting started with Supybot
****************************

Conventions used by Supybot and this document
=============================================

Vocabulary
----------

Plugin
    A plugin contains commands. A plugin can be loaded and unloaded on
    the fly, as you wish.
    Plugin names are always capitalized, and may contain other uppercase
    letter, as a separation between two words, because they cannot contain
    spaces.

Command
    Commands can be called by users of the bot.
    Command names are always lowercased; they always have an help message, that
    can be requested at any moment

Argument
    Most of the commands requires arguments, in order to give them more
    informations about what you want it to do.

Configuration variable
    A configuration variable is set either by a bot owner or by a channel op.

Syntax of the commands
----------------------

The syntax of a command describes how to run a command.
The syntax is given by the help command.
Some examples:

help [<plugin>] [<command>]
    This is the help of :ref:`command-plugin-help`.

    The chevrons mean you have to replace <plugin> and <command> by a plugin
    name and a command name.

    The brackets mean the argument they wrap is **optional**.

    So, the fellowing commands are correct::
    
        help
        help PluginName
        help PluginName CommandName
        help CommandName

ping takes no arguments
    This is the help for :ref:`command-misc-ping`.

    I think it is clear enough.

join <channel> [<key>]
    This is the help for :ref:`command-admin-join`.
    
    It requires a channel name, and the channel key is optional.

    This two commands are ok::

        join #limnoria
        join #limnoria MySecretKey

utilities last <text> [<text> ...]
    This is the help for :ref:`command-utilities-last`.
    By the way, there is another ``last`` command in the `Misc` plugin, which
    doesn't do the same thing, that's why you need to give the plugin name.

    You have to give at least one argument, but you can give as many as you
    wish.

Basics
======

Identifying with the bot
------------------------

Everything you want to do with your bot should be done on IRC (apart starting
the bot, of course). That's why the first thing you need to do is getting your
bot know your are its owner, unless what it won't obey you for administrative
commands.

Open a query window with the bot (make sure this is your bot), and write in
it::
    
    identify <name> <password>

where *<name>* and *<password>* are the name and the password you gave to the
*supybot-wizard*.

Sending the bot a command
-------------------------

There are four ways to ask the bot to do something:

* Give the command in private;
* Give the command on a channel with a prefix character, either set in the
  wizard or in the configuration;
* Give the command on a channel prefixed by the nick;
* Give the command on a channel, prefixed by a string of characters, set in
  the config.

In this documentation, we the bot is called *mybot*, and its prefix char is @,
because @ is the most common prefix for Supybot; and the bot doesn't have a
prefix string of characters.
