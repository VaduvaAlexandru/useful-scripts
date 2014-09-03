#!/usr/bin/python

import getopt, sys

def inspect_args():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:o:vtbpms:', ['help', 'input=', 'output='])
        if not opts:
            print 'No options supplied..'
            usage()
    except getopt.GetoptError,e:
        # print help information and exit:
        print str(e)
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
    output = None
    verbose = False
#    for o, a in opts:
#	if o == "-v":
#            verbose = True
#        elif o in ("-h", "--help"):
#            usage()
#            sys.exit()
#        elif o in ("-o", "--output"):
#            output = a
#        else:
#            assert False, "unhandled option"

def usage():
    print "\nGit commit script usage available"
    print "Usage: \n "+ sys.argv[0] +" [options] filename"
    print "Take the git obtained commit defined in 'filename' and send an email to selected peers."
    print "\nMandatory arguments to long options are mandatory for short options too."
    print "\t-m, --maintainer       send email to maintainers of the package"
    print "\t-c, --committers       send email to committers on the package"
    print "\t-l, --list             send email to a list of committers read from config file"
    print "\t-h, --help             display this help and exit"
    print "\t-v, --version          output version information and exit"
    print "\nReport "+ sys.argv[0] +" bugs to vaduva.jan.alexandry@gmail.com"

if __name__ == "__main__":
	inspect_args()
