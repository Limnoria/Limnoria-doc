
.. _plugin-dict:

The Dict plugin
===============

.. _command-synonym:

synonym <word> [<word> ...]
        Gets a random synonym from the Moby Thesaurus (moby-thes) database.
        
        If given many words, gets a random synonym for each of them.
        
        Quote phrases to have them treated as one lookup word.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _command-dict:

dict [<dictionary>] <word>
^^^^^^^^^^^^^^^^^^^^^^^^^^

Looks up the definition of *<word>* on the dictd server specified by
the supybot.plugins.Dict.server config variable.


.. _command-random:

random
^^^^^^

Returns a random valid dictionary.


.. _command-dictionaries:

dictionaries
^^^^^^^^^^^^

Returns the dictionaries valid for the dict command.


