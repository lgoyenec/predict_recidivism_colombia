import pandas as pd
import numpy as np
import re
import unidecode


class Encoding():
    def __init__(self, query_obj):
        self.queries = query_obj
        
    def get_data(self):
        return self.queries.run('select * from persona \
                                 left join registro on persona.id_persona = registro.persona_id_persona \
                                 left join delito on delito.id_delito = registro.delito_id_delito')
    
    def one_hot(self, df):
        
        df = df.rename(columns={'nombre': 'delito'})
        counts = df['delito'].value_counts().to_frame()
        df.loc[df[~df['delito'].isin(counts.index[:10].values)].index, 'delito'] = 'OTRO'
            
        one_hot = pd.concat([df[['internoen','fecha_ingreso']],
                     pd.get_dummies(df.delito, prefix='delito'),
                     pd.get_dummies(df.tentativa, prefix='tentativa'),
                     pd.get_dummies(df.agravado, prefix='agravado'),
                     pd.get_dummies(df.calificado, prefix='calificado')],
                     axis = 1)
        one_hot = one_hot.groupby(['internoen','fecha_ingreso']).max().reset_index()
        
        col = df.columns.tolist()
        for c in ['delito_id_delito', 'id_delito', 'name_eng', 'delito', 'id_registro','id_persona',
                  'persona_id_persona','condicion_exepcional','tentativa','agravado','calificado',
                  'fecha_captura','anio_nacimiento', 'situacion_juridica','reincidente','municipio_id_municipio',
                  'id_subtitulo_delito']:
            col.remove(c)
        
        return df[col].drop_duplicates().merge(one_hot, on = ['internoen','fecha_ingreso'])