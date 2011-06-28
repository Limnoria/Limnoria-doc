
.. _plugin-topic:

The Topic plugin
================

.. command-restore:

restore [<channel>]
^^^^^^^^^^^^^^^^^^^

Restores the topic to the last topic set by the bot. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-set:

set [<channel>] [<number>] <topic>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the topic *<number>* to be *<text>*. If no *<number>* is given, this
sets the entire topic. *<channel>* is only necessary if the message
isn't sent in the channel itself.


.. command-shuffle:

shuffle [<channel>]
^^^^^^^^^^^^^^^^^^^

Shuffles the topics in *<channel>*. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. command-lock:

lock [<channel>]
^^^^^^^^^^^^^^^^

Locks the topic (sets the mode +t) in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-replace:

replace [<channel>] <number> <topic>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces topic *<number>* with *<topic>*.


.. command-topic:

topic [<channel>]
^^^^^^^^^^^^^^^^^

Returns the topic for *<channel>*. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. command-unlock:

unlock [<channel>]
^^^^^^^^^^^^^^^^^^

Unlocks the topic (sets the mode +t) in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-redo:

redo [<channel>]
^^^^^^^^^^^^^^^^

Undoes the last undo. *<channel>* is only necessary if the message isn't
sent in the channel itself.


.. command-fit:

fit [<channel>] <topic>
^^^^^^^^^^^^^^^^^^^^^^^

Adds *<topic>* to the topics for *<channel>*. If the topic is too long
for the server, topics will be popped until there is enough room.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-swap:

swap [<channel>] <first topic number> <second topic number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Swaps the order of the first topic number and the second topic number.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-reorder:

reorder [<channel>] <number> [<number> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reorders the topics from *<channel>* in the order of the specified
*<number>* arguments. *<number>* is a one-based index into the topics.
*<channel>* is only necessary if the message isn't sent in the channel
itself.


.. command-get:

get [<channel>] <number>
^^^^^^^^^^^^^^^^^^^^^^^^

Returns topic number *<number>* from *<channel>*. *<number>* is a one-based
index into the topics. *<channel>* is only necessary if the message
isn't sent in the channel itself.


.. command-undo:

undo [<channel>]
^^^^^^^^^^^^^^^^

Restores the topic to the one previous to the last topic command that
set it. *<channel>* is only necessary if the message isn't sent in the
channel itself.


.. command-add:

add [<channel>] <topic>
^^^^^^^^^^^^^^^^^^^^^^^

Adds *<topic>* to the topics for *<channel>*. *<channel>* is only necessary
if the message isn't sent in the channel itself.


.. command-change:

change [<channel>] <number> <regexp>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the topic number *<number>* on *<channel>* according to the regular
expression *<regexp>*. *<number>* is the one-based index into the topics;
*<regexp>* is a regular expression of the form
s/regexp/replacement/flags. *<channel>* is only necessary if the message
isn't sent in the channel itself.


.. command-insert:

insert [<channel>] <topic>
^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds *<topic>* to the topics for *<channel>* at the beginning of the topics
currently on *<channel>*. *<channel>* is only necessary if the message
isn't sent in the channel itself.


.. command-default:

default [<channel>]
^^^^^^^^^^^^^^^^^^^

Sets the topic in *<channel>* to the default topic for *<channel>*. The
default topic for a channel may be configured via the configuration
variable supybot.plugins.Topic.default.


.. command-die:

die 
^^^^



.. command-list:

list [<channel>]
^^^^^^^^^^^^^^^^

Returns a list of the topics in *<channel>*, prefixed by their indexes.
Mostly useful for topic reordering. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. command-remove:

remove [<channel>] <number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes topic *<number>* from the topic for *<channel>* Topics are
numbered starting from 1; you can also use negative indexes to refer
to topics starting the from the end of the topic. *<channel>* is only
necessary if the message isn't sent in the channel itself.


.. command-separator:

separator [<channel>] <separator>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the topic separator for *<channel>* to *<separator>* Converts the
current topic appropriately.


