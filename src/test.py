# import pandas as pd
# from data_processing import clean_data, process_data, simple_concatenate, geo_code
import numpy as np
import pandas as pd
from data_processing import simple_concatenate
# clean_data (
#     '../data_sources/valeursfoncieres-2015.txt', 
#     '../data_transformed/test_clean_3.csv'
#     )
print(np.pi)

simple_concatenate(
    '../data_transformed/cleaned_2015.csv', 
    '../data_transformed/cleaned_2016.csv', 
    'simple_concat.csv'
    )

# df_1 = pd.read_csv('../data_transformed/cleaned_2015.csv', low_memory=False)
# print('taille de df 1 : ', len(df_1))
# df_2 = pd.read_csv('../data_transformed/cleaned_2016.csv', low_memory=False)
# print('taille de df 2 : ', len(df_2))
# df_global = pd.concat([df_1, df_2],ignore_index=True)
# print('taille de df concat : ', len(df_global))