import sys
import argparse
import logging

import optirt as ort

logger = logging.getLogger(__name__)


def main(args=sys.argv[1:]):
    """ The main function for ???
    """

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity', action='count', help="increase output verbosity", default=0)
    parser.add_argument('-V', '--version', action='version', version=ort.__version__)
    args = parser.parse_args(args)

    if args.verbosity == 1:
        logging.basicConfig(level=logging.INFO)
    if args.verbosity > 1:
        logging.basicConfig(level=logging.DEBUG)

    print("Hello world")
    return 0


if __name__ == '__main__':
    logging.basicConfig()
    sys.exit(main(sys.argv[1:]))
