.. highlight:: bash

.. _use-install:

*******************
Installing Limnoria
*******************

This is the "easy to follow" guide to installing Limnoria. The installation
documentation provided with the supybot distribution is really quite good
already, but since people keep coming to IRC, asking a repeating pattern of
questions, we thought it would be a good idea to expand it a bit to make it
a little more of a "foolproof guide".

.. note::

    Limnoria is a modified version of Supybot.

Dependencies
============

The only mandatory dependency is `Python`_ 2.6 or greater. However, it is
highly recommended you use Python 3.4 or greater.

You may also install chardet and feedparser, which are used by Limnoria if
they are available.

The remaining of this guide will assume you have Python 3. If you don't,
replace `python3` by `python` in the given commands

.. _Python: http://www.python.org/

Installation: UNIX/Linux/BSD
============================

Install Python
--------------

Python will usually come by installed by default in your distribution. If not,
grab the appropriate packages from the distribution's repository.

If you're installing Python using your distribution's packages, you may need a
''python-dev'' or ''python-devel'' package installed, too. To see if this is
the case, open up a terminal, start python, and run:

.. code-block:: python

    import distutils

If it works, you're good to go. Otherwise, install the `python3-dev` or
`python3-devel` package and try again.

You may also install "manually" by downloading the source archive from
http://python.org, and compiling it. That is outside the scope of this guide,
however.

Install Limnoria
----------------

In the next section of this guide we will use `pip`_, which is a generic
way of installing Python software.

However, you can use any of these **alternatives**:

* Download a .deb or .rpm package at `ProgVal's build repo`_.
* Use `git`_ to clone the `Limnoria repository`_ and follow the
  instructions in `Limnoria's README.md`_.
* Click the "Downloads" button at the `Limnoria repository`_. Then,
  extract the zipball to some temporary directory, and ``cd`` into the
  ``supybot`` directory which contains the extracted code.

**Windows users:** `pip`_ also works on Windows and you need `msysgit`_ in 
which setup you should specify to have UNIX tools in PATH. Also note that
you should run cmd.exe with Administrator rights and remove ``sudo`` from
the beginning of global installation commands.

.. _ProgVal's build repo: https://builds.progval.net/limnoria/
.. _Limnoria repository: https://github.com/ProgVal/Limnoria
.. _pip: http://pip.readthedocs.org/en/latest/installing.html#install-pip
.. _git: http://git-scm.com/
.. _msysgit: https://msysgit.github.io/
.. _Limnoria's README.md: https://github.com/ProgVal/Limnoria/blob/testing/README.md#installing-from-cloned-repo

Global installation (with root access)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you do not have root access, skip this section.

If you are logged in as root, you can remove ``sudo`` from the install 
commands.

*In case you want to use the testing branch which might be more up-to 
date BUT LESS TESTED, replace ``master`` with ``testing`` in the commands.*

First we install Limnoria's optional dependencies (you can skip this
step, but some features won't be available)::

    sudo python3 -m pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt --upgrade

And then Limnoria itself::

    sudo python3 -m pip install limnoria --upgrade

If you have an error saying `No module named pip`, install `pip` using
your package manager (the package is usually named `python3-pip`).

Local installation (without root access)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have followed the previous section, skip this one.

Simply add ``--user`` to the end of both commands. First we install 
requirements (you can skip it, but some features won't be available)
and then Limnoria itself.::

    pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt --user --upgrade
    pip install limnoria --user --upgrade

You might need to add $HOME/.local/bin to your PATH.::

    echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.$(echo $SHELL|cut -d/ -f3)rc
    source ~/.$(echo $SHELL|cut -d/ -f3)rc

If you have an error saying `No module named pip`, install `pip` using this
guide: https://pip.pypa.io/en/stable/installing/

Configure Supybot
-----------------

We are now ready to configure Supybot. Supybot creates quite a few auxiliary
files/directories to store its runtime data. It is thus recommended to create
an empty directory from which you'll be running supybot, to keep all the data
in a nice dedicated location. For example, you may create a 'runbot' directory
inside your home directory. 

Now you can cd to your 'runbot' directory, and from within it run
``supybot-wizard``, which will walk you through a series of questions to
generate the bot config file. 

One thing to make sure to do in the wizard, to make your life easier down the
line, is to select **y** for the *Would you like to add an owner user for your
bot?* question, and actually create the owner user. Remember that password, so
that you can later ''identify'' with the bot on IRC and administer it.

Once you generate the config file, which will be named ``yourbotnick.conf``
(where "yourbotnick" is the nick you have chosen for your bot in the wizard),
it will be placed in your 'runbot' directory. (As long as you leave the default
answer to the ''Where would you like to create these directories?'' question.) 

Now to start the bot, run, still from within the 'runbot' directory::

    supybot yourbotnick.conf

And watch the magic!

For a tutorial on using and managing the bot from here on, see the `Supybook`_.

.. _Supybook: http://supybook.fealdia.org/

Installation: OS X
==================

The steps are essentially the same as those of the previous section, except
there are no repositories. Grab the latest python installer for OS X from
http://python.org, and follow the rest of the steps.

Installation: Windows
=====================

.. highlight:: bat

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

Install git
-----------

In order to install the latest Limnoria from the git repository, you need
git in your %PATH%. You can get it from http://git-scm.com/.

In the "Adjusting your PATH environment", select the last option, "Use Git
and optional Unix tools from the Windows Command Prompt" or you will have
issues in the next step.

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

.. _Supybook: http://supybook.fealdia.org/
