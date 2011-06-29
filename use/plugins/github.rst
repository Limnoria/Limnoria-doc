
.. _plugin-github:

The GitHub plugin
=================

.. _command-github-repo-info:

github repo info <owner> <repository> [--enable <feature> <feature> ...] [--disable <feature> <feature>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Displays informations about *<owner>*'s *<repository>*.
Enable or disable features (ie. displayed data) according to the
request).

.. _command-github-repo-search:

github repo search <searched string> [--page <id>] [--language <language>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches the string in the repository names database. You can
specify the page *<id>* of the results, and restrict the search
to a particular programming *<language>*.

.. _command-github-announce-remove:

github announce remove [<channel>] <owner> <name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Don't announce the commits of the GitHub repository called
*<owner>*/*<name>* in the *<channel>* anymore.
*<channel>* defaults to the current channel.

.. _command-github-announce-add:

github announce add [<channel>] <owner> <name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Announce the commits of the GitHub repository called
*<owner>*/*<name>* in the *<channel>*.
*<channel>* defaults to the current channel.

