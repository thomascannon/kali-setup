#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing Bytecode Viewer", 1)
        make_dir("/opt/bytecode-viewer")
        file_link = run_command_with_output('curl -sL "https://github.com/konloch/bytecode-viewer/releases/latest" | grep \'Bytecode-Viewer-[0-9].*jar"\' | cut -d\\" -f2', safe=True).strip()
        file_download("https://github.com{0}".format(file_link), "/opt/bytecode-viewer/bytecode-viewer.jar")
        print_success("Done!", 1)
