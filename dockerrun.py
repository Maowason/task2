#! /usr/bin/python3
print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
#osname = input("Enter the OS Name: ")
osname = form.getvalue("x")
cmd = "sudo docker run -i -t -d  --name {} ubuntu:14.04".format(osname)
output = sp.getstatusoutput(cmd)
status = output[0]
out = output[1]
