#!/usr/bin/env python3
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json
import httpx
import asyncio

# Função para configurar uma sessão com retry e timeout
def configurar_sessao_com_retry():
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        backoff_factor=2,
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

# Função para logar a resposta de requisição
def logar_resposta(url, status_code, json_resposta, printar=False):
    if printar:
        json_formatted_str = json.dumps(json_resposta, ensure_ascii=False, indent=2)
        print(f"URL: {url}")
        print(f"Status Code: {status_code}")
        print(json_formatted_str)

# Função para requisição POST síncrona com retry e timeout
def RequisitarPostJson(url, headInfo, dataInfo, printar=False):
    session = configurar_sessao_com_retry()
    try:
        r = session.post(url, json=dataInfo, headers=headInfo, timeout=10)
        r.raise_for_status()  # Verifica se há erros HTTP
        json_resposta = r.json()
        logar_resposta(url, r.status_code, json_resposta, printar)
        return json_resposta
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer POST para {url}: {str(e)}")
        return None

# Função para requisição POST assíncrona com timeout
async def RequisitarPostJsonAsync(url, headInfo, dataInfo, printar=False):
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            r = await client.post(url, json=dataInfo, headers=headInfo)
            r.raise_for_status()  # Verifica se há erros HTTP
            json_resposta = r.json()
            logar_resposta(url, r.status_code, json_resposta, printar)
            return json_resposta
        except httpx.HTTPStatusError as e:
            print(f"Erro ao fazer POST assíncrono para {url}: {str(e)}")
            return None

# Função para requisição GET síncrona com retry e timeout
def RequisitarGetJson(url, headInfo, printar=False):
    session = configurar_sessao_com_retry()
    try:
        r = session.get(url, headers=headInfo, timeout=10)
        r.raise_for_status()  # Verifica se há erros HTTP
        json_resposta = r.json()
        logar_resposta(url, r.status_code, json_resposta, printar)
        return json_resposta
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer GET para {url}: {str(e)}")
        return None

# Função para requisição GET assíncrona com timeout
async def RequisitarGetJsonAsync(url, headInfo, printar=False):
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            r = await client.get(url, headers=headInfo)
            r.raise_for_status()  # Verifica se há erros HTTP
            json_resposta = r.json()
            logar_resposta(url, r.status_code, json_resposta, printar)
            return json_resposta
        except httpx.HTTPStatusError as e:
            print(f"Erro ao fazer GET assíncrono para {url}: {str(e)}")
            return None
