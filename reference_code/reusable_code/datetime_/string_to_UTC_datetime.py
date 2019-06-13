from datetime import timezone

from dateutil.parser import parse as dateutil_parse


def string_to_utc_date_or_none(str_date):
    d = None
    try:
        d = dateutil_parse(str_date)
    except Exception:
        return None

    return datetime_to_utc_or_none(d)


def datetime_to_utc_or_none(_date):
    # for aware datetime-s
    try:
        return _date.astimezone(timezone.utc)
    except Exception:
        pass

    # for naive datetime-s
    try:
        return _date.replace(tzinfo=timezone.utc)
    except Exception:
        return None

if __name__ == '__main__':
    s1 = '2010-12-28T17:35:59.023Z'
    s2 = '2010-12-28T12:35:59.023-05:00'
    print(string_to_utc_date_or_none(s1))
    print(string_to_utc_date_or_none(s2))