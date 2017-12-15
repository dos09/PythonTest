import os
import shutil
from datetime import datetime


def merge_files(files_to_merge, res_file):
    """ Merge all files from <files_to_merge> to <res_file> """

    with open(res_file, 'ab') as f_out:
        for file_to_merge in files_to_merge:
            with open(file_to_merge, 'rb') as f_in:
                shutil.copyfileobj(f_in, f_out)


def merge_files_in_dir(from_dir, to_dir, max_file_size=None,
                       res_files_extension=None):
    """ Merge all files from <from_dir>, the result files will be in <to_dir>.
    Each result file, created from merging files will have 
    size <= <max_file_size>. If file from <from_dir> is larger 
    than <max_file_size>, the result file
    will be the same, only the name will be different.
    Parameters:
    - max_file_size, defaults to 1 GB
    - res_files_extension, defaults to no extension
    Return:
    - error message on failure or None
    """

    if not os.path.isdir(from_dir):
        return '%s is not directory' % from_dir

    if not os.path.exists(to_dir):
        os.makedirs(to_dir)

    if not os.path.isdir(to_dir):
        return '%s is not directory' % to_dir

    if not max_file_size:
        max_file_size = 1024 * 1024 * 1024  # 1 GB

    assert isinstance(max_file_size, int)
    res_files_extension = ('.%s' % res_files_extension.lstrip('.')
                           if res_files_extension is not None
                           else '')
    files = []
    for file_name in os.listdir(from_dir):
        file_name = os.path.join(from_dir, file_name)
        files.append((file_name, os.path.getsize(file_name)))

    files.sort(key=lambda x: x[1])
    curr_file_size = 0
    files_to_merge = []
    for file_name, file_size in files:
        if curr_file_size >= max_file_size:
            res_file = '%s%s' % (datetime.utcnow().timestamp(),
                                 res_files_extension)
            res_file = os.path.join(to_dir, res_file)
            merge_files(files_to_merge, res_file)
            curr_file_size = 0
            files_to_merge = []

        curr_file_size += file_size
        files_to_merge.append(file_name)

    if files_to_merge:
        res_file = '%s%s' % (datetime.utcnow().timestamp(),
                             res_files_extension)
        res_file = os.path.join(to_dir, res_file)
        merge_files(files_to_merge, res_file)


def test():
    from_dir = r'C:\Users\julien\eclipse_mars_workspaces\confidential\JustForTest\tests\file_merge_per_size\in_files'
    to_dir = r'C:\Users\julien\eclipse_mars_workspaces\confidential\JustForTest\tests\file_merge_per_size\out_files'
    max_file_size = 1024 * 250  # 250KB
    merge_files_in_dir(from_dir, to_dir, max_file_size=max_file_size)

#test()
