from lxml import etree
import argparse

# parser = argparse.ArgumentParser(
#     description='Process and format files.',
#     prog='Python cli',
#     usage='Python cli for formatting files, might integrate kivy too.'
# )
# parser.add_argument(
#     'filename',
#     dest='format',
# )
# parser.add_argument(
#     'formatter',
#     dest='format',
# )
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

# args = parser.parse_args()
# # print args.format(args.filename)
# print args.accumulate(args.integers)

def foo(parsed_args):
    print "woop is {0!r}".format(getattr(parsed_args, 'woop'))


def bar(parsed_args):
    print "moop is {0!r}".format(getattr(parsed_args, 'moop'))


def printStuff(parsed_args):
    print 'Worked'

parser = argparse.ArgumentParser()

parser.add_argument('--foo', dest='action', action='store_const', const=foo)
parser.add_argument('--bar', dest='action', action='store_const', const=bar)
parser.add_argument('--cat', dest='action', action='store_const', const=printStuff)
parser.add_argument('--woop')
parser.add_argument('--moop')

parsed_args = parser.parse_args()
if parsed_args.action is None:
    parser.parse_args(['-h'])
parsed_args.action(parsed_args)


def printStuff():
    print 'Worked'


def prettyPrintXml(xmlFilePathToPrettyPrint):
    assert xmlFilePathToPrettyPrint is not None
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
    document = etree.parse(xmlFilePathToPrettyPrint, parser)
    document.write(xmlFilePathToPrettyPrint, pretty_print=True, encoding='utf-8')

# prettyPrintXml('large-clean-feed.xml')
prettyPrintXml('test.xml')
