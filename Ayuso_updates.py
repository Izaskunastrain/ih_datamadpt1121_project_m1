# Main file with which I download the data 

from p_acquisition import acquisition as acq
from p_wrangling import wrangling as mwr


if __name__ == '__main__':
    imported_df_bicimad= acq.acquisition_bicimad("./data/bicimad_stations.csv")
    imported_df_sport_centers= acq.acquisition_sport_centers("https://datos.madrid.es/egob/catalogo/212808-0-espacio-deporte.json")
    wrangled_df= mwr.wrangling_function(imported_df_bicimad,imported_df_sport_centers)
    wrangled_df.to_csv("data/bicimad_sport_center_distance.csv", index= False)
    print ('')
    print('Datos actualizaditos!')


