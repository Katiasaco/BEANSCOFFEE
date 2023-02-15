#-----------------------------LIBRERIAS-----------------------------
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt


#-----------------leer datos--------------------------
precio= pd.read_csv(r'C:\Users\katia\.vscode\examplecode\MODULO_3\TRABAJO FINAL\data\coffee-prices-historical-chart-data.csv')
precio.fillna(0, inplace=True) 
precio["date"] = pd.to_datetime(precio["date"])
precio['year'] = precio['date'].dt.year


st.set_page_config(page_title="www.beanscoffee.com")



#INTRODUCCION ------------
st.markdown("<h1 style='text-align: center;width:800; color: WHITE;'>BEANS COFFEE</h1>", unsafe_allow_html=True)

st.write ('Vive una experiencia sensitiva y mágica probando nuestro café de calidad. Desde Beans Coffee queremos hacer llegar CALIDAD a cada rincón de cada país, por eso es que exportamos todo tipo de café de cada región. Nos importas, por eso es que pensamos en cada detalle en nuestro servicio, donde destacamos la sencillez y alta gama del empaquetado, calidad, seguridad en transporte y buen precio.')

# Mostrar la imagen
st.image('eje.jpg')



### TAB PARA ORDENAR LA PÁGINA --------------------
tabs = st.tabs(['HISTORIA', 'CAFÉ', 'CLIENTES'])      
        
tab_plots = tabs[0]

with tab_plots:
    st.markdown("<h1 style='text-align: center; color: WHITE;'>¿QUIÉNES SOMOS?</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .cursiva {
            font-style: italic;
        }
        </style>
        """
        , unsafe_allow_html=True)

    texto = "MISIÓN: Satisfacer a nuestros clientes con nuestra excelente calidad de café, diferenciándonos de otras marcas por nuestra permanente consistencia en la calidad de nuestro café y servicio. Somos una empresa dedicada  a la comercialización de café tostado, molido y en grano.  Fundada por un solido equipo humano con amplia experiencia en el negocio del café. Nuestro café es producido en zonas cafetaleras que ofrecen condiciones ideales para su producción y procesado y producido además en una variedad de microclimas que le confieren aquellas características y cualidades distintivas de cada región."
    st.write("<div class='cursiva'>{}</div>".format(texto), unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image('valle.jpg')

    with col2:
        st.image('grano.jpg')


    st.markdown(
        """
        <style>
        .cursiva {
            font-style: italic;
        }
        </style>
        """
        , unsafe_allow_html=True)

    texto = "VISIÓN: Ser líderes en la producción, industrialización y distribución de café tostado y molido en el mercado nacional e internacional.Somos una empresa integral, comprometida con nuestra calidad y con nuestras responsabilidades sociales y medio ambientales.En Beans Coffee nos regimos por un código de ética y valores que nos caracteriza en la relación con los clientes y colaboradores, manteniendo una profesional relación de confidencialidad."
    st.write("<div class='cursiva'>{}</div>".format(texto), unsafe_allow_html=True)

tab_plots = tabs[1]

with tab_plots:

    col1, col2 = st.columns(2)
    with col1:
        st.image('1k.png')
        st.image('2k.png')
        st.image('6k.png')

    with col2:
        st.image('3k.png')
        st.image('4k.png')
        st.image('5k.png')

    if st.button('Curso Late Art'):
        ('[Click Here](https://www.scoolinary.com/collections?category=barista&gclid=CjwKCAiA85efBhBbEiwAD7oLQBpHLMTRinAzkmyH2i2vwZFcW6fM4oz92dnnssGrFw2XqWYA1ddlmBoCj50QAvD_BwE)')

tab_plots = tabs[2]
with tab_plots:
    st.markdown("<h1 style='text-align: center; color: WHITE;'>Opiniones de nuestros clientes </h1>", unsafe_allow_html=True)
    st.markdown(
            """
            <style>
            .cursiva {
                font-style: italic;
            }
            </style>
            """
            , unsafe_allow_html=True)
    texto = "Para Beans Coffee es muy importante el contacto directo con el cliente ya que toda duda o sugerencia es solucionada por nuestro equipo en menos de 48 horas."
    st.write("<div class='cursiva'>{}</div>".format(texto), unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.video('carrusel1.mp4')

    with col2: 
        st.image('go.png',width=500)



##SIDEBAR-----------
    st.sidebar.image('logo.png',width=150)


    ## MAPA EJE CAFETERO
if st.sidebar.button('Eje Cafetero'):
    st.markdown("<h1 style='text-align: center; color: WHITE;'>EJE CAFETERO COLOMBIANO</h1>", unsafe_allow_html=True)
    st.write('El eje cafetero es una región geográfica, cultural, económica y ecológica de Colombia, ubicada en los departamentos de Caldas, Risaralda y Quindío, además de las regiones del noroccidente de Tolima, el suroeste de Antioquia, y el norte y oriente del Valle del Cauca,incluyendo las ciudades capitales de los cuatro primeros departamentos mencionados (Manizales, Pereira, Armenia e Ibagué, respectivamente).')
    col1, col2 = st.columns(2)
    with col1:
        st.image('mapa.png')
    with col2:
        st.image('cafex.jpg')
    st.write('Ubicado en el corazón del Quindío e inmerso en la riqueza natural del Eje Cafetero colombiano se encuentra el Parque del Café, catalogado como uno de los mejores de Latinoamérica.Su amplia oferta de servicio en un área de 58 hectáreas, brinda una experiencia llena de diversión, aprendizaje sobre la cultura cafetera y gran aventura entre atracciones mecánicas, shows y atractivos culturales; una experiencia inolvidable para vivir con familia y amigos.')
   



if st.sidebar.button('Precios'):

    st.title('GRÁFICO TEMPORAL DE PRECIOS DEL CAFÉ')
    import streamlit as st
    import plotly.express as px

    # Generar el gráfico con Plotly Express
    fig = px.bar(precio.groupby('year').sum(), y=' value', color=' value')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)


link = 'https://forms.gle/6QbkjxZ7QprWMV458'
def botonlink (link): 
    href = f"<a href= '{link}'>COMPRAR CAFÉ</a>" 
    st.sidebar.markdown(href, unsafe_allow_html=True)
botonlink(link)
    
    


