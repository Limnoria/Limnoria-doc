.. highlight:: bash

.. _contribute-translate:

********************
Translating Limnoria
********************

I already wrote a `guide on how to translate`_ plugins.
So, this page will only explain how to translate the core and push your
translations to Limnoria.

.. _guide on how to translate: https://github.com/ProgVal/Supybot-docs/blob/master/i18n/Limnoria_i18n.pdf?raw=true

The best way: using Git yourself
================================

As I said in the :ref:`policy about developer's contributions
<contribute-develop-policy>`, I don't give write access to my repo for the
moment, but I accept pull requests.

As you are a translator, you don't need to know all the technical details
about development, so I write a simplified doc here.

Preparing git
-------------

First you should install git. It's usually package ``git`` in your OS, or
you can download it from `their homepage`_ or download GitHub client for
`Windows`_ or `OS X`_

Then you should tell GitHub who you are and what is your email address.
This information is attached to commits and GitHub uses it to get your
gravatar::

    git config --global user.name "Real Name or Nickname here"
    git config --global user.email "someone@example.com"

If you are going to use the ``https``, you probably want git to remember
your GitHub password for some time so you don't have to write it
continuosly::

    git config --global credential.helper cache
    git config --global credential.helper "cache --timeout=3600"

This would make git remember your password for hour. It can be changed
by changing 3600 to any other amount of seconds.

Cloning the repository
----------------------

You first need an account on `GitHub`_; I think you don't need explaination
for that.

Then, go on `Limnoria repository`_ and click the *Fork* button. This will
create you a copy of my repository where you will have write access (and
I won't have this write access).

Then, open a console, and write (replace *YourName* by the name of your
GitHub account)::

    git clone https://github.com/<YourName>/Limnoria.git --branch=testing

If you are experienced with git, you can
``git clone git@github.com:<YourName>/Limnoria.git --branch=testing``
instead.

This will create a new directory, called *Limnoria*, where all the code and
project history are copied. Now, cd to the directory::

    cd Limnoria/

The things below affect to you only if you didn't specify the branch in
the git clone command.

Then, you need to checkout the *testing* branch. What does that mean? It means
that there is differents stages in Limnoria: all changes are made in testing,
and when I think *testing* is stable, I merge it into *master*.
So, checking out *testing* means Git will use the code in *testing*, you
will translate strings that are in *testing*, and changes you make will be
in *testing*. Now, do it::

    git checkout testing 

Git will reply you that it understood what you mean by *testing*.

Ok, now, you can translate.

Pushing translations
--------------------

Once you have done some translations (let's say you translated Alias), you
have to commit your changes. That mean you tell Git "Ok, I've made some
changes, and I want to take a snapshot (either to be able to roll back
or to publish your changes).

First, you need to tell Git what files you want to be committed (let's say
you are the Finnish translator, so you updated Alias's fi.po)::

    git add plugins/Alias/locales/fi.po

Then, you can commit your files. Depending on what you made, you can use
one of this commands (not all of them!)::

    git commit -m "Alias: Add l10n-fi."
    git commit -m "Alias: Update l10n-fi."
    git commit -m "Alias: Fix l10n-fi."

By the way, the text that follow -m is a message that will be readed by
**humans**, so you can write anything you want, but I think it's better that
everybody use the same kind of messages.

Ok, then, Git knows you have done something. But you didn't send your work on
Internet yet. To send it, run::

    git push

Simple, isn't it?

Now, go back to GitHub and your forked repository, and click the *Pull request*
button. Then, set *testing* on the both side, and run *Update Commit Range*.
I will by mailed that you asked me to merge your changes, and I will do it
soon.

Getting updates
---------------

As you may know, I do some updates in Limnoria repository. ;)

You need to have the latest version of the *messages.pot* files. So, you
need to teach Git how to get this updates::

    git remote add upstream https://github.com/ProgVal/Limnoria.git

Now, every time you want to download updates, run::

    git fetch upstream
    git merge upstream/testing

Another way: mailing me your translations
=========================================

I think this is the simplest way for you. You only have to follow the
translation guide and send me your .po files by mail.

You can choose either one of this way to do it.

Mikaela's way
-------------

Send the fi.po (or whatever the name is) files one by one as an attachment.
Don't forget to tell me what plugin it is.

I (Mikaela) have moved to git long time ago though.

skizzhg's way
-------------

Do many translations. Put them in a tarball/zipball/whatever (but not a RAR
archive, I can't read them because is a proprietary format).

I prefer that you choose this architecture:

* FirstPlugin/locales/it.po
* SecondPlugin/locales/it.po
* ThirdPlugin/locales/it.po

Because I can extract everything with one click.

.. _GitHub: https://github.com/
.. _Limnoria repository: https://github.com/ProgVal/Limnoria
.. _their homepage: http://git-scm.com/
.. _Windows: https://windows.github.com/
.. _OS X: https://mac.github.com/
