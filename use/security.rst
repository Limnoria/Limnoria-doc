********************
Security in Limnoria
********************

Trust in network operators
==========================

to do


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

to do

Fingerprint checking
--------------------

to do

.. _ssl-python-versions:

Supported python versions
-------------------------

Fingerprint checking is available in all Python versions.

CA validation is available in Python 2, starting on 2.7.9; and
Python 3, starting on 3.4.
