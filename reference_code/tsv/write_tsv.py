
import csv
import os


def append_to_file(file_name, field_names, dicts_to_write):
    file_exists = os.path.exists(file_name)
    with open(file_name, 'a', newline='') as tsv_file:
        writer = csv.DictWriter(tsv_file, fieldnames=field_names,
                                extrasaction='ignore', delimiter='\t')
        if not file_exists:
            writer.writeheader()

        for item in dicts_to_write:
            writer.writerow(item)


def test_append():
    file_name = 'orcs.tsv'
    field_names = ['name', 'kills', 'clan']
    orcs = [
        {'clan': 'Black wolfs', 'name': 'Mogka'},
        {'clan': 'Red orcs', 'name': 'Kone', 'kills': 10}
    ]
    append_to_file(
        file_name=file_name, field_names=field_names, dicts_to_write=orcs)

if __name__ == '__main__':
    test_append()
    print('Done')
