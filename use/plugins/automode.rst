
.. _plugin-automode:

The AutoMode plugin
===================

This plugins enables your bot to automatically voice, halfop, and op people on
your channel, according to their capabilities.

Owners
------

Owners are always opped unless you set :ref:`supybot.plugins.AutoMode.owner`
to False.
With stock Supybot and Gribble, setting this to False will cause no automode
at all for owners. In Limnoria, settings this to False will make automode
work as for normal users (only channel capabilities count).
