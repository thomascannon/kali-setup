#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Installing Frida", 1)
        run_command('pip install frida-tools')
        run_command('pip install frida')
        print_success("Done!", 1)
