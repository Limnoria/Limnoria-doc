.. _configuration-tutorial:

***********************************
Plugin Configuration for Developers
***********************************

This page describes how to use Limnoria's config system when developing plugins.
For the user guide, see the :ref:`Configuration page <configuration-guide>` instead.

.. contents::

Adding Plugin Configuration (config.py)
=======================================

Limnoria's configuration is hierarchical. In most cases, plugins will register
its configuration under a group reflecting its name: ``supybot.plugins.<pluginname>``.
The default template provided by :command:`supybot-plugin-doc` will already set
this up, e.g.::

    WorldDom = conf.registerPlugin('WorldDom')

.. _conf-dev-register-global-value:
Creating Configuration Variables
--------------------------------

Global config values are defined using :func:`conf.registerGlobalValue`. The
arguments are as follows:

* The parent group to add the value to.
* The name of the config variable.
* The variable type, including the default value and help text as parameters. Supported variable types are
  listed in :ref:`a later section <config-registry-types>`.

::

    conf.registerGlobalValue(WorldDom, 'globalWorldDominationRequires',
        registry.String('', """Determines the capability required to perform world domination."""))

The full name of the above config value will be
``supybot.plugins.WorldDom.globalWorldDominationRequires``, or
``plugins.WorldDom.globalWorldDominationRequires`` for short.

Note that all configuration variables are groups, and it is possible to register
more variables underneath them. This can be useful as it allows extending existing
config variables without changing their type::

    conf.registerGlobalValue(WorldDom.globalWorldDominationRequires, 'weekends',
        registry.String('', """Determines the capability required to perform world domination on weekends."""))

Nested configuration variables must be declared *after* their parent.

.. _conf-dev-register-group:
Creating Configuration Groups
-----------------------------

To create a group that is not a config variable itself, use
:func:`conf.registerGroup`::

    conf.registerGroup(WorldDom, 'attackTargets')

Adding values to a group is the same as adding one under another config variable::

    conf.registerGlobalValue(WorldDom.attackTargets, 'air',
        registry.SpaceSeparatedListOfStrings('', """Contains the list of air targets."""))

Variations
----------

.. _conf-dev-register-channel-value:
Channel-specific values
^^^^^^^^^^^^^^^^^^^^^^^

Limnoria supports channel-specific variables, which allows bot administrators to
set a global value as well as override it on a per-channel basis.

These are defined using :func:`conf.registerChannelValue`::

    conf.registerChannelValue(WorldDom.attackTargets, 'air',
        registry.SpaceSeparatedListOfStrings('', """Contains the list of air targets."""))

.. _conf-dev-register-network-value:
Network-specific values
^^^^^^^^^^^^^^^^^^^^^^^

Network-specific variables are defined using :func:`conf.registerNetworkValue`::

    conf.registerNetworkValue(WorldDom, 'exempt',
        registry.Boolean(False, """Determines whether the network will be exempt from world domination (for now...)"""))

.. _conf-dev-private-values:
Private values
^^^^^^^^^^^^^^

The variable type also takes an optional ``private`` argument, for setting a configuration
variable to private (useful for passwords, authentication tokens,
api keys, …)::

    conf.registerChannelValue(WorldDom, 'controlRoom',
        registry.Boolean(False, """Whether this channel is the secret control room.""", private=True))

When this is set, the bot will only allow :ref:`bot owners <built-in-capabilities>`
(in the case of global variables) or :ref:`channel administrators <built-in-capabilities-channel-op>`
(in the case of channel-specific variables) to query the config value.

Accessing the config from plugin.py
===================================

To read a config variable from the plugin code, use :func:`self.registryValue`
with the name of the configuration variable. The variable name will include all
group names after the plugin name, e.g.::

    self.registryValue('globalWorldDominationRequires')
    self.registryValue('attackTargets.air')

This will return data in the type that the config variable was declared as
(e.g., a list of strings for ``attackTargets.air``, as it has type
``registry.SpaceSeparatedListOfStrings``).

If it is a channel-specific variable, you should pass in additional ``channel``
and ``network`` arguments like this::

    self.registryValue('attackTargets.air', msg.channel, irc.network)

.. note::

   You will typically obtain the current channel name using the **channel**
   :ref:`converter <wrap-converters-for-state>` (in commands with a ``<channel>`` argument)
   or ``msg.channel`` (in other methods); and the network name with ``irc.network``.

You can also set configuration variables (either globally or for a single
channel)::

    self.setRegistryValue('attackTargets.air', value=['foo', 'bar'])
    self.setRegistryValue('attackTargets.air', value=['foo', 'bar'],
                          channel=channel, network=network)

You can also access other configuration variables (or your own if you want)
via the ``supybot.conf`` module::

    conf.supybot.plugins.WorldDom.attackTargets.air()
    conf.supybot.plugins.WorldDom.attackTargets.get('air')()
    conf.supybot.plugins.WorldDom.attackTargets.air.get('network').get('#channel')()
    conf.supybot.plugins.WorldDom.attackTargets.air.setValue(['foo'])
    conf.supybot.plugins.WorldDom.attackTargets.air.get('network').get('#channel').setValue(['foo'])

.. warning::

   Before version 2019.10.22, Limnoria (and Supybot) did not support
   network-specific configuration variables.
   If you want to support these versions, you must drop the `network` argument,
   and access the configuration variables like this::

       self.registryValue('attackTargets.air', '#channel', 'network')
       self.setRegistryValue('attackTargets.air', value=['foo', 'bar'],
                             channel=channel)
       conf.supybot.plugins.WorldDom.attackTargets.air.get('#channel')()
       conf.supybot.plugins.WorldDom.attackTargets.air.get('#channel').setValue(['foo'])

   This will also work in recent versions of Limnoria, but will prevent users
   from setting different values for each network.

.. _config-registry-types:
The Built-in Registry Types
===========================

Limnoria's ``registry`` module defines the following built-in config variable types:

* :class:`registry.Boolean` - A simple true or false value. Also accepts the
  following for true: "true", "on" "enable", "enabled", "1", and the
  following for false: "false", "off", "disable", "disabled", "0",

* :class:`registry.Integer` - Accepts any integer value, positive or negative.

* :class:`registry.NonNegativeInteger` - Will hold any non-negative integer value.

* :class:`registry.PositiveInteger` - Same as above, except that it doesn't accept 0
  as a value.

* :class:`registry.Float` - Accepts any floating point number.

* :class:`registry.PositiveFloat` - Accepts any positive floating point number.

* :class:`registry.Probability` - Accepts any floating point number between 0 and 1
  (inclusive).

* :class:`registry.String` - Accepts any string.

* :class:`registry.NormalizedString` - Accepts any string but will normalize sequences of
  whitespace to a single space.

* :class:`registry.StringSurroundedBySpaces` - Accepts any string but assures that
  it has a space preceding and following it. Useful for configuring a
  string that goes in the middle of a response.

* :class:`registry.StringWithSpaceOnRight` - Also accepts any string but assures
  that it has a space after it. Useful for configuring a string that
  begins a response.

* :class:`registry.Regexp` - Accepts only valid (Perl or Python) regular expressions

* :class:`registry.SpaceSeparatedListOfStrings` - Accepts a space-separated list of
  strings.

Custom Registry Types
=====================

If your plugin requires a more restrictive set of inputs, we recommend creating
a custom registry type so that invalid values can never be configured. This
in turn can simplify the code in your actual plugin.

Creating a Custom Registry Type
-------------------------------

Creating a custom registry type involves subclassing one of the built-in
registry types. For example, this NegativeInteger type only accepts negative
integers::

    class NegativeInteger(registry.Integer):
        """Value must be a negative integer."""

        def setValue(self, v):
            if v >= 0:
                self.error()
            super().setValue(self, v)

The most important parts here are the :func:`setValue` definition and the
docstring, which determines the error message when setting an invalid value.
Call :func:`self.error` on invalid input, and the superclass' :func:`setValue`
to actually set the value.

For more detailed examples, see ``src/registry.py`` in the source code.

What Subclasses Can I Use?
--------------------------

In addition to the built-in types, the following abstract types can be used
for custom registry types:

* :class:`registry.Value` - Provides all the core functionality of registry types
  (including acting as a group for other config variables to reside
  underneath), but nothing more.

* :class:`registry.OnlySomeStrings` - Allows you to specify only a certain set of
  strings as valid values. Simply override validStrings in the inheriting
  class and you're ready to go.

* :class:`registry.SeparatedListOf` - The generic class which is the parent class to
  registry.SpaceSeparatedListOfStrings. Allows you to customize four
  things: the type of sequence it is (list, set, tuple, etc.), what each
  item must be (String, Boolean, etc.), what separates each item in the
  sequence (using custom splitter/joiner functions), and whether or not
  the sequence is to be sorted.  See the following example, or the definitions
  of registry.SpaceSeparatedListOfStrings and
  registry.CommaSeparatedListOfStrings in :file:`src/registry.py`

Using a Custom Registry Type
----------------------------

Custom registry types can be passed in to any of the :func:`conf.register...` methods
mentioned above::

    class CommaSeparatedListOfProbabilities(registry.SeparatedListOf):
        Value = registry.Probability
        def splitter(self, s):
            return re.split(r'\s*,\s*', s)
        joiner = ', '.join

    conf.registerGlobalValue(SomePlugin, 'someConfVar',
        CommaSeparatedListOfProbabilities('0.0, 1.0', """Holds the list of
        probabilities for whatever."""))

The default value and config variable description are passed in as with any
other registry type.

Using 'configure' for supybot-wizard support
============================================

.. note::
  This section is mostly for reference. In practice, very few third-party
  plugins define support for supybot-wizard, as they are often installed after
  already configuring the bot.

Interactive configuration for plugins is defined in the ``configure`` function.
The ``supybot.questions`` module provides several convenience functions to make
implementing these easier:

* "expect" is the most general prompting mechanism which specifies certain
  inputs and a default response. It takes the following arguments:

    * prompt: The text to be displayed
    * possibilities: The list of possible responses (can be the empty
      list, [])
    * default (optional): Defaults to None. Specifies the default value
      to use if the user enters in no input.
    * acceptEmpty (optional): Defaults to False. Specifies whether or not
      to accept no input as an answer.

* "anything" is a special case of "expect" which takes anything
  (including no input) and has no default value specified. It takes only
  one argument:

    * prompt: The text to be displayed

* "something" is a special case of "expect" requiring some input and
  allowing an optional default. It takes the following arguments:

    * prompt: The text to be displayed
    * default (optional): Defaults to None. The default value to use if
      the user doesn't input anything.

* "yn" is for "yes or no" questions and forces the user to input
  a "y" for yes, or "n" for no. It takes the following arguments:

    * prompt: The text to be displayed
    * default (optional): Defaults to None. Default value to use if the
      user doesn't input anything.

All of these functions, with the exception of "yn", return whatever string
results as the answer whether it be input from the user or specified as the
default when the user inputs nothing. The "yn" function returns True for "yes"
answers and False for "no" answers.

For the most part, the latter three should be sufficient, but we expose "expect"
to anyone who needs a more specialized configuration.

Here is a full example::

  def configure(advanced):
      # This will be called by supybot to configure this module.  advanced is
      # a bool that specifies whether the user identified himself as an advanced
      # user or not.  You should effect your configuration by manipulating the
      # registry as appropriate.
      from supybot.questions import expect, anything, something, yn
      WorldDom = conf.registerPlugin('WorldDom', True)
      if yn("""The WorldDom plugin allows for total world domination
               with simple commands.  Would you like these commands to
               be enabled for everyone?""", default=False):
          WorldDom.globalWorldDominationRequires.setValue("")
      else:
          cap = something("""What capability would you like to require for
                             this command to be used?""", default="Admin")
          WorldDom.globalWorldDominationRequires.setValue(cap)
      dir = expect("""What direction would you like to attack from in
                      your quest for world domination?""",
                   ["north", "south", "east", "west", "ABOVE"],
                   default="ABOVE")
      WorldDom.attackDirection.setValue(dir)

The first thing this configure function asks for is whether
the world domination commands should be available to everyone.
If they say yes, we set the globalWorldDominationRequires
configuration variable to the empty string, signifying that no specific
:ref:`capabilities <capabilities>` are necessary. Otherwise, we prompt them for a specific
capability to check for, defaulting to the "admin" capability. This can also be
set to any arbitrary capability name, which the bot can automatically check for
as well.

Lastly, we ask for which direction they want to attack from as they
venture towards world domination. I prefer "death from above!", so I made that
the default response, but the standard cardinal directions are available as well.

.. _configuration-hooks:

Configuration hooks
===================

It is possible to define callbacks for when a configuration variable is
changed. This is usually not necessary, but can be used for instance to cache
results or pre-fetch data.

Let's say you want to write a plugin that prints `nick changed` in the logs
when `supybot.nick` is edited. You can do it like this::

    class LogNickChange(callbacks.Plugin):
        """Some useless plugin."""

        def __init__(self, irc):
            super().__init__(irc)
            conf.supybot.nick.addCallback(self._configCallback)

        def _configCallback(self, name=None):
            self.log.info('nick changed')

.. note::
    For the moment, the `name` parameter is never given when the callback is
    called. However, in the future, it will be set to the name of the variable
    that has been changed (useful if you want to use the same callback for
    multiple variable), so it is better to allow this parameter.
