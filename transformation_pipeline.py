import pandas as pd
import datetime as dt

class DemandaUsuariosTransformer:


    def __init__(self, df, anio):
        self.df   = df
        self.anio = anio


    def split_lineas(df):
        """Particiona el dataframe en dos, en la cual cada dataframe 
        corresponde a una línea (Línea 1, Línea 2)"""
    
        l1 = []
        l2 = []
        
    
        if df.shape[1] == 3:
            l1 = df.iloc[:, :3].copy()
            l1['Linea'] = 'Linea 1'
            l1.index =  l1.index.rename('Mes')
            l1.reset_index(inplace=True)
    
        elif df.shape[1] == 6: 
            l2 = df.iloc[:, 3:].copy()
            l2['Linea'] = 'Linea 2'
            l2.index.names=['Mes']
            l2.reset_index(inplace=True)
        df = (l1, l2)
        return df


    def df_joiner(df, anio):
        """ Concatena el los dataframes de Línea 1 y Línea 2.
        Asigna el año correspondiente a los datos"""

        if len(df) == 1:
            df['Anio'] = str(anio)
        else:
            df = df[0].append(df[1])
            df['Anio'] = str(anio)
        
        return df


    def rename_columns(df):
        """ Reemplaza el nombre de las columnas.
        Reordena el orden de las columnnas"""
        
        columns_names = {'Demanda Laborable': 'Laborable',
                         'Demanda Sábados' : 'Sabados',
                         'Demanda Feriados' : 'Feriados'
                         }

        df.rename(columns=columns_names, inplace=True)
        columns_order = ['Anio','Mes','Linea','Laborable','Sabados','Feriados']
        df = df[columns_order]
        df.rename_axis(None, axis=1, inplace=True)
    
        return df


    def datetime_transformer(df):
        """ Une las columnas año y mes y las convierte a tipo datetime"""
        
        meses={'enero':'1', 'febrero':'2', 'marzo':'3', 
               'abril':'4', 'mayo':'5', 'junio':'6',
               'julio':'7', 'agosto':'8', 'septiembre':'9', 
               'octubre':'10', 'noviembre':'11', 'diciembre':'12'
               } 
    
        df['Mes'] = df['Mes'].apply(lambda x: x.strip().lower())
        df['Mes'] = df['Mes'].map(meses)
        df['Fecha'] = df['Anio']+"-"+df['Mes']
        df.drop(['Mes','Anio'], axis=1, inplace=True)
        df['Fecha'] = df['Fecha'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m"))
        df.set_index('Fecha', inplace=True)
   
        return df