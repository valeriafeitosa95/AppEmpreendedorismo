import streamlit as st
import pandas as pd
import plotly.express as px

# Layout da página
st.set_page_config(page_title='Empreendedorismo Jundiaí', layout='wide', page_icon= ':coffee:')

# Título
st.title('Análise sobre Microempresas em Jundiaí-SP')
st.write('---')

# Barra lateral
st.sidebar.success('## •**Aqui você encontra**:mag_right:')
st.sidebar.write('• Empresas Abertas x Extintas')
st.sidebar.write('• Análisea Ano a Ano')
st.sidebar.write('• Atividades com mais empresas')
st.sidebar.write('• Atividades com menos empresas')                                              
st.sidebar.write('• Lista completa de atividades')
st.sidebar.write('• Finalizando')
st.sidebar.write('• Sobre esta página')
st.sidebar.write('• Saiba mais')
    
# Introdução
dfAno = pd.read_csv('Dados.csv', sep=';', decimal='.')
st.write("""
Atualmente a cidade de Jundiaí possui 58.517 microempresas(ME) ativas, incluindo MEI.
Considerando que este total é relativo a todos os anos de dados históricos, a análise a seguir mostrará somente dados a partir de 2020.
""")
st.write('---')

# Gráfico abertas x extintas
fig = px.bar(dfAno, x='Ano', y= ['Abertas','Extintas'], title= 'Empresas Abertas e Extintas por Ano', barmode='group')
fig.update_yaxes(title = 'Quantidade (em milhares)', color='white')
fig.update_xaxes(title = 'Ano', color='white')
fig.update_layout(font={'family':'Arial','size': 16, 'color': 'white'})
fig.update_layout(titlefont={'family':'Arial','size': 22, 'color': 'white'})
fig.update_layout(showlegend=True, legend_title='Empresas')
st.plotly_chart(fig)
st.caption('Fonte: Base de dados do Cadastro Nacional da Pessoa Jurídica (CNPJ). Dados até o mês de Agosto/2024.')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')


# Análise entre os anos
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
with col1:
     st.image('abertas.png', caption='pt.vecteezy.com', width=550)
with col2:
     st.write('### Análise Ano a Ano')
     st.write('Olhando apenas para o número de microempresas que abriram:')
     st.write(':ballot_box_with_check: O ano de 2021 apresenta um crescimento de 21% em relação ao ano anterior.')
     st.write(':ballot_box_with_check: Em em 2022, esse número cresceu 22%.')
     st.write(':ballot_box_with_check: No ano de 2023, o crescimento foi de 28%.')
     st.write(''':ballot_box_with_check: Já em 2024, a quantidade de microempresas abertas até agora já é maior do que no ano inteiro de 2020.
     A média mensal, até agosto, é de 1.178, em comparação com 2020, que foi de 782.
     Se considerarmos apenas o mesmo período, essa média cai para 749.''')
     st.write('Mantendo esse ritmo, podemos fechar o ano com um crescimento de até 51% em relação ao primeiro analisado.')
     st.write(' ')
     st.write(' ')
with col3:
     st.write(''' 
     Agora, considerando apenas o número de empresas que foram extintas, 
     observa-se um crescimento constante nos números entre os anos de 2020 até 2023, caindo em 2024, com os dados até o mês de agosto. 
     ''')   
     st.write('''Como as causas não foram investigadas, podem incluir diversos fatores que variam de empresa para empresa.
          Contudo, vale lembrar que entre 2020 até o início de 2023 fomos fortemente abalados pela pandemia da Covid-19,
          um dos principais responsáveis pelo fechamento de muitos comércios.''')
with col4:
     st.image('fechadas.png', caption='flatcon.com', width=400)
    
# Compreensão do momento
st.header('Momento atual')

# Gráfico Mais Atividades
dfAtMais = pd.read_csv('MEI-AtMais.csv', sep=';', decimal='.', encoding='UTF-8')
fig = px.bar(dfAtMais.sort_values(by='Quantidade'), x='Quantidade',y= 'Atividade', 
             title= 'Top 10 atividades com mais microempresas ativas', color='Quantidade')
fig.update_xaxes(title = 'Microempresas',titlefont={'family':'Arial','size': 16, 'color': 'white'})
fig.update_yaxes(titlefont={'family':'Arial','size': 16, 'color': 'white'})
fig.update_layout(titlefont={'family':'Arial','size': 22, 'color': 'white'})
fig.update_layout(font={'family':'Arial','size': 12, 'color': 'white'})
st.plotly_chart(fig, use_container_width=True)

# Gráfico Menos Atividade
dfAtMenos = pd.read_csv('MEI-AtMenos.csv', sep=';', decimal='.', encoding='UTF-8')
fig = px.bar(dfAtMenos.sort_values(by='Quantidade'), x='Quantidade',y= 'Atividade', 
             title='Top 10 atividades com menos microempresas ativas', color='Quantidade')
fig.update_xaxes(title = 'Microempresas', titlefont={'family':'Arial','size': 16, 'color': 'white'})
fig.update_yaxes(title = 'Atividade', titlefont={'family':'Arial','size': 16, 'color': 'white'})
fig.update_layout(titlefont={'family':'Arial','size': 22, 'color': 'white'})
fig.update_layout(font={'family':'Arial','size': 12, 'color': 'white'})
st.plotly_chart(fig, use_container_width=True)
st.caption('Fonte: Base de dados do Cadastro Nacional da Pessoa Jurídica (CNPJ). Dados até o mês de Agosto/2024.')
st.write(' ')
st.write(' ')

st.write('Após analisarmos os números individualmente, devemos agora combinarmos os dois parâmetros.')
st.write('''A diferença entre o número de abertas e extintas é o real aumento de microempresas ativas.
         Por esse ângulo, o ano com o melhor saldo é 2021, com 7.385 microempresas a mais na cidade, em 2020 esse aumento foi de 6.539,
         e em 2022 vai para 6.563.''')
st.write('''No ano de 2023, embora a quantidade de microempresas abertas tenha sido maior, a cidade ganhou 5.963 microempresas, menos que nos outros anos. 
         Em 2024, até agora o aumento é 4.512 microempresas a mais, ou seja, mais da metade de 2021 inteiro.''')

# Lista de todas as atividades
dfAtividade = pd.read_csv('MEI-Atividade.csv', sep=';', decimal='.', encoding='UTF-8')
st.write('### Lista completa de atividades exercidas em Jundiaí')
st.write(' ')
st.data_editor(dfAtividade, column_config={'Atividade': st.column_config.TextColumn('Atividade')}, hide_index=True)
st.caption('Fonte: Base de dados do Cadastro Nacional da Pessoa Jurídica (CNPJ). Dados até o mês de Agosto/2024')

# Conclusão
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write('### Finalizando ...')
st.write('''Mesmo com seus altos e baixos,
      a cidade vem demonstrando que está voltando a crescer e o momento para empreender é muito favorável. 
      Com muitos incentivos vindo do município e de seus vizinhos,
      hoje é possível encontrar muita informação para apoiar quem deseja começar seu negócio e há espaços especialmente
      direcionados para microempreendedores que precisam desse direcionamento.
         ''')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')


# Rodapé
st.write('### Sobre esta página')
with st.container(border=True):
    st.caption('Projeto de pesquisa e análise de dados desenvolvido para atividade extensionista do Centro Universitário Internacional UNINTER.')
    st.caption('Este projeto baseia-se nos Objetivos de Desenvolvimento Sustentável (ODS) 5 e 8 da Organização das Nações Unidade (ONU).')
    col5, col6, col7, col8, col9 = st.columns(5)
    with col5:
        st.image('ODS5.jpg', width=150)
    with col6:
        st.image('ODS8.jpg', width=150)
st.write(' ')
st.write(' ')

# Indicação
st.write('---')


st.write('### Saiba Mais ')
st.link_button('Balcão do Empreendedor',url='https://balcaodoempreendedor.jundiai.sp.gov.br/')
st.link_button('Negócios Jundiaí',url= 'https://negocios.jundiai.sp.gov.br/')
st.link_button('Empreendedorismo em Jundiaí', url='https://www.plataformadosmunicipios.com.br/empreendedorismo-em-jundiai-cidade-e-uma-das-melhores-do-brasil/')
