
.. _plugin-reply:

The Reply plugin
================

.. command-notice:

notice <text>
^^^^^^^^^^^^^

Replies with *<text>* in a notice. Use nested commands to your benefit
here. If you want a private notice, nest the private command.


.. command-private:

private <text>
^^^^^^^^^^^^^^

Replies with *<text>* in private. Use nested commands to your benefit
here.


.. command-replies:

replies <str> [<str> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with each of its arguments *<str>* in separate replies, depending
the configuration of supybot.reply.oneToOne.


.. command-action:

action <text>
^^^^^^^^^^^^^

Replies with *<text>* as an action. use nested commands to your benefit
here.


.. command-reply:

reply <text>
^^^^^^^^^^^^

Replies with *<text>*. Equivalent to the alias, 'echo $nick: $1'.


