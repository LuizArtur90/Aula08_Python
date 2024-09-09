from etl import extrair_dados, calcular_kpi_lucro_bruto, carregar_dados

pasta:str = 'data'
data_frame = extrair_dados(path=pasta)
data_frame_calculado = calcular_kpi_lucro_bruto(data_frame)
#Escolher arquivos de saída .csv, .parquet ou ambos
formato_de_saida: list = ["parquet","csv"]
carregar_dados(data_frame_calculado, formato_de_saida)




