
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

