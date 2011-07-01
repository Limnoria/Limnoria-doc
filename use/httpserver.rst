*********************
Using the HTTP server
*********************

Configuration
=============

The HTTP comes with a couple of additional variables:

* :ref:`supybot.servers.http.host`: The host the bot will bind. In most of
  the cases, you will use 0.0.0.0 (everything) or 127.0.0.1 (restricted to
  local connections). Defaults to 0.0.0.0
* :ref:`supybot.servers.http.port`: The port the bot will bind. May not work
  if the number is too low. Defaults to 8080 (alternative HTTP port).
* :ref:`supybot.servers.http.keepAlive`: Determines weather the HTTP server
  will run even if has nothing to serve. Defaults to False, because the HTTP
  might require to change the port, if it is already taken.

Using the server
================

At the root of the server, you will find a list of the plugins that have a Web
interface, and a link to them. Each plugin has its own subdirectory(ies).

You may also want to have Apache behind Supybot's HTTP server, if you want to
use subdomains. Here is an example of configuration (I didn't test it with the
rewrite, please notify me whether it works or not):

.. code-block:: apache

    <VirtualHost 0.0.0.0:80>
        ServerName stats.yourdomain.org
	    <Location />
                ProxyPass http://localhost:8080/webstats/
                SetEnv force-proxy-request-1.0 1
                SetEnv proxy-nokeepalive 1
                RewriteEngine On
                RewriteRule ^/webstats/(.*)$ /$1
        </Location>
    </VirtualHost>
