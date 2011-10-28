
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


.. _plugin-topic-config:

Configuration
-------------

.. _supybot.plugins.Topic.default:

supybot.plugins.Topic.default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines what the default topic for the channel is. This is used by the default command to set this topic.

.. _supybot.plugins.Topic.format:

supybot.plugins.Topic.format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: $topic ($nick)

Determines what format is used to add topics in the topic. All the standard substitutes apply, in addition to "$topic" for the topic itself.

.. _supybot.plugins.Topic.recognizeTopiclen:

supybot.plugins.Topic.recognizeTopiclen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the bot will recognize the TOPICLEN value sent to it by the server and thus refuse to send TOPICs longer than the TOPICLEN. These topics are likely to be truncated by the server anyway, so this defaults to True.

.. _supybot.plugins.Topic.requireManageCapability:

supybot.plugins.Topic.requireManageCapability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: channel,op; channel,halfop

Determines the capabilities required (if any) to make any topic changes, (everything except for read-only operations). Use 'channel,capab' for channel-level capabilities. Note that absence of an explicit anticapability means user has capability.

.. _supybot.plugins.Topic.separator:

supybot.plugins.Topic.separator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value:  || 

Determines what separator is used between individually added topics in the channel topic.

.. _supybot.plugins.Topic.undo:

supybot.plugins.Topic.undo
^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Topic.undo.max:

supybot.plugins.Topic.undo.max
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 10

Determines the number of previous topics to keep around in case the undo command is called.

.. _supybot.plugins.Topic.public:

supybot.plugins.Topic.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

