
import skip_limit
import find_limit
import sort_file_lines
import cmp_files

def run():
    skip_limit_data = skip_limit.run()
    find_limit_data = find_limit.run()
    sorted_skip_limit_data = sort_file_lines.sort_file(skip_limit_data)
    sorted_find_limit_data = sort_file_lines.sort_file(find_limit_data)
    equal = cmp_files.cmp_files(sorted_skip_limit_data, sorted_find_limit_data)
    print('FAIL' if not equal else 'OK')

if __name__ == '__main__':
    run()