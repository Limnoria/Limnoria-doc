
.. _plugin-utilities:

The Utilities plugin
====================

.. _command-ignore:

ignore requires no arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does nothing. Useful sometimes for sequencing commands when you don't
care about their non-error return values.


.. _command-shuffle:

shuffle <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^

Shuffles the arguments given.


.. _command-success:

success [<text>]
^^^^^^^^^^^^^^^^

Does nothing except to reply with a success message. This is useful
when you want to run multiple commands as nested commands, and don't
care about their output as long as they're successful. An error, of
course, will break out of this command. *<text>*, if given, will be
appended to the end of the success message.


.. _command-echo:

echo <text>
^^^^^^^^^^^

Returns the arguments given it. Uses our standard substitute on the
string(s) given to it; $nick (or $who), $randomNick, $randomInt,
$botnick, $channel, $user, $host, $today, $now, and $randomDate are all
handled appropriately.


.. _command-sample:

sample <num> <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Randomly chooses *<num>* items out of the arguments given.


.. _command-countargs:

countargs <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Counts the arguments given.


.. _command-last:

last <text> [<text> ...]
^^^^^^^^^^^^^^^^^^^^^^^^

Returns the last argument given. Useful when you'd like multiple
nested commands to run, but only the output of the last one to be
returned.


.. _command-apply:

apply <command> <text>
^^^^^^^^^^^^^^^^^^^^^^

Tokenizes *<text>* and calls *<command>* with the resulting arguments.


