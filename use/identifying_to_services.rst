.. _identifying-to-services:

*******************************
Identifying the bot to services
*******************************

The different methods listed here are in the order how they are usually recommended
by network operators.

Please also note that SASL and CertFP are only supported on Limnoria.

SASL PLAIN
----------

*To use SASL EXTERNAL, you must only configure CertFP and it's attempted automatically.*
SASL PLAIN is identifying using username and password, SASL EXTERNAL is identifying by
using CertFP which is explained later on this document. It doesn't need
username or password to be configured.

Note that SASL isn't supported on all networks. You can easily test if it's
supported with ``/msg SaslServ help`` and if you get response, SASL is
probably supported, if you don't get reply or get error about no such nick,
SASL isn't supported.

SASL is widely agreed as the best method to identify to services as it
identifies you before anyone (other than IRC operators) can see that you 
are connected. To enable SASL, simply::

    config networks.<network>.sasl.username AccountName
    config networks.<network>.sasl.password P455w0rd

where you of course replace AccountName and P455w0rd with your actual
NickServ account name and password. Remember to replace ``<network>`` with
the real network name like ``freenode``.

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

    owner ircquote PRIVMSG NickServ :cert add 05dd01fedc1b821b796d0d785160f03e32f53fa8

Or if your bot identifies as you, you can do that by yourself with::

    /msg NickServ cert add 05dd01fedc1b821b796d0d785160f03e32f53fa8 


Remember to replace ``05dd01fedc1b821b796d0d785160f03e32f53fa8`` with your
own fingerprint! Next time your bot connects, it should get identified
automatically.

Server password
---------------

Many networks support identifying using ``username:password`` as server
password. If this is the case with your network (anything that uses a
charybdis-like IRCd), this should work for you. Note that this identifies
you after SASL so, your real host might be seen. To do this, simply::

    config networks.<network>.password username:password

Replace ``<network>`` with the name of network, for example ``freenode``
and username:password with your real username and password.

ZNC users: since ZNC 1.0, ZNC's identification format has been
``username/network:password``.

Services plugin
---------------

The Services plugin comes with Supybot and should be an easy way to 
identify your bot, but SASL and ``username:password`` as server password 
are recommended over it. Start by loading Services with:: 

    load Services 

and then tell it what NickServ and ChanServ are called::

    config plugins.services.nickserv NickServ
    config plugins.services.chanserv ChanServ

Remember to replace NickServ/ChanServ with their real names if they have a
different name on any network. Note that they must have the same name on
all networks, and you must have the same password on all networks.

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

