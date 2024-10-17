#!/usr/bin/env python3

from datetime import datetime
from typing import Optional

# Definindo padrões de formatação de data
PADROES = {
    'datetime': '%Y-%m-%d %H:%M:%S',
    'date': '%Y-%m-%d',
    'date_br': '%d-%m-%Y'
}

def formatarDatetime(datetime_str: str) -> Optional[str]:
    """
    Converte uma string de data e hora no formato '%Y-%m-%d %H:%M:%S' para o formato '%d-%m-%Y'.
    Se a conversão falhar, retorna None.
    
    :param datetime_str: String contendo a data e hora no formato '%Y-%m-%d %H:%M:%S'
    :return: String formatada no formato '%d-%m-%Y' ou None se a conversão falhar.
    """
    try:
        return datetime.strptime(datetime_str, PADROES['datetime']).strftime(PADROES['date_br'])
    except ValueError:
        return None

def formatarDatetimeCustomReturn(datetime_str: str, padrao_retorno: str) -> Optional[str]:
    """
    Converte uma string de data e hora no formato '%Y-%m-%d %H:%M:%S' para um formato customizado.
    Se a conversão falhar, retorna None.
    
    :param datetime_str: String contendo a data e hora no formato '%Y-%m-%d %H:%M:%S'
    :param padrao_retorno: O formato no qual a data deve ser retornada
    :return: String formatada no formato desejado ou None se a conversão falhar.
    """
    try:
        return datetime.strptime(datetime_str, PADROES['datetime']).strftime(padrao_retorno)
    except ValueError:
        return None

def formatarDate(datetime_str: str) -> Optional[str]:
    """
    Converte uma string de data no formato '%Y-%m-%d' para o formato '%d-%m-%Y'.
    Se a conversão falhar, retorna None.
    
    :param datetime_str: String contendo a data no formato '%Y-%m-%d'
    :return: String formatada no formato '%d-%m-%Y' ou None se a conversão falhar.
    """
    try:
        return datetime.strptime(datetime_str, PADROES['date']).strftime(PADROES['date_br'])
    except ValueError:
        return None

def formatarDateCustomReturn(datetime_str: str, padrao_retorno: str) -> Optional[str]:
    """
    Converte uma string de data no formato '%Y-%m-%d' para um formato customizado.
    Se a conversão falhar, retorna None.
    
    :param datetime_str: String contendo a data no formato '%Y-%m-%d'
    :param padrao_retorno: O formato no qual a data deve ser retornada
    :return: String formatada no formato desejado ou None se a conversão falhar.
    """
    try:
        return datetime.strptime(datetime_str, PADROES['date']).strftime(padrao_retorno)
    except ValueError:
        return None
