import pandas as pd
from sqlalchemy import create_engine

def geradf():
    engine = create_engine('postgresql://psicomotricidade:psicomotricidade@172.16.4.190:5432/psicomotricidade_teste').connect()
    df = pd.read_sql_table('primeira_unidade_funcional', engine)
    df = df.sort_values(by='id')
    return df



def separa_por_passagens(df):
    df = df
    df_int= int(df.__len__())

    posicoes = []
    for i in df['id']:
        posicoes.append(i)

    if df_int <= 1:

        print('dados insuficientes')

    elif df_int == 2:

        df1= df[df['id']==posicoes[0]]
        df2 = df[df['id'] == posicoes[1]]
        df1 = df1.drop(columns=['id','paciente_id'])
        df2 = df2.drop(columns=['id', 'paciente_id'])
        frames = [df1,df2]
        return frames

    elif df_int == 3:

        df1 = df[df['id'] == posicoes[0]]
        df2 = df[df['id'] == posicoes[1]]
        df3 = df[df['id'] == posicoes[2]]
        df1 = df1.drop(columns=['id', 'paciente_id'])
        df2 = df2.drop(columns=['id', 'paciente_id'])
        df3 = df3.drop(columns=['id', 'paciente_id'])
        frames = [df1, df2, df3]
        return frames



class separa_em_topicos:
    dataframe = geradf()

    def conceitos_filogeneticos(self, dataframe, id):
        df=self.dataframe[['id','paciente_id','rolar','engatinhar','rastejar']]
        df.columns = ['id', 'paciente_id', 'Rolar', 'Engatinhar', 'Rastejar']
        df=df[df['paciente_id']==id]
        return df.astype(int)
    def extensibilidade(self, dataframe, id):
        df = self.dataframe[['id', 'paciente_id', 'extensibilidade_membros_superiores', 'extensibilidade_membros_inferiores']]
        df.columns = ['id', 'paciente_id', 'Extensibilidade dos membros superiores', 'Extensibilidade dos membros inferiores']
        df = df[df['paciente_id'] == id]
        return df


