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
                print line.decode('utf-8')
            if i > 20:
                break

    return d

def main():
    read_data('../../versions/parsebank_v4_UD_scrambled.conllu-part-aa.gz')


if __name__ == '__main__':
    main()
