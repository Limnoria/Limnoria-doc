
.. _plugin-plugindownloader:

The PluginDownloader plugin
===========================

.. _command-plugindownloader-install:

plugindownloader install <repository> <plugin>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Downloads and installs the *<plugin>* from the *<repository>*.

.. _command-plugindownloader-repolist:

plugindownloader repolist [<repository>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Displays the list of plugins in the *<repository>*.
If *<repository>* is not given, returns a list of available
repositories.



.. _plugin-plugindownloader-config:

Configuration
-------------

.. _supybot.plugins.PluginDownloader.public:

supybot.plugins.PluginDownloader.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

