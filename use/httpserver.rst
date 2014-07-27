*********************
Using the HTTP server
*********************

Configuration
=============

The HTTP comes with a couple of additional variables:

* :ref:`supybot.servers.http.favicon`: Path to the file which is shown to 
  browsers as favicon.
* :ref:`supybot.servers.http.hosts4`: The IPv4 addresses where the bot 
  will  bind. In most of the cases, you will use 0.0.0.0 (everything) or 
  127.0.0.1 (restricted to local connections). Defaults to 0.0.0.0
* :ref:`supybot.servers.http.hosts6`: The IPv6 addresses where the bot 
  will  bind. Defaults to empty.
* :ref:`supybot.servers.http.keepAlive`: Determines weather the HTTP server
  will run even if has nothing to serve. Defaults to False, because the 
  HTTPd might require to change the port, if it is already taken.
* :ref:`supybot.servers.http.port`: The port the bot will bind. May not 
  work if the number is below 1024. Defaults to 8080 (alternative HTTP port).


Using the server
================

At the root of the server, you will find a list of the plugins that have a Web
interface, and a link to them. Each plugin has its own subdirectory(ies).

You may also want to have Apache in front of Supybot's HTTP server, if 
you want to use subdomains. Here is an example of configuration 
(I didn't test it with the rewrite, please notify me whether it works or 
not):

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

Templates
=========

Among plugins which use the http server, some use the standard templates
system which allows you to edit page templates in a standard way (for other
plugins, check their documentation).

Templates are located in the `data/web/` folder. There is a folder per plugin
(and a `generic` folder, which holds generic pages), and all file names end
with `.example`, which is the default template provided by the plugin.
To customize it, rename it to remove `.example` (for instance:
``mv fooplugin/foopage.html.example fooplugin/foopage.html``) and edit it
(either do it intuitively or check the plugin documentation to see how
it handles its templates).
