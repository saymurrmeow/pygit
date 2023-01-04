import argparse

from . import data

def main():
    parser = argparse.ArgumentParser(
            epilog="not for production usage!!!"
            )
    
    commands = parser.add_subparsers(title='command', dest='command', required=True)

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=data.init)

    args = parser.parse_args()
    args.func(args)

