class DemandaUsuariosTransformer:

    def __init__(self, df, anio):
        self.df   = df
        self.anio = anio


    def split_lineas(df):
    
        l1 = df.iloc[:, :3].copy()
        l1['Linea'] = 'Linea 1'
        l1.index =  l1.index.rename('Mes')
        l1.reset_index(inplace=True)
    
        if df.shape[1] == 6:
            l2 = df.iloc[:, 3:].copy()
            l2['Linea'] = 'Linea 2'
            l2.index.names=['Mes']
            l2.reset_index(inplace=True)

        return l1, l2


    def df_joiner(df, anio):
    
        if len(df) == 1:
            df['Anio'] = str(anio)
        else:
            df = df[0].append(df[1])
            df['Anio'] = str(anio)
        
        return df


    def rename_columns(df):
        columns_names = {'Demanda Laborable': 'Laborable',
                         'Demanda Sábados' : 'Sabados',
                         'Demanda Feriados' : 'Feriados'}

        columns_order = [['Linea','Anio','Mes','Laborable','Sabados','Feriados']]
        df.rename(columns=columns_names, inplace=True)
        df.rename_axis(None, axis=1, inplace=True)
    
        return df


    def datetime_transformer(df):
        meses={'enero':'1', 'febrero':'2', 'marzo':'3', 
               'abril':'4', 'mayo':'5', 'junio':'6',
               'julio':'7', 'agosto':'8', 'septiembre':'9', 
               'octubre':'10', 'noviembre':'11', 'diciembre':'12'} 
    
        df['Mes'] = df['Mes'].apply(lambda x: x.strip().lower())
        df['Mes'] = df['Mes'].map(meses)
        df['Fecha'] = df['Anio']+"-"+df['Mes']
        df.drop(['Mes','Anio'], axis=1, inplace=True)
        df['Fecha'] = df['Fecha'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m"))
        df.set_index('Fecha', inplace=True)
   
        return df