from lxml import etree
import argparse

parser = argparse.ArgumentParser(description='Format xml.')
parser.add_argument(
    'formatit',
    metavar='F',
    # type=string,
    help='Formats and xml file.'
)
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.formatit)


def prettyPrintXml(xmlFilePathToPrettyPrint):
    assert xmlFilePathToPrettyPrint is not None
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
    document = etree.parse(xmlFilePathToPrettyPrint, parser)
    document.write(xmlFilePathToPrettyPrint, pretty_print=True, encoding='utf-8')

# prettyPrintXml('large-clean-feed.xml')
prettyPrintXml('test.xml')
