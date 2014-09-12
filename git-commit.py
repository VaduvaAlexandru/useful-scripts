#!/usr/bin/python

import getopt, sys
import re
import os.path
import git

#Define software version
version = 1.0

#Define the emailing list
email_list = []
names_list = []

#Define other global variables
chechM = False
checkC = False
filename = ""
lxcrNo = ""

def inspect_args():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hlvmcf:n:', ['help', 'list', 'verbose', 'maintainer', 'committers', 'filename=', 'lxcr='])
        if not opts:
            print "No options supplied. Default options enabled:"
            print "\tReviewer and merger selected from the given list file."
            read_list()
            usage()
    except getopt.GetoptError,e:
        # print help information and exit:
        print str(e)
        usage()
        sys.exit()

    file_status = False
    opts_check = False
    global checkM
    global checkC
    global filename
    global lxcrNo
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            opts_check = True
            usage()
            sys.exit()
        if opt in ('-v', '--version'):
            opts_check = True
            print  "Software version: " + str(version)
            sys.exit()
        if opt in ('-f', "--filename"):
            opts_check = True
            file_status = True
            if os.path.isfile(arg):
                filename = arg
            else:
                print "Wrong format for the argument passed on option "+opt
        if opt in ('-n', 'lxcr'):
            opts_check = True
            lxcrNo = arg
        if opt in ('-l', '--list'):
            opts_check = True
            parse_list()
        elif opt in ('-m', '--maintainer'):
            opts_check = True
            checkM  = True
        elif opt in ('-c', '--committers'):
            opts_check = True
            checkC = True
        if not opts_check:
            assert False, "unhandled option"
    # No git log output is used the committer options are prioritized.
    # The script believes the commiter about the veridicity of his/hers patch
    if not file_status:
        print "Please specify commit filename.\n"
        usage()
        sys.exit()

#TODO: add -n option for LXCR number specification.
def usage():
    print "\nGit commit script usage available"
    print "Usage: \n "+ sys.argv[0] +" [options]"
    print "Take the git obtained commit and send an email to selected peers. If no filename is offered then the standard 000* file is used."
    print "\nMandatory arguments to long options are mandatory for short options too."
    print "\t-m, --maintainer       send email to maintainers of the package"
    print "\t-c, --committers       send email to committers on the package"
    print "\t-l, --list             send email to a list of committers read from config file"
    print "\t-f, --filename         selected commit file"
    print "\t-n, --lxcr             specify lxcr number for linking patch to Enea Linux internal CRs"
    print "\t-h, --help             display this help and exit"
    print "\t-v, --version          output version information and exit"
    print "\nReport "+ sys.argv[0] +" bugs to vaduva.jan.alexandry@gmail.com"

def read_list():
    with open('input/list.txt') as fp:
        print fp.read()

def parse_list():
    with open('input/list.txt') as fp:
        for line in fp:
            line = "".join(line.split())
            if line.split('-')[0] in ['e', 'enable', 'enabled']:
                email_list.append(line.split('-')[1])
                names_list.append(line.split('-')[2])

def special_match(strg, search=re.compile(r'[^a-z0-9@.]').search):
    return not bool(search(strg))

#def check_options (opt, arg):
#    if opt in ('-m', '--maintainer') or opt in ('-c', '--committers'):
#        return special_match(arg)
#    else:
#        return os.path.isfile(arg)

def git_autocomplete():
    global filename
    repo_dir = os.path.dirname(filename)
#    print repo_dir
    repo = git.Repo('./')
    print repo.git.log(-1, "-p")

if __name__ == "__main__":
    inspect_args()
    git_autocomplete()
#    print filename +":"+ str(checkM)+":"+str(checkC)
#    repo = git.Repo('./')
#    print repo.git.status()
