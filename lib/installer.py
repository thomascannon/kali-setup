#!/usr/bin/env python3

from lib.printer import *
from lib.automation import *
import sys
import glob
import importlib.util


class Installer:
    def __init__(self, config):
        self._config = config
        self._installers = {}


    def run(self):
        print_status("Starting installer...")
        self.load_installers()
        print_status("{0} installers loaded!".format(len(self._installers)))

        list_of_modules = [x.strip() for x in self._config.get_config()['general'].get('modules').split(',')]
        ok_modules = []
        print_status("Checking {0} installation modules...".format(len(list_of_modules)))
        for mod in list_of_modules:
            if mod not in self._installers:
                print_error("Unknown module provided: {0}".format(mod), 1)
            else:
                mod_ret = self._installers[mod].check(self._config.get_config())
                if mod_ret is not True:
                    print_error("Module {0} error: {1}".format(mod, mod_ret), 1)
                else:
                    ok_modules.append(mod)
        if len(list_of_modules) != len(ok_modules):
            print_error("{0} modules were invalid!".format(len(list_of_modules) - len(ok_modules)))
            if get_input("Do you want to continue without those?", 'y', ['y','n']) != 'y':
                print_status("Exiting!")
                sys.exit(1)
            else:
                print_status("Ignoring bad modules, continuing!")
        else:
            print_success("Modules are good to go!")
        print_status("Executing pre-module scripts...")
        self.before_modules()
        print_success("Done with pre-module scripts")
        print_status("Running {0} installation modules!".format(len(ok_modules)))       
        counter = 1
        for mod in ok_modules:
            print_status("[{0}/{1}] Running installation module: {2}...".format(counter, len(ok_modules), mod))
            try:
                self._installers[mod].install(self._config.get_config())
            except Exception as e:
                print_error("Module '{0}' had runtime error: {1}".format(mod, e))
            print_success("Done with {0}!".format(mod))
            counter += 1
        print_status("Executing post-module scripts...")
        self.after_modules()
        print_success("Done with post-module scripts")
        print_success("Done installing!")


    def load_installers(self):
        for fileloc in glob.glob('modules/*.py'):
            if '__init__' not in fileloc:
                module_name = fileloc.replace('/', '.')[:-3]
                type_name = module_name.split('.')[-1]
                spec = importlib.util.spec_from_file_location(module_name, fileloc)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                self._installers[type_name] = mod.InstallerTemplate()
                


    def before_modules(self):
        is_dry_run = self._config.get_config().get('general', 'dry run', fallback=False)

        print_status("Checking internet access", 1)
        ret = run_command('ping -c 1 -W 10 www.google.com', safe=True, show_error=False)
        if is_dry_run:
            ret = 0
        if ret != 0:
            print_error("No internet access! Can't continue without internet!")
            sys.exit(1)
        print_success("Looks good, internet works", 1)

        print_status("Running system updates before starting. This may take a while...", 1)
        if self._config.get_config().getboolean('general', 'update first', fallback=True) and not is_dry_run:
            run_command("apt -y -qq clean")
            run_command("apt -y -qq autoremove")
            run_command('apt -y -qq update')
            run_command('export DEBIAN_FRONTEND=noninteractive; APT_LISTCHANGES_FRONTEND=none apt -o Dpkg::Options::="--force-confnew" -y dist-upgrade --fix-missing')
            run_command("apt -y -qq clean")
            run_command("apt -y -qq autoremove")
            print_success("Done!", 1)
        else:
            print_success("Skipping!", 1)





    def after_modules(self):
        print_success("Done!", 1)
    
