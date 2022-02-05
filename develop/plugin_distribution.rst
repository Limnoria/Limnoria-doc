.. _distributing-plugins:

********************
Distributing plugins
********************

Now that you wrote a plugin, you may want to share it with other people.
There are many way to do this, and we are going to present some of them
below.


Via a VCS repository
====================

If you already use a VCS (such as Git, Mercurial, or Subversion), giving
access to your repository is the easiest way for you to share your plugins.
This method can also easily be adapted to distribute tarballs.

It will however require a little more work for your users.

There are two ways to do it:


With a single plugin per repository
-----------------------------------

By initializing a repository in each folder created by `supybot-plugin-wizard`
(eg. with `git init`).
This allows you to keep each plugin's history independent.

First, users should install a client for your VCS, and dependencies of
your plugin, if any.

Users can then download and install your plugin in a single command::

     cd runbot/plugins/
     git clone https://example.org/~jdoe/YourPlugin.git

(or the equivalent for your VCS)

and then immediately run ``@load YourPlugin``.


With all your plugins in the same repository
--------------------------------------------

By running ``git init`` in a new folder, then call ``supybot-plugin-wizard`` in this
folder to create each plugin in a subdirectory.
This is the easiest for your if you maintain many plugins, as you don't have
to manage many repositories.

First, users should install a client for your VCS, and dependencies of
your plugin(s) they want to use, if any.

Users can download all your plugins at once::

     cd ~/
     git clone https://example.org/~jdoe/LimnoriaPlugins.git JdoePlugins

and configure their bot to look for plugins in this directory::

    @config supybot.directories.plugins [config supybot.directories.plugins], /home/me/JdoePlugins


Alternatively, to make it easier for your users, you can add your repository
to Limnoria's list of known repository, by sending a pull request to:
https://github.com/ProgVal/Limnoria/blob/master/plugins/PluginDownloader/plugin.py

.. note::

   PluginDownloader currently only works on GitHub, but pull requests to add
   support for other forges are welcome.

Once it is accepted, users can then download your plugin in a single step
instead of the commands above::

    @plugindownloader install Jdoe 

Either way, they can now run ``@load YourPlugin``


Via pip / PyPI
==============

This requires a little more work for you, but uses mainstream Python package
management (pip/PyPI) so it is a lot easier for users (as they don't have to
use a VCS, put your plugin in the right directory, or install dependencies
manually)

.. warning::

   The following section assumes both your and your users have
   Limnoria 2020.05.08 or newer.

Setting up your plugin
----------------------

To make your plugin installable via pip, you first need to create a ``setup.py``
file in the same directory as the other files of your plugin.
You have probably seen one already if you are a Python developer.
Limnoria provides a small wrapper over ``setuptools.setup``, so you don't have
to type in most of the fields.
The minimal ``setup.py`` for a plugin named ``YourPlugin`` is::

   from supybot.setup import plugin_setup

   plugin_setup(
       'YourPlugin',
   )

This will automatically populate:

* the package name (``name = "limnoria-yourplugin"``)
* author information (``author`` and ``author_email`` if they are set in ``__init__.py``)
* maintainer information (idem)
* version and URL (based on ``__version__`` and ``__url__`` in ``__init__.py``)
* ``package = "limnoria_yourplugin"``
* ``package_dirs = {"limnoria_yourplugin": "."}``
* add Limnoria as dependency
* etc.

You can add any setuptools fields you like.
For example, to add ``requests`` as a dependency::

   from supybot.setup import plugin_setup

   plugin_setup(
       'YourPlugin',
       install_requires=[
           'requests',
       ],
   )

If you don't like the name `limnoria-yourplugin`, you can also override it.
For example::

   from supybot.setup import plugin_setup

   plugin_setup(
       'YourPlugin',
       name='limnoria-this-is-my-plugin',
   )


Installing plugins
------------------

Finally, once you plushed your plugin, users can install it simply with::

    pip3 install git+https://example.org/~jdoe/YourPlugin.git

Or, if you use a single repository for multiple plugins::

    pip3 install "git+https://example.org/~jdoe/Supybot-plugins.git#subdirectory=YourPlugin"

and this will automatically install your plugin's dependencies as well. Then,
they just need to run ``@load YourPlugin`` as usual.

For example, to install the LinkRelay plugin from https://github.com/progval/Supybot-plugins::

    pip3 install "git+https://github.com/progval/Supybot-plugins.git#subdirectory=LinkRelay"

Publishing your plugin (optional)
---------------------------------

Additionally, you may want to publish your plugin to PyPI, to make it easier
for users to install.

First, you must create an account on https://pypi.org/ and install twine::

    python3 -m pip install --user --upgrade twine

Then, you can generate and publish your plugin::

    python3 -m twine sdist
    python3 -m twine upload dist/*

And every time you want to publish an upgrade, update the version
in ``__init__.py`` and run this last command again.

For more details, see the official Python documentation on:

* `generating archives <https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives>`_
* `uploading archives <https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives>`_

And users can simply install it with::

    sudo pip3 install limnoria-yourplugin
