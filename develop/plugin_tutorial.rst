.. _plugin-tutorial:

**********************************
Writing Your First Limnoria Plugin
**********************************

Introduction
============

This page is a top-down guide on how to write new plugins for Limnoria.

Before you start, you should be more-or-less familiar with how to use and
manage a Limnoria instance (loading plugins, configuring options, etc.).
You should also install a copy of Limnoria on the machine you intend to develop
plugins on, as it includes some additional scripts like
:command:`supybot-plugin-create` to generate the plugin skeleton.

We'll go through this tutorial by actually writing a new plugin, named Random
with just a few commands.

Generating the Plugin template
==============================

The recommended way to start writing a plugin is to use the
:command:`supybot-plugin-create` wizard. You can run this from within your bot's
plugins directory, or make a separate directory for all your own plugins and run
it there. (You can add additional plugin directories to your bot config using
``config directories.plugins``). The latter approach is probably easier if you
intend to publish your code afterwards, as it keeps your code separate from any
other plugins you've installed.

Here's an example session::

    $ supybot-plugin-create
    What should the name of the plugin be? Random

    Sometimes you'll want a callback to be threaded.  If its methods
    (command or regexp-based, either one) will take a significant amount
    of time to run, you'll want to thread them so they don't block the
    entire bot.

    Does your plugin need to be threaded? [y/n] n

    What is your name, so I can fill in the copyright and license
    appropriately? John Doe

    Do you wish to use Supybot's license for your plugin? [y/n] y

    Please provide a short description of the plugin: This plugin contains
    commands relating to random numbers, including random sampling from a list
    and a simple dice roller.

README.md
==========

This is the README page people will see when they download your plugin or view
it from a source control website. It's helpful to include a brief summary of
what the plugin does here, as well as list any third-party dependencies.

The :command:`supybot-plugin-create` wizard should have already filled in the
README with the summary you provided.

__init__.py
===========
The next file we'll look at is :file:`__init__.py`. If you're not so familiar
with the Python import mechanism, think of it as sort of the "glue" file that
pulls all the files in the plugin directory together when you load it.
There are also a few administrative items here that can be queried from the bot,
such as the plugin's author and contact info.

At the top of the file you'll see the copyright header, with your name added as
prompted in :command:`supybot-plugin-create`. Feel free to use whatever
license you choose: the default is the bot's 3-clause BSD. For our example,
we'll leave it as is.

Here is a list of attributes you should usually look at:

* ``__version__``: the plugin version. We'll just make ours "0.1"
* ``__author__`` should be an instance of the :class:`supybot.Author` class.
  This optionally includes a full name, a short name (usually IRC nick), and
  an e-mail address::

    __author__ = supybot.Author(name='Daniel DiPaolo', nick='Strike',
                                email='somewhere@someplace.xxx')

* ``__contributors__`` is a dictionary mapping :class:`supybot.Author`
  instances to lists of things they contributed. See e.g. `in the Plugin plugin
  <https://github.com/progval/Limnoria/blob/master/plugins/Plugin/__init__.py#L42-L49>`_.
  For now we have no contributors, so we'll leave it blank.

* ``__url__`` references the download URL for the plugin. Since this is just an
  example, we'll leave this blank.

The rest of :file:`__init__.py` really shouldn't be touched unless you are
using third-party modules in your plugin. If you are, then you need to add
additional import statements and ``reload`` calls to all those modules, so that
they get reloaded with the rest of the plugin::

    from . import config
    from . import plugin
    from importlib import reload
    reload(plugin) # In case we're being reloaded.
    # Add more reloads here if you add third-party modules and want them
    # to be reloaded when this plugin is reloaded.  Don't forget to
    # import them as well!

config.py
=========
:file:`config.py` is, unsurprisingly, where all the configuration stuff
related to your plugin goes. For this tutorial, the Random plugin is simple
enough that it doesn't need any config variables, so this file can be left as
is.

To briefly outline this file's structure: the ``configure`` function is used by
the :command:`supybot-wizard` wizard and allows users to configure the plugin
further if it's present when the bot is first installed. (In practice though,
this is seldomly used by third-party plugins as they're generally installed
*after* configuring the bot.)

The following line registers an entry for the plugin in Limnoria's config
registry, followed by any configuration groups and variable definitions::

    Random = conf.registerPlugin('Random')
    # This is where your configuration variables (if any) should go.  For example:
    # conf.registerGlobalValue(Random, 'someConfigVariableName',
    #     registry.Boolean(False, _("""Help for someConfigVariableName.""")))

Writing plugin configuration is explained in depth
in the :ref:`Advanced Plugin Config Tutorial <configuration-tutorial>`.

plugin.py
=========
``plugin.py`` includes the core code for the plugin. For most plugins this will
include command handlers, as well as anything else that's relevant to its
particular use case (database queries,
:ref:`HTTP server endpoints <http_plugins>`,
:ref:`IRC command triggers <do-method-handlers>`, etc.)

As with any Python module, you'll need to import any dependencies you want,
in addition to the standard ``supybot`` imports included in the plugin
template::

    import random

The bulk of the plugin definition then resides in a subclass of
:class:`callbacks.Plugin`. By convention, the class name is equal to the name of
the plugin, though this is not strictly required (the actual linkage is done by
the ``Class = Random`` statement at the end of the file). It is helpful to fill
in the plugin docstring with some more details on how to actually use the plugin
too: this info can be shown on a live bot using the
``plugin help <plugin name>`` command.

::

    class Random(callbacks.Plugin):
        """This plugin contains commands relating to random numbers, including random sampling from a list and a simple dice roller."""

        def __init__(self, irc):
            # Make sure to call the superclass' constructor when you define a custom one
            super().__init__(irc)
            self.rng = random.Random()  # create our rng
            self.rng.seed() # automatically seeds with current time

For this sample plugin, we define a custom constructor (``__init__``) that
instantiates a random number generator instance and pre-seeds it. This isn't
technically necessary for Python's ``random`` module, but it helps outline
how to write a similar constructor. Notice in particular how you must pass in
the ``irc`` argument in addition to ``self``.

.. note::
    TODO(jlu): semantically, what does ``irc`` refer to? Most plugins don't
    actually reference it on load time.

Basic command handler
---------------------

Our first command definition can immediately follow::

    # dummy comment to indent the below code consistently
        @wrap
        def random(self, irc, msg, args):
            """takes no arguments

            Returns the next random number from the random number generator.
            """
            irc.reply(str(self.rng.random()))

.. note::
    All functions used as commands must have an all lowercase name.

A command function taking in no arguments from IRC will still require 4
arguments; they are as follows:

- ``self``: refers to the class instance. It is common to keep local state
  for the plugin as instance variables within the plugin class.
- ``irc``: refers to the IRC network instance the command was called on
- ``msg``: a :class:`supybot.ircmsgs.IrcMsg` instance; refers to the
  IRC message that triggered this command.
- ``args``: a raw list of remaining unconverted arguments; new plugins that
  use :ref:`@wrap <using-wrap>` for automatic argument type conversion should
  never need to interact with ``args`` directly.

The function docstring is expected to be in a particular format. First, the very
first line dictates the argument list to be displayed when someone calls the
``help`` command on this command (i.e., ``help random``). Then, leave a blank
line and start the actual help string for the function. Don't worry about the
fact that it's tabbed in or anything like that, as the help command normalizes
it to make it look nice. This part should be fairly brief but sufficient to
explain the function and what (if any) arguments it requires. Remember that this
should fit in one IRC message which is typically around a 450 character limit.

The :py:meth:`irc.reply <supybot.callbacks.NestedCommandsIrcProxy.reply>` call
is a bit of magic: it issues a reply the same place as the message that
triggered the command. i.e. this may be in a channel or in a private
conversation with the bot.

Lastly, notice that commands go through the :ref:`@wrap <using-wrap>`
decorator for automatic argument type conversion. For commands that require no
parameters, calling ``@wrap`` with no arguments is enough.

Command handler with parameters
-------------------------------

Now let's create a command with some arguments and see how we use those in our
plugin commands. This ``seed`` command lets the user pick a specific RNG seed::

    # dummy comment to indent the below code consistently
        @wrap(['float'])
        def seed(self, irc, msg, args, seed):
            """<seed>

            Sets the internal RNG's seed value to <seed>.  <seed> must be a
            floating point number.
            """
            self.rng.seed(seed)
            irc.replySuccess()

For functions that use ``@wrap`` (described further in the
:ref:`Using commands.wrap tutorial <using-wrap>`), additional command arguments
are handled by:

1. Adding :ref:`type converters <wrap-converter-list>`, one for each parameter,
   to the list passed into ``@wrap``
2. Adding one function parameter per argument to the command function
   definition. (i.e. ``def seed(self, irc, msg, args, seed)`` instead of
   ``def seed(self, irc, msg, args)``)

We also modify the docstring to document this function. Note the syntax
on the first line: by convention, required arguments go in ``<>`` and optional
arguments should be surrounded by ``[]``.

The function body includes a new method
:py:meth:`irc.replySuccess <supybot.callbacks.RichReplyMethods.replySuccess>`.
This is just a generic "I succeeded" command which responds with whatever the
bot owner has configured in ``config supybot.replies.success``.
Also, by using ``@wrap``, we don't need to do any type checking inside the
function itself - this is handled separately, and invalid argument values will
cause the command to error before it reaches the wrapped function.

With this alone you'd be able to make a range of useful plugin commands, but
we'll go include some more examples to illustrate common patterns.

Command handler with list-type arguments
----------------------------------------
The next sample command is named ``sample`` (no pun intended): it takes a random
sample of arbitrary size from a list provided by the user::

    # dummy comment to indent the below code consistently
        def sample(self, irc, msg, args, n, items):
            """<number of items> <item1> [<item2> ...]

            Returns a sample of the <number of items> taken from the remaining
            arguments.  <number of items> must be less than the number
            of arguments given.
            """
            if n > len(items):
                # Calling irc.error with Raise=True is an alternative early return
                irc.error('<number of items> must be less than the number '
                          'of arguments.', Raise=True)
            sample = self.rng.sample(items, n)
            sample.sort()
            irc.reply(utils.str.commaAndify(sample))
        sample = wrap(sample, ['int', many('anything')])

The important thing to note is that list type arguments are rolled into one
parameter in the command function by the ``many`` filter. Similar "multiplicity"
handlers are documented :ref:`here <wrap-multiplicity-handlers>`.

We also update the docstring to use the ``[]`` convention when surrounding
optional arguments.

For this function's body,
:py:meth:`irc.error <supybot.callbacks.NestedCommandsIrcProxy.error>`
is like
:py:meth:`irc.replySuccess <supybot.callbacks.NestedCommandsIrcProxy.replySuccess>`
but for error messages. We prefer using this instead of ``irc.reply`` for error
signaling because its behaviour can be configured specially. For example, you
can force all errors to go in private by setting the ``reply.error.inPrivate``
option, and this can help reduce noise on a busy channel.
Also, ``irc.error()`` with no text will return a generic error message
configured in ``supybot.replies.error``, but this is not a valid call to
:py:meth:`irc.reply <supybot.callbacks.NestedCommandsIrcProxy.reply>`.

``utils.str.commaAndify`` is a simple helper that takes a list of strings
and turns it into "item1, item2, item3, item4, and item5" for an arbitrary
length. Limnoria has accumulated many such helpers in its lifetime, many of
which are described in the :ref:`Using Utils <using-utils>` page.

Command handler with optional arguments
---------------------------------------
Now for the last command that we will add to our plugin.py. This ``diceroll``
command will allow the bot users to roll an arbitrary n-sided die, with n
defaulting to 6::

    # dummy comment to indent the below code consistently
        def diceroll(self, irc, msg, args, n):
            """[<number of sides>]

            Rolls a die with <number of sides> sides.  The default number of sides
            is 6.
            """
            s = 'rolls a %s' % self.rng.randrange(1, n)
            irc.reply(s, action=True)
        diceroll = wrap(diceroll, [additional(('int', 'number of sides'), 6)])

The only new thing described here is that ``irc.reply(..., action=True)`` makes
the bot perform a `/me`. There are some other flags described in the
:py:meth:`irc.reply <supybot.callbacks.NestedCommandsIrcProxy.reply>`
documentation too: common ones include ``private=True``, which
forces a private message, and ``notice=True``, which forces the reply to use
NOTICE instead of PRIVMSG.

test.py
=======
The easy way to test any plugin would be to start up a bot, load the plugin, and
run all the commands a few times to verify that they work. But this takes time,
and as a project grows larger, starts to be a tedious and error-prone process...

This is where automated testing comes in. Limnoria has a test harness built upon
the `Python unittest library <https://docs.python.org/3/library/unittest.html>`_
that abstracts away all the dependencies of live testing (i.e. the IRC
client and server) and allows you to cover your entire plugin's functionality
within a few seconds.

How it works
------------

Plugin test cases inherit from
:class:`supybot.test.PluginTestCase` or
:class:`supybot.test.ChannelPluginTestCase` and include
:ref:`several methods <plugin-test-methods>` to interact with a simulated
instance of the bot, in addition to the
`standard assertion functions <https://docs.python.org/3/library/unittest.html#assert-methods>`_
provided by the unittest library.

Running the tests for a Limnoria plugin is done using the
:command:`supybot-test` command: i.e. ``supybot-test /path/to/your/plugin``

The structure of these test classes, as well
as interactions with features like Limnoria's config system are described in
detail in the :ref:`Advanced Plugin Testing guide <plugin-testing-guide>`.

Functional testing examples
---------------------------

For a command where we don't care about the exact output, the usual approach is
to check that invocations raise or don't raise an error. For a command that
generates a purely random output, this applies too since we can't predict what
the result will be::

  class RandomTestCase(PluginTestCase):
      # This tuple determines which plugins to load in the test case
      plugins = ('Random',)

      def testRandom(self):
          self.assertNotError('random')

          # This throws, because the command doesn't expect any arguments
          self.assertError('random abcdef')

However, this is less true if you pre-seed the RNG, as then you're guaranteed
a repeatable result. The following snippet introduces
``assertResponse(commandPlusArgs, expectedOutput)``, where ``commandPlusArgs``
is the full bot command including arguments, all as one string::

    # dummy comment to indent the below code consistently
        def testSeed(self):
            self.assertNotError('seed 20')
            self.assertResponse('random', '0.9056396761745207')
            self.assertResponse('random', '0.6862541570267026')
            self.assertNotError('seed 20')
            self.assertResponse('random', '0.9056396761745207')
            self.assertNotError('seed 1234')
            self.assertResponse('random', '0.9664535356921388')

Alternatively, you can use ``getMsg(command)`` to fetch the output of a bot
command as a string and reuse it::

    # dummy comment to indent the below code consistently
        def testSeed(self):
            self.assertNotError('seed 20')
            num1 = self.getMsg('random')
            num2 = self.getMsg('random')

            self.assertNotError('seed 20')
            num1_again = self.getMsg('random')

            self.assertEqual(num1, num1_again)
            self.assertNotEqual(num1, num2)

Another common practice is to use regular expressions to match the output of
a command:

.. note::
  The :func:`assertRegexp` defined in Limnoria is `not` the same as
  :func:`assertRegex` from the standard unittest library. The latter
  compares a regexp against a bare string, not the output of a bot command.
  (For historical reasons, we have this confusing name.)

::

    # dummy comment to indent the below code consistently
        def testSample(self):
            self.assertError('sample 20 foo')  # can't sample 20 from only 1 element
            self.assertResponse('sample 1 foo', 'foo')
            self.assertRegexp('sample 2 foo bar', '... and ...')
            self.assertRegexp('sample 3 foo bar baz', '..., ..., and ...')
            # assertNotRegexp(commandWithArgs, regexp) also works as expected

        def testDiceRoll(self):
            self.assertActionRegexp('diceroll', 'rolls a \d')

Conclusion
==========
You are now well prepared to write Limnoria plugins. A few words of wisdom:

* Read other people's plugins, especially the included plugins and ones by
  the core developers. We can't possibly document all the things that Limnoria
  can do, though we try our best.

* Hack new functionality into existing plugins first if writing a new
  plugin is too daunting.

* Come ask us questions in #limnoria on Libera. Going back to the
  first point above, the developers themselves can help you even more than
  the docs can (though we prefer you read the docs first).

* :ref:`Share your plugins with the world <distributing-plugins>`
  and make Limnoria all that more attractive for other users so they will want
  to write their plugins for Limnoria as well.

* And of course, have fun!
