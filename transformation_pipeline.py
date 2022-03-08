import pandas as pd


def split_and_join(df):
    """Particiona el dataframe en dos, en la cual cada dataframe 
        corresponde a una línea (Línea 1, Línea 2)"""
    
    if df.shape[1] == 6:
        l1 = df.iloc[:, :3].copy()
        l1['Linea'] = 'Linea 1'
        df1 = pd.DataFrame(l1)
        
        l2 = df.iloc[:, 3:].copy()
        l2['Linea'] = 'Linea 2'
        df2 = pd.DataFrame(l2)
        
        df = df1.append(df2)
        
        return df
    
    else: 
        l1 = df.iloc[:, :3].copy()
        l1['Linea'] = 'Linea 1'
        df = pd.DataFrame(l1)
        
        return df
         
        
def rename_columns(df):
    """ Reemplaza el nombre de las columnas.
        Reordena el orden de las columnnas"""
    
    columns_names = ['Laborable','Sabado','Feriados','Linea']
    df.columns = columns_names
    
    return df


def datetime_transformer(df, anio):
    """ Une las columnas año y mes y las convierte a tipo datetime"""
    
    meses={'enero':'1', 'febrero':'2', 'marzo':'3', 
           'abril':'4', 'mayo':'5', 'junio':'6',
           'julio':'7', 'agosto':'8', 'septiembre':'9', 
           'octubre':'10', 'noviembre':'11', 'diciembre':'12'
          } 
    
    df.reset_index(inplace=True)
    df['mes'] = df['mes'].apply(lambda x: x.strip().lower())
    df['mes'] = df['mes'].map(meses)
    df['anio'] = str(anio)
    df['Fecha'] = df['anio']+"-"+df['mes']
    df.drop(['mes','anio'], axis=1, inplace=True)
    df['Fecha'] = df['Fecha'].apply(lambda x: dt.datetime.strptime(x, "%Y-%m"))
    df.set_index('Fecha', inplace=True)
   
    return df