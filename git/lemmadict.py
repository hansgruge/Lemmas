import gzip
import re
import csv


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
                #print cols[2]
                #split features to pieces
                for feat in feats:
                    #POS to dict and create inner dictionary for lemmas if POS doesn't exist
                    if cols[3] not in d:
                        d[cols[3]] = {}
                    #Lemmas to dict if doesn't exist create new dictionary for features
                    if cols[2] not in d[cols[3]]:
                        d[cols[3]][cols[2]] = {}
                    #Features to correct POS/lemma 1st key: value pair set value 1 else add 1 more to current lemma
                    if feat not in d[cols[3]][cols[2]]:
                        d[cols[3]][cols[2]][feat] = 1
                    else:
                        d[cols[3]][cols[2]][feat] += 1


            #with this you can limit how many rows it reads. Just for testing purposes.
            #if i > 200:
            #    break

    return d


def write_to_csv(dict_to_write):
    with open('output1.csv', 'wb') as csv_file:
        #writer = csv.writer(csv_file)
        for key, value in dict_to_write.items():
            csv_file.write(key + '\n')
            temp = ''
            for k, v in value.items():
                temp = (k)

                for kk, vv in v.items():
                    #print kk, vv
                    if temp == '':
                        temp = temp + str(kk) + ':' + str(vv)
                    else:
                        temp = temp + ', ' + str(kk) + ':' + str(vv)
                #print temp
                temp = temp + '\n'
                csv_file.write(temp)

def main():
    print 'start to read'
    dd = read_data('../../versions/parsebank_v4_UD_scrambled.conllu.gz')
    print 'start to write'
    write_to_csv(dd)
    print 'done'

if __name__ == '__main__':
    main()
