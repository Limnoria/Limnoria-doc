.. _custom-commands:

===============================
Creating custom commands (Akas)
===============================

Limnoria allows you create custom bot commands, also known as aliases, without
writing a full Python plugin. This feature is provided by the
:ref:`Aka <plugin-aka>` plugin, and can be combined with
:ref:`nested commands <nested-commands>` to create expressive commands.

Before proceeding through this page, we recommend reading the
:ref:`command-parsing-primer`, which discusses many of the details that apply
to building custom commands.

If you want to create custom message triggers that aren't bot commands, see the
:ref:`MessageParser guide <custom-regex-triggers>` instead.

.. contents::

Creating & managing aliases
---------------------------

Add an alias, ``trout``, which expects one argument (``$1``). This alias requires
the :ref:`plugin-reply` plugin to be loaded since it
provides the :ref:`action <command-reply-action>` command::

  <jamessan> @aka add trout "reply action slaps $1 with a large trout"
  <Limnoria> The operation succeeded.
  # $1 will be replaced with the input to @trout
  <jamessan> @trout me
  * Limnoria slaps me with a large trout

You can also replace an existing alias with ``aka set``::

  <jlu5> @aka set trout "reply Sorry, we're all out of fish!"
  <Limnoria> The operation succeeded.

To remove an alias, use ``aka remove``::

  <jlu5> @aka remove trout
  <Limnoria> The operation succeeded.

Alias with nested commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

Add an alias, ``randpercent``, which returns a random percentage value.
This requires the :ref:`plugin-filter` and :ref:`plugin-games` plugins for
:ref:`squish <command-filter-squish>` and :ref:`dice <command-games-dice>`
respetively::

  <jlu5> @aka add randpercent "squish [dice 1d100]%"
  <Limnoria> The operation succeeded.
  <jlu5> @randpercent
  <Limnoria> 66%

.. note::

  When defining aliases, you almost always want to **quote the contents** of
  the alias, so that any nested commands are expanded when the actual alias is
  ran, instead of when the ``aka add`` call happens.

  In this above example, not quoting the ``dice`` command would mean that the
  ``randpercent`` always returns the same value!

This, in conjunction with Limnoria's :ref:`command quoting rules <quoting-commands>`
means that aliases towards nested commands may require **two levels of quoting**,
with the inner quotes additionally escaped. This example uses the
:ref:`sample <command-utilities-sample>` command from the :ref:`plugin-utilities` plugin::

  <jlu5> @aka add greetme "reply [sample 1 \"hi there!\" \"what's up?\" \"how are you?\"]"
  <Limnoria> The operation succeeded.
  <jlu5> @greetme
  <Limnoria> jlu5: what's up?
  <jlu5> @greetme
  <Limnoria> jlu5: hi there!

Passing multiple arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^

Aliases can pass multiple arguments (``$1``, ``$2``, etc.), as well as all
remaining arguments (``$*``) to another command. A common use case of this
is to define short-forms to other commands, such as ``config``::

  <jlu5> @aka add cf "config $*"
  <Limnoria> The operation succeeded.

  # using this alias
  <jlu5> @cf reply.whenaddressedby.chars
  <Limnoria> @

Note that the following also works, because ``config`` is technically ambiguous
(it can refer to either the :ref:`plugin-config` plugin or the
:ref:`config <command-config-config>` command)::

  # "@cf help" expands to "@config help"
  <jlu5> @cf help reply.whenaddressedby.chars
  <Limnoria> Determines what prefix characters the bot will reply to. -snip-

Conditionals and optional arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aliases also support optional arguments, using ``@1``, ``@2``, etc. instead of
``$1`` and ``$2``. This can be combined with the :ref:`plugin-conditional`
plugin to make a custom command behave differently depending on how many
arguments were passed in.

Here's a variant of the ``trout`` example from earlier, which will now slap the
caller if no argument was passed in. It uses:

* The :ref:`command-conditional-cif` and :ref:`command-conditional-ceq` commands
  to define an if expression and check whether ``@1`` is an empty string.
* The :ref:`echo <command-utilities-echo>` command from the :ref:`plugin-utilities` plugin.

::

  <jlu5> @aka add trout "reply action slaps [cif [ceq \"@1\" \"\"] \"echo $nick\" \"echo @1\"] with a large trout"
  <Limnoria> The operation succeeded.
  <jlu5> @trout Limnoria
  * Limnoria slaps Limnoria with a large trout
  <jlu5> @trout
  * Limnoria slaps jlu5 with a large trout

Referring to other Akas
^^^^^^^^^^^^^^^^^^^^^^^

Because command aliases are expanded at runtime, they can refer to one another,
and even themselves.

Suppose I define an alias for the :ref:`sample <command-utilities-sample>` command::

  <jlu5> @aka add choose "sample 1 $*"
  <Limnoria> The operation succeeded.

Then I can define more aliases using the ``choose`` command::

  <jlu5> @aka add bloom "choose 🌼 💐 🌹 🌻 🌺 🌸"
  <Limnoria> The operation succeeded.
  <jlu5> @bloom
  <Limnoria> 💐

For completeness, here's an example of a (not particularly efficient) factorial
command. It additionally uses the :ref:`plugin-Math` plugin's
:ref:`calc <command-math-calc>` command::

  <jlu5> @aka add factorial "cif [nle $1 1] \"echo 1\" \"calc [factorial [calc $1 - 1]] * $1\""
  <Limnoria> The operation succeeded.
  <jlu5> @factorial 8
  <Limnoria> 40320
  <jlu5> @factorial 10
  <Limnoria> Error: You've attempted more nesting than is currently allowed on this bot.

Replacing an existing command with your own
-------------------------------------------

Using the :ref:`defaultplugin <command-owner-defaultplugin>` command, it is possible to "replace"
an existing command in the bot by defining an alias with the same name and running::

  @defaultplugin <command> Aka

As an example, you can replace the default :ref:`ping <command-misc-ping>`
reply from the Misc plugin with a silly response::

  <jlu5> @aka add ping "reply I don't respond to ping requests."
  <Limnoria> The operation succeeded.
  <jlu5> @defaultplugin ping Aka
  <Limnoria> The operation succeeded.
  <jlu5> @ping
  <Limnoria> jlu5: I don't respond to ping requests.

The old command will still be accessible via its full name::

  <jlu5> @misc ping
  <Limnoria> pong

If you want to remove access for a command entirely, you should configure
:ref:`default capabilities <capabilities-managing-defaults>` instead.

.. _custom-command-limitations:
Limitations, and when to write a plugin
---------------------------------------

Aliases and nested commands are *not* designed to replace plugins in all cases.
If you need any of the following, it's probably easier to
:ref:`write a custom plugin <plugin-tutorial>` instead:

* Persistent state (databases, etc.)
* For, while loops
* Access to web APIs or external Python libraries
* Fine-grained permission checks
* Threads / processes for slow or long-running tasks

Final notes
-----------

* :ref:`capabilities` apply to aliases as well as the commands they call.
  To run an alias successfully, a caller needs to have access to all commands
  called by the alias as well - keep this in mind if you declare a strict set of
  :ref:`default capabilities <capabilities-managing-defaults>`.
