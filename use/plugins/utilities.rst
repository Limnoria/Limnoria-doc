
.. _plugin-utilities:

The Utilities plugin
====================

.. _command-utilities-ignore:

utilities ignore requires no arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does nothing. Useful sometimes for sequencing commands when you don't
care about their non-error return values.

.. _command-utilities-shuffle:

utilities shuffle <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shuffles the arguments given.

.. _command-utilities-success:

utilities success [<text>]
^^^^^^^^^^^^^^^^^^^^^^^^^^

Does nothing except to reply with a success message. This is useful
when you want to run multiple commands as nested commands, and don't
care about their output as long as they're successful. An error, of
course, will break out of this command. *<text>*, if given, will be
appended to the end of the success message.

.. _command-utilities-echo:

utilities echo <text>
^^^^^^^^^^^^^^^^^^^^^

Returns the arguments given it. Uses our standard substitute on the
string(s) given to it; $nick (or $who), $randomNick, $randomInt,
$botnick, $channel, $user, $host, $today, $now, and $randomDate are all
handled appropriately.

.. _command-utilities-sample:

utilities sample <num> <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Randomly chooses *<num>* items out of the arguments given.

.. _command-utilities-countargs:

utilities countargs <arg> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Counts the arguments given.

.. _command-utilities-last:

utilities last <text> [<text> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the last argument given. Useful when you'd like multiple
nested commands to run, but only the output of the last one to be
returned.

.. _command-utilities-apply:

utilities apply <command> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tokenizes *<text>* and calls *<command>* with the resulting arguments.



.. _plugin-utilities-config:

Configuration
-------------

.. _supybot.plugins.Utilities.public:

supybot.plugins.Utilities.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

