from datetime import datetime, timezone, timedelta
d = datetime.utcnow()
# without timezone.utc, timestamp assumes local time
d_seconds = d.replace(tzinfo=timezone.utc).timestamp()
d2 = datetime(1970,1,1, tzinfo=timezone.utc) + timedelta(seconds=d_seconds)
print('utc now:\n', d)
print('utc now -> seconds -> datetime:\n', d2)