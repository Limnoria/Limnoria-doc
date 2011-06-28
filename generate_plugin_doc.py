#!/usr/bin/env python2

from __future__ import with_statement

import os
import re
import sys

# Commands instances are converted into SynchronizedAndFirewalled
from supybot.callbacks import SynchronizedAndFirewalled as Commands

validCommandName = re.compile('^[a-z]+$')

def main():
    pluginNames = sys.argv[1:]
    for pluginName in pluginNames:
        supybot = __import__('supybot.plugins.%s.plugin' % pluginName)
        PluginClass = getattr(supybot.plugins, pluginName).plugin.Class
        filename = 'use/plugins/%s.rst' % pluginName.lower()
        os.unlink(filename)
        with open(filename, 'a') as fd:
            fd.write('\n.. _plugin-%s:\n\nThe %s plugin\n' %
                     (pluginName.lower(), pluginName))
            fd.write('='*len('The %s plugin' % pluginName))
            fd.write('\n\n')
            writeDoc(PluginClass, fd, '')

def writeDoc(PluginClass, fd, prefix):
    if prefix != '':
        prefix += ' '
    for attributeName, attribute in PluginClass.__dict__.items():
        if not callable(attribute):
            continue
        if not validCommandName.match(attributeName):
            continue
        if isinstance(attribute, Commands):
            writeDoc(attribute, fd, prefix + attributeName)
        else:
            if attribute.__doc__ is None:
                attribute.__doc__ = ''
            syntax = attribute.__doc__.split('\n\n')[0].strip()
            if syntax == 'takes no arguments':
                syntax = ''
            else:
                syntax = ' ' + syntax
            args = {
                    'prefix_dash': prefix.replace(' ', '-'),
                    'command': attributeName, # Does not contain spaces
                    'prefix_with_trailing_space': prefix,
                    'syntax': syntax,
                    'help_string': parseHelpString(attribute.__doc__),
            }
            args['decoration'] = '^'*len('%(prefix_with_trailing_space)s%(command)s%(syntax)s' %
                    args)
            fd.write('.. command-%(prefix_dash)s%(command)s:\n\n'
                     '%(prefix_with_trailing_space)s%(command)s%(syntax)s\n'
                     '%(decoration)s\n\n'
                     '%(help_string)s\n\n' % args)

def parseHelpString(string):
    # Remove the syntax
    string = '\n\n'.join(string.split('\n\n')[1:])
    # Remove the starting and ending spaces
    string = '\n'.join([x.strip(' ') for x in string.split('\n')])
    # Put the argument names into italic
    string = re.sub(r'(<[^>]+>)', r'*\1*', string, re.M)
    string = re.sub(r'(--[^ ]+)', r'*\1*', string, re.M)
    return string


if __name__ == '__main__':
    main()

