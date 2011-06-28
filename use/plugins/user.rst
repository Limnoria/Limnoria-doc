
.. _plugin-user:

The User plugin
===============

.. _command-username:

username <hostmask|nick>
^^^^^^^^^^^^^^^^^^^^^^^^

Returns the username of the user specified by *<hostmask>* or *<nick>* if
the user is registered.


.. _command-set-password:

set password [<name>] <old password> <new password>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the new password for the user specified by *<name>* to *<new
password>*. Obviously this message must be sent to the bot
privately (not in a channel). If the requesting user is an owner
user (and the user whose password is being changed isn't that same
owner user), then *<old password>* needn't be correct.


.. _command-set-secure:

set secure <password> [<True|False>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the secure flag on the user of the person sending the message.
Requires that the person's hostmask be in the list of hostmasks for
that user in addition to the password being correct. When the
secure flag is set, the user *must* identify before he can be
recognized. If a specific True/False value is not given, it
inverts the current value.


.. _command-stats:

stats
^^^^^

Returns some statistics on the user database.


.. _command-hostmask-hostmask:

hostmask hostmask [<nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the hostmask of *<nick>*. If *<nick>* isn't given, return the
hostmask of the person giving the command.


.. _command-hostmask-list:

hostmask list [<name>]
^^^^^^^^^^^^^^^^^^^^^^

Returns the hostmasks of the user specified by *<name>*; if *<name>*
isn't specified, returns the hostmasks of the user calling the
command.


.. _command-hostmask-add:

hostmask add [<name>] [<hostmask>] [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds the hostmask *<hostmask>* to the user specified by *<name>*. The
*<password>* may only be required if the user is not recognized by
hostmask. *<password>* is also not required if an owner user is
giving the command on behalf of some other user. If *<hostmask>* is
not given, it defaults to your current hostmask. If *<name>* is not
given, it defaults to your currently identified name. This message
must be sent to the bot privately (not on a channel) since it may
contain a password.


.. _command-hostmask-remove:

hostmask remove <name> <hostmask> [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the hostmask *<hostmask>* from the record of the user
specified by *<name>*. If the hostmask given is 'all' then all
hostmasks will be removed. The *<password>* may only be required if
the user is not recognized by his hostmask. This message must be
sent to the bot privately (not on a channel) since it may contain a
password.


.. _command-unregister:

unregister <name> [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unregisters *<name>* from the user database. If the user giving this
command is an owner user, the password is not necessary.


.. _command-register:

register <name> <password>
^^^^^^^^^^^^^^^^^^^^^^^^^^

Registers *<name>* with the given password *<password>* and the current
hostmask of the person registering. You shouldn't register twice; if
you're not recognized as a user but you've already registered, use the
hostmask add command to add another hostmask to your already-registered
user, or use the identify command to identify just for a session.
This command (and all other commands that include a password) must be
sent to the bot privately, not in a channel.


.. _command-list:

list [--capability=<capability>] [<glob>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the valid registered usernames matching *<glob>*. If *<glob>* is
not given, returns all registered usernames.


.. _command-capabilities:

capabilities [<name>]
^^^^^^^^^^^^^^^^^^^^^

Returns the capabilities of the user specified by *<name>*; if *<name>*
isn't specified, returns the capabilities of the user calling the
command.


.. _command-unidentify:

unidentify
^^^^^^^^^^

Un-identifies you. Note that this may not result in the desired
effect of causing the bot not to recognize you anymore, since you may
have added hostmasks to your user that can cause the bot to continue to
recognize you.


.. _command-identify:

identify <name> <password>
^^^^^^^^^^^^^^^^^^^^^^^^^^

Identifies the user as *<name>*. This command (and all other
commands that include a password) must be sent to the bot privately,
not in a channel.


.. _command-whoami:

whoami
^^^^^^

Returns the name of the user calling the command.


.. _command-changename:

changename <name> <new name> [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes your current user database name to the new name given.
*<password>* is only necessary if the user isn't recognized by hostmask.
This message must be sent to the bot privately (not on a channel) since
it may contain a password.


