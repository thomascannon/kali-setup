#!/usr/bin/env python3

import configparser
from lib.printer import *
from lib.automation import automation_set_verbose, automation_set_dry_run
import sys
import os

class Config:
    DEFAULTS = {
        'general': {
            'dry run': 'yes',
            'verbose': 'no',
            'update first': 'yes',
            'modules': 'base, vmware'
        },
        'git': {
            'name': 'Anonymous',
            'email': 'anonymous@domain.com'
        }
    }

    def __init__(self, inipath):
        self._inipath = inipath
        self._config = None

    def get_config(self):
        return self._config

    def print_config(self, prefix=''):
        sections = self._config.sections()
        for section in sections:
            print("{0}[{1}]".format(prefix, section))
            for key in self._config[section]:
                print(" {0}{1} = {2}".format(prefix, key, self._config[section][key]))
            print()

    def generate_config(self, outfile):
        if self._config is None:
            self._config = configparser.ConfigParser()
            self._config.read_dict(Config.DEFAULTS)
        with open(outfile, 'w') as writefile:
            self._config.write(writefile)

    def load_config(self):
        self._config = configparser.ConfigParser()
        self._config.read_dict(Config.DEFAULTS)
        if self._inipath is None or not os.path.exists(self._inipath):
            self.warn_about_config()
        if self._inipath is not None:
            self._config.read(self._inipath)
        automation_set_verbose(self._config.getboolean('general','verbose', fallback=False))
        automation_set_dry_run(self._config.getboolean('general','dry run', fallback=False))


    def warn_about_config(self):
        print_warning("You did not specify a configuration file!")
        print_warning("Pass the name of the config file or use -g to generate one")
        print_success("Exiting!")
        sys.exit(1)
