************
Capabilities
************

.. note::
    I wrote this section with the little knowledge I have of the capabilities
    system; I work mainly by testing different possibilities until I get what
    I want.
    As for all the documentation, feel free to contact me to
    correct/enhance it.

First, you should know how capabilities work
:ref:`on the user side <capabilities>`.

Checking for a capability given its name
========================================

You only have to use ``ircdb.checkCapability(prefix, 'capability')``.

You can also override some behavior of the capability system. Here is the
complete documentation of ``ircdb.checkCapabiltiy``:

.. autofunction:: supybot.ircdb.checkCapability
    :noindex:

Manipulating capability names
=============================

Althrough you can manipulate capability names with string operations,
Supybot provides a few methods to do that “in the abstract” (could be
useful if we change the capability syntax one day…):

.. autofunction:: supybot.ircdb.isCapability
    :noindex:

.. autofunction:: supybot.ircdb.makeChannelCapability
    :noindex:

.. autofunction:: supybot.ircdb.isChannelCapability
    :noindex:

.. autofunction:: supybot.ircdb.makeAntiCapability
    :noindex:

.. autofunction:: supybot.ircdb.unAntiCapability
    :noindex:

.. autofunction:: supybot.ircdb.invertCapability
    :noindex:

.. autofunction:: supybot.ircdb.isAntiCapability
    :noindex:

.. autofunction:: supybot.ircdb.canonicalCapability
    :noindex:
