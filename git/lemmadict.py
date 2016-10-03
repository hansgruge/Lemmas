import gzip


with gzip.open('../../versions/parsebank_v4_UD_scrambled.conllu-part-aa.gz', 'r') as rf:
    print [(i, line) for i, line in enumerate(rf) if i < 10]
