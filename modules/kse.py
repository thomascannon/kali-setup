#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing Keystore Explorer", 1)
        file_link = run_command_with_output('curl -sL "https://github.com/kaikramer/keystore-explorer/releases/latest" | grep \'kse.*all.deb"\' | cut -d\\" -f2', safe=True).strip()
        file_download("https://github.com{0}".format(file_link), "/root/kse.deb")
        run_command('dpkg -i /root/kse.deb > /dev/null 2>&1; rm /root/kse.deb')
        print_success("Done!", 1)
