
.. _plugin-channel:

The Channel plugin
==================

.. command-unmoderate:

unmoderate [<channel>]
^^^^^^^^^^^^^^^^^^^^^^

Sets -m on *<channel>*, making it so everyone can
send messages to the channel. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. command-devoice:

devoice [<channel>] [<nick> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will remove voice from all
the nicks given. If no nicks are given, removes voice from the person
sending the message.


.. command-lobotomy-list:

lobotomy list
^^^^^^^^^^^^^

Returns the channels in which this bot is lobotomized.


.. command-lobotomy-remove:

lobotomy remove [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will unlobotomize the
bot, making it respond to requests made in the channel again.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-lobotomy-add:

lobotomy add [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will "lobotomize" the
bot, making it silent and unanswering to all requests made in the
channel. *<channel>* is only necessary if the message isn't sent in
the channel itself.


.. command-deop:

deop [<channel>] [<nick> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will remove operator
privileges from all the nicks given. If no nicks are given, removes
operator privileges from the person sending the message.


.. command-nicks:

nicks [<channel>] [--count]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the nicks in *<channel>*. *<channel>* is only necessary if the
message isn't sent in the channel itself. Returns only the number of
nicks if *--count* option is provided.


.. command-limit:

limit [<channel>] [<limit>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the channel limit to *<limit>*. If *<limit>* is 0, or isn't given,
removes the channel limit. *<channel>* is only necessary if the message
isn't sent in the channel itself.


.. command-moderate:

moderate [<channel>]
^^^^^^^^^^^^^^^^^^^^

Sets +m on *<channel>*, making it so only ops and voiced users can
send messages to the channel. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. command-unban:

unban [<channel>] [<hostmask>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unbans *<hostmask>* on *<channel>*. If *<hostmask>* is not given, unbans
any hostmask currently banned on *<channel>* that matches your current
hostmask. Especially useful for unbanning yourself when you get
unexpectedly (or accidentally) banned from the channel. *<channel>* is
only necessary if the message isn't sent in the channel itself.


.. command-kick:

kick [<channel>] <nick>[, <nick>, ...] [<reason>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kicks *<nick>*(s) from *<channel>* for *<reason>*. If *<reason>* isn't given,
uses the nick of the person making the command as the reason.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-enable:

enable [<channel>] [<plugin>] [<command>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will enable the *<command>*
in *<channel>* if it has been disabled. If *<plugin>* is provided,
*<command>* will be enabled only for that plugin. If only *<plugin>* is
provided, all commands in the given plugin will be enabled. *<channel>*
is only necessary if the message isn't sent in the channel itself.


.. command-invite:

invite [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will invite *<nick>*
to join *<channel>*. *<channel>* is only necessary if the message isn't
sent in the channel itself.


.. command-dehalfop:

dehalfop [<channel>] [<nick> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will remove half-operator
privileges from all the nicks given. If no nicks are given, removes
half-operator privileges from the person sending the message.


.. command-alert:

alert [<channel>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^

Sends *<text>* to all the users in *<channel>* who have the *<channel>*,op
capability.


.. command-disable:

disable [<channel>] [<plugin>] [<command>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will disable the *<command>*
in *<channel>*. If *<plugin>* is provided, *<command>* will be disabled only
for that plugin. If only *<plugin>* is provided, all commands in the
given plugin will be disabled. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. command-key:

key [<channel>] [<key>]
^^^^^^^^^^^^^^^^^^^^^^^

Sets the keyword in *<channel>* to *<key>*. If *<key>* is not given, removes
the keyword requirement to join *<channel>*. *<channel>* is only necessary
if the message isn't sent in the channel itself.


.. command-ignore-list:

ignore list [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^

Lists the hostmasks that the bot is ignoring on the given channel.
*<channel>* is only necessary if the message isn't sent in the
channel itself.


.. command-ignore-remove:

ignore remove [<channel>] <hostmask>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will remove the
persistent ignore on *<hostmask>* in the channel. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-ignore-add:

ignore add [<channel>] <nick|hostmask> [<expires>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will set a persistent
ignore on *<hostmask>* or the hostmask currently
associated with *<nick>*. *<expires>* is an optional argument
specifying when (in "seconds from now") the ignore will expire; if
it isn't given, the ignore will never automatically expire.
*<channel>* is only necessary if the message isn't sent in the
channel itself.


.. command-cycle:

cycle [<channel>]
^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will cause the bot to
"cycle", or PART and then JOIN the channel. *<channel>* is only necessary
if the message isn't sent in the channel itself.


.. command-capability-set:

capability set [<channel>] <capability> [<capability> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will add the channel
capability *<capability>* for all users in the channel. *<channel>* is
only necessary if the message isn't sent in the channel itself.


.. command-capability-setdefault:

capability setdefault [<channel>] {True|False}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will set the default
response to non-power-related (that is, not {op, halfop, voice}
capabilities to be the value you give. *<channel>* is only necessary
if the message isn't sent in the channel itself.


.. command-capability-list:

capability list [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the capabilities present on the *<channel>*. *<channel>* is
only necessary if the message isn't sent in the channel itself.


.. command-capability-remove:

capability remove [<channel>] <name|hostmask> <capability> [<capability> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will take from the
user currently identified as *<name>* (or the user to whom *<hostmask>*
maps) the capability *<capability>* in the channel. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-capability-add:

capability add [<channel>] <nick|username> <capability> [<capability> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will give the user
*<name>* (or the user to whom *<nick>* maps)
the capability *<capability>* in the channel. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-capability-unset:

capability unset [<channel>] <capability> [<capability> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will unset the channel
capability *<capability>* so each user's specific capability or the
channel default capability will take precedence. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-kban:

kban [<channel>] [--{exact,nick,user,host}] <nick> [<seconds>] [<reason>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will kickban *<nick>* for
as many seconds as you specify, or else (if you specify 0 seconds or
don't specify a number of seconds) it will ban the person indefinitely.
*--exact* bans only the exact hostmask; *--nick* bans just the nick;
*--user* bans just the user, and *--host* bans just the host. You can
combine these options as you choose. *<reason>* is a reason to give for
the kick.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-halfop:

halfop [<channel>] [<nick> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,halfop capability, this will give all the
*<nick>*s you provide halfops. If you don't provide any *<nick>*s, this
will give you halfops. *<channel>* is only necessary if the message isn't
sent in the channel itself.


.. command-mode:

mode [<channel>] <mode> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the mode in *<channel>* to *<mode>*, sending the arguments given.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-ban-list:

ban list [<channel>]
^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will show you the
current persistent bans on #channel.


.. command-ban-remove:

ban remove [<channel>] <hostmask>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will remove the
persistent ban on *<hostmask>*. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. command-ban-add:

ban add [<channel>] <nick|hostmask> [<expires>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will effect a
persistent ban from interacting with the bot on the given
*<hostmask>* (or the current hostmask associated with *<nick>*. Other
plugins may enforce this ban by actually banning users with
matching hostmasks when they join. *<expires>* is an optional
argument specifying when (in "seconds from now") the ban should
expire; if none is given, the ban will never automatically expire.
*<channel>* is only necessary if the message isn't sent in the
channel itself.


.. command-voice:

voice [<channel>] [<nick> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,voice capability, this will voice all the
*<nick>*s you provide. If you don't provide any *<nick>*s, this will
voice you. *<channel>* is only necessary if the message isn't sent in the
channel itself.


.. command-op:

op [<channel>] [<nick> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have the #channel,op capability, this will give all the *<nick>*s
you provide ops. If you don't provide any *<nick>*s, this will op you.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


