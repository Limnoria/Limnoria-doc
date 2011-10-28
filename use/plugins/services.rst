
.. _plugin-services:

The Services plugin
===================

NickServ
--------

.. _command-services-identify:

services identify
^^^^^^^^^^^^^^^^^

Identifies with NickServ using the current nick.

.. _command-services-nicks:

services nicks
^^^^^^^^^^^^^^

Returns the nicks that this plugin is configured to identify and ghost
with.

.. _command-services-password:

services password <nick> [<password>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the NickServ password for *<nick>* to *<password>*. If *<password>* is
not given, removes *<nick>* from the configured nicks.

.. _command-services-ghost:

services ghost [<nick>]
^^^^^^^^^^^^^^^^^^^^^^^

Ghosts the bot's given nick and takes it. If no nick is given,
ghosts the bot's configured nick and takes it.

ChanServ
--------

.. _command-services-unban:

services unban [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^

Attempts to get unbanned by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself, but chances
are, if you need this command, you're not sending it in the channel
itself.

.. _command-services-invite:

services invite [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attempts to get invited by ChanServ to *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself, but chances
are, if you need this command, you're not sending it in the channel
itself.

.. _command-services-voice:

services voice [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^^^^

Attempts to get voiced by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.

.. _command-services-op:

services op [<channel>]
^^^^^^^^^^^^^^^^^^^^^^^

Attempts to get opped by ChanServ in *<channel>*. *<channel>* is only
necessary if the message isn't sent in the channel itself.



.. _plugin-services-config:

Configuration
-------------

.. _supybot.plugins.Services.ChanServ:

supybot.plugins.Services.ChanServ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines what nick the 'ChanServ' service has.

.. _supybot.plugins.Services.ChanServ.halfop:

supybot.plugins.Services.ChanServ.halfop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will request to get half-opped by the ChanServ when it joins the channel.

.. _supybot.plugins.Services.ChanServ.op:

supybot.plugins.Services.ChanServ.op
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will request to get opped by the ChanServ when it joins the channel.

.. _supybot.plugins.Services.ChanServ.password:

supybot.plugins.Services.ChanServ.password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines what password the bot will use with ChanServ.

.. _supybot.plugins.Services.ChanServ.voice:

supybot.plugins.Services.ChanServ.voice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will request to get voiced by the ChanServ when it joins the channel.

.. _supybot.plugins.Services.NickServ:

supybot.plugins.Services.NickServ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines what nick the 'NickServ' service has.

.. _supybot.plugins.Services.NickServ.password:

supybot.plugins.Services.NickServ.password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.Services.disabledNetworks:

supybot.plugins.Services.disabledNetworks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: ['QuakeNet']

Determines what networks this plugin will be disabled on.

.. _supybot.plugins.Services.ghostDelay:

supybot.plugins.Services.ghostDelay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 60

Determines how many seconds the bot will wait between successive GHOST attempts.

.. _supybot.plugins.Services.nicks:

supybot.plugins.Services.nicks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

Determines what nicks the bot will use with services.

.. _supybot.plugins.Services.noJoinsUntilIdentified:

supybot.plugins.Services.noJoinsUntilIdentified
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will not join any channels until it is identified. This may be useful, for instances, if you have a vhost that isn't set until you're identified, or if you're joining +r channels that won't allow you to join unless you identify.

.. _supybot.plugins.Services.public:

supybot.plugins.Services.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

