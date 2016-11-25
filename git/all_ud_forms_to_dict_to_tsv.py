#!/usr/bin/env python3
# coding=utf-8
import gzip
import sys
import csv
import pickle

<<<<<<< HEAD


#print current time
def print_time():
    import time
    localtime = time.asctime(time.localtime(time.time()))
    return localtime

# Read desired pickle to memory
# Give filename
def read_pickle(fname):
    with open(fname, 'rb') as f:
        d = pickle.load(f)
    print('Pickle read finished ' + print_time())
=======
# Read desired pickle to memory
# Give filename

def read_pickle(fname):
    with open(fname, 'rb') as f:
        d = pickle.load(f)
>>>>>>> 19c97b4488fdfade0b1ab85663ca7e7ec864fc84
    return d

#Read omorphi UD forms in dict

def read_UD_word_forms_to_dict(fname):
    dd = {}
    FORM, LEMMA, UPOS, FEAT = range(4)
    with open(fname) as wf:
        for line in wf:
            line = line.rstrip()
            if not line:
                continue
            cols = line.split('\t')
            assert len(cols) == 4
            temp = (cols[FORM], cols[LEMMA], cols[UPOS], cols[FEAT])
            dd[temp] = dd.get(temp, 0)
<<<<<<< HEAD
    print('UD read finished ' + print_time())
=======
>>>>>>> 19c97b4488fdfade0b1ab85663ca7e7ec864fc84
    return dd

def print_out_x_lines_from_dict(dname, lines):
    tt = 0
    for i in dname.items():
        print(i)
        if tt < lines:
            tt += 1
        else:
            break

def count_UD_forms(dpickled, dforms):
    dLemma = {}
    for pos, dict1 in dpickled.items():
        for lemma, dict2 in dict1.items():
            for key3, pcs in dict2.items():
                form, feat = key3
                temp = (form, lemma, pos, feat)
                dforms[temp] = dforms.get(temp, 0) + pcs
                dLemma[lemma] = dLemma.get(lemma, 0) + pcs
<<<<<<< HEAD
    print('Counting Finished. ' + print_time())
=======
>>>>>>> 19c97b4488fdfade0b1ab85663ca7e7ec864fc84
    return dLemma, dforms

def write_to_tsv(dname, fname):
    filename = str(fname) + ".tsv.gz"
    with gzip.open(filename, 'wb') as tsv_file:
        for lemma, pcs in dname.items():
            if type(lemma) is tuple:
                lemm, form, pos, feat = lemma
                temp = lemm + '\t' + form + '\t' + pos + '\t' + feat + '\t' + str(pcs) + '\n'
            else:
                temp = lemma + '\t' + str(pcs) + '\n'
            tsv_file.write(temp.encode('utf-8'))
<<<<<<< HEAD
    print('Done writing dictionary to file. ' + print_time())


def main():

    print('Starting to read input: ' + print_time())
    dP = {}
    dUD = {}
    d = {}

    ID, FORM, LEMMA, UPOS, XPOS, FEAT, HEAD, DEPREL, DEPS, MISC = range(10)

    for line in sys.stdin:
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        assert len(cols) == 10
        word_dict = d.setdefault(cols[UPOS], {}).setdefault(cols[LEMMA], {})
        lemma_reading = (cols[FORM], cols[FEAT])
        word_dict[lemma_reading] = word_dict.get(lemma_reading, 0)+1


    # print('Start reading Pickled dictionary.')
    # dP = read_pickle('mydict.pickle')

    print('Start reading Word forms: ' + print_time())
    dUD = read_UD_word_forms_to_dict('word-forms.txt')

    dLemmas, dCountedForms = count_UD_forms(d, dUD)
    d.clear()
    dUD.clear()
    print('Dictionaries cleared.' + print_time())
    write_to_tsv(dLemmas, 'lemma_count')
    write_to_tsv(dCountedForms, 'form_count')
    #print_out_x_lines_from_dict(dCountedForms, 10)

if __name__ == "__main__":
    # execute only if run as a script
    main()
=======
    print('Done writing dictionary to file.')


dP = {}
dUD = {}

dP = read_pickle('pb.pickle')
dUD = read_UD_word_forms_to_dict('word-forms.txt')

dLemmas, dCountedForms = count_UD_forms(dP, dUD)

write_to_tsv(dLemmas, 'lemma_count')
write_to_tsv(dCountedForms, 'form_count')
#print_out_x_lines_from_dict(dCountedForms, 10)
>>>>>>> 19c97b4488fdfade0b1ab85663ca7e7ec864fc84
