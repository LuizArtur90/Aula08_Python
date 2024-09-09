import pandas as pd
import os
import glob

#Uma função de extract e leitura e consolida json

def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path,'*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_concac = pd.concat(df_list,ignore_index=True)
    return df_concac



#Uma função que transforma

def calcular_kpi_lucro_bruto(df:pd.DataFrame)->pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

#Uma função que load csv ou parquet

def carregar_dados(df: pd.DataFrame, format_saida: list):
    
    """
    parametro que vai ser csv ou parquet ou ambos
    """
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet",index=False)
            
