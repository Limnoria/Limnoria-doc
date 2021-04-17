#!/usr/bin/env python3

import importlib
import os
import pkgutil
import subprocess
import textwrap

import supybot.plugins

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "use", "plugins")

def iter_subpackages(package):
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        if ispkg:
            yield modname

os.makedirs(OUTPUT_DIR, exist_ok=True)

subprocess.run([
    "supybot-plugin-doc",
    "--plugins-dir", os.path.dirname(supybot.plugins.__file__),
    "-o", OUTPUT_DIR,
    "-f", "rst",
    "--title-template", "$name",
    ], check=True)

plugins = list(iter_subpackages(supybot.plugins))

with open(os.path.join(OUTPUT_DIR, "index.rst"), "w") as fd:
    fd.write(
        textwrap.dedent(
            """
            Built-in plugins reference
            ==========================

            Here is a list of all built-in plugins and their commands
            and configuration.
            For an overview of all major plugins, see
            `Limnoria.net's plugin page`_

            .. _Limnoria.net's plugin page: https://limnoria.net/plugins.xhtml

            """
        )
    )

    for plugin in plugins:
        if plugin == "Alias":
            # Deprecated
            continue
        plugin_module = importlib.import_module(f"supybot.plugins.{plugin}")
        fd.write(f":doc:`{plugin} <{plugin}>`\n")
        fd.write(textwrap.indent(plugin_module.__doc__, "    "))
        fd.write("\n")

    fd.write(
        textwrap.dedent(
            """
            .. toctree::
               :maxdepth: 1
               :hidden:

            """
        )
    )
    for plugin in plugins:
        fd.write(f"   {plugin}\n")
