
.. _plugin-dict:

The Dict plugin
===============

Commands
--------

.. _command-dict-synonym:

dict synonym <word> [<word> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a random synonym from the Moby Thesaurus (moby-thes) database.

If given many words, gets a random synonym for each of them.

Quote phrases to have them treated as one lookup word.

.. _command-dict-dict:

dict dict [<dictionary>] <word>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Looks up the definition of *<word>* on the dictd server specified by
the :ref:`supybot.plugins.Dict.server` config variable.

.. _command-dict-random:

dict random
^^^^^^^^^^^

Returns a random valid dictionary.

.. _command-dict-dictionaries:

dict dictionaries
^^^^^^^^^^^^^^^^^

Returns the dictionaries valid for the dict command.



.. _plugin-dict-config:

Configuration
-------------

.. _supybot.plugins.Dict.default:

supybot.plugins.Dict.default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines the default dictionary the bot will ask for definitions in. If this value is '*' (without the quotes) the bot will use all dictionaries to define words.

.. _supybot.plugins.Dict.public:

supybot.plugins.Dict.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.Dict.server:

supybot.plugins.Dict.server
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: dict.org

Determines what server the bot will retrieve definitions from.

