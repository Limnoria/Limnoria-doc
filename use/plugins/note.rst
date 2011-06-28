
.. _plugin-note:

The Note plugin
===============

Reading notes
-------------

.. _command-note-search:

note search [--{regexp} <value>] [--sent] [<glob>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches your received notes for ones matching *<glob>*.  If *--regexp* is
given, its associated value is taken as a regexp and matched against
the notes.  If *--sent* is specified, only search sent notes.

.. _command-note-list:

note list [--{old,sent}] [--{from,to} <user>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieves the ids of all your unread notes.  If *--old* is given, list
read notes.  If *--sent* is given, list notes that you have sent.  If
*--from* is specified, only lists notes sent to you from *<user>*.  If
*--to* is specified, only lists notes sent by you to *<user>*.

.. _command-note-next:

note next
^^^^^^^^^

Retrieves your next unread note, if any.

.. _command-note-note:

note note <id>
^^^^^^^^^^^^^^

Retrieves a single note by its unique note id.  Use the 'note list'
command to see what unread notes you have.

Sending notes
-------------

.. _command-note-unsend:

note unsend <id>
^^^^^^^^^^^^^^^^

Unsends the note with the id given.  You must be the
author of the note, and it must be unread.

.. _command-note-reply:

note reply <id> <text>
^^^^^^^^^^^^^^^^^^^^^^

Sends a note in reply to *<id>*.

.. _command-note-send:

note send <recipient>,[<recipient>,[...]] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a new note to the user specified.  Multiple recipients may be
specified by separating their names by commas.

