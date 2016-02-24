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

As you may know, it is possible to do anything from IRC, including loading
the Unix plugin and using the `@call` command.
The only safeguard is checking the user calling the commands is authenticated
as the owner of the bot; and network operators are able to spoof hostmasks
and collect your password, thus allowing them to execute commands as the
owner.

Although network operators of most well-known IRC networks are not known to
do that, you should be aware of that risk.


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
to not break existing bot when updating.

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

Fingerprint checking is available in all Python versions.

CA validation is available in Python 2, starting on 2.7.9; and
Python 3, starting on 3.4.
