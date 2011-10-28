
.. _plugin-todo:

The Todo plugin
===============

Reading
-------

.. _command-todo-todo:

todo todo [<username>] [<task id>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieves a task for the given task id. If no task id is given, it
will return a list of task ids that that user has added to their todo
list.

.. _command-todo-search:

todo search [--{regexp} <value>] [<glob> <glob> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches your todos for tasks matching *<glob>*. If *--regexp* is given,
its associated value is taken as a regexp and matched against the
tasks.

Editing
-------

.. _command-todo-add:

todo add [--priority=<num>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds *<text>* as a task in your own personal todo list. The optional
priority argument allows you to set a task as a high or low priority.
Any integer is valid.

.. _command-todo-remove:

todo remove <task id> [<task id> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes *<task id>* from your personal todo list.

.. _command-todo-setpriority:

todo setpriority <id> <priority>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the priority of the todo with the given id to the specified value.

.. _command-todo-change:

todo change <task id> <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Modify the task with the given id using the supplied regexp.



.. _plugin-todo-config:

Configuration
-------------

.. _supybot.plugins.Todo.allowThirdpartyReader:

supybot.plugins.Todo.allowThirdpartyReader
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether users can read the todo-list of another user.

.. _supybot.plugins.Todo.public:

supybot.plugins.Todo.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

