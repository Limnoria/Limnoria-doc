********************************************
Using Limnoria's HTTP server in your plugins
********************************************

Introduction
============

Having a HTTP server in an IRC may be baffling, because it seems to be useless.
Yes, you are right, it is useless in most of the cases. But it may be cool.

Some plugins (WebStats, Github, and UfrPaste are the only one, as far as I
know) have their own embedded HTTP server. Unfortunately, a HTTP need a port,
and consumes a few resources (CPU/memory). So, if you want many of these plugins,
it becomes embarrassing.
Last pro for this server: a plugin that use this HTTP server is really tinier,
as shown in `this commit`_ (note that the path of the httpserver is no more
*supybot.utils.httpserver* but *supybot.httpserver*)

.. _this commit: https://github.com/ProgVal/Supybot-plugins/commit/220146ea

Anyway, if you are on this page, this is probably because you want to use this
HTTP server, so I don't need to convince you.
Before reading further, be sure you have a Limnoria (or any Supybot fork that
merged this HTTP server).

Using the HTTP server in a plugin
=================================

Let's try to make a basic dictionary about Supybot! We'll call it Supystory.

We want to get plain text information about Supybot, Gribble, and Limnoria when
accessing http://localhost:8080/supystory/supybot,
http://localhost:8080/supystory/gribble, and
http://localhost:8080/supystory/limnoria, and an HTML error page if the page
is not found

Importing the HTTP server
-------------------------

On only have to add this line::

    import supybot.httpserver as httpserver.


Creating a callback
-------------------

If you are familiar with `BaseHTTPServer`, you will recognize the design,
except you don't need to subclass BaseHTTPServer, because I already did
it in *supybot.httpserver*.

Now, you have to subclass `httpserver.SupyHTTPServerCallback`. A callback is
pretty much like an handler, but this is not an handler, because a callback is
called by the handler.

Here is how to do it::

    class SupystoryServerCallback(httpserver.SupyHTTPServerCallback):
        name = 'WebStats'

Now, you have to register the callback, because the HTTP server does not know
what subdirectory it should assign to your callback. Do it with adding a
*__init__* to your plugin (read Supybot's docs about it, for more
informations)::

    class Supystory(callbacks.Plugin):
        def __init__(self, irc):
            # Some stuff needed by Supybot
            self.__parent = super(Supystory, self)
            callbacks.Plugin.__init__(self, irc)

            # registering the callback
            callback = SupystoryServerCallback() # create an instance of the callback
            httpserver.hook('supystory', callback) # register the callback at `/supystory`

By the way, don't forget to unhook your callback when unloading your plugin,
unless what it will be impossible to reload the plugin! Append this code to
the following::

    def die(self):
        # unregister the callback
        httpserver.unhook('supystory') # unregister the callback hooked at /supystory

        # Stuff for Supybot
        self.__parent.die()

Now, you can load your plugin, and you'll see on the server a beautiful link
to `/supystory` called `Supystory`.

Overriding the default error message
------------------------------------

But our plugin does not do anything for the moment. If click the link, you'll
get this message::

    This is a default response of the Supybot HTTP server. If you see this
    message, it probably means you are developping a plugin, and you have
    neither overriden this message or defined an handler for this query.

That mean your browser sent a GET request, but you didn't teach your plugin how
to handle it. First, we'll change this error message.
Here is a new code for your callback::

    class SupystoryServerCallback(httpserver.SupyHTTPServerCallback):
        name = 'Supystory'
        defaultResponse = """
        This plugin handles only GET request, please don't use other requests."""

Now, you'll get your customized message. But your plugin still doesn't work.
You need to implement the GET request.

Implementing the GET request
----------------------------

As I said before, callbacks are pretty much like handlers. In order to handle
GET requests, you have to implement a method called... `doGet` (if you used
BaseHTTPServer, you will notice this is not do_GET, because doGet is more
homogeneous with Supybot naming style: `doPrivmsg`, `doPing`, and so on).

You will get the handler and the URI as arguments. The handler is a
`BaseHTTPRequestHandler`_, and the URI is a string.

.. _BaseHTTPRequestHandler: http://docs.python.org/library/basehttpserver.html#BaseHTTPServer.BaseHTTPRequestHandler

Here is the code of the callback... pretty much simple, as ever::

        class SupystoryServerCallback(httpserver.SupyHTTPServerCallback):
            name = 'Supystory'
            defaultResponse = """
            This plugin handles only GET request, please don't use other requests."""

            def doGet(self, handler, path):
                if path == '/supybot':
                     response = 'Supybot is the best IRC bot ever.'
                elif path == '/gribble':
                     response = 'Thanks to Gribble, we have many bug fixes and SQLite 3 support'
                elif path == '/limnoria':
                     response = 'Because of Limnoria, you need to internationalize your plugins and read this f*cking doc.'
                else:
                     response = None
                if response is None:
                     handler.send_response(404) # Not found, as described by the HTTP protocol
                     handler.send_header('Content-type', 'text/html') # This is the MIME for HTML data
                     handler.end_headers() # We won't send more headers
                     handler.wfile.write("""
                     <html>
                      <head>
                       <title>Error</title>
                      </head>
                      <body>
                       <h1>404 Not found</h1>
                       <p>
                        The document could not be found. Try one of this links:
                        <a href="./supybot">Supybot</a>
                        <a href="./gribble">Gribble</a>
                        <a href="./limnoria">Limnoria</a>
                       </p>
                      </body>
                     </html>""")
                else:
                     handler.send_response(404) # Not found, as described by the HTTP protocol
                     handler.send_header('Content-type', 'text/plain') # This is the MIME for plain text
                     handler.end_headers() # We won't send more headers
                     handler.wfile.write(response)

That's all !

You may not understand everything (I know I don't speak English very well);
come on #limnoria at Freenode and ask for help of make suggestions!
