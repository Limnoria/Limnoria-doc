.. _using-wrap:

*****************************************************
Using commands.wrap to parse your command's arguments
*****************************************************

The :func:`supybot.commands.wrap` decorator is used to register functions as
plugin commands. It abstracts away the repetitive parts of command
parsing, as well as common checks for permissions and semantics
(e.g. for commands that must be associated with a channel).

If you kept the ``from supybot.commands import *`` import from the
plugin template, ``wrap`` should already be available in the global namespace.

.. contents::

Motivation
==========

In the old days, command parsing was done manually by every plugin function
and looked something like this::

    def repeat(self, irc, msg, args):
        """<num> <text>

        Repeats <text> <num> times.
        """
        (num, text) = privmsg.getArgs(args, required=2)
        try:
            num = int(num)
        except ValueError:
            raise callbacks.ArgumentError
        irc.reply(num * text)

For a simple command, the argument parsing and validation accounted for the
majority of the function contents. Compare this with the much shorter wrapped
version::

    @wrap(['int', 'text'])
    def repeat(self, irc, msg, args, num, text):
        """<num> <text>

        Repeats <text> <num> times.
        """
        irc.reply(text * num)

The goal of ``wrap`` is to abstract all these checks into a common place, so
that individual commands don't need as much boilerplate.

Syntax Description
==================

:func:`supybot.commands.wrap` is a decorator, and it takes in a list of
**converters**. Each converter is responsible for parsing a command argument or
performing some check; there is a
:ref:`list of converters <wrap-converter-list>` below.

The function being wrapped takes in one additional argument for
each converter's output variable. At runtime, the *converted* (parsed)
variables will be passed as ``arg1``, ``arg2``, etc. in order::

    @wrap(['converter1', 'converter2', ...])
    def commandname(self, irc, msg, args, <arg1>, <arg2>, ...):
        # ...

.. note::
    In older code you may see definitions in the form::

        commandname = wrap(commandname, ['converter1', 'converter2', ...])

    These are equivalent to the decorator syntax above.

Note that converters are specified by name as *strings*, to avoid conflicts
with built-in functions.

Some converters also take parameters. In these cases, they will be passed in as
a tuple containing the converter name as the first argument::

    @wrap([('converterWithArgs', 123, 456), 'converterWithoutArgs'])
    def commandname(self, irc, msg, args, arg1, arg2):
        # ...

Contexts: Optional Parameters and Multiple Values
=================================================

Whereas converters specify how to parse an individual argument, **converter
contexts** control the multiplicity and placement of a variable. This is akin
to ``nargs`` in :py:class:`argparse.ArgumentParser`, and allows defining
things like optional arguments.

An example, making the number of repetitions **optional** in the ``repeat`` command::

    @wrap([optional('int', 2), 'text'])
    def repeat(self, irc, msg, args, num, text):
        """[<num>] <text>

        Repeats <text> <num> times. <num> defaults to 2 if not specified.
        """
        irc.reply(text * num)

In this example, the command looks for an optional integer argument before the
text. If the num is not provided, e.g. by passing text that doesn't start with
a number, it will default to 2. The default value itself is also optional; it
falls back to ``None`` if not provided.

Another example, using the ``many`` context to parse
:ref:`at least one <wrap-multiplicity-handlers>` parameter::

    @wrap([many('float')])
    def average(self, irc, msg, args, nums):
        """<number 1> [<number 2> <number 3> ...]

        Returns the average of the numbers given.
        """

        average = sum(nums) / len(nums)
        irc.reply(average)

In this case, ``nums`` will be a *list* of numbers.

A :ref:`list of contexts <wrap-context-list>` is provided in this page.

.. _wrap-converters-for-state:
Using Converters to Check State
===============================

Some converters check the bot's state or output a variable from state.
For example, here is the definition of the ``seen`` command::

    @wrap(['channel', 'something'])
    def seen(self, irc, msg, args, channel, name):
        """[<channel>] <nick>

        Returns the last time <nick> was seen and what <nick> was last seen
        saying. <channel> is only necessary if the message isn't sent on the
        channel itself. <nick> may contain * as a wildcard.
        """
        # ...

If a channel is not specified but the command was run inside a channel, the
**channel** converter automatically fills that parameter with the current channel.
When running from a direct message, a channel *must* be specified or the command
will fail.

A more complex example is the ``kick`` command, which includes a couple of
state checks::

    @wrap(['op', ('haveHalfop+', _('kick someone')), commalist('nickInChannel'), additional('text')])
    def kick(self, irc, msg, args, channel, nicks, reason):
        """[<channel>] <nick>[, <nick>, ...] [<reason>]

        Kicks <nick>(s) from <channel> for <reason>.  If <reason> isn't given,
        uses the nick of the person making the command as the reason.
        <channel> is only necessary if the message isn't sent in the channel
        itself.
        """
        # ...

- The **op** converter checks that the caller has the op
  :ref:`capability <capabilities>` (permission) in the bot.
- The **haveHalfop+** converter checks that the bot itself has halfop or above
  in the channel, as otherwise it can't kick anyone.
- **commalist('nickInChannel')** verifies that each nick passed in the list corresponds to
  someone currently in the channel.

.. _wrap-converter-list:
Converter List
==============

Below is a list of all the available converters to use with ``wrap``. If the
converter accepts any arguments, they are listed after it and if they are
optional, the default value is shown.

Numbers and time
----------------

expiry
    Takes a number of seconds and adds it to the current time to create an
    expiration timestamp.

id, kind="integer"
    Returns something that looks like an integer ID number. Takes an optional
    "kind" argument for you to state what kind of ID you are looking for,
    though this doesn't affect the integrity-checking. Basically requires that
    the argument be an integer, does no other integrity-checking, and provides
    a nice error message with the kind in it.

index
    Basically ("int", "index"), but with a twist. This will take a 1-based
    index and turn it into a 0-based index (which is more useful in code). It
    doesn't transform 0, and it maintains negative indices as is (note that it
    does allow them!).

int, type="integer", p=None
    Gets an integer. The "type" text can be used to customize the error message
    received when the argument is not an integer. "p" is an optional predicate
    to test the integer with. If p(i) fails (where i is the integer arg parsed
    out of the argument string), the arg will not be accepted.

now
    Simply returns the current timestamp as an arg, does not reference or
    modify the argument list.

long, type="long"
    Basically the same as int minus the predicate, except that it converts the
    argument to a long integer regardless of the size of the int.

float, type="floating point number"
    Basically the same as int minus the predicate, except that it converts the
    argument to a float.

nonInt, type="non-integer value"
    Accepts everything but integers, and returns them unchanged. The "type"
    value, as always, can be used to customize the error message that is
    displayed upon failure.

positiveInt
    Accepts only positive integers.

nonNegativeInt
    Accepts only non-negative integers.

Channel
-------

channelDb
    Sets the channel appropriately in order to get to the databases for that
    channel (handles whether or not a given channel uses channel-specific
    databases and whatnot).

channel
    Gets a channel to use the command in. If the channel isn't supplied, uses
    the channel the message was sent in. If using a different channel, does
    sanity-checking to make sure the channel exists on the current IRC network.

inChannel
    Requires that the command be called from within any channel that the bot
    is currently in or with one of those channels used as an argument to the
    command.

onlyInChannel
    Requires that the command be called from within any channel that the bot
    is currently in.

callerInGivenChannel
    Takes the given argument as a channel and makes sure that the caller is in
    that channel.

public
    Requires that the command be sent in a channel instead of a private
    message.

private
    Requires that the command be sent in a private message instead of a
    channel.

validChannel
    Gets a channel argument once it makes sure it's a valid channel.

Words
-----

color
    Accepts arguments that describe a text color code (e.g., "black", "light
    blue") and returns the mIRC color code for that color. (Note that many
    other IRC clients support the mIRC color code scheme, not just mIRC)

letter
    Looks for a single letter. (Technically, it looks for any one-element
    sequence).

literal, literals, errmsg=None
    Takes a required sequence or string (literals) and any argument that
    uniquely matches the starting substring of one of the literals is
    transformed into the full literal. For example, with ``("literal", ("bar",
    "baz", "qux"))``, you'd get "bar" for "bar", "baz" for "baz", and "qux"
    for any of "q", "qu", or "qux". "b" and "ba" would raise errors because
    they don't uniquely identify one of the literals in the list. You can
    override errmsg to provide a specific (full) error message, otherwise the
    default argument error message is displayed.

lowered
    Returns the argument lowered (NOTE: it is lowered according to IRC
    conventions, which does strange mapping with some punctuation characters).

to
    Returns the string "to" if the arg is any form of "to" (case-insensitive).

Network
-------

ip
    Checks and makes sure the argument looks like a valid IP and then returns
    it.

url
    Checks for a valid URL.

httpUrl
    Checks for a valid HTTP URL.

Users, nicks, and permissions
-----------------------------

haveOp, action="do that"
    Simply requires that the bot have ops in the channel that the command is
    called in. The action parameter completes the error message: "I need to be
    opped to ...".

nick
    Checks that the arg is a valid nick on the current IRC server.

seenNick
    Checks that the arg is a nick that the bot has seen (NOTE: this is limited
    by the size of the history buffer that the bot has).

nickInChannel
    Requires that the argument be a nick that is in the current channel, and
    returns that nick.

capability
    Used to retrieve an argument that describes a capability.

hostmask
    Returns the hostmask of any provided nick or hostmask argument.

banmask
    Returns a generic banmask of the provided nick or hostmask argument.

user
    Requires that the caller be a registered user.

otherUser
    Returns the user specified by the username or hostmask in the argument.

owner
    Requires that the command caller has the "owner" capability.

admin
    Requires that the command caller has the "admin" capability.

checkCapability, capability
    Checks to make sure that the caller has the specified capability.

checkChannelCapability, capability
    Checks to make sure that the caller has the specified capability on the
    channel the command is called in.

Matching
--------

anything
    Returns anything as is.

something, errorMsg=None, p=None
    Takes anything but the empty string. errorMsg can be used to customize the
    error message. p is any predicate function that can be used to test the
    validity of the input.

somethingWithoutSpaces
    Same as something, only with the exception of disallowing spaces of course.

matches, regexp, errmsg
    Searches the args with the given regexp and returns the matches. If no
    match is found, errmsg is given.

regexpMatcher
    Gets a matching regexp argument (m// or //).

glob
    Gets a glob string. Basically, if there are no wildcards (``*``, ``?``) in
    the argument, returns ``*string*``, making a glob string that matches
    anything containing the given argument.

regexpReplacer
    Gets a replacing regexp argument (s//).

Other
-----

networkIrc, errorIfNoMatch=False
    Returns the IRC object of the specified IRC network. If one isn't
    specified, the IRC object of the IRC network the command was called on is
    returned.

plugin, require=True
    Returns the plugin specified by the arg or None. If require is True, an
    error is raised if the plugin cannot be retrieved.

boolean
    Converts the text string to a boolean value. Acceptable true values are:
    "1", "true", "on", "enable", or "enabled" (case-insensitive). Acceptable
    false values are: "0", false", "off", "disable", or "disabled"
    (case-insensitive).

filename
    Used to get a filename argument.

commandName
    Returns the canonical command name version of the given string (ie, the
    string is lowercased and dashes and underscores are removed).

text
    Takes the rest of the arguments as one big string. Note that this differs
    from the "anything" context in that it clobbers the arg string when it's
    done.  Using any converters after this is most likely incorrect.

.. _wrap-context-list:

Contexts List
=============

The list of available contexts is below. Unless specified otherwise, it can be
assumed that the type returned by the context itself matches the type of the
converter it is applied to.

Options
-------

optional
    Look for an argument that satisfies the supplied converter, but if it's not
    the type I'm expecting or there are no arguments for us to check, then use
    the default value. Will return the converted argument as is or None.

additional
    Look for an argument that satisfies the supplied converter, making sure
    that it's the right type. If there aren't any arguments to check, then use
    the default value. Will return the converted argument as is or None.

first
    Tries each of the supplied converters in order and returns the result of
    the first successfully applied converter.

.. _wrap-multiplicity-handlers:

Multiplicity
------------

any
    Looks for any number of arguments matching the supplied converter. Will
    return a sequence of converted arguments or None.

many
    Looks for multiple arguments matching the supplied converter. Expects at
    least one to work, otherwise it will fail. Will return the sequence of
    converted arguments.

commalist
    Looks for a comma separated list of arguments that match the supplied
    converter. Returns a list of the successfully converted arguments. If any
    of the arguments fail, this whole context fails.

Other
-----

rest
    Treat the rest of the arguments as one big string, and then convert. If the
    conversion is unsuccessful, restores the arguments.

getopts
    Handles --option style arguments. Each option should be a key in a
    dictionary that maps to the name of the converter that is to be used on
    that argument. To make the option take no argument, use "" as the converter
    name in the dictionary. For no conversion, use None as the converter name
    in the dictionary.

reverse
    Reverse the argument list, apply the converters, and then reverse the
    argument list back.


Final Word
==========

Now that you know how to use ``wrap``, writing clean and safe plugins should become
much easier. Enjoy!

