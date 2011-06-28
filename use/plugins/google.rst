
.. _plugin-google:

The Google plugin
=================

Web search
----------

.. _command-google-google:

google google <search> [--{filter,language} <value>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches google.com for the given string. As many results as can fit
are included. *--language* accepts a language abbreviation; *--filter
accepts* a filtering level ('active', 'moderate', 'off').

.. _command-google-cache:

google cache <url>
^^^^^^^^^^^^^^^^^^

Returns a link to the cached version of *<url>* if it is available.

.. _command-google-lucky:

google lucky [--snippet] <search>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a google search, but only returns the first result.
If option *--snippet* is given, returns also the page text snippet.

.. _command-google-fight:

google fight <search string> <search string> [<search string> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the results of each search, in order, from greatest number
of results to least.

Others
------

.. _command-google-phonebook:

google phonebook <phone number>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Looks *<phone number>* up on Google.

.. _command-google-calc:

google calc <expression>
^^^^^^^^^^^^^^^^^^^^^^^^

Uses Google's calculator to calculate the value of *<expression>*.

.. _command-google-translate:

google translate <from-language> [to] <to-language> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* translated from *<from-language>* into *<to-language>*.
Beware that translating to or from languages that use multi-byte
characters may result in some very odd results.

