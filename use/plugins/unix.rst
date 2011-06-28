
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

Returns various unix-y information on the running :ref:`supybot process.`

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
