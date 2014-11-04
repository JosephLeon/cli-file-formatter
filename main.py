from lxml import etree
import argparse


def prettyPrintXml(xmlFilePathToPrettyPrint):
    assert xmlFilePathToPrettyPrint is not None
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
    document = etree.parse(xmlFilePathToPrettyPrint, parser)
    document.write(xmlFilePathToPrettyPrint, pretty_print=True, encoding='utf-8')


def runFormatter(parsed_args):
    print 'File formatted was:', parsed_args
    prettyPrintXml(parsed_args)

parser = argparse.ArgumentParser()

parser.add_argument('--file', dest='file', action='store_const', const=runFormatter)
parser.add_argument('file_name')

parsed_args = parser.parse_args()
if parsed_args.file is None:
    parser.parse_args(['-h'])
parsed_args.file(parsed_args.file_name)
