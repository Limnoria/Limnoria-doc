
.. _plugin-utilities:

The Utilities plugin
====================

.. command-ignore:

ignore requires no arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does nothing. Useful sometimes for sequencing commands when you don't
care about their non-error return values.


.. command-shuffle:

shuffle <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^

Shuffles the arguments given.


.. command-success:

success [<text>]
^^^^^^^^^^^^^^^^

Does nothing except to reply with a success message. This is useful
when you want to run multiple commands as nested commands, and don't
care about their output as long as they're successful. An error, of
course, will break out of this command. *<text>*, if given, will be
appended to the end of the success message.


.. command-echo:

echo <text>
^^^^^^^^^^^

Returns the arguments given it. Uses our standard substitute on the
string(s) given to it; $nick (or $who), $randomNick, $randomInt,
$botnick, $channel, $user, $host, $today, $now, and $randomDate are all
handled appropriately.


.. command-sample:

sample <num> <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Randomly chooses *<num>* items out of the arguments given.


.. command-countargs:

countargs <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Counts the arguments given.


.. command-last:

last <text> [<text> ...]
^^^^^^^^^^^^^^^^^^^^^^^^

Returns the last argument given. Useful when you'd like multiple
nested commands to run, but only the output of the last one to be
returned.


.. command-apply:

apply <command> <text>
^^^^^^^^^^^^^^^^^^^^^^

Tokenizes *<text>* and calls *<command>* with the resulting arguments.


