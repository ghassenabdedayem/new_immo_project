import time
import numpy as np
import pandas as pd
import numpy as np
from data_processing import clean_data, process_data, simple_concatenate, geo_code

start_time = time.time()
start = 2015
end = 2019

# Now we clean each file and we save it in a new file named cleaned
# for i in np.arange(start, end+1):
#     source_path = '../data_sources/valeursfoncieres-' + str (i) + '.txt'    

processed_path = '../data_transformed/'

#     clean_data(source_path, processed_path+'cleaned_'+str(i)+'.csv')

# print('cleaning completed in ' + str(time.time()-start_time) + ' s')


# And now we concatenate the cleaned files into a concatenated one
concat_df = pd.read_csv(processed_path+'cleaned_2015.csv')

concatenated_path = '../concatenated.csv'
concat_df.to_csv(concatenated_path)

for i in np.arange(start+1, end+1):
    simple_concatenate(concatenated_path, processed_path+'cleaned_'+str(i)+'.csv')

print('concatenating completed in ' + str(time.time()-start_time) + ' s')

simple_concatenate('../data_sources/valeursfoncieres-2016.txt', '../data_sources/valeursfoncieres-2017.txt', 'simple_concat.csv')