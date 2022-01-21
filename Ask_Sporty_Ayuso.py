import argparse
import random
import webbrowser
import time

from p_acquisition import acquisition as acq
from p_wrangling import wrangling as mwr


# Argument parser function

def argument_parser():
    parser = argparse.ArgumentParser(description='Bienvenido al consultorio de Ayuso amigo madrileño deportista! ¿En qué necesitas que te ayude hoy? Escribe:')
    parser.add_argument("-d", "--decide", help="Si necesitas ayuda decidiendo si hoy deberías hacer deporte o no", action='store_true')
    parser.add_argument("-a", "--all", help="Si quieres ver todos los centros deportivos de Madrid con sus paradas de bicimad más cercanas", action='store_true')
    parser.add_argument("-o", "--one", help="Si te has decidido por uno y quieres que te de su información", action='store_true')
    args = parser.parse_args()
    return args

# Main pipeline function

def main(arguments):

    if arguments.decide:
        answers = ["De toda la vida se empiezan las cosas los lunes", "Dios no te hizo perfecto y por eso hoy deberías hacer deporte.","Vamos! A ver si hay suerte y vemos un atasco", "Mejor hoy nos vamos de tapitas madrileñas", "Venga que así levantamos la economía!"]
        print("")
        print(random.choice(answers))
        print("")
    
    elif arguments.all:
        imported_df= acq.acquisition_bicimad("./data/bicimad_sport_center_distance.csv")
        imported_df.to_csv("data/bicimad_sport_center_distance.csv", index= False)
        print("")
        print('Ya tienes toda la info actualizada en tu carpetita. Guau!')
        print("")
        

    elif arguments.one:
        print ("")
        print ("ᕙ( ͡❛ ͜ʖ ͡❛)ᕗ")
        center = input('   Escribe el centro deportivo que te interesa:   ')
        
        imported_df_uno= acq.acquisition_bicimad("./data/bicimad_sport_center_distance.csv")
        
        center_list= [center]
        center_info= imported_df_uno[imported_df_uno['Centro deportivo'].isin(center_list)]
        print ("")
        print('    Buena eleccción madrileñito! ')
        print ("")
        print(center_info)
        print ("")
        print ("   Te abro tambien un mapa donde  puedes ver las bicis disponibles de cada estación de bicimad en tiempo real. De nadita!")
        time.sleep(7)
        webbrowser.open("https://u.bicimad.com/mapa")
        time.sleep(20)
        webbrowser.open("https://pbs.twimg.com/media/Exyw4sGUYAkbOvW.jpg")



    

if __name__ == '__main__':
       main(argument_parser())




    

    