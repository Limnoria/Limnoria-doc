.. _use-install_windows:

******************************
Installing Limnoria on Windows
******************************

This is the "easy to follow" guide to installing Limnoria. The installation
documentation provided with the supybot distribution is really quite good
already, but since people keep coming to IRC, asking a repeating pattern of
questions, we thought it would be a good idea to expand it a bit to make it
a little more of a "foolproof guide".

This guide is only for Windows. If you don't want to install on Windows,
check out the :ref:`non-Windows install guide <use-install>`.


.. note::

    Limnoria is a modified version of Supybot.

.. highlight:: bat

Install
=======

Install Python
--------------

Download the latest **Python 3** installer from https://www.python.org, 
3.5.1, as of 2016-01-26) and run it to install Python.

Installing Python is mostly clicking next, but in the next screen remember
the destination directory where you installed Python. These instructions
refer to it as ``C:\Python35\`` which is the current name on 2016-01-26.

Then you are asked to customize your installation. Click the drive on left
side of "Python" text and select "Entire feature will be installed on
local hard drive".

Now Python installs itself which may take several minutes.

Python should be now installed and you can check that the "python" command
points to correct python. Open ``cmd.exe`` (press the Windows button on
your keyboard and type "cmd.exe") and  run ``where python``
and the toppernmost entry should be ``C:\Python35\python.exe``.

Install Supybot
---------------

Now we are ready to install Limnoria and it's requirements. Open 
``cmd.exe`` as **Administrator** (right click it in the previous place)
and run::

    python3 -m pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt --upgrade
    python3 -m pip install limnoria --upgrade

We are now ready to configure Supybot. Supybot creates quite a few
auxiliary files/directories to store its runtime data. It is thus
recommended to create an empty directory from which you'll be running
supybot, to keep all the data in a nice dedicated location. 
For example, you may create a ``C:\Users\<username>\runbot`` for this
purpose. 

Configure Supybot
=================

Now you open cmd.exe as **normal user**, and create and cd into your runbot
directory::

    mkdir runbot
    cd runbot

and from within it run ``supybot-wizard``::

    python3 C:\Python35\Scripts\supybot-wizard

which will walk you through a series of questions to generate the bot
config file. 

One thing to make sure to do in the wizard, to make your life easier down
the line, is to select *y* for the *Would you like to add an owner user 
for your bot?* question, and actually create the owner user. Remember that
password, so that you can later ''identify'' with the bot on IRC and
administer it.

Once you generate the config file, which will be named ``yourbotnick.conf``
(where ``yourbotnick`` is the nick you have chosen for your bot in the 
wizard), it will be placed in your ``runbot`` directory. (As long as you
leave the default answer to the *Where would you like to create these 
directories?* question.) 

Now to start the bot, run, still from within the
``C:\users\<username>\runbot`` directory::

    python3 C:\Python35\Scripts\supybot yourbotnick.conf

And watch the magic!

This guide has been mainly written by nanotube (Daniel Folkinshteyn), and
is licensed under the Creative Commons Attribution ShareAlike 3.0 Unported
license and/or the GNU Free Documentation License v 1.3 or later.

.. _Supybook: https://hoxu.github.io/supybook/

