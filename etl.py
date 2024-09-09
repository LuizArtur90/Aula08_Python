import pandas as pd
import os
import glob

#Uma função de extract e leitura e consolida json
pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta,'*.json'))
df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
print(df_list)




#Uma função que transforma

#Uma função que load csv ou parquet