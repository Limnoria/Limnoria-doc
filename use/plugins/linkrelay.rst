
.. _plugin-linkrelay:

The LinkRelay plugin
====================

Highly configurable messages relay between channels.

.. include:: unofficial.inc

.. WARNING::

    This plugin exists both in :ref:`repository-progval` and in
    :ref:`repository-quantumlemur`. This doc is for the one in ProgVal's,
    because quantumlemur's is the same, without this commands.

.. _command-linkrelay-nosubstitute:

linkrelay nosubstitute <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Undo a substitution.

.. _command-linkrelay-nicks:

linkrelay nicks [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the nicks of the people in the linked channels.
*<channel>* is only necessary if the message
isn't sent on the channel itself.

.. _command-linkrelay-list:

linkrelay list
^^^^^^^^^^^^^^

Returns all the defined relay links

.. _command-linkrelay-remove:

linkrelay remove [--from <channel>@<network>] [--to <channel>@<network>] [--regexp <regexp>] [--reciprocal]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove a relay from the list. You must give at least *--from* or *--to;* if
one of them is not given, it defaults to the current channel@network.
Only messages matching *<regexp>* will be relayed; if *<regexp>* is not
given, everything is relayed.
If *--reciprocal* is given, another relay will be removed automatically,
in the opposite direction.

.. _command-linkrelay-add:

linkrelay add [--from <channel>@<network>] [--to <channel>@<network>] [--regexp <regexp>] [--reciprocal]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a relay to the list. You must give at least *--from* or *--to;* if
one of them is not given, it defaults to the current channel@network.
Only messages matching *<regexp>* will be relayed; if *<regexp>* is not
given, everything is relayed.
If *--reciprocal* is given, another relay will be added automatically,
in the opposite direction.

.. _command-linkrelay-substitute:

linkrelay substitute <regexp> <replacement>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces all nicks that matches the *<regexp>* by the *<replacement>*
string.

