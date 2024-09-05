#!/usr/bin/env python3
import sys
import os 

sys.path.append(os.path.abspath('..'))

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

from libs.Geolocation import calculate_distantece

lat1 = -23.550520 #Lat São Paulo
lon1 = -46.633308 #Long São Paulo

lat2 = 40.712776
lon2 = -74.005974

distance_km = calculate_distantece(lat1, lon1, lat2, lon2)
print(f"Distância entre São Paulo e Nova York é de {distance_km:.2f} km")



