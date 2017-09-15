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

for bytes in (10, 1202, 123444, 100200300):
    print(format_file_size(bytes))