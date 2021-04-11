#!/usr/bin/env python3

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

            .. toctree::
               :maxdepth: 1

            """
        )
    )
    for plugin in plugins:
        fd.write(f"   {plugin}\n")
