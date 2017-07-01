import os
from datetime import datetime
import time

def read_file_lines(filename):
    if not os.path.exists(filename):
        print("%s doesn't exist")
        return
    if not os.path.isfile(filename):
        print('%s is not a file')
        return
        
    with open(filename, 'r') as file:
        print('read line by line (using strip()):')
        for line in file:
            print("'%s'" % line.strip())
        print('current position: %s' % file.tell())
        file.seek(0,2) # offset, from (0-beginning, 1-current position, 2-end)
        print('position at the end: %s' % file.tell())
        file.seek(0,0) 
        print('position at the beginning: %s' % file.tell())

def read_file_all(filename):
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename, 'r') as f:
            print(f.read())
        
def read_file_in_list(filename):
    lines = []
    
    if os.path.exists(filename) and os.path.isfile(filename):    
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line.strip())
    else:
        print("can't read from %s" % filename)
        
    return lines

def append_line_to_file(filename, some_text):
    with open(filename, 'a') as file:
        file.write(some_text + '\n')

def test_file_read_append():
    filename = 'file.asd'
    lines = read_file_in_list(filename)
    print('lines read: %s' % len(lines))
    print(lines)
    append_line_to_file(filename, 'line added ({0})'.format(str(datetime.now())))
    lines = read_file_in_list(filename)
    print('lines read: %s' % len(lines))
    print(lines)

def list_files_in_dir(dirname):
    if os.path.exists(dirname) and os.path.isdir(dirname):
        for filename in os.listdir(dirname):
            print("%s -> %s" % (filename, os.path.abspath(filename)))
    else:
        print("can't read from directory: %s" % dirname)

def list_txt_files_in_dir(dirname):
    if os.path.exists(dirname) and os.path.isdir(dirname):
        for filename in os.listdir(dirname):
            rel_filename = os.path.join(dirname, filename)
            print('%s is file: %s' % (rel_filename, os.path.isfile(rel_filename)))
            if os.path.isfile(rel_filename) and rel_filename.endswith(".txt"):
                print("    %s is txt file" % (rel_filename))
    else:
        print("can't read from directory: %s" % dirname)

def test_move_files():
    scanned = os.path.abspath('scanned')
    scan_dir = os.path.abspath('scan_dir')
    
    print('scanned', scanned)
    print('scan_dir', scan_dir)
    
    if not os.path.exists(scanned):
        os.makedirs(scanned)
        
    if os.path.exists(scan_dir) and os.path.isdir(scan_dir):
        for filename in os.listdir(scan_dir):
            abs_filename = os.path.join(scan_dir, filename)
            if os.path.isfile(abs_filename) and abs_filename.endswith(".txt"):
                print("processed %s" % (abs_filename))
                timestamp = round(time.time() * 1000)
                new_filename  = os.path.join(scanned, str(timestamp) + '_' + filename)
                os.rename(abs_filename, new_filename)

# filename = 'file.asd'
# dirname = 'mydir'
# # list_txt_files_in_dir(dirname)
# 
# print(filename)
# abs_filename = os.path.abspath(filename)
# print(abs_filename)
# print(os.path.basename(abs_filename))

# test_move_files()

