#!/usr/bin/env python3
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json
import httpx
import asyncio


#def GetConteudo(url, head):

def RequisitarPostJson(url, headInfo, dataInfo, printar = False):
    r = requests.post(url, data=dataInfo, headers=headInfo)
    jsonResposta = r.json()
    
    if printar :
        json_formatted_str = json.dumps(jsonResposta, ensure_ascii=False, indent=2)
        print("Post URL: "+ url )
        print("Post Status Code: "+ str(r.status_code))
        print(json_formatted_str)
    return jsonResposta

async def RequisitarPostJsonAsync(url, headInfo, dataInfo, printar = False):
     async with httpx.AsyncClient() as client:
        r = await client.post(url, data=dataInfo, headers=headInfo)
        jsonResposta = r.json()
        
        if printar :
            json_formatted_str = json.dumps(jsonResposta, ensure_ascii=False, indent=2)
            print("Post URL: "+ url )
            print("Post Status Code: "+ str(r.status_code))
            print(json_formatted_str)
        return jsonResposta

def RequisitarGetJson(url, headInfo, dataInfo, printar = False):
    retry_strategy = Retry(
        total =3,
        status_forcelist= [429,500,502,503,504],
        backoff_factor=2,
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter =HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    r = http.get(url, data=dataInfo, headers=headInfo)
    jsonResposta = r.json()
    
    if printar :
        json_formatted_str = json.dumps(jsonResposta, ensure_ascii=False, indent=2)
        print("Post URL: "+ url )
        print("Post Status Code: "+ str(r.status_code))
        print(json_formatted_str)
    return jsonResposta

async def RequisitarGetJsonAsync(url, headInfo, printar = False):

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=headInfo)
        jsonResposta = r.json()
        
        if printar :
            json_formatted_str = json.dumps(jsonResposta, ensure_ascii=False, indent=2)
            print("Post URL: "+ url )
            print("Post Status Code: "+ str(r.status_code))
            print(json_formatted_str)
        return jsonResposta



