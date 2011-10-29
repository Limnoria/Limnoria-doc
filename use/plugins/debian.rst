
.. _plugin-debian:

The Debian plugin
=================

.. include:: unofficial.inc

Commands
--------

.. _command-debian-file:

debian file [--exact]         [--mode {path,filename,exactfilename}]         [--branch {oldstable,stable,testing,unstable,experimental}]         [--section {main,contrib,non-free}] <file name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the package(s) containing the *<file name>*.
*--mode* defaults to path, and defines how to search.
*--branch* defaults to stable, and defines in what branch to search.

.. _command-debian-bug:

debian bug <num>
^^^^^^^^^^^^^^^^

Returns a description of the bug with bug id *<num>*.

.. _command-debian-stats:

debian stats <source package>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reports various statistics (from http://packages.qa.debian.org/) about
*<source package>*.

.. _command-debian-incoming:

debian incoming [--{regexp,arch} <value>] [<glob> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks debian incoming for a matching package name.  The arch
parameter defaults to i386; *--regexp* returns only those package names
that match a given regexp, and normal matches use standard \*nix
globbing.

.. _command-debian-version:

debian version [--exact]         [--searchon {names,all,sourcenames}]         [--branch {oldstable,stable,testing,unstable,experimental}]         [--section {main,contrib,non-free}] <package name>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current version(s) of the Debian package *<package name>*.
*--exact,* if given, means you want only the *<package name>*, and not
package names containing this name.
*--searchon* defaults to names, and defines where to search.
*--branch* defaults to all, and defines in what branch to search.
*--section* defaults to all, and defines in what section to search.

.. _command-debian-new:

debian new [{main,contrib,non-free}] [<version>] [<glob>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks for packages that have been added to Debian's unstable branch
in the past week.  If no glob is specified, returns a list of all
packages.  If no section is specified, defaults to main.



.. _plugin-debian-config:

Configuration
-------------

.. _supybot.plugins.Debian.bold:

supybot.plugins.Debian.bold
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the plugin will use bold in the responses to some of its commands.

.. _supybot.plugins.Debian.public:

supybot.plugins.Debian.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

