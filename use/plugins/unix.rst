
.. _plugin-unix:

The Unix plugin
===============

Utitilies
---------

.. _command-unix-errno:

unix errno <error number or code>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of an errno code, or the errno code of a number.

.. _command-unix-spell:

unix spell <word>
^^^^^^^^^^^^^^^^^

Returns the result of passing *<word>* to aspell/ispell. The results
shown are sorted from best to worst in terms of being a likely match
for the spelling of *<word>*.

.. _command-unix-pid:

unix pid
^^^^^^^^

Returns the current pid of the process for this Supybot.

.. _command-unix-call:

unix call <command to call with any arguments> 

Calls any command available on the system, and returns its output.
Requires owner capability.
Note that being restricted to owner, this command does not do any
sanity checking on input/output. So it is up to you to make sure
you don't run anything that will spamify your channel or that 
will bring your machine to its knees.

.. _command-unix-crypt:

unix crypt <password> [<salt>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the resulting of doing a crypt() on *<password>* If *<salt>* is
not given, uses a random salt. If running on a glibc2 system,
prepending '$1$' to your salt will cause crypt to return an MD5sum
based crypt rather than the standard DES based crypt.

.. _command-unix-progstats:

unix progstats
^^^^^^^^^^^^^^

Returns various unix-y information on the running supybot process.

.. _command-unix-ping:

unix ping [--c <count>] [--i <interval>] [--t <ttl>] [--W <timeout>] <host or ip>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends an ICMP echo request to the specified host.
The arguments correspond with those listed in ping(8). --c is
limited to 10 packets or less (default is 5). --i is limited to 5
or less. --W is limited to 10 or less.

Fun
---

.. _command-unix-fortune:

unix fortune
^^^^^^^^^^^^

Returns a fortune from the \*nix fortune program.

.. _command-unix-wtf:

unix wtf [is] <something>
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns wtf *<something>* is. 'wtf' is a \*nix command that first
appeared in NetBSD 1.5. In most \*nices, it's available in some sort
of 'bsdgames' package.


.. _plugin-unix-config:

Configuration
-------------

.. _supybot.plugins.Unix.fortune:

supybot.plugins.Unix.fortune
^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Unix.fortune.command:

supybot.plugins.Unix.fortune.command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines what command will be called for the fortune command.

.. _supybot.plugins.Unix.fortune.equal:

supybot.plugins.Unix.fortune.equal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether fortune will give equal weight to the different fortune databases. If false, then larger databases will be given more weight. This sends the -e option to the fortune program.

.. _supybot.plugins.Unix.fortune.files:

supybot.plugins.Unix.fortune.files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Determines what specific file (if any) will be used with the fortune command; if none is given, the system-wide default will be used. Do note that this fortune file must be placed with the rest of your system's fortune files.

.. _supybot.plugins.Unix.fortune.offensive:

supybot.plugins.Unix.fortune.offensive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether fortune will retrieve offensive fortunes along with the normal fortunes. This sends the -a option to the fortune program.

.. _supybot.plugins.Unix.fortune.short:

supybot.plugins.Unix.fortune.short
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether only short fortunes will be used if possible. This sends the -s option to the fortune program.

.. _supybot.plugins.Unix.ping:

supybot.plugins.Unix.ping
^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Unix.ping.command:

supybot.plugins.Unix.ping.command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: /bin/ping

Determines what command will be called for the ping command.

.. _supybot.plugins.Unix.spell:

supybot.plugins.Unix.spell
^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Unix.spell.command:

supybot.plugins.Unix.spell.command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: /usr/bin/aspell

Determines what command will be called for the spell command.

.. _supybot.plugins.Unix.wtf:

supybot.plugins.Unix.wtf
^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Unix.wtf.command:

supybot.plugins.Unix.wtf.command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines what command will be called for the wtf command.

.. _supybot.plugins.Unix.public:

supybot.plugins.Unix.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

