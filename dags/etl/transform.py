import pandas as pd
def transform_data(df:pd.DataFrame) -> pd.DataFrame:
    # Transforma los datos agregando el gasto total por mes y categoria
    try:
        # Crear columna 'month' a partir de la fecha
        df['month'] = df['date'].dt.to_period('M').astype(str)

        # Agrupar por mes y categoría
        resumen = df.groupby(['month', 'category'])['amount'].sum().reset_index()

        # Renombrar columna
        resumen.rename(columns={'amount': 'total_amount'}, inplace=True)

        print(f" Datos transformados: {len(resumen)} registros")
        return resumen

    except Exception as e:
        print(f" Error en la transformación de datos: {e}")
        return pd.DataFrame()