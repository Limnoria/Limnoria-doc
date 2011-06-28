
.. _plugin-scheduler:

The Scheduler plugin
====================

.. _command-scheduler-repeat:

scheduler repeat <name> <seconds> <command>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Schedules the command *<command>* to run every *<seconds>* seconds,
starting now (i.e., the command runs now, and every *<seconds>* seconds
thereafter). *<name>* is a name by which the command can be
unscheduled.

.. _command-scheduler-list:

scheduler list
^^^^^^^^^^^^^^

Lists the currently scheduled events.

.. _command-scheduler-add:

scheduler add <seconds> <command>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Schedules the command string *<command>* to run *<seconds>* seconds in the
future. For example, 'scheduler add [seconds 30m] "echo [cpu]"' will
schedule the command "cpu" to be sent to the channel the schedule add
command was given in (with no prefixed nick, a consequence of using
echo). Do pay attention to the quotes in that example.

.. _command-scheduler-remove:

scheduler remove <id>
^^^^^^^^^^^^^^^^^^^^^

Removes the event scheduled with id *<id>* from the schedule.

