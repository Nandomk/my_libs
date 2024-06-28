import os
import time

def SalvarLog(caminho_arquivo, conteudo, printar = False):
    if os.path.exists(caminho_arquivo):
        arquivo = open(caminho_arquivo, "a", newline='', encoding="utf8")
        arquivo.write(conteudo+"\n")
        arquivo.close()
    else:
        arquivo = open(caminho_arquivo, "w", newline='', encoding="utf8")
        arquivo.write(conteudo+ "\n")
        arquivo.close()
    if printar :
        print(time.strftime("%Y-%m-%d_%H:%M:%S")+": "+ conteudo)