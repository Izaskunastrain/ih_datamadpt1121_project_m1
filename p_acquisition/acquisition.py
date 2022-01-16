import pandas as pd
import requests
import re

#BICIMAD: Read data from the csv stored in the data folder

def acquisition_bicimad (path_file_csv_bicimad):
    df_bicimad_raw= pd.read_csv(path_file_csv_bicimad)
    return df_bicimad_raw

#MADRID SPORT CENTERS: Read data from the API REST of Madrid city hall
# Link: https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/ 

def acquisition_sport_centers (url_madrid_sport_centers):
    r= requests.get(url_madrid_sport_centers).json()
    df_sport_centers_raw = pd.json_normalize(r['@graph'])
    return df_sport_centers_raw