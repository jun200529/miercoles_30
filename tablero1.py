import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='centered', 
                   page_title='Talento tech',
                   page_icon=':smile:')

#Titulo de la pagina 
t1, t2= st.columns([0.3,0.7])
t1.image('descarga.jpeg', width=300)
t2.title('mi primer tablero')
t2.markdown('**tel:** 123| email:** youcaregato@gmail.com')

#secciones

steps = st.tabs(['pestaña 1', 'pestaña 2', 'pestaña $\sqrt{9}$','pestaña 4'])
with steps[0]:
    st.write('Estos solos graficos son de prueba')
    st.image('images.jpeg', width=10000)
    data={'Nombbre':['Adan', 'Eva', 'Cain', 'Abel'],'Fecha de nacimiento':[0, 0, 0, 0]}
    df=pd.DataFrame(data)
    st.table(df)
    st.dataframe(df)
    
with steps[1]:
    if st.button('Boton 1', key='boton1'):
        st.session_state['boton1_presionado'] = True

    if st.session_state.get('boton1_presionado', False):
        st.write('Boton 1 presionado')
        

with steps[2]:
    st.selectbox('escoja una opcion, [1,2,3]', ['opcion 1','opcion 2','opcion 3'], key='selectbox1')

with steps[3]:
    camp_df = pd.read_csv('Campanhas.csv', encoding='latin-1', sep=';')
    camp = st.selectbox('Escoge un ID de campaña', camp_df['ID_Campana'], help='Selecciona un ID de campaña')
    
    met_df = pd.read_csv('Metricas.csv', encoding='latin-1', sep=';')
    
    m1, m2, m3= st.columns([1,1,1])
    
    id1 = met_df[(met_df['ID_Campana']==camp)]#|(met_df['ID_Campana']==1)]
    id2 = met_df[met_df['ID_Campana']==camp]
    m1.write('Metricas filtradas: ')
    m1.metric(label='Metrica 1',value=sum(id1['Conversiones']),
              delta=str(sum(id1['Rebotes']))+'total de Rebotes',
              delta_color='inverse')
    m2.metric(label='Metrica 2',value=np.mean(id2['Clics']),
              delta=str(np.mean(id2['Impresiones']))+'total de Rebotes',
              delta_color='inverse')
    
    with steps[3]:
        
        df=pd.read_csv("https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso1/master/s03/dataVentas2009.csv")
        df.Fecha = pd.to_datetime(df.Fecha, format='%d/%m/%Y')
        df.set_index('Fecha', inplace=True)
        st.table(df)
        varx=st.selectbox('Escoge la variable x ', df.columns)
        #vary=st.selectbox('Escoge la variable y ', met_df['Clic'])
        fig, ax = plt.subplots()
        ax=sns.histplot(data=df, x=varx)
        st.pyplot(fig)
        
        
