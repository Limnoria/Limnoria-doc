
.. _plugin-ctcp:

The Ctcp plugin
===============

.. _command-ctcp-version:

ctcp version [<channel>] [--nicks]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a CTCP VERSION to *<channel>*, returning the various
version strings returned. It waits for 10 seconds before returning
the versions received at that point. If *--nicks* is given, nicks are
associated with the version strings; otherwise, only the version
strings are given.

