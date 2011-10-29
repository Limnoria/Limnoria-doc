
.. _plugin-github:

The GitHub plugin
=================

.. include:: unofficial.inc

Main commands
-------------

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

Announces
---------

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



.. _plugin-github-config:

Configuration
-------------

.. _supybot.plugins.GitHub.api:

supybot.plugins.GitHub.api
^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.GitHub.api.url:

supybot.plugins.GitHub.api.url
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: http://github.com/api/v2/json

The URL of the GitHub API to use. You probably don't need to edit it, but I let it there, just in case.

.. _supybot.plugins.GitHub.announces:

supybot.plugins.GitHub.announces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

You shouldn't edit this configuration variable yourself, unless you know what you do. Use '@Github announce add' or '@Github announce remove' instead.

.. _supybot.plugins.GitHub.public:

supybot.plugins.GitHub.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

