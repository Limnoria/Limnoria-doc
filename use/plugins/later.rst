
.. _plugin-later:

The Later plugin
================

.. _command-later-notes:

later notes [<nick>]
^^^^^^^^^^^^^^^^^^^^

If *<nick>* is given, replies with what notes are waiting on *<nick>*,
otherwise, replies with the nicks that have notes waiting for them.

.. _command-later-remove:

later remove <nick>
^^^^^^^^^^^^^^^^^^^

Removes the notes waiting on *<nick>*.

.. _command-later-tell:

later tell <nick> <text>
^^^^^^^^^^^^^^^^^^^^^^^^

Tells *<nick>* *<text>* the next time *<nick>* is in seen. *<nick>* can
contain wildcard characters, and the first matching nick will be
given the note.

