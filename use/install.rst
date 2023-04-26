.. highlight:: bash

.. _use-install:

***************************************************************
Installing Limnoria on GNU/Linux and UNIX (FreeBSD, macOS, ...)
***************************************************************

This is the "easy to follow" guide to installing Limnoria.

This guide is for non-Windows operating systems. If you want to install
on Windows, check out the :ref:`Windows install guide <use-install_windows>`.

Install
*******

Install using your OS' package manager
======================================

* Debian or Ubuntu: ``sudo apt-get install limnoria``

  Note that stable / LTS releases may not have the latest features or bug fixes for Limnoria.
  If you want a newer version than what's in the default repositories, you can enable `Backports`_ on Debian or `Unit 193's PPA`_ on Ubuntu.
* Fedora: ``sudo dnf install limnoria``
* CentOS and Red Hat Enterprise Linux: you have to first add the right EPEL repository for your CentOS/RHEL version before being able to install the package on CentOS / RHEL.
  Once you have, you can run the following command to install Limnoria: ``sudo yum install limnoria``
* Arch Linux: You can install Limnoria from the AUR, using either `limnoria <https://aur.archlinux.org/packages/limnoria/>`__ (stable releases) or `limnoria-git <https://aur.archlinux.org/packages/limnoria-git/>`__ (git snapshots).
* Gentoo: ``sudo emerge net-irc/limnoria``
* Guix and GuixSD: ``guix package --install limnoria``

If any of the methods above works for you, skip the next section and go to :ref:`initial-configuration`.

.. _Backports: https://wiki.debian.org/Backports
.. _Unit 193's PPA: https://launchpad.net/~unit193/+archive/ubuntu/limnoria


Other operating systems (manual install)
========================================

If you followed the section above, skip this one.

Dependencies
------------

The only mandatory dependency is Python 3.4 or greater.

You may also install chardet and feedparser, which are used by Limnoria if
they are available.

The remaining of this guide will assume you have Python 3.

.. _Python: https://www.python.org/

Install Python
--------------

Python will usually come by installed by default in your distribution. If not,
grab the appropriate packages from the distribution's repository, or download
it from https://python.org.

Install Limnoria
----------------

In the next section of this guide we will use `pip`_, which is a generic
way of installing Python software.

.. _pip: https://pip.readthedocs.org/en/latest/installing.html#install-pip

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

.. _initial-configuration:

Configuration
*************

.. note::

   For historical reasons, commands are called ``supybot``; but they actually
   run Limnoria.

We are now ready to configure Limnoria. Limnoria creates quite a few auxiliary
files/directories to store its runtime data. It is thus recommended to create
an empty directory from which you'll be running Limnoria, to keep all the data
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

.. _Supybook: https://hoxu.github.io/supybook/
