import pandas as pd
# extrae los datos de un archivo CSV y retorna un dataframe

def extract_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path,parse_dates=['date'])
        print(f"Datos extraidos correctamente:{len(df)} filas")
        return df
    except Exception as e :
        print(f"Error al extraer los datos : {e} ")