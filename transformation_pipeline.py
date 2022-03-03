import numpy as np



class demanda_transformer(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        self.df      = df
        self.anio    = anio
        
    
    def copy_df(self):
        return self.df.copy()


    def split_lineas(self):
        """Particiona el dataframe en dos, en la cual cada dataframe 
        corresponde a una línea (Línea 1, Línea 2)"""
    
        l1 = self.df.iloc[:, :3].copy()
        l1['Linea'] = 'Linea 1'
        l1.index =  l1.index.rename('Mes')
        l1.reset_index(inplace=True)
    
        if self.df.shape[1] == 6: 
            l2 = self.df.iloc[:, 3:].copy()
            l2['Linea'] = 'Linea 2'
            l2.index.names=['Mes']
            l2.reset_index(inplace=True)
    
        return l1, l2