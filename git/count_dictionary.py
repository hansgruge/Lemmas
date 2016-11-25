import sys
import pickle

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

#import pandas as pd
#import matplotlib as mpl
#
#df = pd.DataFrame([(k1,k2,k3,v) for k1, k23v in d.items()
#                  for k2, k3v in k23v.items()
#                  for k3, v in k3v.items()],
#                  columns=['POS', 'LEMMA', 'FORM + FEAT', 'pcs'])
#print(df.head())
#
#
#df['POS'].value_counts().plot(kind='bar')


with open("mydict.pickle", "wb") as f:
    pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)

#pos_counts = {}
#for pos, pos_dict in d.items():
#    pos_d = pos_counts.setdefault(pos, {})
#    for word_dict in pos_dict.values():
#        for (lemma, reading), count in word_dict.items():
#            pos_d[reading] = pos_d.get(reading, 0)+1
#
#for reading, count in sorted(pos_counts["ADJ"].items(), key=lambda x: x[1],
#                             reverse=True):
#    print(reading, " : ", count)
