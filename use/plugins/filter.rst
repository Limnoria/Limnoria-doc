
.. _plugin-filter:

The Filter plugin
=================

Administration
--------------

.. _command-filter-outfilter:

filter outfilter [<channel>] [<command>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the outFilter of this plugin to be *<command>*. If no command is
given, unsets the outFilter. *<channel>* is only necessary if the
message isn't sent in the channel itself.

Encoding and decoding
---------------------

.. _command-filter-hexlify:

filter hexlify <text>
^^^^^^^^^^^^^^^^^^^^^

Returns a hexstring from the given string; a hexstring is a string
composed of the hexadecimal value of each character in the string

.. _command-filter-unhexlify:

filter unhexlify <hexstring>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the string corresponding to *<hexstring>*. Obviously,
*<hexstring>* must be a string of hexadecimal digits.

.. _command-filter-binary:

filter binary <text>
^^^^^^^^^^^^^^^^^^^^

Returns the binary representation of *<text>*.

.. _command-filter-unbinary:

filter unbinary <text>
^^^^^^^^^^^^^^^^^^^^^^

Returns the character representation of binary *<text>*.
Assumes ASCII, 8 digits per character.

.. _command-filter-morse:

filter morse <text>
^^^^^^^^^^^^^^^^^^^

Gives the Morse code equivalent of a given string.

.. _command-filter-unmorse:

filter unmorse <Morse code text>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Does the reverse of the morse command.


Colors
------

.. _command-filter-stripcolor:

filter stripcolor <text>
^^^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* stripped of all color codes.

.. _command-filter-colorize:

filter colorize <text>
^^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* with each character randomly colorized.

.. _command-filter-rainbow:

filter rainbow <text>
^^^^^^^^^^^^^^^^^^^^^

Returns *<text>* colorized like a rainbow.

Utils
-----

.. _command-filter-shrink:

filter shrink <text>
^^^^^^^^^^^^^^^^^^^^

Returns *<text>* with each word longer than
:ref:`supybot.plugins.Filter.shrink.minimum` being shrunken (i.e., like
"internationalization" becomes "i18n").

.. _command-filter-uniud:

filter uniud <text>
^^^^^^^^^^^^^^^^^^^

Returns *<text>* rotated 180 degrees. Only really works for ASCII
printable characters.

.. _command-filter-scramble:

filter scramble <text>
^^^^^^^^^^^^^^^^^^^^^^

Replies with a string where each word is scrambled; i.e., each internal
letter (that is, all letters but the first and last) are shuffled.

Fun
---

.. _command-filter-undup:

filter undup <text>
^^^^^^^^^^^^^^^^^^^

Returns *<text>*, with all consecutive duplicated letters removed.

.. _command-filter-hebrew:

filter hebrew <text>
^^^^^^^^^^^^^^^^^^^^

Removes all the vowels from *<text>*. (If you're curious why this is
named 'hebrew' it's because I (jemfinch) thought of it in Hebrew class,
and printed Hebrew often elides the vowels.)

.. _command-filter-leet:

filter leet <text>
^^^^^^^^^^^^^^^^^^

Returns the l33tspeak version of *<text>*

.. _command-filter-lithp:

filter lithp <text>
^^^^^^^^^^^^^^^^^^^

Returns the lisping version of *<text>*

.. _command-filter-spellit:

filter spellit <text>
^^^^^^^^^^^^^^^^^^^^^

Returns *<text>*, phonetically spelled out.

.. _command-filter-aol:

filter aol <text>
^^^^^^^^^^^^^^^^^

Returns *<text>* as if an AOLuser had said it.

.. _command-filter-squish:

filter squish <text>
^^^^^^^^^^^^^^^^^^^^

Removes all the spaces from *<text>*.

.. _command-filter-reverse:

filter reverse <text>
^^^^^^^^^^^^^^^^^^^^^

Reverses *<text>*.

.. _command-filter-azn:

filter azn <text>
^^^^^^^^^^^^^^^^^

Returns *<text>* with the l's made into r's and r's made into l's.

.. _command-filter-gnu:

filter gnu <text>
^^^^^^^^^^^^^^^^^

Returns *<text>* as GNU/RMS would say it.

.. _command-filter-jeffk:

filter jeffk <text>
^^^^^^^^^^^^^^^^^^^

Returns *<text>* as if JeffK had said it himself.

