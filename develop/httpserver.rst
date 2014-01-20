********************************************
Using Limnoria's HTTP server in your plugins
********************************************

Introduction
============

Limnoria provides an HTTP server to plugins. This is not relevant for most
plugins, but some of them have to start a server (either for serving a website
or for being remotely called).
The HTTP server provided by Limnoria aims at starting a single server for
all of them, which means less used port and less resources usage.

Some example plugins are `Factoids`_, `WebStats`_, `GitHub`_, UfrPaste, and
`WebDoc`_

.. _Factoids: https://github.com/ProgVal/Limnoria/tree/master/plugins/Factoids
.. _WebStats: https://github.com/ProgVal/Limnoria/tree/master/plugins/WebStats
.. _GitHub: https://github.com/ProgVal/Limnoria/tree/master/plugins/GitHub
.. _WebDoc: https://github.com/ProgVal/Limnoria/tree/master/plugins/WebDoc


Using the HTTP server in a plugin
=================================

Let's try to make a basic dictionary about Supybot! We'll call it Supystory.

We want to get plain text information about Supybot, Gribble, and Limnoria when
accessing http://localhost:8080/supystory/supybot,
http://localhost:8080/supystory/gribble, and
http://localhost:8080/supystory/limnoria, an index page, and an HTML error page
if the page is not found

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
                     response = b'Supybot is the best IRC bot ever.'
                elif path == '/gribble':
                     response = b'Thanks to Gribble, we have many bug fixes and SQLite 3 support'
                elif path == '/limnoria':
                     response = b'Thanks to Limnoria, you can to internationalize your plugins and write a web server.'
                elif path == '' or path == '/':
                     handler.send_response(200) # Found
                     handler.send_header('Content-type', 'text/html') # This is the MIME for HTML data
                     handler.end_headers() # We won't send more headers
                     handler.wfile.write(b"""
                     <html>
                      <head>
                       <title>Supystory</title>
                      </head>
                      <body>
                       <h1>Supystory</h1>
                       <p>
                        Here are some links you can visit:
                        <a href="./supybot">Supybot</a>
                        <a href="./gribble">Gribble</a>
                        <a href="./limnoria">Limnoria</a>
                       </p>
                      </body>
                     </html>""")
                     return
                else:
                     handler.send_response(404) # Not found
                     handler.send_header('Content-type', 'text/html') # This is the MIME for HTML data
                     handler.end_headers() # We won't send more headers
                     handler.wfile.write(b"""
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
                     return
                handler.send_response(200)
                handler.send_header('Content-type', 'text/plain') # This is the MIME for plain text
                handler.end_headers() # We won't send more headers
                handler.wfile.write(response)


Using templates
---------------

You may also want to allow your plugin's users to customize the web pages
without editing the source code of the plugin itself.

Limnoria provides a template facility, which takes a file name, returns the
content of a file from the file system if it exists (the user-defined template),
and a default one otherwise (the developer's default template).
does not exist.

In our case, we will do it only for the home page and the error page (which
are the only 'big' pages), like this::

        DEFAULT_TEMPLATES = {
            'supystory/index.html': """
        <html>
            <head>
                <title>Supystory</title>
            </head>
            <body>
                <h1>Supystory</h1>
                <p>
                    Here are some links you can visit:
                    <a href="./supybot">Supybot</a>
                    <a href="./gribble">Gribble</a>
                    <a href="./limnoria">Limnoria</a>
                </p>
            </body>
        </html>""",
            'supystory/error.html': """
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
        </html>"""
        }

        httpserver.set_default_templates(DEFAULT_TEMPLATES)



        class SupystoryServerCallback(httpserver.SupyHTTPServerCallback):
            name = 'Supystory'
            defaultResponse = """
            This plugin handles only GET request, please don't use other requests."""

            def doGet(self, handler, path):
                if path == '/supybot':
                     response = b'Supybot is the best IRC bot ever.'
                elif path == '/gribble':
                     response = b'Thanks to Gribble, we have many bug fixes and SQLite 3 support'
                elif path == '/limnoria':
                     response = b'Thanks to Limnoria, you can to internationalize your plugins and write a web server.'
                elif path == '' or path == '/':
                     handler.send_response(200) # Found
                     handler.send_header('Content-type', 'text/html') # This is the MIME for HTML data
                     handler.end_headers() # We won't send more headers
                     handler.wfile.write(httpserver.get_template('supystory/index.html').encode('utf8'))
                     return
                else:
                     handler.send_response(404) # Not found
                     handler.send_header('Content-type', 'text/html') # This is the MIME for HTML data
                     handler.end_headers() # We won't send more headers
                     handler.wfile.write(httpserver.get_template('supystory/error.html').encode('utf8'))
                     return
                handler.send_response(200)
                handler.send_header('Content-type', 'text/plain') # This is the MIME for plain text
                handler.end_headers() # We won't send more headers
                handler.wfile.write(response)

