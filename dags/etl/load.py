import pandas as pd
def load_data(df: pd.DataFrame, output_path: str):
    """
    Carga los datos transformados a un archivo CSV.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f" Datos cargados en {output_path}")
    except Exception as e:
        print(f" Error al cargar los datos: {e}")