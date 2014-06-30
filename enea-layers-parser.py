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
page = urllib2.urlopen('http://git.enea.com/git/')
soup = BeautifulSoup(page)
erepos = []
#print soup.body.find('tr', attrs={'class' : 'layertype_A'})
#http://git.enea.com/git/?p=linux/eclipse-poky-kepler.git;a=summary
for layers in soup.body.findAll('a', attrs={'class' : 'list'}):
    #text = layers.renderContents().strip()
    if "title" in layers.text:
        continue
    info = "git://git.enea.com/"
    strlen = len(layers['href'])
    info += layers['href'][8:strlen-10]
    erepos.append(info)

for repo in erepos:
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
