#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing JADX", 1)
        make_dir("/opt/jadx")
        file_link = run_command_with_output('curl -sL "https://github.com/skylot/jadx/releases/latest" | grep \'jadx-[0-9].*zip"\' | cut -d\\" -f2', safe=True).strip()
        file_download("https://github.com{0}".format(file_link), "/opt/jadx/jadx.zip")
        run_command('cd /opt/jadx; unzip jadx.zip; rm jadx.zip')
        file_append_once('/root/.bashrc', 'export PATH="${PATH}:/opt/jadx/bin/"')
        print_success("Done!", 1)
