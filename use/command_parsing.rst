.. _command-parsing-primer:
======================
Command parsing primer
======================

This page discusses some of the details and features in Limnoria's command
parser, such as the ability to nest commands. This is mainly useful
when building :ref:`custom commands <custom-commands>` or
message triggers using the :ref:`Aka <plugin-aka>` and
:ref:`MessageParser <plugin-messageparser>` plugins.

.. _quoting-commands:
Quoting command arguments
-------------------------

In most cases, commands are simple enough that their arguments don't need to be
quoted::

  <jlu5> @echo hello world
  <Limnoria> hello world

However, when a command takes in multiple strings, you will have to quote
multi-word inputs to prevent them from being split::

  # wrong
  <jlu5> @sample 1 hello hi what's up
  <Limnoria> what's

  # right
  <jlu5> @sample 1 "hello" "hi" "what's up"
  <Limnoria> hello

Similarly, if a text argument includes ``"``, ``[``, or ``]``, you'll have to
quote it and escape any double quotes::

  <jlu5> @len "waiter, there's a \" in my soup!"
  <Limnoria> 31

  <jlu5> @echo "test" "test"
  <Limnoria> test test
  <jlu5> @echo "\"test\" \"test\""
  <Limnoria> "test" "test"

You can use quotes to express an empty argument::

  <jlu5> @format replace a "" abacadabra
  <Limnoria> bcdbr

And also to expand non-printable characters::

  <jlu5> @echo \x0308hello world
  <Limnoria> \x0308hello world

  <jlu5> @echo "\x0308hello world"
  # this text would be yellow on IRC
  <Limnoria> hello world

.. _nested-commands:
Nested commands
---------------

Commands can be nested in Limnoria by surrounding them in square brackets.
This example runs some text through two commands from the
:ref:`Filter <plugin-filter>` plugin::

  <jlu5> @caps [filter reverse hello world]
  <Limnoria> DLROW OLLEH

Similarly, the output of multiple commands can be combined using
:ref:`echo <command-utilities-echo>` or :ref:`reply <command-reply-reply>`.
The below command flips two coins using the :ref:`plugin-games` plugin::

  <jlu5> @echo [coin] [coin]
  <Limnoria> heads tails

  <jlu5> @reply [coin] [coin]
  <Limnoria> jlu5: heads heads

There are a few differences between ``echo`` and ``reply``:

- ``reply`` always prefixes the output with the caller's nick, while ``echo`` does not.
- ``echo`` supports standard substitutions, such as ``$nick``, ``$version``, etc., while ``reply`` does not

Note that the bot will always add spaces around the output of a nested
command. To work around this, you may want to use the
:ref:`concat <command-format-concat>` command to join two outputs without a space::

  <jlu5> @echo Random percent value: [dice 1d100]%
  <Limnoria> Random percent value: 56 %

  <jlu5> @echo Random percent value: [concat [dice 1d100]%]
  <Limnoria> Random percent value: 78%

The above example shows how commands can be nested more than once as well; this
limit is controlled by the :ref:`config option <configuration-guide>`
``commands.nested.maximum``.
