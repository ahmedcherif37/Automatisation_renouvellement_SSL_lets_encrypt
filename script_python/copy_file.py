#!/usr/bin/env python
# ce script  permet de parcourir le dossier des certificats letsencrypt et de verifier si il ya un certificat generer la copier et la coller dans le dossier de partage
# importing the required modules
import  os, os.path, time
from datetime import datetime
import shutil

files = os.listdir("/etc/letsencrypt/archive/stecherif.fr")

x= datetime.today().strftime('%Y-%m-%d')
#print(x)


for filename in files:
        file = "/etc/letsencrypt/archive/stecherif.fr/"+ filename
        y= time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(file)))
        y=y[-4:]+"-"+y[0:2]+"-"+y[3:5]
        if x == y:
                if filename[0] == "f":
                        #print(filename)
                        destination="/etc/ssl/certs/stecherif/fullchain1.pem"
                        shutil.copyfile(file, destination)
                if filename[0] == "p":
                        #print(filename)
                        destination="/etc/ssl/certs/stecherif/privkey1.pem"
                        shutil.copyfile(file, destination)

