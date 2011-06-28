
.. _plugin-topic:

The Topic plugin
================

Getting
-------

.. _command-topic-topic:

topic topic [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^

Returns the topic for *<channel>*. *<channel>* is only necessary if the
message isn't sent in the channel itself.

.. _command-topic-get:

topic get [<channel>] <number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns topic number *<number>* from *<channel>*. *<number>* is a one-based
index into the topics. *<channel>* is only necessary if the message
isn't sent in the channel itself.

.. _command-topic-list:

topic list [<channel>]
^^^^^^^^^^^^^^^^^^^^^^

Returns a list of the topics in *<channel>*, prefixed by their indexes.
Mostly useful for topic reordering. *<channel>* is only necessary if the
message isn't sent in the channel itself.

Defining
--------

.. _command-topic-restore:

topic restore [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^

Restores the topic to the last topic set by the bot. *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-topic-set:

topic set [<channel>] [<number>] <topic>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the topic *<number>* to be *<text>*. If no *<number>* is given, this
sets the entire topic. *<channel>* is only necessary if the message
isn't sent in the channel itself.

.. _command-topic-replace:

topic replace [<channel>] <number> <topic>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces topic *<number>* with *<topic>*.

.. _command-topic-fit:

topic fit [<channel>] <topic>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds *<topic>* to the topics for *<channel>*. If the topic is too long
for the server, topics will be popped until there is enough room.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-topic-add:

topic add [<channel>] <topic>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds *<topic>* to the topics for *<channel>*. *<channel>* is only necessary
if the message isn't sent in the channel itself.

.. _command-topic-remove:

topic remove [<channel>] <number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes topic *<number>* from the topic for *<channel>* Topics are
numbered starting from 1; you can also use negative indexes to refer
to topics starting the from the end of the topic. *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-topic-change:

topic change [<channel>] <number> <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the topic number *<number>* on *<channel>* according to the regular
expression *<regexp>*. *<number>* is the one-based index into the topics;
*<regexp>* is a regular expression of the form
s/regexp/replacement/flags. *<channel>* is only necessary if the message
isn't sent in the channel itself.

.. _command-topic-insert:

topic insert [<channel>] <topic>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds *<topic>* to the topics for *<channel>* at the beginning of the topics
currently on *<channel>*. *<channel>* is only necessary if the message
isn't sent in the channel itself.

.. _command-topic-default:

topic default [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the topic in *<channel>* to the default topic for *<channel>*. The
default topic for a channel may be configured via the configuration
variable :ref:`supybot.plugins.Topic.default.`

Re-ordering
-----------

.. _command-topic-shuffle:

topic shuffle [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^

Shuffles the topics in *<channel>*. *<channel>* is only necessary if the
message isn't sent in the channel itself.

.. _command-topic-reorder:

topic reorder [<channel>] <number> [<number> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reorders the topics from *<channel>* in the order of the specified
*<number>* arguments. *<number>* is a one-based index into the topics.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

.. _command-topic-swap:

topic swap [<channel>] <first topic number> <second topic number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Swaps the order of the first topic number and the second topic number.
*<channel>* is only necessary if the message isn't sent in the channel
itself.

Locking
-------

.. _command-topic-lock:

topic lock [<channel>]
^^^^^^^^^^^^^^^^^^^^^^

Locks the topic (sets the mode +t) in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-topic-unlock:

topic unlock [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^

Unlocks the topic (sets the mode +t) in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.

Utilities
---------

.. _command-topic-undo:

topic undo [<channel>]
^^^^^^^^^^^^^^^^^^^^^^

Restores the topic to the one previous to the last topic command that
set it. *<channel>* is only necessary if the message isn't sent in the
channel itself.

.. _command-topic-redo:

topic redo [<channel>]
^^^^^^^^^^^^^^^^^^^^^^

Undoes the last undo. *<channel>* is only necessary if the message isn't
sent in the channel itself.

.. _command-topic-separator:

topic separator [<channel>] <separator>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the topic separator for *<channel>* to *<separator>* Converts the
current topic appropriately.
