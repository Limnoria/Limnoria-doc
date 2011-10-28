
.. _plugin-string:

The String plugin
=================

Hashes
------

.. _command-string-soundex:

string soundex <string> [<length>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Soundex hash to a given length. The length defaults to
4, since that's the standard length for a soundex hash. For unlimited
length, use 0.

.. _command-string-sha:

string sha <text>
^^^^^^^^^^^^^^^^^

Returns the SHA hash of a given string. Read
http://www.secure-hash-algorithm-md5-sha-1.co.uk/ for more information
about SHA.

Encoding/decoding
-----------------

.. _command-string-xor:

string xor <password> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* XOR-encrypted with *<password>*. See
http://www.yoe.org/developer/xor.html for information about XOR
encryption.

.. _command-string-encode:

string encode <encoding> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns an encoded form of the given text; the valid encodings are
available in the documentation of the Python codecs module:
*<http://docs.python.org/library/codecs.html#standard-encodings>*.

.. _command-string-decode:

string decode <encoding> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns an un-encoded form of the given text; the valid encodings are
available in the documentation of the Python codecs module:
*<http://docs.python.org/library/codecs.html#standard-encodings>*.

.. _command-string-ord:

string ord <letter>
^^^^^^^^^^^^^^^^^^^

Returns the 8-bit value of *<letter>*.

.. _command-string-chr:

string chr <number>
^^^^^^^^^^^^^^^^^^^

Returns the character associated with the 8-bit value *<number>*

Miscellaneous
-------------

.. _command-string-re:

string re <regexp> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^

If *<regexp>* is of the form m/regexp/flags, returns the portion of
*<text>* that matches the regexp. If *<regexp>* is of the form
s/regexp/replacement/flags, returns the result of applying such a
regexp to *<text>*.

.. _command-string-levenshtein:

string levenshtein <string1> <string2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the levenshtein distance (also known as the "edit distance"
between *<string1>* and *<string2>*)

.. _command-string-len:

string len <text>
^^^^^^^^^^^^^^^^^

Returns the length of *<text>*.



.. _plugin-string-config:

Configuration
-------------

.. _supybot.plugins.String.levenshtein:

supybot.plugins.String.levenshtein
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.String.levenshtein.max:

supybot.plugins.String.levenshtein.max
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 256

Determines the maximum size of a string given to the levenshtein command. The levenshtein command uses an O(m*n) algorithm, which means that with strings of length 256, it can take 1.5 seconds to finish; with strings of length 384, though, it can take 4 seconds to finish, and with strings of much larger lengths, it takes more and more time. Using nested commands, strings can get quite large, hence this variable, to limit the size of arguments passed to the levenshtein command.

.. _supybot.plugins.String.re:

supybot.plugins.String.re
^^^^^^^^^^^^^^^^^^^^^^^^^





.. _supybot.plugins.String.re.timeout:

supybot.plugins.String.re.timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 0.1

Determines the maximum time, in seconds, that a regular expression is given to execute before being terminated. Since there is a possibility that user input for the re command can cause it to eat up large amounts of ram or cpu time, it's a good idea to keep this low. Most normal regexps should not take very long at all.

.. _supybot.plugins.String.public:

supybot.plugins.String.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

