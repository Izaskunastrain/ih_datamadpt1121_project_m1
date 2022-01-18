import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

def wrangling_function(df_bicimad_raw,df_sport_centers_raw):
    
    # Function to clean and separate values of latitude and longitude of bicimad
    def lat (x):
        b= x.split(',')
        c= b[0].replace('[','')
        d= float(c)
        return d
    def long (x):
        b= x.split(',')
        c= b[1].replace(']','')
        d= float(c)
        return d
    
    # Function to transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    def to_mercator(lat, long):
        c = gpd.GeoSeries([Point(lat, long)], crs=4326)
        c = c.to_crs(3857)
        return c
    
    # Function to return the distance in metres between two pseudo-mercator coordinates

    def distance_meters(location_centros, location_bicimad):
        return location_centros.distance(location_bicimad)
    
    #BICIMAD
    # I create the latitude and longitude columns 
    df_bicimad_raw['Latitude.bicimad'] = df_bicimad_raw.apply(lambda x: long(x['geometry_coordinates']),axis=1)
    df_bicimad_raw['Longitude.bicimad'] = df_bicimad_raw.apply(lambda x: lat(x['geometry_coordinates']),axis=1)
    
    # I create the new column location applying the function to_mercator on latitude and longitude     
    df_bicimad_raw['location_bicimad']= df_bicimad_raw.apply(lambda x: to_mercator (x['Latitude.bicimad'], x['Longitude.bicimad']), axis=1)
    
    # I keep only the columns I am interested in
    df_bicimad= df_bicimad_raw[['name', 'address', 'Latitude.bicimad', 'Longitude.bicimad', 'location_bicimad']]
    
    
    # SPORT CENTERS 
    # We first remove empty values 
    df_sport_centers_raw= df_sport_centers_raw.dropna()
    
    # I create the new column location_centros applying the function to_mercator on latitude and longitude 
    df_sport_centers_raw['location_centros']= df_sport_centers_raw.apply(lambda x: to_mercator (x['location.latitude'], x['location.longitude']), axis=1)
    
    # I keep only the columns I am interested in
    df_sport_centers= df_sport_centers_raw [['title', 'address.street-address', 'location.latitude', 'location.longitude', 'location_centros'] ]
    
    #MERGE BOTH DATAFRAMES
    
    df_merged = df_sport_centers.assign(key=0).merge(df_bicimad.assign(key=0),how='left', on = 'key')
    
    # Calculate the distance between the combination of all bicimad points and all sport center points  
    df_merged['Distance']= df_merged.apply(lambda x: distance_meters (x ['location_bicimad'], x ['location_centros']),axis=1 )
    
    # I create a table with the minimum distances grouped bye sport center
    min_distances= df_merged.groupby('title')['Distance'].min().reset_index()
    
    # I merge with the df_merged table to obtain more than the title and Distance columns
    df_final = min_distances.merge(df_merged, how='left', on = ['Distance', 'title'])
    return df_final


    
