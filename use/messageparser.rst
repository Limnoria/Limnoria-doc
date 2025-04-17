.. _custom-regex-triggers:

==============================================
Creating custom regex triggers (MessageParser)
==============================================

In addition to creating :ref:`custom commands using the Aka plugin <custom-commands>`,
Limnoria also allows you to create custom, regular expression based message
triggers using the :ref:`plugin-messageparser` plugin.

Before proceeding through this page, we recommend reading the
:ref:`command-parsing-primer`, which discusses many of the details that apply
to running commands via message triggers.

.. contents::

Creating & managing regex triggers
----------------------------------

Regex triggers are created using the :ref:`messageparser add <command-messageparser-add>` command::

    <user> @messageparser add "some words" "echo Blah blah"
    <Limnoria> Done.
    [...]
    <user> I am saying some words.
    <Limnoria> Blah blah

:ref:`messageparser list <command-messageparser-list>` will show a list of configured triggers, and
:ref:`messageparser remove <command-messageparser-remove>` will remove them::

    <user> @messageparser list
    <Limnoria> #1: some words
    <user> @messageparser remove --id 1
    <Limnoria> Done.

In practice, it's usually easier to remove a trigger by its ID instead of
repeating out the regex in full, since you may have to escape symbols within the
expression otherwise.

Case sensitivity
----------------

To make a trigger case-insensitive, preface it with the ``(?i)`` modifier::

    <user> @messageparser add "(?i)^test$" "echo Test failed, try again later"
    <Limnoria> Done.
    <user> TEST
    <Limnoria> Test failed, try again later

Extracting parameters from capture groups
-----------------------------------------

When the regular expression has a capture group, its content will be passed in
as ``$1``, ``$2``, etc. in a similar way to command aliases::

    <user> @messageparser add "define (.+)" "dict $1"
    <Limnoria> Done.
    [...]
    <user> define ice cream
    <Limnoria> wn: ice cream n 1: frozen dessert containing cream and sugar and flavoring [syn: {ice cream}, {icecream}]

The :ref:`command-dict-dict` command in this example is provided by the
:ref:`plugin-dict` plugin.

Example: run commands sent through relay bots
---------------------------------------------

One practical use of MessageParser may be to make Limnoria run messages sent
by other relay bots, as these would normally not match Limnoria's command
prefix. For example, if your bot uses "!" as its command prefix and you have a
relay bot that sends text in the format::

    <RelayBot> [othernetwork] <user> hi

You could add a MessageParser trigger like this::

    <user> @messageparser add "^\[.*?\] <.*?> !(.*)$" "apply $1"
    <Limnoria> Done.
    <RelayBot> [othernetwork] <user> !echo hello world
    <Limnoria> hello world

This would read all messages sent over the relay bot that start with a "!", and
run them as a command via :ref:`command-utilities-apply`.

Note that in this case, all relayed commands will be treated as if RelayBot
itself ran it, so there is no fine grained access control.

Limitations
-----------

Custom command triggers are not designed to replace plugins in all cases. The
same :ref:`limitations for the Aka plugin <custom-command-limitations>` apply
here as well.
