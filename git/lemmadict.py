import gzip
import re

def read_data(file_to_read):
    d = {}
    with gzip.open(file_to_read, 'r') as rf:
        for i, line in enumerate(rf):
            if re.match('#', line):
                continue
            elif len(line) <= 1:
                continue
            else:
                cols = line.split('\t')
                assert (len(cols) == 10), ('Wrong amount of columns, while reading file. ' + str(i) + ' line')
                if cols[3] == 'PUNCT':
                    continue
                print i, cols[2], cols[1], cols[3],cols[5].split('|')
            if i > 20:
                break

    return d

def main():
    read_data('../../versions/parsebank_v4_UD_scrambled.conllu-part-aa.gz')


if __name__ == '__main__':
    main()
