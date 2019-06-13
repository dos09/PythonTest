from datetime import timedelta

from dateutil import parser


def parse_to_utc(str_date):
    """
    example:
        "2019-06-13T03:05:42-04:00" (str) -> 
        2019-06-12 23:05:42 (datetime)
    """
    date_ = parser.parse(str_date)
    tz_info = date_.tzinfo
    if not tz_info:
        return date_

    tz_offset = tz_info.utcoffset(None)  # timedelta
    if not tz_offset:
        return date_

    # can be negative
    utc_seconds_offset = int(tz_offset.total_seconds())
    date_ = date_.replace(tzinfo=None)
    return date_ + timedelta(seconds=utc_seconds_offset)


def t():
    s = '2019-06-13T03:05:42-04:00'
    print(s, type(s))
    d = parse_to_utc(s)
    print(d, type(d), d.tzinfo)


if __name__ == '__main__':
    t()
