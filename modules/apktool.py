#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing APKTool", 1)
        make_dir("/opt/apktool")
        file_download("https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool", "/opt/apktool/apktool")
        file_link = run_command_with_output('curl -sL "https://github.com/iBotPeaches/Apktool/releases/latest" | grep \'.jar"\' | cut -d\\" -f2', safe=True).strip()
        file_download("https://github.com{0}".format(file_link), "/opt/apktool/apktool.jar")
        run_command('chmod +x /opt/apktool/*')
        file_append_once('/root/.bashrc', 'export PATH="${PATH}:/opt/apktool/"')
        print_success("Done!", 1)
