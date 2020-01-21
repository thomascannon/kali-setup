#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True if command_exists("git") else "'git' package not installed"

    def install(self, config):
        proj = "oblique/create_ap"
        print_status("Cloning {0}...".format(proj), 1)
        github_clone(proj, "/opt/")
        folder_name = "/opt/{0}-git".format(proj.replace('/','_').lower())
        run_command("cd {0}; make install".format(folder_name))
        run_command("rm -rf {0}".format(folder_name))
        print_success("Done!", 1)
