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