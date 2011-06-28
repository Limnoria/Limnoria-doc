
.. _plugin-string:

The String plugin
=================

.. _command-soundex:

soundex <string> [<length>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Soundex hash to a given length. The length defaults to
4, since that's the standard length for a soundex hash. For unlimited
length, use 0.


.. _command-xor:

xor <password> <text>
^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* XOR-encrypted with *<password>*. See
http://www.yoe.org/developer/xor.html for information about XOR
encryption.


.. _command-re:

re <regexp> <text>
^^^^^^^^^^^^^^^^^^

If *<regexp>* is of the form m/regexp/flags, returns the portion of
*<text>* that matches the regexp. If *<regexp>* is of the form
s/regexp/replacement/flags, returns the result of applying such a
regexp to *<text>*.


.. _command-levenshtein:

levenshtein <string1> <string2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the levenshtein distance (also known as the "edit distance"
between *<string1>* and *<string2>*)


.. _command-decode:

decode <encoding> <text>
^^^^^^^^^^^^^^^^^^^^^^^^

Returns an un-encoded form of the given text; the valid encodings are
available in the documentation of the Python codecs module:
*<http://docs.python.org/library/codecs.html#standard-encodings>*.


.. _command-sha:

sha <text>
^^^^^^^^^^

Returns the SHA hash of a given string. Read
http://www.secure-hash-algorithm-md5-sha-1.co.uk/ for more information
about SHA.


.. _command-chr:

chr <number>
^^^^^^^^^^^^

Returns the character associated with the 8-bit value *<number>*


.. _command-len:

len <text>
^^^^^^^^^^

Returns the length of *<text>*.


.. _command-encode:

encode <encoding> <text>
^^^^^^^^^^^^^^^^^^^^^^^^

Returns an encoded form of the given text; the valid encodings are
available in the documentation of the Python codecs module:
*<http://docs.python.org/library/codecs.html#standard-encodings>*.


.. _command-ord:

ord <letter>
^^^^^^^^^^^^

Returns the 8-bit value of *<letter>*.


