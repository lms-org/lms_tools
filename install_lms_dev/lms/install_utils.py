#!/usr/bin/env python3
#parse xml file
import xml.etree.ElementTree
import json
import sys, os
from subprocess import call


def parseFrameworkXml(configFilePath):
    root = xml.etree.ElementTree.parse(configFilePath).getroot()
    usedPackages = set()
    for xmlUsedMods in root.findall('module'):
        usedPackages.add(xmlUsedMods.find('package').text)
    return usedPackages


def parsePackageList(packageFilePath):
    with open(packageFilePath) as file:
        return json.load(file)

def getPackageLists():
    result = set()
    result.add('packagelist.json') # TODO hier später alle möglichen ausführen
    return result

def getPackageUrlFromName(packageName):
    for packageListPath in getPackageLists():
        packagesData = parsePackageList(packageListPath)
        if packageName in packagesData:
            return packagesData[packageName]['path']

def getNeededPackageUrls(neededPackages,packagesData):
#TODO später kann man selbst orte festlegen an denen packagelisten sind und somit seine lokalen versionen bevorzugen -> mehrere paketlisten
    result = dict()
    for packageName in neededPackages:
        if packageName in packagesData:
            result[packageName] = packagesData[packageName]['path']
#TODO noch überprüfen ob ein package keine url hat!
    return result

def isGitUrl(url):
    return True #TODO

def isLocalFolder(url):
    return False #TODO

def isZipFile(url):
    return False #TODO

def installPackage(packageName,packageUrl):
    if isGitUrl(packageUrl):
        #TODO check if folder already exists
        ret = call(["git","clone",packageUrl, 'dependencies/'+packageName])
        if ret != 0:
            print("clone failed")
            sys.exit(1)
        print("cloned package")
    if isLocalFolder :
        #TODO create hardlink
    else :
        print("no valid url-type given")
        sys.exit(1)
        

