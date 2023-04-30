.. _supybot-schedule:

***************************************
Event scheduling using supybot.schedule
***************************************

.. code-block:: python

   ###
   # This is an example plugin that sends a message to a channel every 60 seconds,
   # includes commands to stop, start, and reset the spammer, and a command to
   # schedule a one-off event
   ###

   # these are the default plugin modules
   import supybot.utils as utils
   from supybot.commands import *
   import supybot.plugins as plugins
   import supybot.ircutils as ircutils
   import supybot.callbacks as callbacks
   # these are the extra modules we'll be using
   import time
   import supybot.ircmsgs as ircmsgs
   import supybot.schedule as schedule

   class Spam(callbacks.Plugin):
       """Add the help for "@plugin help Spam" here
       This should describe *how* to use this plugin."""

       def __init__(self, irc):
           super().__init__(irc)
           # this is the channel we want to spam, and how frequently we want to do it.
           # It would be nicer to put it in a supybot config variable instead, but for
           # this demonstration, defining it in the plugin itself is fine.
           self.spamChannel = '#testytest'
           self.spamTime = 60
           # scheduler events are global, so we want to test to make sure the event doesn't
           # already exist.  That is, even if the plugin is reloaded, the event sticks
           # around.  That means that you also have to be a little careful with your
           # event names, especially if you have multiple plugins adding events.  It also
           # means that events will stick around even if the plugin they originated in
           # is unloaded.  I don't know how to delete them automatically on an unload, but
           # it's not normally an issue.  Just make sure to stop the event before unloading
           # the plugin if that's what you want.
           try:
               schedule.removeEvent('mySpamEvent')
           except KeyError:
               pass
           # now that we know there's no event by that name scheduled, we can create one.
           # but first, we need to define a local helper function that will do the thing
           # that we want.  You can put the full contents into here, but I prefer to use
           # separate methods, as it makes the code easier to get around in.  We need
           # the helper function because when you add events, you can't include arguments.
           def myEventCaller():
               self.spamEvent(irc)
           # and now we can schedule the actual event
           # schedule.addPeriodicEvent(f, t, name=None, now=True)
           # f is the method, t is the time in seconds, name gives it a name and is optional
           # (but highly recommended, so that you can refer to the event in the future.
           # otherwise, it's easy to accumulate duplicate events), and 'now' specifies
           # whether to perform the action immediately, or to wait until time is up to
           # perform it for the first time.  Default is True.
           schedule.addPeriodicEvent(myEventCaller, self.spamTime, 'mySpamEvent')
           self.irc = irc

       # make sure to have a capital letter or underscore or something, as it's not a method
       # that we want turned into an IRC command
       def spamEvent(self, irc):
           # we need to use queueMsg() rather than reply(), because when the event is
           # scheduled on loading the plugin (as opposed to scheduling it with one of the
           # commands that we'll define next), it recieves its irc object from __init__().
           # When the bot is started, the irc object that comes from __init__() doesn't
           # include a reply() method, because it's not loading in response to a command;
           # it's loading on the bot startup.  If you don't want your event to be scheduled
           # automatically and so don't schedule it from __init__(), but only from an IRC
           # command, then it's safe to use irc.reply(), as there are no circumstances
           # under which the irc object won't have a reply() method.
           irc.queueMsg(ircmsgs.privmsg(self.spamChannel, 'I\'m spamming the channel!'))

       def start(self, irc, msg, args):
           """takes no arguments

           A command to start the spammer."""
           # don't forget to redefine the event wrapper
           def myEventCaller():
               self.spamEvent(irc)
           try:
               schedule.addPeriodicEvent(myEventCaller, self.spamTime, 'mySpamEvent', False)
           except AssertionError:
               irc.reply('Error: the spammer was already running!')
           else:
               irc.reply('Spammer started!')
       start = wrap(start)

       def stop(self, irc, msg, args):
           """takes no arguments

           A command to stop the spammer."""
           try:
               schedule.removeEvent('mySpamEvent')
           except KeyError:
               irc.reply('Error: the spammer wasn\'t running!')
           else:
               irc.reply('Spammer stopped.')
       stop = wrap(stop)

       def reset(self, irc, msg, args):
           """takes no arguments

           Resets the spammer.  Can be useful if something changes and you want the
           spam to reflect that.  For example, if you defined the spamChannel as a
           supybot config, and changed it while the spammer was running, it would still
           keep going on the same channel until you reset it."""
           def myEventCaller():
               self.spamEvent(irc)
           try:
               schedule.removeEvent('mySpamEvent')
           except KeyError:
               irc.reply('Spammer wasn\'t running')
           schedule.addPeriodicEvent(myEventCaller, self.spamTime, 'mySpamEvent', False)
           irc.reply('Spammer reset sucessfully!')
       reset = wrap(reset)

       # Here's an example of a one-off event, scheduled by an IRC command
       def sayhi(self, irc, msg, args, delay):
           """&lt;time delay&gt;

           Says hi after the specified delay"""
           def myEventCaller():
               self.Hello(irc)
           # for a one-off event, the time is an absolute time, not relative.  So we need
           # to get the current time and add to it however long we want to wait
           t = time.time() + delay
           # since we don't specify a name, we won't be able to reference the events in
           # the future, but that's ok, because these are one-off events, so even if you
           # do call it multiple times, it'll just reply that same number of times and
           # then stop.  But in some circumstances you might want to name them.  Just
           # remember that it'll give an AssertionError if you try to create two events
           # with the same name
           schedule.addEvent(myEventCaller, t)
           irc.reply('"hi" scheduled for %d seconds from now!' % delay)
       sayhi = wrap(sayhi, ['positiveInt'])

       def Hello(self, irc):
           # since the irc object is coming from an IRC command, rather than from __init__(),
           # it's guaranteed to have a reply() method, so it's safe to use that.  It
           # might be better to to use queueMsg() instead, regardless, but I don't know
           # enough about the supybot internals to say whether one is prefered over
           # the other
           irc.reply('hi!')

   Class = Spam

This example comes from the Gribble Wiki:
https://sourceforge.net/p/gribble/wiki/Supybot.schedule/history

Copyright 2010, 2015, nanotube and quantumlemur
licensed under the `Creative Commons Attribution ShareAlike 3.0 Unported license <https://creativecommons.org/licenses/by-sa/3.0/>`_
and/or the `GNU Free Documentation License v 1.3 or later <https://www.gnu.org/licenses/fdl.html>`_
