#!/usr/bin/env python3
from datetime import datetime

padraoDateTime = '%Y-%m-%d %H:%M:%S'
padraoDate = '%Y-%m-%d'
padraoDateBr = '%d-%m-%Y'

def formatarDatetime(datetime_str):
    try:
        return datetime.strptime(datetime_str, padraoDateTime).date().strftime(padraoDateBr)

    except:
        return datetime_str
    
def formatarDatetimeCustomReturn(datetime_str, padrao_retorno):
    return datetime.strptime(datetime_str, padraoDateTime).date().strftime(padrao_retorno)

def formatarDate(datetime_str):
    try:
        return datetime.strptime(datetime_str, padraoDate).date().strftime(padraoDateBr)
    except:
        return datetime_str

def formatarDateCustomReturn(datetime_str, padrao_retorno):
    return datetime.strptime(datetime_str, padraoDate).date().strftime(padrao_retorno)