
.. _plugin-reply:

The Reply plugin
================

Commands
--------

.. _command-reply-notice:

reply notice <text>
^^^^^^^^^^^^^^^^^^^

Replies with *<text>* in a notice. Use nested commands to your benefit
here. If you want a private notice, nest the private command.

.. _command-reply-private:

reply private <text>
^^^^^^^^^^^^^^^^^^^^

Replies with *<text>* in private. Use nested commands to your benefit
here.

.. _command-reply-replies:

reply replies <str> [<str> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with each of its arguments *<str>* in separate replies, depending
the configuration of :ref:`supybot.reply.oneToOne.`

.. _command-reply-action:

reply action <text>
^^^^^^^^^^^^^^^^^^^

Replies with *<text>* as an action. use nested commands to your benefit
here.

.. _command-reply-reply:

reply reply <text>
^^^^^^^^^^^^^^^^^^

Replies with *<text>*. Equivalent to the alias, 'echo $nick: $1'.



.. _plugin-reply-config:

Configuration
-------------

.. _supybot.plugins.Reply.public:

supybot.plugins.Reply.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

