from optparse import OptionParser
import pprint
import xml.etree.cElementTree as ET
import re


__version__ = "0.9"


def version():
    return __version__


def main():

    pp = pprint.PrettyPrinter(indent=2)

    junit_xml_output = "ansible-lint-junit.xml"

    parser = OptionParser(
        usage="%prog [ansible-lint output file] [options]",
        version="%prog " + version()
    )

    parser.add_option("-o", "--output", action="store", dest="output_file", help="output XML to file", default=junit_xml_output)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="print XML to console as command output", default=False)
    # parser.add_option(""--version", dest="verbose", help="print XML to console as command output", default=False)

    (options, args) = parser.parse_args()

    if len(args) == 0 or not args[0]:
        parser.print_help()
        parser.error('You need to provide file with output from "ansible-lint -p" command.')
        exit(1)

    ansible_lint_output = open(args[0], "r").read().split("\n")

    testsuites = ET.Element("testsuites")

    errors_count = str(len(ansible_lint_output))

    testsuite = ET.SubElement(testsuites, "testsuite", errors=errors_count, failures="0", tests=errors_count, time="0")

    line_regex = re.compile('^(.*?):(\d+?):\s\[(.*)\]\s(.*)$')

    if 0 == len(ansible_lint_output):
        testcase = ET.SubElement(testsuite, "testcase", name="dummy_testcase.py")
    else:
        parsed_lines = []
        for line in ansible_lint_output:
            if 0 < len(line):
                # print line

                line_match = line_regex.match(line)

                line_data = {
                    "filename": line_match.group(1),
                    "line": int(line_match.group(2)),
                    "error": {
                        "code": line_match.group(3),
                        "message": line_match.group(4),
                        "text": "[" + line_match.group(3) + "] " + line_match.group(4)
                    }
                }
                parsed_lines.append(line_data)
                testcase = ET.SubElement(testsuite, "testcase", name=line_data['filename'])
                ET.SubElement(
                    testcase,
                    "failure",
                    file=line_data['filename'],
                    line=str(line_data['line']),
                    message=line_data['error']['text'],
                    type="Ansible Lint"
                ).text = line_data['error']['text']

    tree = ET.ElementTree(testsuites)
    tree.write(options.output_file, encoding='utf8', method='xml')
    parsed_lines_xml = ET.tostring(testsuites, encoding='utf8', method='xml')

    if options.verbose:
        print parsed_lines_xml
