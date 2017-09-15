
def format_time(seconds):
    minute = 60
    hour = minute * 60
    if seconds < minute:
        return '{} sec.'.format(int(seconds))

    if seconds < hour:
        _m = int(seconds / minute)
        _s = int(seconds % minute)
        return '{} min. {} sec.'.format(_m, _s)

    _h = int(seconds / hour)
    seconds = seconds % hour
    _m = int(seconds / minute)
    _s = int(seconds % minute)
    return '{} h. {} min. {} sec.'.format(_h, _m, _s)


for seconds in [10, 120, 3612]:
    print(format_time(seconds))
