#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Installing Androguard", 1)
        run_command('pip install androguard')
        print_success("Done!", 1)
