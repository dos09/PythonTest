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

def all_actions():
    parser = argparse.ArgumentParser()
    # parser.add_argument('-b', '--banana')
    args = parser.parse_args()
    print('NOT READY')

if __name__ == '__main__':
    all_actions()
    """
    TODO: the other actions
    self.register('action', None, _StoreAction)
    self.register('action', 'store', _StoreAction)
    self.register('action', 'store_const', _StoreConstAction)
    self.register('action', 'store_true', _StoreTrueAction)
    self.register('action', 'store_false', _StoreFalseAction)
    self.register('action', 'append', _AppendAction)
    self.register('action', 'append_const', _AppendConstAction)
    self.register('action', 'count', _CountAction)
    self.register('action', 'help', _HelpAction)
    self.register('action', 'version', _VersionAction)
    self.register('action', 'parsers', _SubParsersAction)
    """
