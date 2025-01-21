.. _use-install_windows:

******************************
Installing Limnoria on Windows
******************************

This guide is for installing Limnoria on Windows. If you don't want to install on Windows,
check out the :ref:`non-Windows install guide <use-install>`.


.. highlight:: bat

Install
=======

Install Python
--------------

Download the latest **Python 3** installer from https://www.python.org, 
3.11.2, as of 2023-03-14) and run it to install Python.

Installing Python is mostly clicking next, but in the next screen remember
the destination directory where you installed Python. These instructions
refer to it as ``C:\Python311\`` which is the current name on 2023-03-14.
If you downloaded a newer version, replace the version number with the new one.

Then you are asked to customize your installation. Click the drive on left
side of "Python" text and select "Entire feature will be installed on
local hard drive".

Now Python installs itself which may take several minutes.

Python should be now installed and you can check that the "python" command
points to correct python. Open ``cmd.exe`` (press the Windows button on
your keyboard and type "cmd.exe") and  run ``where python``
and the toppernmost entry should be ``C:\Python311\python.exe``.

Install Limnoria
---------------

Now we are ready to install Limnoria and it's requirements. Open 
``cmd.exe`` as **Administrator** (right click it in the previous place)
and run::

    python3 -m pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt --upgrade
    python3 -m pip install limnoria --upgrade

We are now ready to configure Limnoria. Limnoria creates quite a few
auxiliary files/directories to store its runtime data. It is thus
recommended to create an empty directory from which you'll be running
Limnoria, to keep all the data in a nice dedicated location. 
For example, you may create a ``C:\Users\<username>\runbot`` for this
purpose. 

Configure Limnoria
==================

.. note::

   For historical reasons, commands are called ``supybot``; but they actually
   run Limnoria.

Now you open cmd.exe as **normal user**, and create and cd into your runbot
directory::

    mkdir runbot
    cd runbot

and from within it run ``supybot-wizard``::

    python3 C:\Python311\Scripts\supybot-wizard

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

    python3 C:\Python311\Scripts\supybot yourbotnick.conf

And watch the magic!

This guide has been mainly written by nanotube (Daniel Folkinshteyn), and
is licensed under the Creative Commons Attribution ShareAlike 3.0 Unported
license and/or the GNU Free Documentation License v 1.3 or later.

