#!/usr/bin/env python3

from lib.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Configuring bash", 1)
        file_backup('/etc/bash.bashrc')
        file_append_once('/etc/bash.bashrc', 'shopt -sq cdspell', 'cdspell')
        file_append_once('/etc/bash.bashrc', 'shopt -s autocd', 'autocd')
        file_append_once('/etc/bash.bashrc', 'shopt -sq checkwinsize', 'checkwinsize')
        file_append_once('/etc/bash.bashrc', 'shopt -sq nocaseglob', 'nocaseglob')
        file_append_once('/etc/bash.bashrc', 'HISTSIZE=10000', 'HISTSIZE')
        file_append_once('/etc/bash.bashrc', 'HISTFILESIZE=10000', 'HISTFILESIZE')
        print_success("Done", 1)
        
