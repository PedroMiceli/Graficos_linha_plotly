import pandas as pd
from sqlalchemy import create_engine

def geradf_primeiro():
    engine = create_engine('postgresql://psicomotricidade:psicomotricidade@172.16.4.190:5432/psicomotricidade_teste').connect()
    df = pd.read_sql_table('primeira_unidade_funcional', engine)
    df = df.sort_values(by='id')
    return df
def geradf_segundo():
    engine = create_engine('postgresql://psicomotricidade:psicomotricidade@172.16.4.190:5432/psicomotricidade_teste').connect()
    df = pd.read_sql_table('segunda_unidade_funcional', engine)
    df = df.sort_values(by='id')
    return df

def geradf_terceiro():
    engine = create_engine('postgresql://psicomotricidade:psicomotricidade@172.16.4.190:5432/psicomotricidade_teste').connect()
    df = pd.read_sql_table('terceira_unidade_funcional', engine)
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
    dataframe1 = geradf_primeiro()
    dataframe2 = geradf_segundo()
    dataframe3 = geradf_terceiro()


    # -----------------Segunda unidade funcional------------------



    #-----------------TONICIDADE----------------------
    def conceitos_filogeneticos(self, dataframe, id):
        df=self.dataframe1[['id','paciente_id','rolar','engatinhar','rastejar']]
        df.columns = ['id', 'paciente_id', 'Rolar', 'Engatinhar', 'Rastejar']
        df=df[df['paciente_id']==id]
        return df.astype(int)

    def extensibilidade(self, dataframe, id):
        df = self.dataframe1[['id', 'paciente_id', 'extensibilidade_membros_superiores', 'extensibilidade_membros_inferiores']]
        df.columns = ['id', 'paciente_id', 'Membros superiores', 'Membros inferiores']
        df = df[df['paciente_id'] == id]
        return df

    def balanco_passivo(self, dataframe, id):
        df = self.dataframe1[['id', 'paciente_id', 'balanco_membros_superiores', 'balanco_membros_inferiores']]
        df.columns = ['id', 'paciente_id', 'Membros superiores', 'Membros inferiores']
        df = df[df['paciente_id'] == id]
        return df

    def paratonia(self, dataframe, id):
        df = self.dataframe1[['id', 'paciente_id', 'paratonia_membros_superiores', 'paratonia_membros_inferiores']]
        df.columns = ['id', 'paciente_id', 'Membros superiores', 'Membros inferiores']
        df = df[df['paciente_id'] == id]
        return df

    def diadococinesia(self, dataframe, id):
        df = self.dataframe1[['id', 'paciente_id', 'pronacao', 'supinacao']]
        df.columns = ['id', 'paciente_id', 'Pronação', 'Supinação']
        df = df[df['paciente_id'] == id]
        return df

    def sincinesia(self, dataframe, id):
        df = self.dataframe1[['id','paciente_id', 'sincinesia']]
        df.columns = ['id','paciente_id', 'Sincinesia']
        df = df[df['paciente_id'] == id]
        return df
    #-----------------EQUILIBRAÇÂO-------------------------------

    def imobilidade(self, dataframe, id):
        df = self.dataframe1[['id', 'paciente_id', 'imobilidade']]
        df.columns = ['id', 'paciente_id', 'Imobilidade']
        df = df[df['paciente_id'] == id]
        return df
    def equilibrio_estatico(self, dataframe, id):
        df = self.dataframe1[['id', 'paciente_id', 'equilibrio_estatico']]
        df.columns = ['id', 'paciente_id', 'Equilibrio estático']
        df = df[df['paciente_id'] == id]
        return df
    def equilibrio_dinamico_ponte(self, dataframe, id):
        df = self.dataframe1[['id', 'paciente_id', 'ponte_equilibrio_frente', 'ponte_equilibrio_tras', 'ponte_equilibrio_direita', 'ponte_equilibrio_esquerda']]
        df.columns = ['id', 'paciente_id', 'Frente', 'Trás', 'Direita', 'Esquerda']
        df = df[df['paciente_id'] == id]
        return df
    def equilibrio_dinamico_corda(self, dataframe, id):
        df = self.dataframe1[['id', 'paciente_id', 'corda_olhos_abertos', 'corda_olhos_fechados']]
        df.columns = ['id', 'paciente_id', 'Olhos Abertos', 'Olhos fechados']
        df = df[df['paciente_id'] == id]
        return df




    #-----------------Segunda unidade funcional------------------



    # -----------------Noção corporal----------------------
    def cinestesia(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'nomeia_pontos_tateis']]
        df.columns = ['id', 'paciente_id', 'Nomeia pontos táteis do corpo']
        df = df[df['paciente_id'] == id]
        return df
    def imitacao_de_gestos(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'imitacao_de_gestos']]
        df.columns = ['id', 'paciente_id', 'Imitação de gestos']
        df = df[df['paciente_id'] == id]
        return df
    def desenho_figura_humana(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'desenho_figura_humana']]
        df.columns = ['id', 'paciente_id', 'Desenho da figura humana']
        df = df[df['paciente_id'] == id]
        return df
    def auto_imagem(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'auto_imagem']]
        df.columns = ['id', 'paciente_id', 'Auto-Imagem']
        df = df[df['paciente_id'] == id]
        return df
    # -----------------Lateralização----------------------
    def lateralizacao_ocular(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'lateralizacao_ocular']]
        df.columns = ['id', 'paciente_id', 'Lateralização ocular']
        df = df[df['paciente_id'] == id]
        return df
    def lateralizacao_manual(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'lateralizacao_manual']]
        df.columns = ['id', 'paciente_id', 'Lateralização manual']
        df = df[df['paciente_id'] == id]
        return df
    def lateralizacao_pedal(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'lateralizacao_pedal']]
        df.columns = ['id', 'paciente_id', 'Lateralização pedal']
        df = df[df['paciente_id'] == id]
        return df
    def reconhecimento_direita_esquerda(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'reconhecimento_verbal', 'reconhecimento_gestual', 'reconhecimento_tatil']]
        df.columns = ['id', 'paciente_id', 'reconhecimento_verbal', 'Reconhecimento gestual', 'Reconhecimento tátil']
        df = df[df['paciente_id'] == id]
        return df

    # -----------------Estruturação Espaço Temporal----------------------
    def organizacao_perceptiva(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'organizacao_perceptiva']]
        df.columns = ['id', 'paciente_id', 'Organização perceptiva']
        df = df[df['paciente_id'] == id]
        return df
    def estruturacao_dinamica_espacial(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'estruturacao_dinamica_espacial']]
        df.columns = ['id', 'paciente_id', 'Estruturação dinâmica espacial']
        df = df[df['paciente_id'] == id]
        return df
    def representacao_topografica(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'representacao_topografica']]
        df.columns = ['id', 'paciente_id', 'Representação topográfica']
        df = df[df['paciente_id'] == id]
        return df
    def estruturacao_ritmica(self, dataframe, id):
        df = self.dataframe2[['id', 'paciente_id', 'transcodificacao_auditiva', 'transcodificacao_visual']]
        df.columns = ['id', 'paciente_id', 'Transcodificação auditiva', 'Transcodificação visual']
        df = df[df['paciente_id'] == id]
        return df



    #-----------------Terceira unidade funcional------------------




    # -----------------Praxia Global----------------------
    def coordenacao_oculo_manual(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'jogar_quatro_bolas', 'agarrar_bola_de_tenis']]
        df.columns = ['id', 'paciente_id', 'jogar quatro bolas', 'Agarrar bola de tênis']
        df = df[df['paciente_id'] == id]
        return df

    def coordenacao_oculo_pedal(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'quatro_chutes_ao_gol']]
        df.columns = ['id', 'paciente_id', 'Quatro chutes ao gol']
        df = df[df['paciente_id'] == id]
        return df

    def dissociacao(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'dissociacao_membros_superiores', 'dissociacao_membros_inferiores']]
        df.columns = ['id', 'paciente_id', 'Dissociação dos membros superiores', 'Dissociação dos membros inferiores']
        df = df[df['paciente_id'] == id]
        return df
    def agilidade(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'agilidade']]
        df.columns = ['id', 'paciente_id', 'Agilidade']
        df = df[df['paciente_id'] == id]
        return df

    # -----------------Praxia Fina----------------------
    def praxia_fina_pulseira_de_clipes(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'dissociacao_membros_superiores']]
        df.columns = ['id', 'paciente_id', 'Dissociação dos membros superiores']
        df = df[df['paciente_id'] == id]
        return df

    def praxia_fina_tamborilar(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'tamborilar']]
        df.columns = ['id', 'paciente_id', 'Tamborilar']
        df = df[df['paciente_id'] == id]
        return df

    def praxia_fina_velocidade_precisao(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'velocidade_precisao']]
        df.columns = ['id', 'paciente_id', 'Velocidade / Precisão']
        df = df[df['paciente_id'] == id]
        return df

    # -----------------Grafomotricidade----------------------
    def grafomotricidade_tracados(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'tracado_vertical', 'tracado_horizontal', 'tracado_zig_zag', 'tracado_curvo']]
        df.columns = ['id', 'paciente_id', 'Traçado vertical', 'Traçado horizontal', 'Traçado zig-zag', 'traçado curvo']
        df = df[df['paciente_id'] == id]
        return df

    def grafomotricidade_pontilhados(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'pontilhados']]
        df.columns = ['id', 'paciente_id', 'Pontilhados']
        df = df[df['paciente_id'] == id]
        return df

    def grafomotricidade_circulos(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'circulos']]
        df.columns = ['id', 'paciente_id', 'Círculos']
        df = df[df['paciente_id'] == id]
        return df

    def grafomotricidade_cruz(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'cruz']]
        df.columns = ['id', 'paciente_id', 'Cruz']
        df = df[df['paciente_id'] == id]
        return df

    def grafomotricidade_colorir(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'colorir_graficamente']]
        df.columns = ['id', 'paciente_id', 'Colorir graficamente']
        df = df[df['paciente_id'] == id]
        return df

    # -----------------Montar Quebra-Cabeça----------------------
    def montar_quebra_cabecas(self, dataframe, id):
        df = self.dataframe3[['id', 'paciente_id', 'montar_quebra_cabeca']]
        df.columns = ['id', 'paciente_id', 'Montar quebra-cabeças']
        df = df[df['paciente_id'] == id]
        return df