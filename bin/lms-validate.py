#!/usr/bin/env python3
from lxml import etree
import sys, os

script_path = os.path.dirname(os.path.realpath(sys.argv[0]))
share_path = os.path.join(script_path, os.path.pardir, "share", "xml", "lms")

# Check if a path was given as command line argument
if len(sys.argv) != 2:
    print("Usage: lms-validate <file_or_folder>")
    sys.exit(1)

path = sys.argv[1]
schema = etree.XMLSchema(etree.parse(os.path.join(share_path, 'framework.xsd')))
transform = etree.XSLT(etree.parse(os.path.join(share_path, 'preprocess.xsl')))

def process(file):
    if os.path.isdir(file):
        for child in os.listdir(file):
            process(os.path.join(file, child))
    elif file.lower().endswith(".xml"):
        validate_xml(file)
    elif file.lower().endswith(".lconf"):
        validate_lconf(file)

def validate_xml(file):
    parser = etree.XMLParser()
    try:
        doc = etree.parse(file, parser)
    except etree.XMLSyntaxError as e:
        print(file)
        for log in parser.error_log:
            print("{0} - {1}".format(log.line, log.message))
        return
    doc = transform(doc)
    schema.validate(doc)

    if len(schema.error_log) != 0:
        print(file)
        for log in schema.error_log:
            print("{0} - {1}".format(log.line, log.message))

def validate_lconf(file):
    error_log = []

    with open(file) as f:
        line_number = 0
        last_continue = False
        for line in f.readlines():
            line_number += 1
            line = line.rstrip()
            comment_line = line == "" or line.startswith("#")
            current_continue = line.endswith("\\")
            key_value = "=" in line

            if comment_line and last_continue:
                error_log.append({
                    "line" : line_number,
                    "message" : "Can not continue line with a comment."
                })
            if not key_value and not current_continue and not comment_line and not last_continue:
                error_log.append({
                    "line" : line_number,
                    "message" : "Non-comment line without meaning."
                })

            last_continue = current_continue

    if len(error_log) != 0:
        print(file)
        for log in error_log:
            print("{line} - {message}".format(**log))

process(path)
