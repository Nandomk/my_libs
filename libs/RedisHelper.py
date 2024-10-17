#!/usr/bin/env python3
import redis
from redis.exceptions import ConnectionError, RedisError

def get_redis_client(
    host="localhost", port=6379, username=None, password=None,
    ssl=False, ssl_certfile=None, ssl_keyfile=None, ssl_ca_certs=None
):
    """
    Cria e retorna um cliente Redis com base nas configurações fornecidas.
    
    :param host: Endereço do servidor Redis.
    :param port: Porta do servidor Redis.
    :param username: Usuário para autenticação no Redis.
    :param password: Senha para autenticação no Redis.
    :param ssl: Usar SSL para a conexão.
    :param ssl_certfile: Caminho para o certificado SSL.
    :param ssl_keyfile: Caminho para a chave privada SSL.
    :param ssl_ca_certs: Caminho para o certificado da autoridade certificadora.
    
    :return: Um objeto Redis pronto para uso.
    """
    try:
        client = redis.Redis(
            host=host,
            port=port,
            username=username,
            password=password,
            ssl=ssl,
            ssl_certfile=ssl_certfile,
            ssl_keyfile=ssl_keyfile,
            ssl_ca_certs=ssl_ca_certs
        )
        # Teste de conexão
        client.ping()
        return client
    except ConnectionError as e:
        print(f"Erro de conexão com Redis: {e}")
        return None
    except RedisError as e:
        print(f"Erro geral no Redis: {e}")
        return None

def SaveStrData(r, chave, valor):
    """
    Salva uma string no Redis.
    
    :param r: Instância do cliente Redis.
    :param chave: A chave para identificar o valor no Redis.
    :param valor: O valor a ser salvo.
    """
    try:
        r.set(chave, valor)
    except RedisError as e:
        print(f"Erro ao salvar dados no Redis: {e}")

def GetDados(r, chave):
    """
    Recupera dados do Redis com base na chave fornecida.
    
    :param r: Instância do cliente Redis.
    :param chave: A chave para identificar o valor no Redis.
    :return: O valor correspondente à chave ou None se não encontrado.
    """
    try:
        return r.get(chave)
    except RedisError as e:
        print(f"Erro ao recuperar dados do Redis: {e}")
        return None

def Deletar(r, chave):
    """
    Deleta um valor no Redis com base na chave fornecida.
    
    :param r: Instância do cliente Redis.
    :param chave: A chave a ser deletada.
    :return: O número de chaves deletadas.
    """
    try:
        return r.delete(chave)
    except RedisError as e:
        print(f"Erro ao deletar dados no Redis: {e}")
        return 0

# Exemplo de uso
if __name__ == "__main__":
    redis_client = get_redis_client()

    if redis_client:
        SaveStrData(redis_client, "chave_exemplo", "valor_exemplo")
        valor = GetDados(redis_client, "chave_exemplo")
        print(f"Valor recuperado: {valor.decode('utf-8') if valor else None}")
        Deletar(redis_client, "chave_exemplo")
