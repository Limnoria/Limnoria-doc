
.. _plugin-seen:

The Seen plugin
===============

.. _command-seen-user:

seen user [<channel>] <name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the last time *<name>* was seen and what *<name>* was last seen
saying. This looks up *<name>* in the user seen database, which means
that it could be any nick recognized as user *<name>* that was seen.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-seen-seen:

seen seen [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the last time *<nick>* was seen and what *<nick>* was last seen
saying. *<channel>* is only necessary if the message isn't sent on the
channel itself. *<nick>* may contain * as a wildcard.

.. _command-seen-any:

seen any [<channel>] [--user <name>] [<nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the last time *<nick>* was seen and what *<nick>* was last seen
doing. This includes any form of activity, instead of just PRIVMSGs.
If *<nick>* isn't specified, returns the last activity seen in
*<channel>*. If *--user* is specified, looks up name in the user database
and returns the last time user was active in *<channel>*. *<channel>* is
only necessary if the message isn't sent on the channel itself.

.. _command-seen-last:

seen last [<channel>]
^^^^^^^^^^^^^^^^^^^^^

Returns the last thing said in *<channel>*. *<channel>* is only necessary
if the message isn't sent in the channel itself.

.. _command-seen-since:

seen since [<channel>] <nick>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the messages since *<nick>* last left the channel.

