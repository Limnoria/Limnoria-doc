.. _asking-for-help:

***************
Asking for help
***************

First, check out the Frequently Asked Questions for :ref:`users <user-faq>`
or :ref:`developers <develop-faq>`. If you cannot find your answer there,
read on.


Where to ask
============

`#limnoria on Libera.Chat <ircs://irc.libera.chat:6697/#limnoria>`
(main channel, in English) or
`#limnoria-fr on Libera.Chat <ircs://irc.libera.chat:6697/#limnoria-fr>`
(French, significantly less active)


Question checklist
==================

To make sure you get an answer as fast as possible, make sure to provide
this information up front:

1. Whether you are a user or a plugin developer
2. What you want to do (eg. "when I run command X, I want the bot to reply Y")
3. If relevant, what you tried and why it does not work
   (eg. "when I run command X, the but replies Z")
4. If you get any error, copy-paste it instead of paraphrasing, and only redact
   sensitive information
5. If you get an error, look at the logs (:file:`logs/messages.log` in your
   bot's config directory) from the ~10 seconds before and after the error,
   redact sensitive information, and pastebin them as-is.
   Do not remove log lines that seem irrelevant unless you are sure they are.


Specific details to include
===========================


If your question is about a specific plugin
-------------------------------------------

Mention the plugin's name.
If it is not a built-in plugin, please provide a link to where you got it from.


If the issue is about an unexpected bot behavior
------------------------------------------------

(eg. if it sends a message it should not),

Give us the list of plugins loaded (using the ``list``) command.


If the bot does not start
-------------------------

Run this in the same shell as you are trying to start the bot from:

```bash
which limnoria
head -n 1 $(which limnoria)
```

and tell us what this returns.


If you are writing a plugin
---------------------------

Make the whole source code available online (eg. on `Codeberg <https://codeberg.org/>`_
or `GitHub <https://github.com/>`_) and give us a link to it.
