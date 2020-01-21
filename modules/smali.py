#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing smali and baksmali", 1)
        make_dir("/opt/smali")
        file_link = run_command_with_output('curl -s "https://bitbucket.org/JesusFreke/smali/downloads/" | grep \'downloads/smali-[0-9].*.jar"\' -m 1 | cut -d\\" -f2', safe=True).strip()
        file_download("https://bitbucket.org{0}".format(file_link), "/opt/smali/smali.jar")
        file_link = run_command_with_output('curl -s "https://bitbucket.org/JesusFreke/smali/downloads/" | grep \'downloads/baksmali-[0-9].*.jar"\' -m 1 | cut -d\\" -f2', safe=True).strip()
        file_download("https://bitbucket.org{0}".format(file_link), "/opt/smali/baksmali.jar")
        print_success("Done!", 1)
