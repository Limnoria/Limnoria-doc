.. _capabilities:

************
Capabilities
************

Introduction
------------

Limnoria's access control feature is called the *capabilities* system. This behaves
similarly to access flags, except the name of each flag reflects a command
name in the bot. Compared to a traditional access scheme based on numeric levels
or flags with hardcoded meanings, this system aims to be both more expressive
and self-documenting.

Capabilities and Anticapabilities
---------------------------------

Capabilities are automatically checked whenever someone runs a bot command.
Each command implicitly has a **capability** and an **anticapability** based on
its command name. For instance, the ``rot13`` command will have "rot13" as its
capability and "-rot13" as its anticapability. This command does not require
special privileges, so by default, everyone will have the "rot13" capability
unless they also have the corresponding "-rot13" anticapability.

In short, capabilities declare what a user *can* do, while anticapabilities
declare what a user *cannot* do.

Capabilities and anticapabilities may take many forms, to account for many
plugins potentially having the same command name:

- "rot13", "-rot13": applies to all commands named ``rot13``
- "Filter.rot13", "-Filter.rot13": applies to only the *Filter* plugin's ``rot13`` command
- "Filter", "-Filter": applies to all commands in the *Filter* plugin

Compound command names like ``user hostmask add`` are also supported, and can
be matched many ways:

- "add" (last part of command name)
- "User" (plugin name)
- "User.hostmask.add" (full command name)
- "User.hostmask" (all commands under ``user hostmask``)

Capabilities can be assigned to bot users either globally, or on a per-channel
basis using "channel capabilities". The commands to do so are described in the
:ref:`Managing capabilities <capabilities-manage>` section.

Channel capabilities
^^^^^^^^^^^^^^^^^^^^

In addition to global capabilities, Limnoria also defines channel-specific
capabilities in the form "#channel,capability". These take the form of a
regular (anti)capability, but with a channel name prefix.

For example, if someone runs the ``echo`` command in a channel named "#chat",
the bot will check:

- Whether the caller has the global "-echo" anticapability
- Whether the caller has the global "echo" capability
- Whether the caller has the "#chat,-echo" anti-channel capability
- Whether the caller has the "#chat,echo" channel capability

These 4 checks will then be repeated for the "Utilities" and "Utilities.echo"
capabilities, as the ``echo`` command is part of the *Utilities* plugin.

Beyond solely restricting privileged commands, the capabilities system allows
toggling access for all commands on a global or per-channel level. See the
:ref:`Example section <capabilities-example>` for some examples on how to do
this.

.. _built-in-capabilities:
Special Built-in Capabilities
-----------------------------

Limnoria includes some special built-in capabilities, which are described below:

owner
^^^^^

"owner" is the highest-privilege capability inside Limnoria. It is typically
reserved for the bot owner that also has shell access to the machine running
Limnoria, and grants them access to *all* commands on the bot.
By default, this also allows downloading third-party plugins and thus running
arbitrary code as the bot's system user. (This can be further hardened, see the
:ref:`Security <security>` page for more details.)

The more technical definition is that users with the "owner" capability have
all capabilities and override all anticapabilities.

For security reasons, this capability cannot be added to users via IRC.
Instead, you will need to run the ``supybot-adduser`` script or edit the
configuration manually to add an owner user.

admin
^^^^^

"admin" is the less-privileged capability for bot administrators. They can
do things such as change the bot's nick, manage ignored users, make the bot
join or part channels, etc. They cannot, however, load plugins or connect the
bot to new networks.

This capability does not automatically grant access to channel administration
commands, which is instead included in the following capability.

.. _built-in-capabilities-channel-op:
#channel,op
^^^^^^^^^^^

The "#channel,op" capability allows a caller to use channel administration
commands such as ``op``, ``kban`` (kickban), and ``channel ignore add``
(setting a channel-specific user to ignore). "#channel" should be replaced with
the actual name of the channel, such as "#limnoria".

The "#channel,op" capability implies all channel capabilities for a particular
channel, and overrides any channel anticapabilities. (It is akin to the "owner"
capability, but on a per-channel basis.)

When the AutoMode plugin is loaded, the bot will automatically try to grant
op (@) to users with this capability when they join.

#channel,halfop
^^^^^^^^^^^^^^^

Grants access to the ``halfop`` command (i.e. asking the bot to give you halfop).

When the AutoMode plugin is loaded, the bot will automatically try to grant
halfop (%) to users with this capability when they join.

#channel,voice
^^^^^^^^^^^^^^

Grants access to the ``voice`` command (i.e. asking the bot to give you voice).

When the AutoMode plugin is loaded, the bot will automatically try to grant
voice (+) to users with this capability when they join.

trusted
^^^^^^^

The "trusted" capability grants people access to commands that may slow down or
crash the bot, but do not otherwise demand special permissions. One example is
the ``icalc`` command in the *Math* plugin, which allows trusted users to run
large calculations even if they never complete (e.g. 10**10**10**10).

.. _capabilities-manage:
Managing capabilities
---------------------

Managing User and Channel Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User capabilities are controlled with the ``admin capability <add|remove>`` commands.
These commands can only be used by admins (those who have the "admin" capability),
and admins can only grant capabilities that they have themselves.

To make user1 admin, run::

    admin capability add user1 admin

To undo this, run::

    admin capability remove user1 admin

Channel capabilities are managed with the  ``channel capability <add|remove>``
commands. These commands require the ``#channel,op`` capability for a channel.

To give user2 op privileges for #channel::

    channel capability add #channel user2 op

The above command is equivalent to::

    admin capability add user2 #channel,op

but this requires the caller to have the ``admin`` capability in addition to ``#channel,op``.

Anticapabilities override capabilities. For instance, if user3 had the "op"
capability on #channel, this can be removed with either::

    channel capability add user3 -op

or::

    channel capability remove user3 op

Finally, user capabilities can be viewed with ``user capabilities`` command.

Managing Default Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default capabilities affect everyone, whether they are logged in the the bot or
not. They are controlled by the ``owner defaultcapability <add|remove>`` command.

As mentioned in the introduction, normally commands that do not require
special privileges are accessible by everyone. You can disable certain commands
by default by adding default anticapabilities. For instance, to disallow
users from registering new bot accounts::

    defaultcapability add -user.register

To undo this::

    defaultcapability remove -user.register

Default capabilities can be restored to default with the following command::

    config setdefault capabilities

Managing Channel Default Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Default channel capabilities affect everyone on a specific channel.
They are controlled with the ``channel capability <set|unset>`` commands.

For instance, to make everyone on the channel able to voice themselves and get
automatically voiced by the AutoMode plugin, unset the default anticapability
and set the capability::

    channel capability unset -voice
    channel capability set voice

If there was some unwanted plugin or plugin whose output was causing spam, Games
for example, a channel default anticapability can be added which prevents the
whole plugin from being used::

    channel capability set -Games

.. _capabilities-example:

Example: limiting noisy commands
--------------------------------

To make this less abstract, here is a popular example of what
capabilities are used for: disabling a plugin or command for everyone
but a select group of people.

Disallowing everyone from using the ``Games`` plugin, globally::

    defaultcapability add -games

Allowing only user ``foo`` to use the ``Games`` plugin, globally::

    admin capability add foo games

To undo all this::

    defaultcapability remove -Games
    admin capability remove foo Games

Same, but only on ``#channel``::

    channel capability set #channel -games
    channel capability add #channel foo games

    channel capability unset #channel -games
    channel capability remove #channel foo games


And to forbid only the ``dice`` command of the ``Games`` plugin instead of the
entire plugin, you would use the same commands, but with ``-games.dice`` and
``games.dice`` instead of ``-games`` and ``games``.


Final Word
----------

From a programmer's perspective, capabilities are flexible and easy to use.
The bulk of permission checking is abstracted away from the plugin itself,
so fine-grained access control is possible without extra code in each plugin.
Plugins may also check for custom capabilities - this only requires checking
for a specific capability name, and documenting somewhere how it is used.

From an bot owner's perspective, capabilities provide fine-grained access control
for both admins and regular users. Default capabilities can also be set for both
individual channels and the bot as a whole, allowing owners to set policies even
for users that are not registered with the bot.
