import pandas as pd
import plotly.graph_objects as go
import psycopg2
from sqlalchemy import create_engine

def geradf():
    engine = create_engine('postgresql://psicomotricidade:psicomotricidade@172.16.4.190:5432/psicomotricidade_teste').connect()
    df = pd.read_sql_table('protocolos', engine)
    df = df.sort_values(by='id')
    return df

class separa_em_topicos():
    df = geradf()

    def conceitos_filogeneticos(self):
        df=self.df[['id','rolar','engatinhar_quatro_apoios','rastejar','posicao_bipede']]
        return df

    def coordenacao_oculopedal_oculomanual(self):
        df = self.df[['id', 'apoio_unipodal_bracos_torax', 'saltar_dois_apoios', 'saltar_um_apoio','saltar_alternadamente','corrida_de_obstaculos','chutar_bola','atirar_bola','agilidade_movimentos_globais']]
        return df

    def extensibilidade_dos_membros(self):
        df = self.df[['id', 'extensibilidade_membros_inferiores', 'extensibilidade_membros_superiores', 'balanco_passivo','acao_paratonia','relaxamento_passivo','sustentabilidade_bracos','sincinesias','persistencia_motora_global','freio_inibitorio','membros_inferiores','membros_superiores']]
        return df
    def equilibrio_postural(self):
        df = self.df[
            ['id', 'ponte_equilibrio_frente', 'ponte_equilibrio_tras', 'permanece_ponta_pes']]
        return df


print(separa_em_topicos().equilibrio_postural())



class graficos():

    class graficolinha():
        print('teste')

    class graficoradar():
        print('teste')

