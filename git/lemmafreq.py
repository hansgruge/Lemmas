import lemmadict

file_to_read = '../../versions/parsebank_v4_UD_scrambled.conllu.gz'
d = {}
d = lemmadict.read_data(file_to_read)

print