.. _identifying-to-services:

*******************************
Identifying the bot to services
*******************************

The different methods listed here are in the order how they are usually recommended
by network operators.

Please also note that SASL and CertFP are only fully supported on Limnoria. Gribble
has imported partial SASL support (only PLAIN).

Registering to services
-----------------------

You can safely jump over this section if your bot is already registered to
services.

First start by checking what is the syntax for registering with
``/msg nickserv help register``. It returns you something like this (Atheme
7.x)::

    NickServ: Syntax: REGISTER <password> <email-address>

Assuming that that is the syntax, we can register the bot with::

    load Services
    nickserv register mypassword bot@example.com

Or, on Limnoria versions older than 2021.06.15::

    nickserv register mypassword bot@example.com

Note that the email address must be correct. Next check that
``/msg nickserv info bot`` doesn't say something about being unverified. If
it does, go to the email address and run::

    nickserv VERIFY nick <code from the email>

Now your bot should be successfully registered and you can move to setting
up automatic identifying below. If you need to identify to services now,
``/msg nickserv help identify`` and following the syntax (I am still
assuming that you are on Atheme 7.x)::

    nickserv IDENTIFY username password

Note: the ``nickserv`` command was added in Limnoria 2021.06.15.
If you have an older version, you need to run
something like ``ircquote privmsg nickserv :register ...`` instead (note
the placement of the ``:`` after ``nickserv`` and before the command name).

SASL PLAIN
----------

*To use SASL EXTERNAL, you must only configure CertFP and it's attempted automatically.*
SASL PLAIN is identifying using username and password, SASL EXTERNAL is identifying by
using CertFP which is explained later on this document. It doesn't need
username or password to be configured.

Note that SASL isn't supported on all networks. As the only way to check
if SASL is supported is either ``/quote CAP LS`` (which usually gets eaten
by bouncers) or connecting to the network and seeing if it works, we
recommend always configuring SASL and whoising the bot to see if it worked.
If it didn't work, you might want to ask the network operators about their
SASL support and request them to start supporting it.

SASL is widely agreed as the best method to identify to services as it
identifies you before anyone (other than IRC operators) can see that you
are connected. To enable SASL, simply::

    config networks.<network>.sasl.username AccountName
    config networks.<network>.sasl.password P455w0rd

where you of course replace AccountName and P455w0rd with your actual
NickServ account name and password. Remember to replace ``<network>`` with
the real network name like ``Libera``.

CertFP
------

You can test if CertFP is supported by services simply by doing
``/msg NickServ cert``. If you get an error about "Insufficient parameters
for CERT", CertFP is supported, and if you get an error about unknown
command, it's not supported.

CertFP identifies you to services using a client (SSL) certificate and
naturally requires an SSL connection. It doesn't identify you as soon as
SASL, but unlike SASL, it identifies you even when services return from a
netsplit, unlike any other mechanism.

First you must generate a certificate, and the easiest method is probably
using OpenSSL which you should have even on Windows if you installed with pip::

    openssl req -nodes -newkey rsa:4096 -keyout <BOT>.pem -x509 -days 3650 -out <BOT>.pem -subj "/CN=<BOT>"

Now you should have a ``<BOT>.pem`` file in the directory where you ran
the command, presumably your home directory and you only tell your
bot where to find it and tell NickServ that it belongs to you.
Note that you should replace ``<BOT>`` with the account name of your bot.

You have two choices, using the same certificate on all networks::

    config protocols.irc.certfile /home/<username>/<BOT>.pem

or only on one or more network where it's manually configured::

    config networks.<network>.certfile /home/<username>/<BOT>.pem

And lastly, you must tell the services what is your certificate
fingerprint, which you can find out with::

    openssl x509 -sha1 -noout -fingerprint -in <BOT>.pem | tr -d ':' | tr 'A-Z' 'a-z'

This results in something like
``05dd01fedc1b821b796d0d785160f03e32f53fa8`` which you tell your bot to
tell services::

    nickserv cert add 05dd01fedc1b821b796d0d785160f03e32f53fa8

Or if your bot identifies as you, you can do that by yourself with::

    /msg NickServ cert add 05dd01fedc1b821b796d0d785160f03e32f53fa8


Remember to replace ``05dd01fedc1b821b796d0d785160f03e32f53fa8`` with your
own fingerprint! Next time your bot connects, it should get identified
automatically.

SASL ECDSA-NIST256P-CHALLENGE
-----------------------------

First you must ECDSA key for the bot to use::

    openssl ecparam -name prime256v1 -genkey -out <bot>_ecdsa.pem

and get the public key using::

    openssl ec -noout -text -conv_form compressed -in <bot>_ecdsa.pem | grep '^pub:' -A 3 | tail -n 3 | tr -d ' \n:' | xxd -r -p | base64

After getting the public key, you must tell your bot to use it and tell
services about it (just like with CertFP/SASL EXTERNAL)::

    config supybot.networks.<network>.sasl.username AccountName
    config supybot.networks.<network>.sasl.ecdsa_key /home/<username>/<BOT>_ecdsa.pem
    nickserv set pubkey PUBKEY_WHICH_YOU_GOT_EARLIER

and after reconnecting, the bot should successfully identify using SASL
ECDSA-NIST256P-CHALLENGE.

*NOTE:* You can use ``ecdsa pubkey`` to get the public key, but you cannot
generate the key pair using it as pyecdsa doesn't support ecdsatool
generated keys.

Server password
---------------

Many networks support identifying using ``username:password`` as server
password. If this is the case with your network (anything that uses a
charybdis-like IRCd), this should work for you. Note that this identifies
you after SASL so, your real host might be seen. To do this, simply::

    config networks.<network>.password username:password

Replace ``<network>`` with the name of network, for example ``Libera``
and username:password with your real username and password.

ZNC
^^^

If you wish to connect your bot to ZNC, the recommended way is::

    config networks.<network>.ident <username>@<identifier>/<network>
    config networks.<network>.password <password>

The identifier is free text to describe which client your Limnoria is. It
came with ZNC 1.6.0 and is completely optional. ``<network>`` again has
been there since ZNC 1.0 which is very old and has multiple security issues
that have been fixed since then. You should always run the latest release.

Services plugin
---------------

The Services plugin comes with Supybot and should be an easy way to
identify your bot, but SASL is recommended over it. Start by loading
Services with::

    load Services

and then tell it what NickServ and ChanServ are called::

    config network [<network>] plugins.services.nickserv NickServ
    config network [<network>] plugins.services.chanserv ChanServ

``[<network>]`` is only necessary if the message isn't sent in the network
itself. Remember to replace NickServ/ChanServ with their real names if they
have a different name on any network.

If you wish to ensure that your bot never contacts an user impersonating
NickServ, you may specify the server name from ``/MAP`` command (in your IRC
client), e.g. on Libera.Chat::

    config network [<network>] plugins.services.nickserv NickServ@services.
    config network [<network>] plugins.services.chanserv ChanServ@services.

Now you can set your password::

    services password Bot P455w0rd

makes the bot attempt identifying as Bot using password P455w0rd. Replace
them with your real nickname and password. Note that if you have multiple
nicknames, you must run ``services password`` for them all.

If your bot happens to get a nickname that isn't configured, it won't
know how to identify. You might be able to avoid this issue by loading
NickCapture, (``load NickCapture``) which attempts to regain the primary
nick, when it's possible, and when it regains the primary nick, the
identification should work.

