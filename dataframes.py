import pandas as pd
from sqlalchemy import create_engine
from graficos import *
import os


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






def executa_dataframes_e_graficos(id):


    if os.path.isfile('templates/graficos.html'):
        os.remove('templates/graficos.html')

    f = open('templates/graficos.html', 'w+')

    graficos = """<html>
        <head>
        <title>Graficos</title>
        </head>
        <body>
        <h2>Bem vindo aos Graficos Opentech</h2>
        <p></p>
        </body>
        </html>
        """
    f.write(f'{graficos}')
    f.close()

    # ---------------Gera os Dataframes ja filtrados -----------------------
    # ----------------------------Primeira Unidade Funcional----------------------
    relatorio1 = separa_por_passagens(separa_em_topicos().conceitos_filogeneticos(geradf_primeiro(), id))
    relatorio2 = separa_por_passagens(separa_em_topicos().extensibilidade(geradf_primeiro(), id))
    relatorio3 = separa_por_passagens(separa_em_topicos().balanco_passivo(geradf_primeiro(), id))
    relatorio4 = separa_por_passagens(separa_em_topicos().paratonia(geradf_primeiro(), id))
    relatorio5 = separa_por_passagens(separa_em_topicos().diadococinesia(geradf_primeiro(), id))
    relatorio6 = separa_por_passagens(separa_em_topicos().sincinesia(geradf_primeiro(), id))
    relatorio7 = separa_por_passagens(separa_em_topicos().imobilidade(geradf_primeiro(), id))
    relatorio8 = separa_por_passagens(separa_em_topicos().equilibrio_estatico(geradf_primeiro(), id))
    relatorio9 = separa_por_passagens(separa_em_topicos().equilibrio_dinamico_ponte(geradf_primeiro(), id))
    relatorio10 = separa_por_passagens(separa_em_topicos().equilibrio_dinamico_corda(geradf_primeiro(), id))
    # ----------------------------Segunda Unidade Funcional----------------------
    relatorio11 = separa_por_passagens(separa_em_topicos().cinestesia(geradf_segundo(), id))
    relatorio12 = separa_por_passagens(separa_em_topicos().imitacao_de_gestos(geradf_segundo(), id))
    relatorio13 = separa_por_passagens(separa_em_topicos().desenho_figura_humana(geradf_segundo(), id))
    relatorio14 = separa_por_passagens(separa_em_topicos().auto_imagem(geradf_segundo(), id))
    relatorio15 = separa_por_passagens(separa_em_topicos().lateralizacao_ocular(geradf_segundo(), id))
    relatorio16 = separa_por_passagens(separa_em_topicos().lateralizacao_manual(geradf_segundo(), id))
    relatorio17 = separa_por_passagens(separa_em_topicos().lateralizacao_pedal(geradf_segundo(), id))
    relatorio18 = separa_por_passagens(separa_em_topicos().reconhecimento_direita_esquerda(geradf_segundo(), id))
    relatorio19 = separa_por_passagens(separa_em_topicos().organizacao_perceptiva(geradf_segundo(), id))
    relatorio20 = separa_por_passagens(separa_em_topicos().estruturacao_dinamica_espacial(geradf_segundo(), id))
    relatorio21 = separa_por_passagens(separa_em_topicos().representacao_topografica(geradf_segundo(), id))
    relatorio22 = separa_por_passagens(separa_em_topicos().estruturacao_ritmica(geradf_segundo(), id))
    # ----------------------------Segunda Unidade Funcional----------------------
    relatorio23 = separa_por_passagens(separa_em_topicos().coordenacao_oculo_manual(geradf_terceiro(), id))
    relatorio24 = separa_por_passagens(separa_em_topicos().coordenacao_oculo_pedal(geradf_terceiro(), id))
    relatorio25 = separa_por_passagens(separa_em_topicos().dissociacao(geradf_terceiro(), id))
    relatorio26 = separa_por_passagens(separa_em_topicos().agilidade(geradf_terceiro(), id))
    relatorio27 = separa_por_passagens(separa_em_topicos().praxia_fina_pulseira_de_clipes(geradf_terceiro(), id))
    relatorio28 = separa_por_passagens(separa_em_topicos().praxia_fina_tamborilar(geradf_terceiro(), id))
    relatorio29 = separa_por_passagens(separa_em_topicos().praxia_fina_velocidade_precisao(geradf_terceiro(), id))
    relatorio30 = separa_por_passagens(separa_em_topicos().grafomotricidade_tracados(geradf_terceiro(), id))
    relatorio31 = separa_por_passagens(separa_em_topicos().grafomotricidade_pontilhados(geradf_terceiro(), id))
    relatorio32 = separa_por_passagens(separa_em_topicos().grafomotricidade_circulos(geradf_terceiro(), id))
    relatorio33 = separa_por_passagens(separa_em_topicos().grafomotricidade_cruz(geradf_terceiro(), id))
    relatorio34 = separa_por_passagens(separa_em_topicos().grafomotricidade_colorir(geradf_terceiro(), id))
    relatorio35 = separa_por_passagens(separa_em_topicos().montar_quebra_cabecas(geradf_terceiro(), id))

    # -------------Gera os graficos baseados nos dataframes de cima--------------

    # ----------------------------Primeira Unidade Funcional----------------------
    grafico_de_linha(relatorio1, 'Conceitos Filogeneticos', [1, 2, 3, 4])
    grafico_de_linha(relatorio2, 'Extensibilidade dos membros', ['Reduzida', 'Normal', 'Aumentada'])
    grafico_de_linha(relatorio3, 'Balanco Passivo',
                     ['Movimentos pendulares', 'Passivo e relaxado', 'Apresenta resistência'])
    grafico_de_linha(relatorio4, 'Paratonia', ['Com paratonia', 'Sem paratonia'])
    grafico_de_linha(relatorio5, 'Diadococinesia', [1, 2, 3, 4])
    grafico_de_barra(relatorio6, 'Sincinesia', ['Tônica', 'Tônica-cinética'])
    grafico_de_barra(relatorio7, 'Imobilidade', ['Sem imobilidade', 'Imobilidade parcial', 'Imobilidade integral'])
    grafico_de_barra(relatorio8, 'Equilíbrio estático', ['Sem rquilíbrio', '3 segundos', '5 segundos'])
    grafico_de_linha(relatorio9, 'Ponte de equilíbrio', [1, 2, 3, 4])
    grafico_de_linha(relatorio10, 'Pular uma corda estendida no chão', [1, 2, 3, 4])
    # ----------------------------Segunda Unidade Funcional----------------------
    grafico_de_barra(relatorio11, 'Nomeia pontos táteis do corpo',
                     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
    grafico_de_barra(relatorio12, 'Imitação de gestos',
                     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    grafico_de_barra(relatorio13, 'Desenho da figura humana',
                     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43])
    grafico_de_barra(relatorio14, 'Auto-Imagem', ['Não realizou', 'Realizou parcialmente', 'Realizou integralmente'])
    grafico_de_barra(relatorio15, 'Lateralização Ocular', ['Esquerda', 'Direita', 'Indefinida'])
    grafico_de_linha(relatorio16, 'Lateralização Manual', ['Esquerda', 'Direita', 'Indefinida'])
    grafico_de_linha(relatorio17, 'Lateralização Pedal', ['Esquerda', 'Direita', 'Indefinida'])
    grafico_de_linha(relatorio18, 'Reconhecimento Direita/Esquerda',
                     ['Não reconheceu', 'Reconhecimento parcial', 'Reconhecimento integral'])
    grafico_de_barra(relatorio19, 'Organização Perceptiva',
                     ['Não realizou', 'Realizou parcialmente', 'Realizou integralmente'])
    grafico_de_barra(relatorio20, 'Estruturação dinâmica espacial',
                     ['Não estruturou', 'Estruturou parcialmente', 'Estruturou integralmente'])
    grafico_de_barra(relatorio21, 'Representação topográfica',
                     ['Não representou', 'Representou parcialmente', 'Representou integralmente'])
    grafico_de_linha(relatorio22, 'Estruturação rítmica',
                     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    # ----------------------------Terceira Unidade Funcional----------------------
    grafico_de_linha(relatorio23, 'Coordenação Óculo-manual',
                     ['Não realizou', 'Realizou parcialmente', 'Realizou integralmente'])
    grafico_de_barra(relatorio24, 'Coordenação Óculo-pedal', [0, 1, 2, 3, 4])
    grafico_de_linha(relatorio25, 'Dissociação', [1, 2, 3, 4])
    grafico_de_linha(relatorio26, 'Agilidade', [1, 2, 3, 4])
    grafico_de_linha(relatorio27, 'Pulseira de clipes', ['Não realizou', '6 peças', '8 peças'])
    grafico_de_linha(relatorio28, 'Tamborilar', ['Não realizou', 'Realizou parcialmente', 'Realizou integralmente'])
    grafico_de_linha(relatorio29, 'Velocidade-Precisão',
                     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                      51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                      75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
                      99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115])
    grafico_de_linha(relatorio30, 'Traçados', [1, 2, 3, 4])
    grafico_de_linha(relatorio31, 'Pontilhados', [1, 2, 3, 4])
    grafico_de_linha(relatorio32, 'Círculos', [1, 2, 3, 4])
    grafico_de_linha(relatorio33, 'Cruz', [1, 2, 3, 4])
    grafico_de_linha(relatorio34, 'Colorir graficamente em diferentes posições', [1, 2, 3, 4])
    grafico_de_linha(relatorio35, 'Montar quebra-cabeça', ['Não realizou', '4 peças', '8 peças', '10 peças'])

