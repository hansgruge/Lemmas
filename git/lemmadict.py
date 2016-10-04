import gzip
import re

def read_data(file_to_read):
    d = {}
    with gzip.open(file_to_read, 'r') as rf:
        for i, line in enumerate(rf):
            if re.match('#', line) or len(line) <= 1:
                continue
            else:
                cols = line.split('\t')
                assert (len(cols) == 10), ('Wrong amount of columns, while reading file. ' + str(i) + ' line')
                if cols[3] == 'PUNCT':
                    continue
                #         Lemma     word      POS    Features
                #print i, cols[2], cols[1], cols[3], cols[5].split('|')
                feats = cols[5].split('|')
                for feat in feats:
                    if cols[3] not in d:
                        d[cols[3]] = {}
                    if cols[2] not in d[cols[3]]:
                        d[cols[3]][cols[2]] = {}
                    if feat not in d[cols[3]][cols[2]]:
                        d[cols[3]][cols[2]][feat] = 1
                    else:
                        d[cols[3]][cols[2]][feat] += 1
                    #else:
                    #    d[cols[3]] = dict(cols[2])
                    #if d[cols[3]][cols[2]] in d:
                    #    d[cols[3]][cols[2]] ='test'

                    # if d[cols[3]][cols[2]][feat] in d:
                    #     d[cols[3]][cols[2]][feat] += 1
                    # else:
                    #     d[cols[3]][cols[2]][feat] = 1


            if i > 200:
                break

    return d

def main():
    dd = read_data('../../versions/parsebank_v4_UD_scrambled.conllu-part-aa.gz')
    print dd.items()


if __name__ == '__main__':
    main()
