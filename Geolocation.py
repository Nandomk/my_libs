#!/usr/bin/env python3
import math

def calculate_distantece(lat1, lon1, lat2, lon2):
    #conversao para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    #diferencas de coordenadas
    d_lat = lat2_rad - lat1_rad
    d_lon = lon2_rad - lon1_rad
    
    #raio medio da Terra em quilometros
    earth_radius_km = 6371.0

    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(d_lon/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance_km =earth_radius_km * c

    return distance_km

