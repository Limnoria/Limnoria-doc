
.. _plugin-alias:

The Alias plugin
================

Protecting
----------

.. _command-alias-lock:

lock <alias>
^^^^^^^^^^^^

Locks an alias so that no one else can change it.

.. _command-alias-unlock:

unlock <alias>
^^^^^^^^^^^^^^

Unlocks an alias so that people can define new aliases over it.

Adding and removing
-------------------

.. _command-alias-add:

add <name> <alias>
^^^^^^^^^^^^^^^^^^

Defines an alias *<name>* that executes *<alias>*. The *<alias>*
should be in the standard "command argument [nestedcommand argument]"
arguments to the alias; they'll be filled with the first, second, etc.
arguments. $1, $2, etc. can be used for required arguments. @1, @2,
etc. can be used for optional arguments. $* simply means "all
remaining arguments," and cannot be combined with optional arguments.

.. _command-alias-remove:

remove <name>
^^^^^^^^^^^^^

Removes the given alias, if unlocked.

