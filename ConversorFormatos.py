#!/usr/bin/env python3
import pandas as pd
import json



#for ind in df.index:
#    print(df['id'][ind], df['nome'][ind], df['tipoPessoa'][ind])
#print(df)
def ConverterJsonToExcel(fileIn, fileOut):
    f = open(fileIn, encoding="utf8")
    data = json.load(f)
    f.close()
    df = pd.DataFrame(data['pessoas'])
    df.to_excel(fileOut, index=False)

def ConvertCsvToExcel(fileIn, fileOut):
    # reading the csv file
    cvsDataframe = pd.read_csv(fileIn)

    cvsDataframe2 = pd.read_csv(fileIn)

    # creating an output excel file
    resultExcelFile = pd.ExcelWriter(fileOut)

    # converting the csv file to an excel file
    #cvsDataframe.to_excel(resultExcelFile,sheet_name="Cadastro", index=False)

    cvsDataframe2.to_excel(resultExcelFile,sheet_name="Histórico", index=False)

    workbook = resultExcelFile.book
    #worksheetCadastro = resultExcelFile.sheets["Cadastro"]
    worksheetHistorico = resultExcelFile.sheets["Histórico"]

    #worksheetCadastro.auto_filter.ref='A:Z'
    worksheetHistorico.auto_filter.ref='A:Z'

    # for col in worksheetCadastro.columns:
    #     max_length = 0
    #     column = col[0].column_letter # Get the column name
    #     for cell in col:
    #         try: # Necessary to avoid error on empty cells
    #             if len(str(cell.value)) > max_length:
    #                 max_length = len(str(cell.value))
    #         except:
    #             pass
    #     adjusted_width = (max_length + 2) * 1.2
    #     worksheetCadastro.column_dimensions[column].width = adjusted_width

    for col in worksheetHistorico.columns:
        max_length = 0
        column = col[0].column_letter # Get the column name
        for cell in col:
            try: # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        worksheetHistorico.column_dimensions[column].width = adjusted_width
   
    # saving the excel file
    resultExcelFile._save()

 