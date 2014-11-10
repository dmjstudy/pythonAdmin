#!/usr/bin/env python
#pysysinfo_func.py
import subprocess

#Command 1
def uname_func():
	uname = "uname"
	uname_arg ="-a"
	print "Gathering System information with %s command:\n" % uname
	subprocess.call([uname,uname_arg])

#Command 2
def disk_func():
	diskspace = "df"
	diskspace_arg = "-h"
	print "Gathering diskspace information %s command:\n" % diskspace
	subprocess.call([diskspace,diskspace_arg])

#Main function that call other functions
def main():
	uname_func()
	disk_func()

main()