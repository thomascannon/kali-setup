#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing uber-apk-signer", 1)
        make_dir("/opt/uber-apk-signer")
        file_link = run_command_with_output('curl -sL "https://github.com/patrickfav/uber-apk-signer/releases/latest" | grep \'uber-apk-signer-[0-9].*jar"\' | cut -d\\" -f2', safe=True).strip()
        file_download("https://github.com{0}".format(file_link), "/opt/uber-apk-signer/uber-apk-signer.jar")
        print_success("Done!", 1)
