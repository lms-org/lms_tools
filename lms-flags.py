#!/usr/bin/env python3
import sys, os
from lxml import etree

if len(sys.argv) != 2:
    print("Usage: lms-flags <file_or_folder>")
    sys.exit(1)

ATTRIBUTES = ["set", "notSet", "anyOf", "allOf", "nothingOf"]

flags = set()

def process(file):
    """ Validate a file or recursively all files in a directory """
    if os.path.isdir(file):
        for child in os.listdir(file):
            process(os.path.join(file, child))
    elif file.lower().endswith(".xml"):
        process_xml(file)

def process_xml(path):
    xml = etree.parse(path)
    for tag in xml.xpath("//if"):
        for attr in ATTRIBUTES:
            if tag.attrib.has_key(attr):
                for flag in tag.attrib[attr].split(","):
                    flags.add(flag.strip())

process(sys.argv[1])

for flag in flags:
    print(flag)
