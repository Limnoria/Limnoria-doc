
.. _plugin-todo:

The Todo plugin
===============

.. command-die:

die 
^^^^



.. command-search:

search [--{regexp} <value>] [<glob> <glob> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches your todos for tasks matching *<glob>*. If *--regexp* is given,
its associated value is taken as a regexp and matched against the
tasks.


.. command-remove:

remove <task id> [<task id> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes *<task id>* from your personal todo list.


.. command-add:

add [--priority=<num>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds *<text>* as a task in your own personal todo list. The optional
priority argument allows you to set a task as a high or low priority.
Any integer is valid.


.. command-setpriority:

setpriority <id> <priority>
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the priority of the todo with the given id to the specified value.


.. command-todo:

todo [<username>] [<task id>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieves a task for the given task id. If no task id is given, it
will return a list of task ids that that user has added to their todo
list.


.. command-change:

change <task id> <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^

Modify the task with the given id using the supplied regexp.


