#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing Ghidra", 1)
        ghidra_link = run_command_with_output('curl -s "https://ghidra-sre.org/" | grep \'Download Ghidra\' | cut -d\\" -f6', safe=True).strip()
        file_download("https://ghidra-sre.org/{0}".format(ghidra_link), "/opt/ghidra.zip")
        run_command('cd /opt/; unzip ghidra.zip')
        run_command('rm /opt/ghidra.zip')
        run_command('cd /opt/; mv ghidra_* ghidra')
        file_append_once('/root/.bashrc', 'export PATH="${PATH}:/opt/ghidra/"')
        print_success("Done!", 1)
