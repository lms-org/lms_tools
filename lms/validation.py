import pkg_resources, os
from lxml import etree

SCHEMA = etree.XMLSchema(etree.parse(
    pkg_resources.resource_stream(__name__, 'data/framework.xsd')))
TRANSFORM = etree.XSLT(etree.parse(
    pkg_resources.resource_stream(__name__, 'data/preprocess.xsl')))

def validate(file):
    """ Validate a file or recursively all files in a directory """
    if os.path.isdir(file):
        for child in os.listdir(file):
            validate(os.path.join(file, child))
    elif file.lower().endswith(".xml"):
        validate_xml(file)
    elif file.lower().endswith(".lconf"):
        validate_lconf(file)

def validate_xml(file):
    """ Validate an XML with the help of the schema file """
    parser = etree.XMLParser()
    try:
        doc = etree.parse(file, parser)
    except etree.XMLSyntaxError as e:
        print(file)
        for log in parser.error_log:
            print("{0} - {1}".format(log.line, log.message))
        return
    doc = TRANSFORM(doc)
    SCHEMA.validate(doc)

    if len(SCHEMA.error_log) != 0:
        print(file)
        for log in schema.error_log:
            print("{0} - {1}".format(log.line, log.message))

def validate_lconf(file):
    """ Find common mistakes in a LCONF file """
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
