
.. _plugin-brainfuck:

The Brainfuck plugin
====================

.. _command-brainfuck-brainfuck:

brainfuck brainfuck [--recover] [--input <characters>] <command>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interprets the given Brainfuck code. You should quote the code if you
use brackets, because Supybot would interpret it as nested commands.
If *--recover* is given, the bot will recover the previous processor
memory and memory pointer.
The code will be fed the *<characters>* when it asks for input.

.. _command-brainfuck-checksyntax:

brainfuck checksyntax <command>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tests the Brainfuck syntax without running it. You should quote the
code if you use brackets, because Supybot would interpret it as nested
commands.



.. _plugin-brainfuck-config:

Configuration
-------------

.. _supybot.plugins.Brainfuck.public:

supybot.plugins.Brainfuck.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

