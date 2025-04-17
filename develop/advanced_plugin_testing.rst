.. _plugin-testing-guide:

***********************
Advanced Plugin Testing
***********************

Why Write Tests?
================

`Automated testing <https://en.wikipedia.org/wiki/Test_automation>`_ is a
hallmark of modern software development. Adding a test suite to your plugin
makes it easier to update and redesign your code, update its dependencies, etc.
without having to manually check that every feature still works.

Plugin Tests
============

First, we assume that you have already gone through the
:ref:`Plugin Development Tutorial <plugin-tutorial>` and created the plugin
boilerplate with :command:`supybot-plugin-create`.

Plugin Test Case Classes
------------------------

Limnoria comes with two plugin test case classes,
:class:`supybot.test.PluginTestCase` and
:class:`supybot.test.ChannelPluginTestCase`. Use the latter when the plugin's
commands need to be run in a channel, and the former otherwise.

Both of these classes inherit from Python's built-in
`unittest.TestCase <https://docs.python.org/3/library/unittest.html>`_; as such,
most of the documentation there applies to plugin tests too.

Note that instead
of ``python -m unittest``, Limnoria plugin tests are run using the
:command:`limnoria-test` command: e.g. ``limnoria-test /path/to/your/Plugin``

Plugin Test Case Example
------------------------

A basic plugin test case requires:

* The class declaration (subclassing one of the TestCase classes above)
* A list of plugins to be loaded for these tests. Usually this is just the name
  of the plugin you're testing. Note that the **Owner**, **Misc**, and **Config**
  plugins are always automatically loaded
* Some test methods

::

    class MyPluginTestCase(PluginTestCase):
        # List of plugins to load
        plugins = ('MyPlugin',)

        def testEcho(self):
            # Replace the command and expected response with your own,
            # add other assertions, etc.
            self.assertResponse('echo Hello world', 'Hello world')

        def testSomethingElse(self):
            # Add another test case here

As with Python's unittest module in general, test methods must begin with
``test``. When adding helper methods in this class, they should start with
something else.

We recommend keeping each test method short and targeted to a specific feature,
so that running the test file will clearly show which checks passed or failed.
It is fine to give test methods longer, more specific names
(e.g. ``testOnlyRespondToRegisteredUsers``) to achieve this.

Including Extra Setup
---------------------

Plugin tests may define extra setup commands by overriding ``setUp()`` from
Python's unittest module:

.. code-block::
    :dedent: 0

        def setUp(self):
            # Important! This sets up the bot's simulated IRC network for testing
            super().setUp()

            # Define the identity of the user who we send messages as
            self.prefix = 'foo!bar@baz'

            # Send a message to the simulated IRC network, in this case to register
            # an account with the bot. self.nick refers to the bot's nick.
            self.feedMsg('register tester moo', to=self.nick, frm=self.prefix)
            m = self.getMsg(' ')  # Get the response for the last command

If your ``setUp`` function does work that should be cleaned up after, add a
``tearDown`` method as well. As with ``setUp``, you should also call the
parent class' ``tearDown`` method *after* running your own cleanup.

Setting Config Variables for Testing
------------------------------------

Config variables can be set at the test case level. For example, to disable
nested commands for this test, you can add a ``config`` dict::

    class MyPluginTestCase(PluginTestCase):
        config = {'supybot.commands.nested': False}

        def testThisThing(self):
            # stuff

Temporarily setting a configuration variable
--------------------------------------------

To temporarily set a config variable inside a test method, use the
``conf.supybot.<variable name>.context(<new value>)`` context manager::

    import supybot.conf as conf

    class MyPluginTestCase(PluginTestCase):
        def testThisThing(self):
            with conf.supybot.commands.nested.context(False):
                # stuff
            # when leaving the context manager, the config value is reverted to default

.. _plugin-test-methods:

Plugin Test Methods
===================

In addition to Python's `built-in assertions <https://docs.python.org/3/library/unittest.html#assert-methods>`_,
here are all the test methods defined in Limnoria. These are instance methods,
so they should be accessed as ``self.assertResponse(...)``, etc.

assertResponse(query, expectedResponse)
    Feeds query to the bot as a
    message and checks to make sure the response is expectedResponse. The
    test fails if they do not match (note that prefixed nicks in the
    response do not need to be included in the expectedResponse).

assertError(query)
    Feeds query to the bot and expects an error in
    return. Fails if the bot doesn't return an error.

assertNotError(query)
    The opposite of assertError. It doesn't matter
    what the response to query is, as long as it isn't an error. If it is
    not an error, this test passes, otherwise it fails.

assertRegexp(query, regexp, flags=re.I)
    Feeds query to the bot and
    expects something matching the regexp (no m// required) in regexp with
    the supplied flags. Fails if the regexp does not match the bot's
    response.

.. note::
  This :func:`assertRegexp` function is `not` the same as :func:`assertRegex`
  from Python's unittest library. :func:`assertRegex` compares a regexp against
  a bare string, while :func:`assertRegexp` compares it to the output of a bot
  command.
  (For historical reasons, we have this confusing name.)

assertNotRegexp(query, regexp, flags=re.I)
    The opposite of
    assertRegexp. Fails if the bot's output matches regexp with the
    supplied flags.

assertHelp(query)
    Expects query to return the help for that command.
    Fails if the command help is not triggered.

assertAction(query, expectedResponse=None)
    Feeds query to the bot and
    expects an action in response, specifically expectedResponse if it is
    supplied. Otherwise, the test passes for any action response.

assertActionRegexp(query, regexp, flags=re.I)
    Basically like
    assertRegexp but carries the extra requirement that the response must
    be an action or the test will fail.

Utilities
---------

feedMsg(query, to=None, frm=None)
    Simply feeds query to whoever is
    specified in to or to the bot itself if no one is specified. Can also
    optionally specify the hostmask of the sender with the frm keyword.
    Does not actually perform any assertions.

getMsg(query)
    Feeds query to the bot and gets the response.

Tests for Helper Code
=====================

If you want to test plugin helpers individually without running commands from
your commands, you can add additional test classes inheriting from
:class:`supybot.test.SupyTestCase`. This is a light wrapper around
:class:`unittest.TestCase` that provides some additional logging.

The **MoobotFactoids** plugin has an example of this (``OptionListTestCase``).

The same rules for using ``setUp`` and ``tearDown`` apply: be sure to call the
parent class implementations in your overridden functions.
