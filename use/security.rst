********************
Security in Limnoria
********************

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

to do

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
