.. _glossary:

Glossary
========

.. note::

   This page is a work in progress, and is still very incomplete.
   Please send your ideas/suggestions on the IRC channel!

.. glossary::

   boolean
      A value that can be either True or False.

   command
      An action that can be triggered by typing its name on IRC.

   configuration variable
   configuration value
      A configuration variable is an object with a name that can be set
      to different values to change the behavior of the bot.

      They can be changed with the :ref:`plugin-Config` plugin.

   inFilter
      Some code that replaces messages right after
      the bot receives them from IRC, and before it starts processing them.

      This is the opposite of :term:`outFilter`.

   network
      An IRC network, ie. a group of connected IRC servers, that share
      the same set of channels and users

   outfilter
   outFilter
      Some code or command that replaces messages just before
      the bot sends them to IRC.

      Some plugins define them for their own purposes, such as
      :ref:`plugin-ShrinkUrl` to replace URLs.
      The :ref:`plugin-Filter` plugin provides an ``outfilter`` command
      to allow bot admins to customize the messages written by their bot.

      This is the opposite of :term:`inFilter`.

   plugin
      Some Python code/package that provides :term:`commands`.

   server
      A node in an IRC :term`network`. Limnoria usually does not care
      about servers, and deals with entire networks as a single entity.

   specific
   channel-specific
   network-specific
      A :term:`configuration variable` is said to be channel-specific
      and/or network-specific when it can takes different values depending
      on the channel/network it is used in.
