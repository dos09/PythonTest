import argparse


def positional_arg():
    parser = argparse.ArgumentParser()
    # positional and required
    parser.add_argument('num',
                        help='enter number', type=int)
    args = parser.parse_args()
    print(args.num + 100)


def optional_arg():
    parser = argparse.ArgumentParser()
    # optional flag (True or False)
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increases logging')
    parser.add_argument('--banana', action='store_true')
    parser.add_argument('--no-banana', action='store_false')
    parser.add_argument('--orc', choices=['yes', 'no', 'true', 'false'])
    args = parser.parse_args()
    lines = [
        'verbose %s' % args.verbose,
        'banana %s' % args.banana,
        'no banana %s' % args.no_banana,
        'orc %s' % args.orc
    ]
    print('\n'.join(lines))


def optional_verbosity():
    parser = argparse.ArgumentParser()
    # counts the occurrence of the verbose option
    # >> run --verbose --verbose --verbose
    # >> run -vvv
    parser.add_argument('-v', '--verbose', action='count', default=0)
    args = parser.parse_args()

    if args.verbose >= 2:
        print('Running %s' % __file__)

    if args.verbose >= 1:
        print('verbose = ', end='')

    print(args.verbose)


def optional_mutually_exclusive():
    parser = argparse.ArgumentParser(
        description='Test mutually exclusive options')
    # pass required=True to make option from the group required
    group = parser.add_mutually_exclusive_group()
    # when action is store_true the arg has True only if it's passed
    # when action is store_false the arg has False only if it's passed
    group.add_argument('--banana', action='store_true')  # True if passed
    group.add_argument('--no-banana', action='store_false')  # False if passed
    args = parser.parse_args()
    lines = [
        '--banana %s' % args.banana,
        '--no-banana %s' % args.no_banana
    ]
    print('\n'.join(lines))


def parent_parser():
    # add_help=False to avoid conflict with the -h, --help options of the
    # parsers
    clan_parser = argparse.ArgumentParser(add_help=False)
    clan_parser.add_argument('--clan')

    orc_parser = argparse.ArgumentParser(parents=[clan_parser, ])
    orc_parser.add_argument('name')
    args = orc_parser.parse_args()
    print(args)


def sub_commands():
    def orc(args):
        print('Orc name: %s' % args.orc_name)

    def troll(args):
        print('Troll name: %s' % args.troll_name)

    parser = argparse.ArgumentParser()
    parser.add_argument('--clan', required=True, help='(required)')

    sub_parsers = parser.add_subparsers(title='sub commands')

    orc_parser = sub_parsers.add_parser('orc', aliases=['o'])
    orc_parser.add_argument('orc_name')
    orc_parser.set_defaults(func=orc)

    troll_parser = sub_parsers.add_parser('troll', aliases=['t'])
    troll_parser.add_argument('troll_name')
    troll_parser.set_defaults(func=troll)

    print('Using test args for parsing')
    args = parser.parse_args('--clan Mofos orc Mogka'.split())
    #args = parser.parse_args()
    print('args:', args)
    args.func(args)

def grouping_in_help():
    parser = argparse.ArgumentParser()
    
    group_required = parser.add_argument_group(title='required arguments')
    group_required.add_argument('fraction')
    group_required.add_argument('--race', required=True)
    group_required.add_argument('--name', required=True)
    
    parser.add_argument('--clan')
    
    args = parser.parse_args()
    print(args)

def add_attributes_to_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('a')
    parser.set_defaults(b='bear')
    parser.set_defaults(c='crocodile')
    args = parser.parse_args(['ape'])
    print(args)

if __name__ == '__main__':
    add_attributes_to_parser()
