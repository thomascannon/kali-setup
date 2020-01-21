#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    _REPOS_TO_ADD = {
        #"sublime-text": "deb https://download.sublimetext.com/ apt/stable/",
    }

    _PACKAGES = {
        "OpenJDK 8": ["openjdk-8-jdk"],
        "hostapd": ["hostapd"],
        "grc": ['grc'],
        "pip": ['python-pip'],
    }

    _COMMANDS_BEFORE = {
        #"Adding sublime repo key": ["wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -"],
    }

    _COMMANDS_AFTER = {
        "Updating IEEE oui list": ["airodump-ng-oui-update"],
        "Generating SSH key": ["ssh-keygen -b 4096 -t rsa -f ~/.ssh/id_rsa -P ''"],
    }

    def check(self, config):
        return True

    def install(self, config):
        print_status("Executing pre-install commands...", 1)
        for title,cmds in self._COMMANDS_BEFORE.items():
            print_status("{0}...".format(title), 2)
            for cmd in cmds:
                run_command(cmd)
            print_success("Done!",2)
        print_success("Done executing pre-install commands", 1)

        print_status("Adding new repositories", 1)
        for name,repo in self._REPOS_TO_ADD.items():
            file_write("/etc/apt/sources.list.d/{0}.list".format(name), repo)

        print_status("Updating repos before starting installs", 1)
        run_command("apt update")

        print_status("Installing packages!", 1)
        for title,pkgs in self._PACKAGES.items():
            print_status("Installing {0}...".format(title), 2)
            apt_install(pkgs)
            print_success("Done!",2)
        print_success("Done installing packages!", 1)

        print_status("Executing post-install commands...", 1)
        for title, cmds in self._COMMANDS_AFTER.items():
            print_status("{0}...".format(title), 2)
            for cmd in cmds:
                run_command(cmd)
            print_success("Done!", 2)
        print_success("Done executing post-install commands", 1)



