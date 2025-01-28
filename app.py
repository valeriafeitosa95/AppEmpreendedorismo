import streamlit as st
import pandas as pd
import plotly.express as px

# Layout da página
st.set_page_config(page_title='Empreendedorismo Jundiaí', layout='wide', page_icon= ':coffee:')

# Link CSS
with open('style.css') as f:st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Título
st.title('Análise sobre Microempresas em Jundiaí-SP')
st.write('---')

# Barra lateral
st.sidebar.success('## **Aqui você encontra**:mag_right:')
st.sidebar.html("<a href='#c0b565a4'>Empresas Abertas e Extintas</a>")
st.sidebar.html("<a href='#f8a4799b'>Análise Ano a Ano</a>")
st.sidebar.html("<a href='#momento-atual'>Momento Atual</a>")
st.sidebar.html("<a href='#8c81a348'>Lista completa de atividades</a>")
st.sidebar.html("<a href='#finalizando'>Finalizando</a>")
st.sidebar.html("<a href='#bc7ba040'>Sobre esta página</a>")
st.sidebar.html("<a href='#saiba-mais'>Saiba mais</a>")
                                              
# Introdução
dfDados = pd.read_csv('data/Dados.csv', sep=';', decimal='.')
st.write("""
Atualmente a cidade de Jundiaí possui 72.541 empresas, destas 61.356 são microempresas (ME), incluindo a opção MEI e não MEI.
Considerando que este total é relativo a todos os anos de dados históricos, a análise a seguir mostrará somente dados a partir de 2020.
""")
st.write('---')

# Gráfico abertas x extintas
fig = px.bar(dfDados, x='Ano', y= ['Abertas','Extintas'], title= 'Empresas Abertas e Extintas por Ano', barmode='group', text_auto=True)
fig.update_yaxes(title = 'Quantidade (em milhares)', color='white')
fig.update_xaxes(title = ' ')
fig.update_layout(font={'family':'Arial','size': 16, 'color': 'white'})
fig.update_layout(showlegend=True, legend_title='Empresas')
fig.update_traces (textfont_size = 12 ,  textangle = 0 ,  textposition = "outside",  cliponaxis = False ) 
st.plotly_chart(fig)
st.caption('Fonte: Base de dados do Cadastro Nacional da Pessoa Jurídica (CNPJ). Dados até o mês de dezembro/2024.')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

# Análise entre os anos
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
with col1:
     st.write(' ')
     st.write(' ')
     st.write(' ')
     st.write(' ')
     st.image('img/abertas.png', caption='pt.vecteezy.com', width=450)
with col2:
     st.write('### Análise Ano a Ano')
     st.write('Olhando apenas para o número de microempresas que abriram:')
     st.write(':ballot_box_with_check: O ano de 2021 apresenta um aumento de 21% em relação ao ano anterior.')
     st.write(':ballot_box_with_check: Em 2022, esse número cresceu 22%.')
     st.write(':ballot_box_with_check: No ano de 2023,  28%.')
     st.write(''':ballot_box_with_check: Já em 2024, temos um aumento de 43% em relação a 2020.
     A média mensal de 2024 foi de, aproximadamente, 1121 empresas, em comparação com 2020, que foi de 782.''')
     st.write(' ')
     st.write(' ')
     st.write(' ')
     st.write(' ')
with col3:
     st.write(' ')
     st.write(' ')
     st.write(''' Agora, considerando apenas o número de empresas que foram extintas, 
     observa-se um crescimento constante de 2020 até 2024 e podemos dizer que é um aumento diretamente proporcional,
     já que conforme um número sobe o outro também, o que quer dizer que algumas empresas fecharam, mas muitas outras abriram.
     ''')   
     st.write('''As causas não foram investigadas, mas podem incluir diversos fatores que variam de empresa para empresa.
          Contudo, vale lembrar que de 2020 até o início de 2023 fomos fortemente abalados pela pandemia da Covid-19,
          uma das principais responsáveis pelo fechamento de muitos comércios.''')
with col4:
     st.write(' ')
     st.write(' ')
     st.image('img/fechadas.png', caption='flatcon.com', width=350)
st.write(' ')    
st.write(' ')    
st.write(' ') 
st.write(' ') 
st.write(' ') 

# Compreensão do momento
col5, col6 = st.columns(2)
with col5:
     st.header('Momento atual')
with col6: 
     st.write('')
     st.html('<div class="tooltip"><div class="icon">🛈</div><span class="tooltiptext">Passe o mouse sobre as barras para visualizar os valores.</span></div>')

# Gráfico Mais Atividades
dfAtividade = pd.read_csv('data/Atividade.csv', sep=';', decimal='.')
fig = px.bar(dfAtividade.head(10).sort_values(by='Quantidade'), x='Quantidade',y= 'Atividade', 
             title= 'Top 10 atividades com mais microempresas ativas', color='Quantidade')
fig.update_xaxes(title = 'Microempresas',titlefont={'family':'Arial','size': 16, 'color': 'white'})
fig.update_yaxes(title=' ')
fig.update_layout(titlefont={'family':'Arial','size': 22, 'color': 'white'})
fig.update_layout(font={'family':'Arial','size': 12, 'color': 'white'})
st.plotly_chart(fig, use_container_width=True)

# Gráfico Menos Atividade
dfMenos = pd.read_csv('data/AtMenos.csv', sep=';', decimal='.', encoding='UTF-8')
fig = px.bar(dfMenos.sort_values(by='Quantidade'), x='Quantidade',y= 'Atividade', 
             title='Top 10 atividades com menos microempresas ativas', color='Quantidade')
fig.update_xaxes(title = 'Microempresas', titlefont={'family':'Arial','size': 16, 'color': 'white'})
fig.update_yaxes(title = ' ')
fig.update_layout(titlefont={'family':'Arial','size': 22, 'color': 'white'})
fig.update_layout(font={'family':'Arial','size': 12, 'color': 'white'})
st.plotly_chart(fig, use_container_width=True)
st.caption('Fonte: Base de dados do Cadastro Nacional da Pessoa Jurídica (CNPJ). Dados até o mês de dezembro/2024.')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

st.write('Após analisarmos os números individualmente, devemos agora combinar os dois parâmetros.')
st.write('''A diferença entre o número de estabelecimentos abertos e fechados é o real aumento de microempresas ativas, o saldo positivo.
         Por esse ângulo, o ano com o melhor resultado é 2021, com 7.371 microempresas a mais no total da cidade. Em 2020 o saldo foi de 6.545,
         e em 2022 vai para 6.561.''')
st.write('No ano de 2023, um pouco menos mas ainda muito bom, 5.963 microempresas, e em 2024, um total de 6.213.' )
st.write('No fim das contas, Jundiaí teve, nos últimos 5 anos, um saldo positivo médio de 6.532 microempresas a mais anualmente.')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

# Lista de todas as atividades
dfAtividade = pd.read_csv('data/Atividade.csv', sep=';', decimal='.', encoding='UTF-8')
st.write('### Lista completa de atividades econômicas')
st.write(' ')
st.data_editor(dfAtividade, column_config={'Atividade': st.column_config.TextColumn('Atividade')}, hide_index=True)
st.caption('Fonte: Base de dados do Cadastro Nacional da Pessoa Jurídica (CNPJ). Dados até o mês de dezembro/2024.')
st.write(' ')
st.write(' ')

# Conclusão
st.write(' ')
st.write('### Finalizando ...')
st.write('''Mesmo com seus altos e baixos, a cidade vem demonstrando que está voltando a crescer, e, com o mercado aquecido, o momento para empreender é muito favorável. 
      Com muitos incentivos vindos do município e de seus vizinhos, hoje é possível encontrar muita informação para apoiar quem deseja começar seu negócio e há espaços especialmente
      pensados para microempreendedores que precisam de direcionamento. Ao final desta leitura, você encontra o caminho até estes locais.''')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

# Rodapé
st.write('### Sobre esta página')
with st.container(border=True):
    st.caption('Projeto de pesquisa e análise de dados desenvolvido para atividade extensionista do Centro Universitário Internacional UNINTER.')
    st.caption('Este projeto baseia-se nos Objetivos de Desenvolvimento Sustentável (ODS) 5 e 8 da Organização das Nações Unidade (ONU).')
    col7, col8, col9, col10, col11 = st.columns(5)
    with col7:
        st.image('img/ODS5.jpg', width=150)
    with col8:
        st.image('img/ODS8.jpg', width=150)
st.write(' ')
st.write(' ')

# Indicação
st.write('---')
st.write('### Saiba Mais ')
st.link_button('Balcão do Empreendedor',url='https://balcaodoempreendedor.jundiai.sp.gov.br/')
st.link_button('Negócios Jundiaí',url= 'https://negocios.jundiai.sp.gov.br/')
st.link_button('Empreendedorismo em Jundiaí', url='https://www.plataformadosmunicipios.com.br/empreendedorismo-em-jundiai-cidade-e-uma-das-melhores-do-brasil/')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write('👇 :blue[Baixe os arquivos desta pesquisa e não se esqueça de compartilhar.] ')
st.page_link(page='https://empreendedorismojundiai-arquivos.netlify.app/', label='Clique aqui',
             help='Você será redirecionado para outra página.')
