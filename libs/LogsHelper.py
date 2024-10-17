#!/usr/bin/env python3
import os
import time

def SalvarLog(caminho_arquivo, conteudo, printar=False):
    """
    Função para salvar o conteúdo em um arquivo de log.
    
    :param caminho_arquivo: Caminho do arquivo onde o log será salvo.
    :param conteudo: Conteúdo a ser salvo no log.
    :param printar: Se True, imprime o conteúdo no console com timestamp.
    """
    timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
    
    # Abre o arquivo no modo append e escreve o conteúdo com uma nova linha
    with open(caminho_arquivo, "a", newline='', encoding="utf8") as arquivo:
        arquivo.write(conteudo + "\n")
    
    # Se printar=True, exibe o log no console
    if printar:
        print(f"{timestamp}: {conteudo}")