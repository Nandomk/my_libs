#!/usr/bin/env python3
import redis

r = redis.Redis(
    host="localhost", port=6379,
    #username=""
    #password=""
    #ssl=True,
    #ssl_certfile="./redis_user.crt",
    #ssl_keyfile="./redis_user_private.key",
    #ssl_ca_certs="./redis_ca.pem",
)
def SaveStrData(chave, valor):
    r.set(chave, valor)

def GetDados(chave):
    return r.get(chave)

def Deletar(chave):
    return r.delete(chave)