import argparse
import xml.etree.cElementTree as ET
import xml.dom.minidom as minidom
import re
import sys
import signal


__version__ = "0.17"


def signal_handler(signal, frame):
    exit(0)


"""This stops ctrl+c from rendering typical Python stack trace and cleanly exits program."""
signal.signal(signal.SIGINT, signal_handler)


def version():
    return __version__


def main():

    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument(dest="input", action="store", nargs='*', help="output from 'ansible-lint -p' command.", type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument("-o", "--output", dest="output_file", default="ansible-lint-junit.xml", action="store", help="print XML to output file")
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="print XML to console as command output", default=False)
    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=version()))

    arguments = parser.parse_args()

    if isinstance(arguments.input, list):
        arguments.input = arguments.input[0]

    ansible_lint_output = arguments.input.read().split("\n")

    testsuites = ET.Element("testsuites")
    errors_count = "0"

    for line in ansible_lint_output:
        if len(line):
            errors_count = str(len(ansible_lint_output) - 1)
            break

    testsuite = ET.SubElement(testsuites, "testsuite", errors=errors_count, failures="0", tests=errors_count, time="0")

    line_regex = re.compile('^(.*?):(\\d+?):\\s(.*)$')

    if 0 == len(ansible_lint_output):
        ET.SubElement(testsuite, "testcase", name="dummy_testcase.py")
    else:
        parsed_lines = []
        for line in ansible_lint_output:
            if 0 < len(line):

                line_match = line_regex.match(line)

                line_data = {
                    "filename": line_match.group(1),
                    "line": int(line_match.group(2)),
                    "error": line_match.group(3),
                    "text": line_match.group(3),
                }
                parsed_lines.append(line_data)

                testcase = ET.SubElement(testsuite, "testcase", name="{}-{}".format(line_data['filename'], len(parsed_lines)))

                ET.SubElement(
                    testcase,
                    "failure",
                    file=line_data['filename'],
                    line=str(line_data['line']),
                    message=line_data['error'],
                    type="Ansible Lint"
                ).text = line_data['error']

    tree = ET.ElementTree(testsuites)

    xml_string = ET.tostring(testsuites, encoding='utf8', method='xml')
    xml_nice = minidom.parseString(xml_string)
    xml_nice = xml_nice.toprettyxml(indent="\t")

    text_file = open(arguments.output_file, "w")
    text_file.write(xml_nice)
    text_file.close()

    if arguments.verbose:
        print(xml_nice)

if __name__== "__main__" :
    main()
