
.. _plugin-shrinkurl:

The ShrinkUrl plugin
====================

Commands
--------

.. _command-shrinkurl-xrl:

shrinkurl xrl <url>
^^^^^^^^^^^^^^^^^^^

Returns an xrl.us version of *<url>*.

.. _command-shrinkurl-tiny:

shrinkurl tiny <url>
^^^^^^^^^^^^^^^^^^^^

Returns a TinyURL.com version of *<url>*

.. _command-shrinkurl-ln:

shrinkurl ln <url>
^^^^^^^^^^^^^^^^^^

Returns an ln-s.net version of *<url>*.



.. _plugin-shrinkurl-config:

Configuration
-------------

.. _supybot.plugins.ShrinkUrl.default:

supybot.plugins.ShrinkUrl.default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: ln

Determines what website the bot will use when shrinking a URL.

.. _supybot.plugins.ShrinkUrl.minimumLength:

supybot.plugins.ShrinkUrl.minimumLength
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 48

The minimum length a URL must be before the bot will shrink it.

.. _supybot.plugins.ShrinkUrl.nonSnarfingRegexp:

supybot.plugins.ShrinkUrl.nonSnarfingRegexp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: None

Determines what URLs are to be snarfed; URLs matching the regexp given will not be snarfed. Give the empty string if you have no URLs that you'd like to exclude from being snarfed.

.. _supybot.plugins.ShrinkUrl.outFilter:

supybot.plugins.ShrinkUrl.outFilter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will shrink the URLs of outgoing messages if those URLs are longer than supybot.plugins.ShrinkUrl.minimumLength.

.. _supybot.plugins.ShrinkUrl.serviceRotation:

supybot.plugins.ShrinkUrl.serviceRotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: []

If set to a non-empty value, specifies the list of services to rotate through for the shrinkSnarfer and outFilter.

.. _supybot.plugins.ShrinkUrl.shrinkSnarfer:

supybot.plugins.ShrinkUrl.shrinkSnarfer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the shrink snarfer is enabled. This snarfer will watch for URLs in the channel, and if they're sufficiently long (as determined by supybot.plugins.ShrinkUrl.minimumLength) it will post a smaller URL from either ln-s.net or tinyurl.com, as denoted in supybot.plugins.ShrinkUrl.default.

.. _supybot.plugins.ShrinkUrl.shrinkSnarfer.showDomain:

supybot.plugins.ShrinkUrl.shrinkSnarfer.showDomain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether the snarfer will show the domain of the URL being snarfed along with the shrunken URL.

.. _supybot.plugins.ShrinkUrl.bold:

supybot.plugins.ShrinkUrl.bold
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin will bold certain portions of its replies.

.. _supybot.plugins.ShrinkUrl.public:

supybot.plugins.ShrinkUrl.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

