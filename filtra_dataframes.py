from dataframes import separa_em_topicos, separa_por_passagens, geradf
from graficos import *
import os


#---------------Dataframes para graficos-----------------



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

#---------------Gera os Dataframes ja filtrados -----------------------

id= 14
relatorio0 = separa_por_passagens(separa_em_topicos().conceitos_filogeneticos(geradf(), id))
relatorio1 = separa_por_passagens(separa_em_topicos().extensibilidade(geradf(), id))


#-------------Gera os graficos baseados nos dataframes de cima--------------

grafico_de_linha(relatorio0, 'Conceitos Filogeneticos')
grafico_de_linha(relatorio1, 'Extensibilidade dos membros')

