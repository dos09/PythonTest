import csv

# with open("a.tsv") as tsv:
#     for line in csv.reader(tsv, delimiter='\t'):
#         print(line)

def load_tsv_data(filename):
    tsv_data = []

    with open(filename) as tsv:
        for row in csv.DictReader(tsv, delimiter='\t'):
            row["Linked CVE's"] = [
                cve[4:] for cve in row["Linked CVE's"].split(',')
            ]
            tsv_data.append(row)
    
    return tsv_data

data = load_tsv_data('a.tsv')
print(data)