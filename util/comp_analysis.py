from colorama import init, Fore, Back, Style
import os
import sys
import logging
import argparse

cwd = os.getcwd()

DEFAULT_CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../conf/pipeline.json")

DEFAULT_LOG_FILE = os.path.join(cwd, 'my.log')


##-------------------------------------------
## check_directory() will check whether the
## thing specified is in fact a directory and
## not something else.
##-------------------------------------------
def check_directory(dir):

    if not os.path.isdir(dir):

        print(Fore.RED + "'%s' is not a directory" % dir)
        print(Style.RESET_ALL)
        sys.exit(1)


curdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../pythonlib")

check_directory(curdir)

print(Fore.YELLOW + "Appended %s to path" % curdir)

print(Style.RESET_ALL)

sys.path.append(curdir)


import Athlete.Encyclopedia.Logger
import Athlete.Encyclopedia.Config.Manager
import Athlete.Encyclopedia.Manager


command_args = {}

config_manager = None

##-------------------------------------------
## append_lib_to_search_path() will append the
## pythonlib directory to the current seearch
## path thus making the Python modules 
## available to this program.
##-------------------------------------------
def append_lib_to_search_path():

    curdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../pythonlib")

    check_directory(curdir)

    print(Fore.YELLOW + "Appended %s to path" % curdir)

    print(Style.RESET_ALL)

    sys.path.append(curdir)


##--------------------------------------------
## check_command_line_args() will parse the
## command-line arguments for this executable
## and will abort if required values are not
## provided by the invoker.
##--------------------------------------------
def check_command_line_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-v', "--verbose", help="set verbose mode (default is True)", action="store_true")
    
    parser.add_argument("--config_file", help="configuration file in JSON format")
    
    parser.add_argument('-i', "--indir", help="input directory (default is [current working directory]")
    
    parser.add_argument('-l', "--logfile", help="output log file (default is [current working directory]/my.log)")
    
    parser.add_argument('-o', "--outdir", help="output directory (default is '/tmp/comp_analysis')")
    



    args = parser.parse_args()

    fatal_ctr = 0

    if not args.verbose:    
        args.verbose = True
        print(Fore.YELLOW + "--verbose was not specified and therefore was set to default %d" % args.verbose)
        print(Style.RESET_ALL)


    if not args.indir:
        args.indir = cwd
        print(Fore.YELLOW + "--indir was not specified and therefore was set to default %s" % args.indir) 
        print(Style.RESET_ALL)

    if not args.logfile:
        args.logfile = DEFAULT_LOG_FILE
        print(Fore.YELLOW + "--config_file was not specified and therefore was set to default %s" % args.config_file) 
        print(Style.RESET_ALL)

    if not args.config_file:
        args.config_file = DEFAULT_CONFIG_FILE
        print(Fore.YELLOW + "--config_file was not specified and therefore was set to default %s" % args.config_file) 
        print(Style.RESET_ALL)

    if not args.outdir:
        args.outdir = DEFAULT_OUTDIR
        print(Fore.YELLOW + "--outdir was not specified and therefore was set to default %s" % args.outdir) 
        print(Style.RESET_ALL)

    if not os.path.isfile(args.config_file):
        print(Fore.RED + "'%s' is not a file" % args.config_file)
        print(Style.RESET_ALL)
        sys.exit(1)
        

    global command_args

    command_args = args



def init_logger():

    logging.basicConfig(
    format   = config_manager.getLogFormat(),
    datefmt  = config_manager.getLogDateFormat(),
    filename = command_args.logfile,
    level    = logging.INFO
    )

    logger = logging.getLogger(__name__)


##-----------------------------------------
## main() is the main directory that will
## carry out the key steps of the program.
##
##-----------------------------------------
def main():


    check_command_line_args()

    global config_manager

    config_manager = Athlete.Encyclopedia.Config.Manager.Manager.getInstance(command_args.config_file)

    init_logger()

    check_directory(command_args.indir)

    manager = Athlete.Encyclopedia.Manager.Manager.getInstance()   

    manager.setIndir(command_args.indir)

    manager.setOutdir(commnad_args.outdir)

    manager.run()

    print("%s execution completed" % os.path.abspath(__file__))

    sys.exit(0)


if __name__ == "__main__":
    main()
