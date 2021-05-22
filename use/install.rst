.. highlight:: bash

.. _use-install:

***************************************************************
Installing Limnoria on GNU/Linux and UNIX (FreeBSD, macOS, ...)
***************************************************************

This is the "easy to follow" guide to installing Limnoria. The installation
documentation provided with the supybot distribution is really quite good
already, but since people keep coming to IRC, asking a repeating pattern of
questions, we thought it would be a good idea to expand it a bit to make it
a little more of a "foolproof guide".

This guide is for non-Windows operating systems. If you want to install
on Windows, check out the :ref:`Windows install guide <use-install_windows>`.

.. note::

    Limnoria is a modified version of Supybot.

Install
*******

Install using your OS' package manager
======================================

On Debian (8.0 and above) or Ubuntu (16.10 and above)
-----------------------------------------------------

.. code-block:: bash

    sudo apt-get install limnoria

Note that stable / LTS releases may not have the latest features or bug fixes for Limnoria. If you want a newer version than what's in the default repositories, you can enable `Backports`_ on Debian or `Unit 193's PPA`_ on Ubuntu.

.. _Backports: https://wiki.debian.org/Backports
.. _Unit 193's PPA: https://launchpad.net/~unit193/+archive/ubuntu/limnoria

On Fedora (23 and above)
------------------------

.. code-block:: bash

    sudo dnf install limnoria

On CentOS and Red Hat Enterprise Linux
--------------------------------------

You have to first add the EPEL repository (`EL7`_, `EL6`_, `EL5`_) before being able to install the package on CentOS / RHEL. Once you have, you can run the following command to install Limnoria:

.. code-block:: bash

    sudo yum install limnoria

.. _EL7: https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
.. _EL6: https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
.. _EL5: https://dl.fedoraproject.org/pub/epel/epel-release-latest-5.noarch.rpm

On FreeBSD
----------

Port:

.. code-block:: bash

    cd /usr/ports/irc/py-limnoria && sudo PYTHON_VERSION=3.7 make install clean

Package:

.. code-block:: bash

    sudo pkg install py37-limnoria

On Arch Linux
-------------

You can install Limnoria `from the AUR`_.

.. _from the AUR: https://aur.archlinux.org/packages/limnoria-git/

On Gentoo
---------

.. code-block:: bash

    sudo emerge net-irc/limnoria

With Guix and GuixSD
--------------------

.. code-block:: bash

    guix package --install limnoria


Other operating systems (manual install)
========================================

If you followed the section above, skip this one.

Dependencies
------------

The only mandatory dependency is Python 3.4 or greater.

You may also install chardet and feedparser, which are used by Limnoria if
they are available.

The remaining of this guide will assume you have Python 3.

.. _Python: http://www.python.org/

Install Python
--------------

Python will usually come by installed by default in your distribution. If not,
grab the appropriate packages from the distribution's repository, or download
it from http://python.org.

If you're installing Python using your distribution's packages, you may need a
''python-dev'' or ''python-devel'' package installed, too. To see if this is
the case, open up a terminal, start python, and run:

.. code-block:: python

    import distutils

If it works, you're good to go. Otherwise, install the ``python3-dev`` or
``python3-devel`` package and try again.

You may also install "manually" by downloading the source archive from
http://python.org, and compiling it. That is outside the scope of this guide,
however.

Install Limnoria
----------------

In the next section of this guide we will use `pip`_, which is a generic
way of installing Python software.

There are some :ref:`alternative install methods <alternative-install>`
at the bottom of this guide, if you don't want to use ``pip``.

.. _pip: http://pip.readthedocs.org/en/latest/installing.html#install-pip

Global installation (with root access)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you do not have root access, skip this section.

If you are logged in as root, you can remove ``sudo`` from the install
commands.

If you want to use the testing branch which might be more up-to
date BUT LESS TESTED, replace ``master`` with ``testing`` in the commands.

First, install Limnoria's optional dependencies (you can skip this
step, but some features won't be available)::

    sudo python3 -m pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt --upgrade

Then Limnoria itself::

    sudo python3 -m pip install limnoria --upgrade

If you have an error saying ``No module named pip``, install ``pip`` using
your package manager (the package is usually named ``python3-pip``).

Local installation (without root access)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have followed the previous section, skip this one.

Simply add ``--user`` to the end of both commands. First we install
requirements (you can skip it, but some features won't be available)
and then Limnoria itself.::

    python3 -m pip install -r https://raw.githubusercontent.com/ProgVal/Limnoria/master/requirements.txt --user --upgrade
    python3 -m pip install limnoria --user --upgrade

You might need to add $HOME/.local/bin to your PATH.::

    echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.$(echo $SHELL|cut -d/ -f3)rc
    source ~/.$(echo $SHELL|cut -d/ -f3)rc

If you have an error saying ``No module named pip``, install ``pip`` using this
guide: https://pip.pypa.io/en/stable/installing/

Configuration
*************

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




.. _alternative-install:

Alternative install methods
***************************

If you know what you are doing and you don't want to use pip, you
can use one of these methods:

* Download a .deb or .rpm package at `ProgVal's build repo`_.
* Use `git`_ to clone the `Limnoria repository`_ and follow the
  instructions in `Limnoria's README.md`_.
* Click the "Download ZIP" button at the `Limnoria repository`_. Then,
  extract the zipball to some temporary directory, and ``cd`` to the
  ``Limnoria-master`` directory which contains the extracted code.

.. _ProgVal's build repo: https://builds.progval.net/limnoria/
.. _Limnoria repository: https://github.com/ProgVal/Limnoria
.. _git: http://git-scm.com/
.. _Limnoria's README.md: https://github.com/ProgVal/Limnoria/blob/testing/README.md#installing-from-cloned-repo
