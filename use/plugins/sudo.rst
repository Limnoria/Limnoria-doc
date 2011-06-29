
.. _plugin-sudo:

The Sudo plugin
===============

.. WARNING::

    Use this plugin carefully. It may be dangerous with a bad configuration.

.. include:: unofficial.inc

.. _command-sudo-sudo:

sudo sudo <commande> [<arg1> [<arg2> ...]]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Runs the command fellowing the Sudo rules.

.. _command-sudo-add:

sudo add [<priority>] <name> {allow,deny} [<hostmask>] <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new Sudo rule, called *<name>* with the given *<priority>*
(greatest numbers have precedence),
allowing or denying to run commands matching the pattern *<regexp>*,
from users to run commands as wearing the *<hostmask>*.
The *<priority>* must be a relative integer.
If *<priority>* is not given, it defaults to 0.
The *<hostmask>* defaults to your hostmask.
The *<hostmask>* is only needed if you set an 'allow' rule.

.. _command-sudo-remove:

sudo remove <id>
^^^^^^^^^^^^^^^^

Remove a Sudo rule.

