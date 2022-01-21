import argparse

from p_acquisition import acquisition as acq
from p_wrangling import wrangling as mwr


# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description='Bienvenido al consultorio de Ayuso. Te puedo conceder un deseo amigo madrileño deportista:')
    parser.add_argument("-t", "--todo", help="Si quieres saberlo TODO: todas las paraditas de bicimad mas ceranas de todos los centros deportivos", action='store_true')
    parser.add_argument("-u", "--uno", help="Si eres realista, no podemita y sabes que como mucho irás a uno", action='store_true')
    args = parser.parse_args()
    return args

# Main pipeline function

def main(arguments):

    if arguments.todo:
        imported_df= acq.acquisition_bicimad("./data/bicimad_sport_center_distance.csv")
        imported_df.to_csv("data/bicimad_sport_center_distance.csv", index= False)
        print('Ya tienes toda la info actualizada en tu carpetita. Guau!')

    elif arguments.uno:
        center = input('Escribe el centro deportivo que te interesa:   ')
        
        imported_df_uno= acq.acquisition_bicimad("./data/bicimad_sport_center_distance.csv")
        
        center_list= [center]
        center_info= imported_df_uno[imported_df_uno['Centro deportivo'].isin(center_list)]
        
        print('Buena eleccción madrileñito! Como verás en Madrid está todo cerca:')
        print ("")
        print(center_info)
        print ("")



    

if __name__ == '__main__':
       main(argument_parser())




    

    