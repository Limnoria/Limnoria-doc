
.. _plugin-plugin:

The Plugin plugin
=================

.. _command-help:

help <plugin>
^^^^^^^^^^^^^

Returns a useful description of how to use *<plugin>*, if the plugin has
one.


.. _command-contributors:

contributors <plugin> [<nick>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replies with a list of people who made contributions to a given plugin.
If *<nick>* is specified, that person's specific contributions will
be listed. Note: The *<nick>* is the part inside of the parentheses
in the people listing.


.. _command-plugin:

plugin <command>
^^^^^^^^^^^^^^^^

Returns the name of the plugin that would be used to call *<command>*.

If it is not uniquely determined, returns list of all plugins that
contain *<command>*.


.. _command-author:

author <plugin>
^^^^^^^^^^^^^^^

Returns the author of *<plugin>*.  This is the person you should talk to
if you have ideas, suggestions, or other comments about a given plugin.


.. _command-list:

list
^^^^

Returns a list of the currently loaded plugins.


.. _command-plugins:

plugins <command>
^^^^^^^^^^^^^^^^^

Returns the names of all plugins that contain *<command>*.


