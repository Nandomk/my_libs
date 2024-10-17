#!/usr/bin/env python3
import math

# Constante para o raio médio da Terra em quilômetros
EARTH_RADIUS_KM = 6371.0

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calcula a distância entre duas coordenadas geográficas usando a fórmula de Haversine.

    :param lat1: Latitude do primeiro ponto (em graus).
    :param lon1: Longitude do primeiro ponto (em graus).
    :param lat2: Latitude do segundo ponto (em graus).
    :param lon2: Longitude do segundo ponto (em graus).
    
    :return: Distância entre os dois pontos em quilômetros.
    """
    # Conversão de coordenadas de graus para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Diferença entre as coordenadas
    d_lat = lat2_rad - lat1_rad
    d_lon = lon2_rad - lon1_rad
    
    # Fórmula de Haversine
    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Cálculo da distância
    distance_km = EARTH_RADIUS_KM * c

    return distance_km
