import numpy as np
import pandas as pd


def clean_data(source_path, destination_path):
    # I define 3 functions to clean data and handle string, float and date types
    def str_float(x):
        return float(str(x).replace(',', '.'))

    # def str_float_simple(x):
    #     return float(x)

    # str_2 = lambda x: str(x).replace(',', '.')

    def convert_to_int(x):
        if np.isnan(x):
            return np.nan
        else:
            return (int(x))

    # Read the CSV file into a dataframe
    df = pd.read_csv(source_path,
                     sep='|',
                     low_memory=False,
                     parse_dates=[2],
                     squeeze=True)

    # Drop the useless columns
    columns_to_drop = [
        'Code service CH', 'Reference document', '1 Articles CGI', '2 Articles CGI',
        '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', 'B/T/Q', 'Code voie', 'Identifiant local',
        'Code commune', 'Prefixe de section', 'Section', 'No plan', 'No Volume'
    ]

    df = df.drop(labels=columns_to_drop, axis=1)

    # Rename column labels and remove spaces
    df = df.rename(columns={'No disposition': 'No_disposition', 'Date mutation': 'Date_mutation',
                            'Nature mutation': 'Nature_mutation',
                            'Valeur fonciere': 'Valeur_fonciere', 'No voie': 'No_voie', 'Type de voie': 'Type_de_voie',
                            'Voie': 'Voie',
                            'Code postal': 'Code_postal', 'Commune': 'Commune',
                            '1er lot': '1er_lot', 'Surface Carrez du 1er lot': 'Surface_Carrez_du_1er_lot',
                            '2eme lot': '2eme_lot', 'Surface Carrez du 2eme lot': 'Surface_Carrez_du_2eme_lot',
                            '3eme lot': '3eme_lot', 'Surface Carrez du 3eme lot': 'Surface_Carrez_du_3eme_lot',
                            '4eme lot': '4eme_lot', 'Surface Carrez du 4eme lot': 'Surface_Carrez_du_4eme_lot',
                            '5eme lot': '5eme_lot', 'Surface Carrez du 5eme lot': 'Surface_Carrez_du_5eme_lot',
                            'Nombre de lots': 'Nombre_de_lots', 'Code type local': 'Code_type_local',
                            'Type local': 'Type_local',
                            'Surface reelle bati': 'Surface_reelle_bati',
                            'Nombre pieces principales': 'Nombre_pieces_principales',
                            'Nature culture': 'Nature_culture', 'Code departement': 'Code_departement',
                            'Nature culture speciale': 'Nature_culture_speciale', 'Surface terrain': 'Surface_terrain'})

    # list of columns that contain strings to be converted into float
    columns_float = [
        '1er_lot', 'Surface_Carrez_du_1er_lot', '2eme_lot', 'Surface_Carrez_du_2eme_lot', '3eme_lot',
        'Surface_Carrez_du_3eme_lot', '4eme_lot', 'Surface_Carrez_du_4eme_lot',
        '5eme_lot', 'Surface_Carrez_du_5eme_lot', 'Valeur_fonciere'
    ]

    # list of columns to be converted into int
    columns_int = [
        'No_voie', 'Code_postal', 'Code_departement', 'Code_type_local', 'Nombre_pieces_principales',
    ]

    # Converting the values into float
    for col in columns_float:
        try:
            df[col] = df[col].apply(str_float)
        except:
            pass

        # Converting the values into int
    for col in columns_int:
        try:
            df[col] = df[col].apply(convert_to_int)  #### It does not work, maybe because of NaN ?
        except:
            pass

    # destination_path = 'C:/Users/Ghassen/Documents/Projects/Immobilier/1_Project/Data_assets/Temp/clean_data_' + str(file_number) + '.csv'
    df.to_csv(destination_path)


def geo_code(source_path, destination_path):
    df = pd.read_csv(source_path,
                     low_memory=False,
                     parse_dates=[2],
                     index_col=0,
                     squeeze=True)

    ############\\\\\\\\\ Other transformations should be written here //////////##############

    df.to_csv(destination_path)


def process_data(source_path, destination_path):
    # Read the CSV file into a dataframe
    df = pd.read_csv(source_path,
                     low_memory=False,
                     parse_dates=[2],
                     index_col=0,
                     squeeze=True)

    ############\\\\\\\\\ Other transformations should be written here //////////##############

    df.to_csv(destination_path)


def concatenate(paths_list, destination_path):
    global_df = pd.DataFrame()
    for path in paths_list:
        df = pd.read_csv(
            path['cleaned_path'],  #### To be modified with processed_path instead
            low_memory=False,
            parse_dates=[2],
            index_col=0,
            squeeze=True
        )
        global_df = pd.concat([df, global_df], ignore_index=True)
    global_df.to_csv(destination_path)

def simple_concatenate(source_path_1, source_path_2, destination_path):
    df_1 = pd.read_csv(source_path_1, low_memory=False)
    print('taille de df 1 : ', len(df_1))
    df_2 = pd.read_csv(source_path_2, low_memory=False)
    print('taille de df 2 : ', len(df_2))
    df_global = pd.concat([df_1, df_2],ignore_index=True)
    print('taille de df concat : ', len(df_global))

    df_global.to_csv(destination_path)
