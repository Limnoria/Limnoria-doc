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

Here's the list of recommended software to run Supybot/Limnoria:

* Supybot is written in Python, and requires `Python`_
  2.6 or greater.
* `Twisted`_ framework 1.2.0 or greater (optional, you probably don't need it).
* `SQLAlchemy`_ If you want the Aka plugin (and probably other plugins in the future)

.. _Python: http://www.python.org/
.. _Twisted: http://twistedmatrix.com/
.. _SQLAlchemy: http://www.sqlalchemy.org/

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

If it works, you're good to go. Otherwise, install the `python-dev` or
`python-devel` package and try again.

You may also install "manually" by downloading the source archive from
http://python.org, and compiling it. That is outside the scope of this guide,
however.

Install Limnoria
----------------

In the next section of this guide we will use `pip`_, which is a generic
way of installing Python software

However, you can use any of these alternatives:

* Download a .deb package at `ProgVal's build repo`_.
* Use `git`_ to clone the `Limnoria repository`_ and run
  ``python setup.py install`` or ``python setup.py install --user``.
* Click the "Downloads" button at the `Limnoria repository`_. Then,
  extract the zipball to some temporary directory, and ``cd`` into the
  ``supybot`` directory which contains the extracted code.

**Windows users:** `pip`_ also works on Windows and you need `msysgit`_ in 
which setup you should specify to have UNIX tools in PATH.


.. _ProgVal's build repo: http://builds.progval.net/
.. _Limnoria repository: https://github.com/ProgVal/Limnoria
.. _pip: http://pip.readthedocs.org/en/latest/installing.html#install-pip
.. _git: http://git-scm.com/
.. _msysgit: https://msysgit.github.io/

Global installation
^^^^^^^^^^^^^^^^^^^

You can either run these as root or prepend ``sudo`` in front of every 
message.

In case you want to use the testing branch which might be more up-to date 
**but less tested**, replace ``master`` with ``testing`` in the commands.

First we install Limnoria's requirements::

    pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt 

And then Limnoria itself::

    pip install git+https://github.com/ProgVal/Limnoria.git@master

Local installation
^^^^^^^^^^^^^^^^^^

Simply add ``--user`` to the end of both commands. First we install 
requirements and then Limnoria itself.::

    pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt --user
    pip install git+https://github.com/ProgVal/Limnoria.git@master --user

You might need to add $HOME/.local/bin to your PATH.::

    echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.$(echo $SHELL|cut -d/ -f3)rc
    source ~/.$(echo $SHELL|cut -d/ -f3)rc

Upgrading
^^^^^^^^^

To upgrade Limnoria, simply add ``--upgrade`` to the end of both commands.


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

Download the latest Python 2 installer from http://python.org, (Python 2.7, as
of Mars 6, 2011) and run it to install Python.

The rest of this document will assume that you have Python 2.7, and thus that
your install directory is ''C:\Python27''.

Install Supybot
---------------

We are now ready to install Supybot itself. First, you need to grab the latest
code snapshot of Supybot. Easiest way to do that is to  click the "Downloads"
button at the `Limnoria repository`_.

If you downloaded the code archive, extract it to some temporary directory,
and ``cd`` into the ``supybot`` directory which contains the extracted code.

Once you have the code archive, extract it to some temporary directory, then
open up a command prompt (Programs -> Run -> ``cmd``) and ``cd`` into the
``supybot`` directory which contains the extracted code. For example, if you
have extracted the archive to ``C:\sometempdir\``, you would enter in the
prompt::

    cd "C:\sometempdir\supybot"

Once there, run the installer to install, with the following command::

    C:\Python27\python.exe setup.py install

This will place some supybot scripts under ``C:\Python27\Scripts\``, and the
supybot python module under ``C:\Python27\Lib\site-packages``.

.. _Limnoria repository: https://github.com/ProgVal/Limnoria

Configure Supybot
-----------------

We are now ready to configure Supybot. Supybot creates quite a few auxiliary
files/directories to store its runtime data. It is thus recommended to create
an empty directory from which you'll be running supybot, to keep all the data
in a nice dedicated location. For example, you may create a 'C:\runbot' for
this purpose. 

Now you open a command prompt, and ``cd`` to your ``C:\runbot`` directory::

    cd "C:\runbot"

and from within it run ``supybot-wizard``::

    C:\Python27\python.exe C:\Python27\Scripts\supybot-wizard

which will walk you through a series of questions to generate the bot config
file. 

One thing to make sure to do in the wizard, to make your life easier down the
line, is to select *y* for the *Would you like to add an owner user for
your bot?* question, and actually create the owner user. Remember that
password, so that you can later ''identify'' with the bot on IRC and
administer it.

Once you generate the config file, which will be named ``yourbotnick.conf``
(where ``yourbotnick`` is the nick you have chosen for your bot in the wizard),
it will be placed in your ``runbot`` directory. (As long as you leave the
default answer to the *Where would you like to create these directories?*
question.) 

Now to start the bot, run, still from within the ``C:\runbot`` directory::

    C:\Python27\python.exe C:\Python27\Scripts\supybot yourbotnick.conf

And watch the magic!

This guide has been mainly written by nanotube (Daniel Folkinshteyn), and is
licensed under the Creative Commons Attribution ShareAlike 3.0 Unported license
and/or the GNU Free Documentation License v 1.3 or later.

.. _Supybook: http://supybook.fealdia.org/
