#!/usr/bin/env python3
import pandas as pd
import json

def ConverterJsonToExcel(fileIn, fileOut):
    """
    Converte um arquivo JSON contendo uma lista de pessoas em um arquivo Excel.
    
    :param fileIn: Caminho do arquivo JSON de entrada.
    :param fileOut: Caminho do arquivo Excel de saída.
    """
    with open(fileIn, encoding="utf8") as f:
        data = json.load(f)
    
    df = pd.DataFrame(data['pessoas'])
    df.to_excel(fileOut, index=False)

def ConvertCsvToExcel(fileIn, fileOut):
    """
    Converte um arquivo CSV em um arquivo Excel, aplicando ajustes automáticos na largura das colunas.
    
    :param fileIn: Caminho do arquivo CSV de entrada.
    :param fileOut: Caminho do arquivo Excel de saída.
    """
    # Lê o arquivo CSV
    df = pd.read_csv(fileIn)

    # Cria um arquivo Excel de saída com a folha "Histórico"
    with pd.ExcelWriter(fileOut, engine='openpyxl') as resultExcelFile:
        df.to_excel(resultExcelFile, sheet_name="Histórico", index=False)

        # Acessa o objeto do workbook e da worksheet
        workbook = resultExcelFile.book
        worksheet = resultExcelFile.sheets["Histórico"]

        # Ajusta automaticamente a largura das colunas
        for col in worksheet.columns:
            max_length = 0
            column = col[0].column_letter  # Pega o nome da coluna (letra)
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            worksheet.column_dimensions[column].width = adjusted_width

    print(f"Arquivo Excel '{fileOut}' criado com sucesso.")

# Exemplo de uso:
# ConverterJsonToExcel('pessoas.json', 'pessoas.xlsx')
# ConvertCsvToExcel('dados.csv', 'dados.xlsx')