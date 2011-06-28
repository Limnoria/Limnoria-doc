
.. _plugin-filter:

The Filter plugin
=================

.. _command-undup:

undup <text>
^^^^^^^^^^^^

Returns *<text>*, with all consecutive duplicated letters removed.


.. _command-unhexlify:

unhexlify <hexstring>
^^^^^^^^^^^^^^^^^^^^^

Returns the string corresponding to *<hexstring>*. Obviously,
*<hexstring>* must be a string of hexadecimal digits.


.. _command-stripcolor:

stripcolor <text>
^^^^^^^^^^^^^^^^^

Returns *<text>* stripped of all color codes.


.. _command-unbinary:

unbinary <text>
^^^^^^^^^^^^^^^

Returns the character representation of binary *<text>*.
Assumes ASCII, 8 digits per character.


.. _command-hebrew:

hebrew <text>
^^^^^^^^^^^^^

Removes all the vowels from *<text>*. (If you're curious why this is
named 'hebrew' it's because I (jemfinch) thought of it in Hebrew class,
and printed Hebrew often elides the vowels.)


.. _command-colorize:

colorize <text>
^^^^^^^^^^^^^^^

Returns *<text>* with each character randomly colorized.


.. _command-binary:

binary <text>
^^^^^^^^^^^^^

Returns the binary representation of *<text>*.


.. _command-leet:

leet <text>
^^^^^^^^^^^

Returns the l33tspeak version of *<text>*


.. _command-lithp:

lithp <text>
^^^^^^^^^^^^

Returns the lisping version of *<text>*


.. _command-morse:

morse <text>
^^^^^^^^^^^^

Gives the Morse code equivalent of a given string.


.. _command-outfilter:

outfilter [<channel>] [<command>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the outFilter of this plugin to be *<command>*. If no command is
given, unsets the outFilter. *<channel>* is only necessary if the
message isn't sent in the channel itself.


.. _command-spellit:

spellit <text>
^^^^^^^^^^^^^^

Returns *<text>*, phonetically spelled out.


.. _command-rainbow:

rainbow <text>
^^^^^^^^^^^^^^

Returns *<text>* colorized like a rainbow.


.. _command-aol:

aol <text>
^^^^^^^^^^

Returns *<text>* as if an AOLuser had said it.


.. _command-hexlify:

hexlify <text>
^^^^^^^^^^^^^^

Returns a hexstring from the given string; a hexstring is a string
composed of the hexadecimal value of each character in the string


.. _command-unmorse:

unmorse <Morse code text>
^^^^^^^^^^^^^^^^^^^^^^^^^

Does the reverse of the morse command.


.. _command-squish:

squish <text>
^^^^^^^^^^^^^

Removes all the spaces from *<text>*.


.. _command-reverse:

reverse <text>
^^^^^^^^^^^^^^

Reverses *<text>*.


.. _command-azn:

azn <text>
^^^^^^^^^^

Returns *<text>* with the l's made into r's and r's made into l's.


.. _command-gnu:

gnu <text>
^^^^^^^^^^

Returns *<text>* as GNU/RMS would say it.


.. _command-jeffk:

jeffk <text>
^^^^^^^^^^^^

Returns *<text>* as if JeffK had said it himself.


.. _command-shrink:

shrink <text>
^^^^^^^^^^^^^

Returns *<text>* with each word longer than
supybot.plugins.Filter.shrink.minimum being shrunken (i.e., like
"internationalization" becomes "i18n").


.. _command-uniud:

uniud <text>
^^^^^^^^^^^^

Returns *<text>* rotated 180 degrees. Only really works for ASCII
printable characters.


.. _command-scramble:

scramble <text>
^^^^^^^^^^^^^^^

Replies with a string where each word is scrambled; i.e., each internal
letter (that is, all letters but the first and last) are shuffled.


