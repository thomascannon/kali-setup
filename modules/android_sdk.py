#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Downloading and Installing Android SDK", 1)
        make_dir("/opt/android_sdk")
        sdk_link = run_command_with_output('curl -s "https://developer.android.com/studio" | grep \'repository/sdk-tools-linux\' | cut -d\\" -f2', safe=True).strip()
        file_download(sdk_link, "/opt/android_sdk/android_sdk.zip")
        run_command('cd /opt/android_sdk; unzip android_sdk.zip')
        run_command('rm /opt/android_sdk/android_sdk.zip')

        #sdkmanager still depends on Java 8 which needs to be installed before this and be the default jdk
        print_status("Installing platform-tools", 1)
        run_command('yes | /opt/android_sdk/tools/bin/sdkmanager "platform-tools"')
        file_append_once('/root/.bashrc', 'export ANDROID_HOME="/opt/android_sdk/"')
        file_append_once('/root/.bashrc', 'export PATH="${PATH}:${ANDROID_HOME}tools/:${ANDROID_HOME}platform-tools/"')
        print_success("Done!", 1)
