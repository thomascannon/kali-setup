#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Installing scrcpy", 1)
        apt_install('scrcpy')
        print_success("Done!", 1)
