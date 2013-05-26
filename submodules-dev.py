#!/usr/bin/python3

import sys, os, re
from subprocess import call

# This script will allow you to checkout all your submodules to the master
# of their remoted and thus avoid the detached head problems 
# This is useful in development environments

workdir = os.getcwd()
try:
    modules = open('.gitmodules').read()

    # Find all the submodules from the .gitmodules file
    submodules = re.findall('\[submodule "(.+?)"\]\n([^\[]+)', modules, re.MULTILINE|re.DOTALL)
    for module, config in submodules:
        print('Processing module %s...' % module)

        # Parse the options to find the path and the url
        options = {}
        keyvalue = re.findall('(.+?) = (.+?)\n', config)
        for key, value in keyvalue:
            options[key.strip()] = value.strip()
        if 'url' not in options or 'path' not in options:
            print('! Module has no url or path')
            continue

        # If the directory does not exists, git clone the submodule to it
        directory = options['path']
        if not os.path.isdir(directory):
            print('- Cloning into directory')
            call(['git', 'clone', options['url'], directory])
        # If it already exists, checkout master and pull
        else:
            print('- Checking out master & updating')
            os.chdir(directory)
            call(['git', 'checkout', 'master'])
            call(['git', 'pull', 'origin', 'master'])
            os.chdir(workdir)
except IOError:
    print('Error while opening/reading .gitmodules')
