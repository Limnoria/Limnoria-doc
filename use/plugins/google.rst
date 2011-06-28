
.. _plugin-google:

The Google plugin
=================

.. command-google:

google <search> [--{filter,language} <value>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches google.com for the given string. As many results as can fit
are included. *--language* accepts a language abbreviation; *--filter
accepts* a filtering level ('active', 'moderate', 'off').


.. command-search:

search Perform a search using Google's AJAX API.
 search("search phrase", options={})
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Valid options are:
smallsearch - True/False (Default: False)
filter - {active,moderate,off} (Default: "moderate")
language - Restrict search to documents in the given language
(Default: "lang_en")


.. command-cache:

cache <url>
^^^^^^^^^^^

Returns a link to the cached version of *<url>* if it is available.


.. command-lucky:

lucky [--snippet] <search>
^^^^^^^^^^^^^^^^^^^^^^^^^^

Does a google search, but only returns the first result.
If option *--snippet* is given, returns also the page text snippet.


.. command-fight:

fight <search string> <search string> [<search string> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the results of each search, in order, from greatest number
of results to least.


.. command-phonebook:

phonebook <phone number>
^^^^^^^^^^^^^^^^^^^^^^^^

Looks *<phone number>* up on Google.


.. command-calc:

calc <expression>
^^^^^^^^^^^^^^^^^

Uses Google's calculator to calculate the value of *<expression>*.


.. command-translate:

translate <from-language> [to] <to-language> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* translated from *<from-language>* into *<to-language>*.
Beware that translating to or from languages that use multi-byte
characters may result in some very odd results.


