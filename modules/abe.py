#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing Android Backup Extractor", 1)
        make_dir("/opt/abe")
        file_link = run_command_with_output('curl -sL "https://github.com/nelenkov/android-backup-extractor/releases/latest" | grep \'abe-all.jar"\' | cut -d\\" -f2', safe=True).strip()
        file_download("https://github.com{0}".format(file_link), "/opt/abe/abe.jar")
        print_success("Done!", 1)
