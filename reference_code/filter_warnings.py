from warnings import warn
import warnings


def test_filter_by_message():
    # "message" is a string containing a regular expression that the start of
    # the warning message must match. The expression is compiled
    # to always be case-insensitive.
    warnings.filterwarnings(action='ignore',
                            message='xxx')
    warn('xxx ONE')
    warn('TWO (X)')
    warn('xxx THREE')


def test_filter_by_message_in_context_manager():
    with warnings.catch_warnings():
        # this will not be reflected in the global warnings filter list
        warnings.filterwarnings(action='ignore',
                                message='yyy')
        warn('xxx IGNORED')
        warn('yyy ONE')
        warn('TWO (Y)')
        warn('yyy THREE')


class BananaWarning(Warning):
    pass


def test_filter_by_category():
    with warnings.catch_warnings():
        warnings.filterwarnings(action='ignore',
                                category=BananaWarning)
        warn('BananaWarning ONE', BananaWarning)
        warn('UserWarning TWO')  # UserWarning is the default category


def test():
    test_filter_by_message()
    warn('xxx FOUR')  # this is also ignored because the warnings filter list
    # is altered in test_filter_by_message()
    test_filter_by_message_in_context_manager()
    warn('yyy FOUR (not ignored, used context manager for yyy warnings)')
    test_filter_by_category()

if __name__ == '__main__':
    test()
