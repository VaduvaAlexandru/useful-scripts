#!/bin/bash
#===============================================================================
#
#          FILE:  clone-script.sh
#
#         USAGE:  ./clone-script.sh
#
#   DESCRIPTION:  Script used for multiple 'git clone' calls.
#
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:   (),
#       COMPANY:
#       VERSION:  1.0
#       CREATED:  06/24/2014 01:54:55 PM EEST
#      REVISION:  ---
#===============================================================================

usage() {
    echo "Usage: $0 [-l <location-for-cloning>] [-f <file-with-repositories>] [-b <branch-name>]" 1>&2;
    exit 1;
}

counter=0
branch="master"
file=[]
while getopts ":l:f:b:" opt; do
    case $opt in
        l)
            location=${OPTARG}
            ;;
        f)
            file[counter]=${OPTARG}
            ((counter++))
            ;;
        b)
            branch=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))
if [ -z "${location}" ]; then
    location="/home/alex/workspace/alvd-linux/test"
fi
#echo ${location}
#echo ${file[@]}
#echo ${counter}
for (( i=0; i<${counter}; i++ ))
do
    filename=$(pwd)/${file[${i}]}
#    echo ${filename}
    while read -r line
    do
        git clone -b ${branch} ${line} ${location}
    done < "${filename}"
done
