import pandas as pd
import numpy as np

class FakeExample:
    
    colunas:str='id,userId,title,completed'
    primaryKey:str='id'
    field_update:str=''

    def __init__(self,colunas:str=colunas,primaryKey:str=primaryKey,field_update:str=field_update):
        self.colunas =colunas
        self.primaryKey =primaryKey
        self.field_update =field_update

    def transformData(self,dataframe:pd.DataFrame):
        if dataframe is not None:

            dataframe = dataframe[self.colunas.split(',')]
            dataframe = dataframe.replace(r'^\s*$', np.nan, regex=True)
            # dataframe["id"] = pd.to_numeric(dataframe["id"].replace(r'^\s*$', 0, regex=True),downcast='integer')
            # dataframe["userId"] = pd.to_numeric(dataframe["userId"].replace(r'^\s*$', 0, regex=True),downcast='integer')
            # dataframe["completed"] = dataframe['completed'].str.lower().map({'true': True, 'false': False})
        return dataframe

    def filterExample(self,dataframe:pd.DataFrame,filter:str,typefilter:str):
        if dataframe is not None:
            if typefilter=='like':
                dataframe= dataframe[dataframe.apply(lambda row: row.astype(str).str.contains(filter, case=False).any(), axis=1)] # igual ao like %string%, mas procurando em todas as colunas
            elif typefilter=='start':
                dataframe= dataframe[dataframe.apply(lambda row: row.astype(str).str.match(filter, case=False).any(), axis=1)] # igual ao like string%, mas procurando em todas as colunas
        
        return dataframe