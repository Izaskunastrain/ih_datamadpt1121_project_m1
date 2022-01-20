
import argparse

from p_acquisition import acquisition as acq
from p_wrangling import wrangling as mwr


# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description='Bienvenido al consultorio de Ayuso. Te puedo conceder tres deseos amigo madrileño deportista:')
    parser.add_argument("-t", "--todo", help="Si quieres ir saber los puestos más cercanos de bicimad de todos los centros deportivos de Madrid", action='store_true')
    parser.add_argument("-u", "--uno", help="Si quieres ir saber el puesto más cercanos de bicimad de un centro en concreto", action='store_true')
    args = parser.parse_args()
    return args

# Main pipeline function

def main(arguments):

    if arguments.todo:
        imported_df_bicimad= acq.acquisition_bicimad("./data/bicimad_stations.csv")
        imported_df_sport_centers= acq.acquisition_sport_centers("https://datos.madrid.es/egob/catalogo/212808-0-espacio-deporte.json")
        wrangled_df= mwr.wrangling_function(imported_df_bicimad,imported_df_sport_centers)
        wrangled_df.to_csv("data/bicimad_sport_center_distance.csv", index= False)
        print('Ya tienes toda la info en tu carpetita. Guau!')

    elif arguments.uno:
        center = input('Escribe el centro deportivos que te intersa:   ')
        
        imported_df_bicimad= acq.acquisition_bicimad("./data/bicimad_stations.csv")
        imported_df_sport_centers= acq.acquisition_sport_centers("https://datos.madrid.es/egob/catalogo/212808-0-espacio-deporte.json")
        wrangled_df= mwr.wrangling_function(imported_df_bicimad,imported_df_sport_centers)
        
        center_list= [center]
        center_info= wrangled_df[wrangled_df['Centro deportivo'].isin(center_list)]
        print(center_info)



    

if __name__ == '__main__':
       main(argument_parser())




    

    