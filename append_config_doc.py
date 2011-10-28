#!/usr/bin/env python2

from __future__ import with_statement

import os
import re
import sys

import supybot.conf as conf
import supybot.plugins.Config.plugin as Config # Utilities

class ConfigPlugin(Config.Config):
    def __init__(self):
        # I just want to use methods that should be static, but are not,
        # so I will have to create a dummy instance for that.
        pass

# Commands instances are converted into SynchronizedAndFirewalled
from supybot.callbacks import SynchronizedAndFirewalled as Commands

sys.path.append('/home/progval/workspace/Supybot/Limnoria/plugins')

def main():
    pluginNames = sys.argv[1:]
    for pluginName in pluginNames:
        supybot = __import__('supybot.plugins.%s.config' % pluginName)
        pluginConfig = getattr(getattr(supybot.plugins, pluginName).config,
                pluginName) # combo!
        filename = 'use/plugins/%s.rst' % pluginName.lower()
        configRoot = 'supybot.plugins.%s' % pluginName
        with open(filename, 'a') as fd:
            fd.write('\n.. _plugin-%s-config:\n\nConfiguration\n' %
                     (pluginName.lower()))
            # I'm too lazy to count it by myself:
            fd.write('-'*len('Configuration'))
            fd.write('\n\n')
            writeDoc(pluginConfig, fd, 'supybot.plugins.' + pluginName)

def writeDoc(baseConfigNode, fd, prefix):
    for variableName in ConfigPlugin()._list(baseConfigNode):
        variablePrefix = ''
        while variableName[0] in '@#':
            variablePrefix += variableName[0]
            variableName = variableName[1:]
        print repr(prefix)
        print repr(variableName)
        fullPath = prefix + '.' + variableName
        print repr(fullPath)
        configVar = Config.getWrapper(fullPath)
        if hasattr(configVar, '_default'):
            defaultValue = 'Default value: %s' % configVar._default
        else:
            defaultValue = ''
        args = {
                'fullpath': fullPath,
                'decoration': '^'*len(fullPath),
                'default_value': defaultValue,
                'help': configVar._help}
        fd.write('.. _%(fullpath)s:\n\n%(fullpath)s\n%(decoration)s\n\n'
                '%(default_value)s\n\n'
                '%(help)s' % args)
        if '@' in variablePrefix:
            writeDoc(configVar, fd, fullPath)

def parseHelpString(string):
    # Remove the syntax
    string = '\n\n'.join(string.split('\n\n')[1:])
    # Remove the starting and ending spaces
    string = '\n'.join([x.strip(' ') for x in string.split('\n')])
    if string.endswith('\n'):
        string = string[0:-1]
    # Put the argument names into italic
    string = re.sub(r'(<[^>]+>)', r'*\1*', string, re.M)
    string = re.sub(r'(--[^ ]+)', r'*\1*', string, re.M)
    # Turn config variable names into refs
    string = re.sub(r'(supybot.[a-zA-Z0-9.]+)', r':ref:`\1`', string, re.M)
    return string


if __name__ == '__main__':
    main()

