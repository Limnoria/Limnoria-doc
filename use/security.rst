********************
Security in Limnoria
********************

Some security features are disabled by default.
We know this is arguable, but enabling them would make it quite hard
to start using the bot.
This guide is for people who want to enable these features to make
their bot as secure as possible.

.. note::

    Limnoria (or Gribble or Supybot) have never been audited by a security
    professional.
    We do the best we can to make it secure, but we cannot guarantee it is
    completely safe.

Trust in network operators
==========================

As you may know, by default, it is possible to do anything from IRC, including
loading the Unix plugin and using the ``@call`` command.
The only safeguard is checking the user calling the commands is authenticated
as the owner of the bot; and network operators are able to spoof hostmasks
and collect your password, thus allowing them to execute commands as the
owner.

Although network operators of most well-known IRC networks are not known to
do that, you should be aware of that risk.

Starting on commit `4f6a5e7db`_ (version 2017.10.01), there is a new
configuration variable, `supybot.commands.allowShell`, to prevent malicious
network operators from getting shell access on your bot's computer.
It defaults to ``True`` to make it easy for new users to install plugins using
PluginDownloader, but it is recommended you set it to ``False`` if you do not
care about that feature.

Finally, you can remove the ``owner`` user account entirely
(or remove the ``owner`` capability) for that account.
This causes every privileged commands to be disabled, so neither you
nor server operators can access it.
Channel-specific configuration variables can still be configured by
users with the ``#channel,op`` capability (if any), but global configuration
variables can only be modified by accessing the config files.

.. _4f6a5e7db: https://github.com/ProgVal/Limnoria/commit/4f6a5e7db


.. _security-ssl:

Network connections / SSL
=========================

Background on SSL certification validation
------------------------------------------

It is often believed using SSL magically makes impossible any attack on your
connection (from the bot to the server).
It is true that it prevents passive eavesdropping, but other attack methods
are still possible.

The main one involves man-in-the-middle, ie. someone acting as a proxy between
you (your bot, in that case) and the IRC network.
If certificates are not validated, the attacker can allow you to connect
to itself using their own SSL certificate, and you would never know about it.

This is why it is important to check the SSL certificate of the server
you connect to: an attacker cannot spoof a certificate, or the trust of
a Certificate Authority in a network's certificates.

Of course, this assumes there is no bug in your SSL library, the network's,
and the protocols involved.

Certificate validation in Limnoria
----------------------------------

Until version 2016.02.24, Limnoria did not support certificate validation.
Starting from this version, it is possible, but disabled by default, in order
to not break existing bots when updating.

Certificate validation can be enabled using this command::

    @config supybot.protocols.ssl.verifyCertificates true

Available validation mechanisms are Certification Authorities and
fingerprint checking.

Certificate Authorities
-----------------------

By default, Limnoria only checks certificates using CA certificates installed
on your system. However, some networks use a CA that is not trusted by your
system, such as CACert.

Limnoria allows you to add a CA certificate for a network::

    @config networks.NETWORKNAME.ssl.authorityCertificate /path/to/the/certificate.crt

Note that you are responsible for making sure this is the right certificate
for the CA, and trust this CA to sign correctly certificates valid for the
network's hostname(s).


Fingerprint checking
--------------------

Alternatively, for networks that do not use a CA, you can give Limnoria
the list of fingerprints of certificates used by the network::

    @config supybot.networks.NETWORKNAME.ssl.serverFingerprints: <fingerprint1> <fingerprint2> ...

Adding fingerprints will disable CA verifications (useful if you do not
want to trust CAs).

Note that you are responsible for giving the correct list of fingerprints.

.. _ssl-python-versions:

Supported python versions
-------------------------

Fingerprint checking and CA validation are available in all Python versions
supported by Limnoria.


Flooding via command abuse
==========================

Limnoria answers at most one message per command, but its message can be
rather long (up to about 450 to 500 characters) for even a small command.

If this is undesirable for you, you can take the following measures:

* Limit the size of a single message with ``supybot.reply.mores.length``.
* Limit how many messages the ``@more`` command may be called to get
  a response to a command: ``supybot.reply.mores.maximum``
* Disable large error replies with ``supybot.reply.error.detailed`` and
  ``supybot.reply.error.noCapability``, and/or
  send them in private with ``supybot.reply.error.inPrivate``.
* And check out the various variables in ``supybot.abuse.flood``.

For old bot configurations, you may also want to set the ``-scheduler``
capability to prevent users from using the ``@scheduler add`` and
``@scheduler repeat`` commands (bot configurations created with Limnoria
versions greater than 2020.05.13 already have this by default).

We also recommend you report users abusing your bot to network operators,
so they take extra measures against these users if this is against their
network's policy.

Hardening
=========

By default, Limnoria exposes much of its configuration. This is by design,
to improve discoverability and debugging.

Again, if this is undesirable to you, you can do the following:

* Prevent users from using the Config plugin to read the configuration:
  ``defaultcapability add -config`` (note that sensitive configuration
  variables are, of course, always hidden from users by default).
* Prevent users from listing available plugins and commands:
  ``defaultcapability add -misc.list``,
  ``defaultcapability add -misc.apropos``, and
  ``defaultcapability add -plugin``
* Hide the version from users: ``defaultcapability add -misc.version``,
  and also make sure it's not in ``supybot.user`` or
  ``supybot.plugins.Owner.quitMsg``.
* Hide capabilities users are missing to run a command:
  ``supybot.reply.error.noCapability``
* Replace errors with a generic reply: ``supybot.reply.error.detailed``

Note that, when asking for help involving an error, you should enable verbose
errors when providing logs (ie. reset these last values to their default),
so it is easier to help you diagnose your problems.
