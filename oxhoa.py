import os
import sys
follow = """
{+}-- https://www.facebook.com/dzmanisso
{+}-- https://twitter.com/ManissoDz
{+}-- https://github.com/Manisso
{+}-- https://www.linkedin.com/in/Manisso
{+}-- https://www.instagram.com/man.i.s/
"""

driftnet = """
Driftnet watches network traffic, and picks out and displays JPEG and GIF images for display.
It is a horrific invasion of privacy and shouldn't be used by anyone anywhere.
It can also extract MPEG audio data from the network and play it. 
If you live in a house with thick walls, this may be a useful way to find out about your neighbours' musical taste.

Source : https://github.com/deiv/driftnet
"""
logo = """                            
                 __        _   _        ___  
               / _ \      | | | |      / _ \ 
              | | | |_   _| |_| | ___ | |_| |
              | | | \ \ / /  _  |/ _ \|  _  |
              | |_| |\ v /| | | ( (_) ) | | |
               \___/  > < |_| |_|\___/|_| |_|
                     / ^ \                   
                    /_/ \_\                    
       }--{+}         Coded By Manisso       {+}--{
     }----{+}  Priv8 Tool  Based On Driftnet {+}----{
       }--{+}          Greetz To IcoDz       {+}--{           """
menu = """
    {1}--Start Image Capturing
    {2}--About Driftnet
    {3}--Follow Me
    
    {99}--Exit
    
"""
if not os.geteuid() == 0:
  sys.exit("""\033[1;91m\n[!] Must be run as root. [!]\n\033[1;m""")

os.system("clear && clear")
print logo  
print menu 
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()   

def  select():
  try:
    choice = input("OxHoA~# ")
    if choice == 1:
	  print("\033[1m\033[93m\n [++++]======================================================[++++] \033[1;m")
	  print("\033[1m\033[93m\n [++++] Capture image through Network                        [++++] \033[91m")
	  print("\033[1m\033[93m\n [++++] All images will be temporarily saved in \033[92m /opt/ochoa/\033[93m [++++] \033[91m")
	  print("\033[1m\033[93m\n [++++]======================================================[++++] \033[1;m")
	  os.system("mkdir -p /opt/ochoa/ && driftnet -d /opt/ochoa/ > /dev/null 2>&1 &")
	  os.system("xettercap  -X")
	  os.system("rm -R /opt/ochoa/")
	  quit()
    elif choice == 2:
	  print driftnet
	  quit()
    elif choice == 3:
	  print follow
	  quit()
    elif choice == 99:
	  exit()
  except(KeyboardInterrupt):
    print ""
select()
