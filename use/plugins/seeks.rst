
.. _plugin-seeks:

The Seeks plugin
================

.. _command-seeks-search:

seeks search <query>
^^^^^^^^^^^^^^^^^^^^

Searches the *<query>* in a seeks node.



.. _plugin-seeks-config:

Configuration
-------------

.. _supybot.plugins.Seeks.format:

supybot.plugins.Seeks.format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: %(url)s - %(seeks_score)s

The format used to display each result.

.. _supybot.plugins.Seeks.number:

supybot.plugins.Seeks.number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 5

The number of results to display.

.. _supybot.plugins.Seeks.separator:

supybot.plugins.Seeks.separator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: /

The character(s) to use between search results.

.. _supybot.plugins.Seeks.url:

supybot.plugins.Seeks.url
^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: http://www.seeks.fr/search?expansion=1&action=expand&output=json&q=

The Seeks server that this plugin will use.

.. _supybot.plugins.Seeks.public:

supybot.plugins.Seeks.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

