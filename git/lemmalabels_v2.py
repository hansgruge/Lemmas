import pandas as pd
import time
import numpy as np
#import pp

start_time = time.time()
def readData():
  start_time = time.time()
  df = pd.read_table('../parsebank_v4_UD_scrambled.conllu.gz', engine='c', compression='gzip', nrows=100000, names=['LABEL','FORM','LEMMA','CPOS','POS','FEAT','HEAD','DEPREL','DEPS','MISC'],index_col=False)
  #
  print("--- %s seconds ---" % round(time.time() - start_time, 2))
  return df

def removeNoise(df):
  # Remove comments and "PUNCTS" "X" "SYM" "_"
  df.drop(df[df['LABEL'].str.contains('#') |df['CPOS'].str.contains('SYM')|df['CPOS'].str.contains('PUNCT')|df['CPOS'].str.contains('X')|df['CPOS'].str.contains('_')].index, inplace=True)
  df.dropna(axis=0, subset=['LEMMA'],inplace=True)
  # Reindexing
  df.reset_index(drop=True, inplace=True)
  df.sort_values(by="LEMMA", ascending=True, inplace=True, kind='heapsort')
  return df

'''
    takes in pandas dataframe and gives out dictionary
'''
def runToLabels(df):
  start_time = time.time()
  print len(df)
  
  ADJ = pd.DataFrame(data=np.nan, index=['LEMMA'],columns=['LEMMA'])
  for i in xrange(0,len(df)):
      lemma = df.at[i,'LEMMA']
      feat = df.at[i,'FEAT']

      cpos = df.at[i,'CPOS']

      #print lemma, tem
      #print type(tem)
      #print type(lemma)
      #print cpos
      if(cpos != 'ADJ' or feat == '_'):
          continue
      else:
          #temp =  [ s.split('=') for s in feat.split('|')]
          temp = [s for s in feat.split('|')]
          #print temp
          #keys == feature name values == column name featurevalue
          #for keys, values in temp:
          for values in temp:
              #if column exists
              if values in ADJ:
                  #if lemma exists
                  if lemma in ADJ['LEMMA']:
                      ADJ.loc[lemma, values] += 1
                  #new lemma
                  else:
                      ADJ.loc[lemma,values] = 1
              #new column
              else:
                  #if lemma exists
                  if lemma in ADJ['LEMMA']:
                      ADJ.loc[lemma, values] = 1
                  #new lemma
                  else:
                      ADJ.loc[lemma, values] = 1


              #print lemma, cpos, keys, values
          #print temp
  print("--- %s seconds ---" % round(time.time() - start_time, 2))
  return ADJ
  #769791 --- 63.33 seconds --- 1 000 000 rows at first place
  #3850635 --- 494.25 seconds ---

df = readData()
print 'luettu'
uli = removeNoise(df)
print 'denoise done'
adj = runToLabels(uli)
print 'laput laitettu'
start_time1 = time.time()
adj.to_csv('tulos2.csv', sep='\t', encoding='utf-8' )
print('out to csv done')
print("--- %s seconds ---" % round(time.time() - start_time1, 2))
print("--- %s seconds ---" % round(time.time() - start_time, 2))
