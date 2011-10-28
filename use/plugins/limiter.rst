
.. _plugin-limiter:

The Limiter plugin
==================



.. _plugin-limiter-config:

Configuration
-------------

.. _supybot.plugins.Limiter.enable:

supybot.plugins.Limiter.enable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the bot will maintain the channel limit to be slightly above the current number of people in the channel, in order to make clone/drone attacks harder.

.. _supybot.plugins.Limiter.maximumExcess:

supybot.plugins.Limiter.maximumExcess
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 10

Determines the maximum number of free spots that will be saved when limits are being enforced. This should always be larger than supybot.plugins.Limiter.limit.minimumExcess.

.. _supybot.plugins.Limiter.minimumExcess:

supybot.plugins.Limiter.minimumExcess
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 5

Determines the minimum number of free spots that will be saved when limits are being enforced. This should always be smaller than supybot.plugins.Limiter.limit.maximumExcess.

.. _supybot.plugins.Limiter.public:

supybot.plugins.Limiter.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

