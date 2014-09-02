.. _supybot-botchk:

##############
supybot-botchk
##############

supybot-botchk is a script that comes with Supybot which restarts the bot
if it quits or system reboots or anything that causes the bot to quit. It's
placed to crontab so cron will run it with scheduled intervals.

How to use it?
==============

Configuring the bot
-------------------

Start by telling your bot to write a pidfile somewhere where it can write
and restart the bot. For example::

    config supybot.pidfile /home/<username>/<bot>/<bot>.pid

where <username> is replaced with the system username and <bot> is replaced
with the name of the bot.

crontab
-------

After the pidfile is configured, you can modify crontab. First you should
copy the output of::

    printf 'PATH=%s\n' "$PATH"

and open crontab with ``EDITOR=nano crontab -e`` and paste the output of
previous command to the first lines which don't have comments. This should
be on top. You will probably also want to configure locale and timezone
which happens by adding the following lines::

    # Replace en_US.utf8 with your own locale! You should see list of
    # available locales with `locale` command, just use something which
    # ends with "utf8".
    LC_ALL=en_US.utf8
    
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

    */5 * * * * LC_ALL=en_US.utf8 TZ=UTC supybot-botchk --botdir=/home/<username>/<bot2>/ --pidfile=/home/<username>/<bot2>/<bot2>.pid --conffile=/home/<username>/<bot2>/<bot2>.conf

Note that environment doesn't need to be specified on supybot-botchk line
unless it differs from globally specified environment which we added as the
first thing to crontab.

Now you can save the crontab by pressing ``CTRL + O`` answering ``y`` and
then quitting nano with ``CTRL + X``.

If you are wondering what ``*/5 * * * *`` means, it simply means "run this
every five minutes every day". The 5 can be replaced with any other number
and there are also ``@hourly`` etc. which can be used on it's place, but
you most likely won't want to wait hour or more if your bot crashes.
