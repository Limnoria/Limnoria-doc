
.. _plugin-format:

The Format plugin
=================

.. command-upper:

upper <text>
^^^^^^^^^^^^

Returns *<text>* uppercased.


.. command-bold:

bold <text>
^^^^^^^^^^^

Returns *<text>* bolded.


.. command-format:

format <format string> [<arg> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Expands a Python-style format string using the remaining args. Just be
sure always to use %s, not %d or %f or whatever, because all the args
are strings.


.. command-color:

color <foreground> [<background>] <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* with foreground color *<foreground>* and background color
*<background>* (if given)


.. command-repr:

repr <text>
^^^^^^^^^^^

Returns the text surrounded by double quotes.


.. command-replace:

replace <substring to translate> <substring to replace it with> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces all non-overlapping occurrences of *<substring to translate>*
with *<substring to replace it with>* in *<text>*.


.. command-capitalize:

capitalize <text>
^^^^^^^^^^^^^^^^^

Returns *<text>* capitalized.


.. command-underline:

underline <text>
^^^^^^^^^^^^^^^^

Returns *<text>* underlined.


.. command-lower:

lower <text>
^^^^^^^^^^^^

Returns *<text>* lowercased.


.. command-cut:

cut <size> <text>
^^^^^^^^^^^^^^^^^

Cuts *<text>* down to *<size>* by chopping off the rightmost characters in
excess of *<size>*. If *<size>* is a negative number, it chops that many
characters off the end of *<text>*.


.. command-join:

join <separator> <string 1> [<string> ...]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Joins all the arguments together with *<separator>*.


.. command-reverse:

reverse <text>
^^^^^^^^^^^^^^

Returns *<text>* in reverse-video.


.. command-title:

title <text>
^^^^^^^^^^^^

Returns *<text>* titlecased.


.. command-field:

field <number> <text>
^^^^^^^^^^^^^^^^^^^^^

Returns the *<number>*th space-separated field of *<text>*. I.e., if text
is "foo bar baz" and *<number>* is 2, "bar" is returned.


.. command-concat:

concat <string 1> <string 2>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Concatenates two strings. Do keep in mind that this is *not* the same
thing as join "", since if *<string 2>* contains spaces, they won't be
removed by concat.


.. command-translate:

translate <chars to translate> <chars to replace those with> <text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces *<chars to translate>* with *<chars to replace those with>* in
*<text>*. The first and second arguments must necessarily be the same
length.


