from pathlib import Path
import os
import urllib.request
import zipfile


def assure_user_dir(dirname):
    home = str(Path.home())
    dir = os.path.join(home, dirname)
    if not os.path.exists(dir):
        print('Created directory %s' % (dir))
        os.makedirs(dir)

    return dir


def download_file(url, destination_dir, overwrite_existing=False):
    """Download a file from url to specified directory.
    url - url to file
    destination_dir - where to store the downloaded file
    overwrite_existing - if True and the file exists it will be overwritten 
    """
    if (destination_dir is None or
            not os.path.exists(destination_dir) or
            not os.path.isdir(destination_dir)):
        raise ValueError('%s must be existing directory' % destination_dir)

    file_name = url.split('/')[-1]
    file_name = os.path.join(destination_dir, file_name)

    if os.path.exists(file_name) and not overwrite_existing:
        print('%s already exists' % file_name)
        return file_name

    request = urllib.request.Request(
        url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    meta = response.info()
#     print('Response info:')
#     print(meta)
    file_size = int(meta['Content-Length'])
    fmt_file_size = format_file_size(file_size)
    downloaded = 0
    block_size = 8192
    out_file = open(file_name, 'wb')

    print('Downloading {0} {1}'.format(
        file_name, fmt_file_size))
    step_milestone = 7
    next_milestone = step_milestone
    try:
        while True:
            data = response.read(block_size)
            if not data:
                break

            out_file.write(data)
            downloaded += len(data)
            percent = downloaded * 100. / file_size
            if percent >= next_milestone:
                print('Downloaded {0} from {1} [{2:6.2f} %]'.format(
                    format_file_size(downloaded), fmt_file_size, percent))
                next_milestone += step_milestone
    finally:
        response.close()
        out_file.close()

    return file_name


def format_file_size(size):
    KB = 1024
    MB = KB * 1024
    GB = MB * 1024

    if size < KB:
        res = '{0:d} bytes'.format(size)
    elif size < MB:
        size = size / KB
        res = '{0:.2f} KB'.format(size)
    elif size < GB:
        size = size / MB
        res = '{0:.2f} MB'.format(size)
    else:
        size = size / GB
        res = '{0:.2f} GB'.format(size)

    return res

def extract_zip(file_name, destination_dir):
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(destination_dir)


dir = assure_user_dir('download_zip_test')
url = ('http://dev.maxmind.com/wp-content/uploads/2015/07/'
       'GeoIP2-Enterprise-CSV_Example.zip')
file_name = download_file(url, dir, overwrite_existing=False)
extract_zip(file_name, dir)
print('Data extracted successfully to %s' % dir)
