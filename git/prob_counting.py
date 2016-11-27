import pandas as pd
import gzip
import time


# print current time
def print_time():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime


# Read Lemma counts to dict for quick search of lemmas and their values
# Uses gzipped file
def read_Lemma_counts_to_dict(fname):
    dd = {}
    LEMMA, COUNT = range(2)
    with gzip.open(fname, 'rt') as wf:
        for line in wf:
            line = line.rstrip()
            if not line:
                continue
            cols = line.split('\t')
            assert len(cols) == 2
            temp = (cols[LEMMA])
            dd[temp] = dd.get(temp, 0) + int(cols[COUNT])
    print('LEMMA counts read finished: ' + print_time())
    return dd

# Dictionary for lemmas and their values.
dLemmas = {}

print('Read lemma counts to dictionary: ', print_time())
# Reading Lemmas from gzipped file set correct filename
dLemmas = read_Lemma_counts_to_dict('lemma_count.tsv.gz')

# Column names to Pandas dataframe
names = ['FORM', 'LEMMA', 'POS', 'FEAT', 'PCS']

print('Read form counts to Pandas dataframe: ', print_time())
# Read form counts to Pandas Dataframe
df = pd.read_csv('form_count.tsv.gz', nrows=None, sep='\t',
                 names=names, compression='gzip')


# Create column for probability P(TAG | LEMMA)
df.loc[:, 'PROB'] = pd.Series(0.0, index=df.index)

print('Calculate probs: ', print_time())
# Calculate all probabilities by adding them
# iat[] uses numeric notation getting data out from dataframe
# it is very fast compared to loc[] function
for i in range(0, len(df)):
    # if lemma count is zero then it gives None
    if dLemmas.get(df.iat[i, 1]) is not None:
        df.iat[i, 5] = (df.iat[i, 4]) / (dLemmas.get(df.iat[i, 1]))
    else:
        df.iat[i, 5] = 0

# write back to gzipped file with calculated probabilities
print('Print dataframe to file: ', print_time())
df.to_csv('test.tsv.gz', sep='\t', header=False, index=False,
          compression='gzip')

print('Done: ', print_time())
