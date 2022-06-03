import plotly.graph_objects as go

def grafico_de_linha(dataframe, nome, ordem):
    categorias = dataframe[0].columns.values
    ordem = ordem
    fig = go.Figure()
    conta = 0
    for i in dataframe:

        valores = None
        for itens in i.values:
            valores = itens

        fig.add_trace(go.Scatter(
            x= categorias,
            y=valores,
            name=f'{conta + 1}ª passagem'

        ))
        conta += 1

    fig.update_layout(
        autosize=True,
        width=800,
        height=450,
        margin_l=200,
        template='xgridoff',
        margin_r=80,

        xaxis = dict(
            showgrid=True,
            showspikes=False,
            ticklabelposition="outside right",
            tickfont=dict(size=12),
        ),

        yaxis = dict(
            showgrid=True,
            tickmode='linear',
            autorange = True,
            categoryorder='array',
            categoryarray= ordem,
            range=[-0.5,3.5]
        ),

        title = dict(
            font=dict(
             size=26,
             color='black'
            ),
            text=f'{nome}'
        )
    )

    with open('templates/graficos.html', 'a') as f:
        f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))


def grafico_de_barra(dataframe, nome, ordem):
    categorias = dataframe[0].columns.values

    fig = go.Figure()
    conta = 0
    for i in dataframe:

        valores = None
        for itens in i.values:
            valores = itens

        fig.add_trace(go.Bar(
            x= categorias,
            y= valores,
            name=f'{conta + 1}ª passagem',
            marker = {"line": {"width": 3, "color": "rgb(0,0,0)"}}
        ))
        conta += 1

    fig.update_layout(
        autosize=False,
        width=800,
        height=450,
        template='xgridoff',
        margin_l=200,
        bargap=0.30,
        bargroupgap=0.3,

        xaxis = dict(
            showgrid=True,
            showspikes=False,

        ),
        xaxis_tickfont=dict(size=18),
        yaxis = dict(
            showgrid=True,
            tickmode='linear',
            autorange = True,
            range=[-1, 4],
            zeroline = True,
            categoryorder='array',
            categoryarray=ordem,
        ),
        title = dict(
            font=dict(
             size=26,
             color='black'
            ),
            text=f'{nome}'
        )
    )

    with open('templates/graficos.html', 'a') as f:
        f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))


