import json
import time
from dateutil.parser import parse as dateutil_parse
from datetime import datetime, timedelta, timezone
import warnings

import feedparser


def json_print(d):
    print(json.dumps(d, indent=2))


def str_to_date(s):
    if not s:
        return None

    try:
        return dateutil_parse(s)
    except Exception as ex:
        warnings.warn('Failed to parse %s: %s' % (s, ex))

    return None


def struct_time_to_datetime(time_struct):
    return str(time_struct)  # TODO
    if not isinstance(time_struct, time.struct_time):
        return None

    try:
        return datetime.fromtimestamp(time.mktime(time_struct))
    except Exception as ex:
        print('WARNING: failed to parse %s:\n%s' % (time_struct, ex))


def accessing_common_rss_elements():
    url = 'https://www.us-cert.gov/ncas/alerts.xml'
    d = feedparser.parse(url)
    feed = d.get('feed', {})
    # json_print(feed)
    lines = [
        'feed ----------',
        'title %s' % feed.get('title'),
        'link %s' % feed.get('link'),
        'description %s' % feed.get('description'),
        'published %s' % feed.get('published'),
        'published as date %s' % str_to_date(feed.get('published')),
    ]
    print('\n'.join(lines))
    items = d.get('entries', [])
    print('Items found %s' % (len(items)))
    for item in items:
        lines = [
            '\n\n - - - item (rss) - - -',
            'title %s' % item.get('title'),
            'link %s' % item.get('link'),
            'description %s' % item.get('description'),
            'published %s' % item.get('published'),
            # item.get('published_parsed')
            'published as date %s' % str_to_date(item.get('published')),
            'id %s' % item.get('id')
        ]
        print('\n'.join(lines))
    
    print('version', d.version)

def accessing_common_atom_elements():
    """
    NOTES:
    - summary and content (dict) are the same as description
    - published/updated can miss
    """
    url = 'https://www.reddit.com/r/python/.rss'
    d = feedparser.parse(url)
    feed = d.get('feed', {})
    # json_print(feed)
    lines = [
        'feed ---------------',
        'title %s' % feed.get('title'),
        'link %s' % feed.get('link'),
        'subtitle %s' % feed.get('description'), # same as feed.get('subtitle'),
        'updated %s' % feed.get('updated'),
        # feed.get('updated_parsed')
        'updated as date %s' % str_to_date(feed.get('updated')),
    ]
    print('\n'.join(lines))
    items = d.get('entries', [])
    print('Items found %s' % (len(items)))
    for item in items:
        lines = [
            '\n\n - - - item (atom) - - -',
            'title %s' % item.get('title'),
            'link %s' % item.get('link'),
            'description %s' % item.get('description'),
            'published %s' % item.get('published'),
            'published as date %s' % str_to_date(item.get('published')),
            'updated %s' % item.get('updated'),
            'updated as date %s' % str_to_date(item.get('updated')),
            # same as description (when not provided?)
            #'summary %s' % item.get('summary'),
            # same as description (when not provided?) 
            #'content %s' % item.get('content'),
            'id %s' % item.get('id')
        ]
        print('\n'.join(lines))

    print('version', d.version)


def run():
    #accessing_common_atom_elements()
    # accessing_common_rss_elements()
    
    # CAN NOT FILTER BY DATE, THE BELOW DOES *NOT* WORK
    url = 'https://www.us-cert.gov/ncas/alerts.xml'
    _date = datetime.utcnow() - timedelta(days=70)
    _date = _date.replace(tzinfo=timezone.utc) # make it timezone aware
    d = feedparser.parse(url)#, modified=_date)
    items = d.get('entries') or []
    print('entities', len(items))
    print('version', d.version)
    print('status', d.status)


if __name__ == '__main__':
    run()
