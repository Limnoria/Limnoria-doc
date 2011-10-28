
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



.. _plugin-google-config:

Configuration
-------------

.. _supybot.plugins.Google.bold:

supybot.plugins.Google.bold
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether results are bolded.

.. _supybot.plugins.Google.colorfulFilter:

supybot.plugins.Google.colorfulFilter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the word 'google' in the bot's output will be made colorful (like Google's logo).

.. _supybot.plugins.Google.defaultLanguage:

supybot.plugins.Google.defaultLanguage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: lang_en

Determines what default language is used in searches. If left empty, no specific language will be requested.

.. _supybot.plugins.Google.maximumResults:

supybot.plugins.Google.maximumResults
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 8

Determines the maximum number of results returned from the google command.

.. _supybot.plugins.Google.searchFilter:

supybot.plugins.Google.searchFilter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: moderate

Determines what level of search filtering to use by default. 'active' - most filtering, 'moderate' - default filtering, 'off' - no filtering

.. _supybot.plugins.Google.searchSnarfer:

supybot.plugins.Google.searchSnarfer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: False

Determines whether the search snarfer is enabled. If so, messages (even unaddressed ones) beginning with the word 'google' will result in the first URL Google returns being sent to the channel.

.. _supybot.plugins.Google.public:

supybot.plugins.Google.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

.. _supybot.plugins.Google.referer:

supybot.plugins.Google.referer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 

Determines the URL that will be sent to Google for the Referer field of the search requests. If this value is empty, a Referer will be generated in the following format: http://$server/$botName

