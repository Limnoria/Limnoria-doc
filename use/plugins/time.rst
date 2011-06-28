
.. _plugin-time:

The Time plugin
===============

.. _command-ctime:

ctime [<seconds since epoch>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the ctime for *<seconds since epoch>*, or the current ctime if
no *<seconds since epoch>* is given.


.. _command-seconds:

seconds [<years>y] [<weeks>w] [<days>d] [<hours>h] [<minutes>m] [<seconds>s]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of seconds in the number of *<years>*, *<weeks>*,
*<days>*, *<hours>*, *<minutes>*, and *<seconds>* given. An example usage is
"seconds 2h 30m", which would return 9000, which is '3600*2 + 30*60'.
Useful for scheduling events at a given number of seconds in the
future.


.. _command-time:

time [<format>] [<seconds since epoch>]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current time in *<format>* format, or, if *<format>* is not
given, uses the configurable format for the current channel. If no
*<seconds since epoch>* time is given, the current time is used.


.. _command-elapsed:

elapsed <seconds>
^^^^^^^^^^^^^^^^^

Returns a pretty string that is the amount of time represented by
*<seconds>*.


.. _command-at:

at <time string>
^^^^^^^^^^^^^^^^

Returns the number of seconds since epoch *<time string>* is.
*<time string>* can be any number of natural formats; just try something
and see if it will work.


.. _command-tztime:

tztime <region>/<city>
^^^^^^^^^^^^^^^^^^^^^^

Takes a city and its region, and returns the locale time.

.. _command-until:

until <time string>
^^^^^^^^^^^^^^^^^^^

Returns the number of seconds until *<time string>*.


