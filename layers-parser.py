#!/usr/bin/python

import commands
import subprocess
import os
import sys
import urllib2
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

sFileName = "info-log"
f = open('output/{0}.log'.format(sFileName),'w')
#OpenEmbedded Layers Index
#layer_types = ['layertype_A', 'layertype_B', 'layertype_D', 'layertype_M', 'layertype_S']
page = urllib2.urlopen('http://layers.openembedded.org/layerindex/branch/master/layers/')
soup = BeautifulSoup(page)
orepos = []
#print soup.body.find('tr', attrs={'class' : 'layertype_A'})
for layers in soup.body.findAll('td', attrs={'class' : 'showRollie'}):
    info = layers.getText().split()
    orepos.append(info[0])

#YoctoProject Layers Index
page = urllib2.urlopen('https://git.yoctoproject.org/')
soup = BeautifulSoup(page)
yrepos = []
check = False
for layers in soup.body.findAll('td', attrs={'class' : 'sublevel-repo'}):
    text = layers.renderContents().strip()
    if "experimental/meta-m2" in text:
        check = True
    if check:
        info = "https://git.yoctoproject.org"
        info += layers.a['href']
        yrepos.append(info)

for repo in orepos:
    print repo

#repos = orepos + [i for i in yrepos if i not in orepos]
#for repo in repos:
#    print repo
#command = "/usr/bin/git clone "
#dirName = '/home/alex/workspace/alvd-linux/test/'
#for repo in repos:
#    command += repo
#    print command
#    pr = subprocess.Popen(command , cwd = os.path.dirname(dirName), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
#    (out, error) = pr.communicate()
#    f.write("Error : " + str(error))
#    f.write("out : " + str(out))
f.close()
