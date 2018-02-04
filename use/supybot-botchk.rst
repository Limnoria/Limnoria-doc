.. _supybot-botchk:

################################
Restarting the bot automatically
################################

This page documents the different ways to automatically restart your bot
in case of crash or system reboot or anything that can make the bot quit.

Note that you only need to use one.

supybot-botchk
==============

supybot-botchk is a script that comes with Supybot which restarts the bot
if it quits or system reboots or anything that causes the bot to quit. It's
placed to crontab so cron will run it with scheduled intervals.

How to use it?
--------------

Configuring the bot
^^^^^^^^^^^^^^^^^^^

Start by telling your bot to write a pidfile somewhere where it can write,
and restart the bot. For example::

    config supybot.pidfile /home/<username>/<bot>/<bot>.pid

where <username> is replaced with the system username and <bot> is replaced
with the name of the bot.

crontab
^^^^^^^

After the pidfile is configured, you can modify crontab. First you should
copy the output of::

    printf 'PATH=%s\n' "$PATH"

and open crontab with ``EDITOR=nano crontab -e`` and paste the output of
previous command to the first lines which don't have comments. This should
be on top. You will probably also want to configure locale and timezone
which happens by adding the following lines::

    # Replace en_US.utf8 with your own locale! You should see list of
    # available locales with `locale` command, just use something which
    # ends with "utf8" or "UTF-8" (the latter is required on some operating
    # systems like OS X).
    LC_ALL=en_US.UTF-8
    
    # Specifying timezone is optional, but you probably want to do it if
    # your system is on different timezone. Replace ``UTC`` with 
    # ``Area/Region`` as it appears in IANA Time Zone Database if you don't
    # want to use UTC.
    TZ=UTC

NOTE: Lines starting with # are comments and don't need to be written.

Now you finally add the bot. If you have multiple bots, simply add separate
lines for them all::

    */5 * * * * supybot-botchk --botdir=/home/<username>/<bot>/ --pidfile=/home/<username>/<bot>/<bot>.pid --conffile=/home/<username>/<bot>/<bot>.conf

If you needed to use diferent environment for other bot, you could specify
that on the same line. For example, my other bot uses en_US.utf8 as locale
and UTC as timezone::

    */5 * * * * LC_ALL=en_US.UTF-8 TZ=UTC supybot-botchk --botdir=/home/<username>/<bot2>/ --pidfile=/home/<username>/<bot2>/<bot2>.pid --conffile=/home/<username>/<bot2>/<bot2>.conf

Note that environment doesn't need to be specified on supybot-botchk line
unless it differs from globally specified environment which we added as the
first thing to crontab.

Now you can save the crontab by pressing ``CTRL + O`` answering ``y`` and
then quitting nano with ``CTRL + X``.

If you are wondering what ``*/5 * * * *`` means, it simply means "run this
every five minutes every day". The 5 can be replaced with any other number
and there are also ``@hourly`` etc. which can be used on it's place, but
you most likely won't want to wait hour or more if your bot crashes.

systemd service
===============

You need root access as no one has got this to work as user service yet.
You must also use systemd as your init.

Create a new file ``/etc/systemd/system/<BOTNAME>.service`` with the
following content replacing things were suitable::

    [Unit]
    Description=Supybot
    After=network.target

    [Service]
    Environment="PATH=/usr/local/bin:/usr/local/sbin:/usr/local/games:/usr/bin:/usr/sbin:/usr/games:/bin:/sbin:/bin:/opt/local/bin:/opt/local/sbin:/opt/local/games TZ=UTC"
    Type=simple
    ExecStart=/usr/local/bin/supybot /home/bot/botname/botname.conf
    ExecReload=/bin/kill -HUP $MAINPID
    Restart=always
    User=BOTUSERNAME
    SyslogIdentifier=Supybot
    # Uncomment these lines for extra security at the cost of breaking some third-party plugins:
    # SystemCallFilter=~@raw-io @clock @cpu-emulation @debug @keyring @module @mount @obsolete @privileged @raw-io
    # ProtectSystem=strict
    # ProtectHome=read-only
    # ReadWritePaths=/home/bot/botname

    [Install]
    WantedBy=multi-user.target

Now you should run ``systemctl daemon-reload`` to make systemd aware
of changed files and ``systemctl enable <BOTNAME>.service`` to make the
bot start on boot etc. and ``systemctl start <BOTNAME>.service`` to start
the bot.

Remember to check the ``Ènvironment`` line. You can get your PATH with
``printf 'PATH=%s\n' "$PATH"``.

Some commands
-------------

* autostart on boot: ``systemctl enable <BOTNAME>.service``
* disable autostart on boot: ``systemctl disable <BOTNAME>.service``
* start the bot: ``systemctl start <BOTNAME>.service``
* stop the bot: ``systemctl stop <BOTNAME>.service``
* reload config files: ``systemctl reload <BOTNAME>.service``
