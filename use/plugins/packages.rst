
.. _plugin-packages:

The Packages plugin
===================

.. _command-packages-info:

packages info [<repository url>] <package> [<version>] [--author-full]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Displays informations about the *<package>*, at the given *<version>*.
*<repository url>* defaults to http://packages.supybot.fr.cr/ and
*<version>* defaults to the latest available.

.. _command-packages-install:

packages install <filename> [--force]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installs the package. If the package has been downloaded with Package,
just give the package name; otherwise, give the full path (including
the extension).
If given, *--force* disables sanity checks (usage is deprecated).

.. _command-packages-search:

packages search [<repository url>] [--name <name>] [--version <version>] [--author <author>] [<description>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches the packages matching the query in the *<repository url>*.
*<repository url>* defaults to http://packages.supybot.fr.cr/

.. _command-packages-checkupdates:

packages checkupdates [<repository url>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks for updates for loaded plugins at the *<repository url>*.
*<repository url>* defaults to http://packages.supybot.fr.cr/

.. _command-packages-download:

packages download <package> [--version <version>] [--repo <repository url>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Downloads the *<package>* at the *<repository url>*.
*<version>* defaults to the latest version available.
*<repository url>* defaults to http://packages.supybot.fr.cr/

