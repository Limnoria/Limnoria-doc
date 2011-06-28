
.. _plugin-format:

The Format plugin
=================

Capitals
--------

.. _command-format-upper:

format upper <text>
^^^^^^^^^^^^^^^^^^^

Returns *<text>* uppercased.

.. _command-format-capitalize:

format capitalize <text>
^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* capitalized.

.. _command-format-lower:

format lower <text>
^^^^^^^^^^^^^^^^^^^

Returns *<text>* lowercased.

.. _command-format-title:

format title <text>
^^^^^^^^^^^^^^^^^^^

Returns *<text>* titlecased.

Text modifications
------------------

.. _command-format-format:

format format <format string> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Expands a Python-style format string using the remaining args. Just be
sure always to use %s, not %d or %f or whatever, because all the args
are strings.

.. _command-format-color:

format color <foreground> [<background>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* with foreground color *<foreground>* and background color
*<background>* (if given)

.. _command-format-repr:

format repr <text>
^^^^^^^^^^^^^^^^^^

Returns the text surrounded by double quotes.

.. _command-format-replace:

format replace <substring to translate> <substring to replace it with> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces all non-overlapping occurrences of *<substring to translate>*
with *<substring to replace it with>* in *<text>*.

.. _command-format-field:

format field <number> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the *<number>th* space-separated field of *<text>*. I.e., if text
is "foo bar baz" and *<number>* is 2, "bar" is returned.

.. _command-format-concat:

format concat <string 1> <string 2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Concatenates two strings. Do keep in mind that this is *not* the same
thing as join "", since if *<string 2>* contains spaces, they won't be
removed by concat.

.. _command-format-translate:

format translate <chars to translate> <chars to replace those with> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces *<chars to translate>* with *<chars to replace those with>* in
*<text>*. The first and second arguments must necessarily be the same
length.

.. _command-format-cut:

format cut <size> <text>
^^^^^^^^^^^^^^^^^^^^^^^^

Cuts *<text>* down to *<size>* by chopping off the rightmost characters in
excess of *<size>*. If *<size>* is a negative number, it chops that many
characters off the end of *<text>*.

.. _command-format-join:

format join <separator> <string 1> [<string> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Joins all the arguments together with *<separator>*.

.. _command-format-reverse:

format reverse <text>
^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* in reverse-video.

Text properties
---------------

.. _command-format-bold:

format bold <text>
^^^^^^^^^^^^^^^^^^

Returns *<text>* bolded.

.. _command-format-underline:

format underline <text>
^^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* underlined.

