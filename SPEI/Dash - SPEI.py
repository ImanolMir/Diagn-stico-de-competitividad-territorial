##############################################################################  IMPORTAR LIBRERIAS  ################################################################

import pandas as pd #Librería para tratar los dataframes
import numpy as np # Algebra lineal
import plotly.io as pio #Construye figuras a partir de archivos JSON
import plotly.express as px #Contruye figuras a partir de DataFrame
import dash #Librería que permite crear DashBoards
import dash_core_components as dcc #Da acceso a multiples objetos interactivos dropdown, checklist, slide, etc.
import dash_html_components as html #Permite redactar código html en el DashBoard
import dash_bootstrap_components as dbc #Ordena el layout de la página
from dash.dependencies import Input, Output #Habilita el uso de las funciones @callbacks
import base64 #Codifica la imagen en base 64

##############################################################################  DECLARAR TUPLAS  ################################################################

#Tupla de comarcas y territorios historicos
lista =('Bidasoa Beherea / Bajo Bidasoa','Durangaldea / Duranguesado','C.A. de Euskadi','Araba/Álava', 'Bizkaia', 'Gipuzkoa', 'Debabarrena / Bajo Deba','Debagoiena / Alto Deba','Donostialdea','Goierri','Tolosaldea','Urola Kosta','Enkartazioak / Encartaciones', 'Bilbo Handia / Gran Bilbao','Plentzia-Mungia','Gernika-Bermeo','Markina-Ondarroa','Arratia-Nerbioi / Arratia-Nervión','Añana','Arabako Errioxa / Rioja Alavesa','Arabako Kantaurialdea / Cantábrica Alavesa','Arabako Lautada / Llanada Alavesa','Arabako Mendialdea / Montaña Alavesa','Gorbeialdea / Estribaciones del Gorbea')

#Tuplas de nivel de estudio
nivel1 = ('Analfabetos', 'Sin estudios', 'Primarios', 'Secundarios', 'Medio-superiores', 'Superiores', 'Profesionales')

#Comarcas de gipuzkoa
# g_comarca = ('Bidasoa Beherea / Bajo Bidasoa', 'Debabarrena / Bajo Deba','Debagoiena / Alto Deba','Donostialdea','Goierri','Tolosaldea','Urola Kosta')

#Comarcas de Bizkaia
# b_comarca = ('Enkartazioak / Encartaciones', 'Bilbo Handia / Gran Bilbao','Plentzia-Mungia','Gernika-Bermeo','Markina-Ondarroa','Durangaldea / Duranguesado','Arratia-Nerbioi / Arratia-Nervión')

#Comarcas de Álava
# a_comarca = ('Añana','Arabako Errioxa / Rioja Alavesa','Arabako Kantaurialdea / Cantábrica Alavesa','Arabako Lautada / Llanada Alavesa','Arabako Mendialdea / Montaña Alavesa','Gorbeialdea / Estribaciones del Gorbea')

#Tupla territorio historico EUSTAT
th = ('Araba / Álava', 'Bizkaia', 'Gipuzkoa')

#Tupla de territorio historico LANBIDE
tA=['ARABA', 'GIPUZKOA', 'BIZKAIA']

#Tupla de comarcas LANBIDE
hA=['BAJO BIDASOA','DURANGUESADO','LLANADA ALAVESA', 'VALLE DE AIALA', 'ESTRIB. GORBEA','VALLES ALAVESES', 'RIOJA ALAVESA', 'MONTAÃ\x91A ALAVESA','VITORIA-GASTEIZ', 'TOLOSALDEA', 'UROLA ERDIA','DONOSTIALDEA OESTE', 'ALTO DEBA', 'GOIHERRI', 'UROLA KOSTA','BAJO DEBA', 'UROLA GARAIA',  'OARSOALDEA','DONOSTIA', 'MARGEN IZQUIERDA','ARRATIA - ZORNOTZA', 'LEA - ARTIBAI', 'MEDIO NERVION','ENCARTACIONES', 'URIBEALDEA', 'IBAIZABAL', 'BUSTURIALDE','BILBAO', 'GOBELA', 'TXORIERRI']

#Tupla de años en tapla paro LANBIDE
nivel = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]


##############################################################################  DECLARAR VARIABLES DE LOS DROPDOWNS  ################################################################

drop = [    {'label': 'C.A. de Euskadi', 'value': 'C.A. de Euskadi' },
            {'label': 'Bidasoa Beherea / Bajo Bidasoa', 'value': 'Bidasoa Beherea / Bajo Bidasoa'},
            {'label': 'Debabarrena / Bajo Deba', 'value': 'Debabarrena / Bajo Deba'},
            {'label': 'Debagoiena / Alto Deba', 'value': 'Debagoiena / Alto Deba'},
            {'label': 'Donostialdea', 'value': 'Donostialdea'},
            {'label': 'Goierri', 'value': 'Goierri'},
            {'label': 'Tolosaldea', 'value': 'Tolosaldea'},
            {'label': 'Urola Kosta', 'value': 'Urola Kosta'},
            {'label': 'Enkartazioak / Encartaciones', 'value': 'Enkartazioak / Encartaciones'},
            {'label': 'Bilbo Handia / Gran Bilbao', 'value': 'Bilbo Handia / Gran Bilbao'},
            {'label': 'Plentzia-Mungia', 'value': 'Plentzia-Mungia'},
            {'label': 'Gernika-Bermeo', 'value': 'Gernika-Bermeo'},
            {'label': 'Markina-Ondarroa', 'value': 'Markina-Ondarroa'},
            {'label': 'Durangaldea / Duranguesado', 'value': 'Durangaldea / Duranguesado'},
            {'label': 'Arratia-Nerbioi / Arratia-Nervión', 'value': 'Arratia-Nerbioi / Arratia-Nervión'},
            {'label': 'Añana', 'value': 'Añana'},
            {'label': 'Arabako Errioxa / Rioja Alavesa', 'value': 'Arabako Errioxa / Rioja Alavesa'},
            {'label': 'Arabako Kantaurialdea / Cantábrica Alavesa', 'value': 'Arabako Kantaurialdea / Cantábrica Alavesa'},
            {'label': 'Arabako Lautada / Llanada Alavesa', 'value': 'Arabako Lautada / Llanada Alavesa'},
            {'label': 'Arabako Mendialdea / Montaña Alavesa', 'value': 'Arabako Mendialdea / Montaña Alavesa'},
            {'label': 'Gorbeialdea / Estribaciones del Gorbea', 'value': 'Gorbeialdea / Estribaciones del Gorbea'},
            {'label': 'Araba/Álava', 'value': 'Araba/Álava'},
            {'label': 'Bizkaia', 'value': 'Bizkaia'},
            {'label': 'Gipuzkoa', 'value': 'Gipuzkoa'}
       ]

dropdp = [  {'label': 'C.A. de Euskadi', 'value': 'C.A. de Euskadi' },
            {'label': 'Enkartazioak / Encartaciones', 'value': 'Enkartazioak / Encartaciones'},
            {'label': 'Bilbo Handia / Gran Bilbao', 'value': 'Bilbo Handia / Gran Bilbao'},
            {'label': 'Plentzia-Mungia', 'value': 'Plentzia-Mungia'},
            {'label': 'Gernika-Bermeo', 'value': 'Gernika-Bermeo'},
            {'label': 'Markina-Ondarroa', 'value': 'Markina-Ondarroa'},
            {'label': 'Kantauri Arabarra / Cantábrica Alavesa', 'value': 'Kantauri Arabarra / Cantábrica Alavesa'},
            {'label': 'Gorbeia Inguruak / Estribaciones del Gorbea', 'value': 'Gorbeia Inguruak / Estribaciones del Gorbea'},
            {'label': 'Arratia Nerbioi / Arratia-Nervión', 'value': 'Arratia Nerbioi / Arratia-Nervión'},
            {'label': 'Durangaldea / Duranguesado', 'value': 'Durangaldea / Duranguesado'},
            {'label': 'Debabarrena / Bajo Deba', 'value': 'Debabarrena / Bajo Deba'},
            {'label': 'Urola-Kostaldea / Urola Costa', 'value': 'Urola-Kostaldea / Urola Costaa'},
            {'label': 'Donostialdea / Donostia-San Sebastián', 'value': 'Donostialdea / Donostia-San Sebastián'},
            {'label': 'Debagoiena / Alto Deba', 'value': 'Debagoiena / Alto Deba'},
            {'label': 'Goierri', 'value': 'Goierri'},
            {'label': 'Tolosaldea/Tolosa', 'value': 'Tolosaldea/Tolosa'},
            {'label': 'Bidasoa Beherea / Bajo Bidasoa', 'value': 'Bidasoa Beherea / Bajo Bidasoa'},
            {'label': 'Araba/Álava', 'value': 'Araba/Álava'},
            {'label': 'Bizkaia', 'value': 'Bizkaia'},
            {'label': 'Gipuzkoa', 'value': 'Gipuzkoa'}
        ]

dropinn = [ {'label': 'C.A. de Euskadi', 'value': 'C.A. de Euskadi' },
            {'label': 'Vitoria - Gasteiz', 'value': 'Vitoria - Gasteiz'},
            {'label': 'Bilbao', 'value': 'Bilbao'},
            {'label': 'Donostia - San Sebastian', 'value': 'Donostia - San Sebastian'},
            {'label': 'Araba/Álava', 'value': 'Araba/Álava'},
            {'label': 'Arabako Lautada  /  Llanada Alavesa', 'value': 'Arabako Lautada  /  Llanada Alavesa'},
            {'label': 'Errioxa Arabarra  /  Rioja Alavesa', 'value': 'Errioxa Arabarra  /  Rioja Alavesa'},
            {'label': 'Kantauri Arabarra  /  Cantábrica Alavesa', 'value': 'Kantauri Arabarra  /  Cantábrica Alavesa'},
            {'label': 'Arabako Besteak / Resto de Álava', 'value': 'Arabako Besteak / Resto de Álava'},
            {'label': 'Bizkaia', 'value': 'Bizkaia'},
            {'label': 'Arratia Nerbioi  /  Arratia-Nervión', 'value': 'Arratia Nerbioi  /  Arratia-Nervión'},
            {'label': 'Bilbo Handia  /  Gran Bilbao', 'value': 'Bilbo Handia  /  Gran Bilbao'},
            {'label': 'Durangaldea  /  Duranguesado', 'value': 'Durangaldea  /  Duranguesado'},
            {'label': 'Enkartazioak  /  Encartaciones', 'value': 'Enkartazioak  /  Encartaciones'},
            {'label': 'Gernika-Bermeo', 'value': 'Gernika-Bermeo'},
            {'label': 'Markina-Ondarroa', 'value': 'Markina-Ondarroa'},
            {'label': 'Plentzia-Mungia', 'value': 'Plentzia-Mungia'},
            {'label': 'Gipuzkoa', 'value': 'Gipuzkoa'},
            {'label': 'Bidasoa Beherea  /  Bajo Bidasoa', 'value': 'Bidasoa Beherea  /  Bajo Bidasoa'},
            {'label': 'Deba Beherea  /  Bajo Deba', 'value': 'Deba Beherea  /  Bajo Deba'},
            {'label': 'Debagoiena  /  Alto Deba', 'value': 'Debagoiena  /  Alto Deba'},
            {'label': 'Donostialdea', 'value': 'Donostialdea'},
            {'label': 'Goierri', 'value': 'Goierri'},
            {'label': 'Tolosaldea  /  Tolosa', 'value': 'Tolosaldea  /  Tolosa'},
            {'label': 'Urola-Kostaldea  /  Urola Costa', 'value': 'Urola-Kostaldea  /  Urola Costa'},
        ]
dropth = [  {'label': 'Araba / Álava', 'value': 'Araba / Álava' },
            {'label': 'Bizkaia', 'value': 'Bizkaia'},
            {'label': 'Gipuzkoa', 'value': 'Gipuzkoa'}
        ]



dropparo = [{'label': 'C.A. de Euskadi', 'value': 'C.A. de Euskadi' },
            {'label': 'LLANADA ALAVESA', 'value': 'LLANADA ALAVESA' },
            {'label': 'VALLE DE AIALA', 'value': 'VALLE DE AIALA' },
            {'label': 'ESTRIB. GORBEA', 'value': 'ESTRIB. GORBEA' },
            {'label': 'VALLES ALAVESES', 'value': 'VALLES ALAVESES' },
            {'label': 'RIOJA ALAVESA', 'value': 'RIOJA ALAVESA' },
            {'label': 'MONTAÑA ALAVESA', 'value': 'MONTAÃ\x91A ALAVESA' },
            {'label': 'VITORIA-GASTEIZ', 'value': 'VITORIA-GASTEIZ' },
            {'label': 'TOLOSALDEA', 'value': 'TOLOSALDEA' },
            {'label': 'UROLA ERDIA', 'value': 'UROLA ERDIA' },
            {'label': 'DONOSTIALDEA OESTE', 'value': 'DONOSTIALDEA OESTE' },
            {'label': 'ALTO DEBA', 'value': 'ALTO DEBA'},
            {'label': 'GOIHERRI', 'value': 'GOIHERRI'},
            {'label': 'UROLA KOSTA', 'value': 'UROLA KOSTA'},
            {'label': 'BAJO DEBA', 'value': 'BAJO DEBA'},
            {'label': 'UROLA GARAIA', 'value': 'UROLA GARAIA'},
            {'label': 'BAJO BIDASOA', 'value': 'BAJO BIDASOA'},
            {'label': 'OARSOALDEA', 'value': 'OARSOALDEA'},
            {'label': 'DONOSTIA', 'value': 'DONOSTIA'},
            {'label': 'DURANGUESADO', 'value': 'DURANGUESADO'},
            {'label': 'MARGEN IZQUIERDA', 'value': 'MARGEN IZQUIERDA'},
            {'label': 'ARRATIA - ZORNOTZA', 'value': 'ARRATIA - ZORNOTZA'},
            {'label': 'LEA - ARTIBAI', 'value': 'LEA - ARTIBAI'},
            {'label': 'MEDIO NERVION', 'value': 'MEDIO NERVION'},
            {'label': 'ENCARTACIONES', 'value': 'ENCARTACIONES'},
            {'label': 'URIBEALDEA', 'value': 'URIBEALDEA'},
            {'label': 'IBAIZABAL', 'value': 'IBAIZABAL'},
            {'label': 'BUSTURIALDE', 'value': 'BUSTURIALDE'},
            {'label': 'BILBAO', 'value': 'BILBAO'},
            {'label': 'GOBELA', 'value': 'GOBELA'},
            {'label': 'TXORIERRI', 'value': 'TXORIERRI'},
         ]

##############################################################################  DECLARAR IMAGENES EN BASE 64  ################################################################

test_png = '../SPEI/logo.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

dafo_png = '../SPEI/dafo.jpeg'
dafo_base64 = base64.b64encode(open(dafo_png, 'rb').read()).decode('ascii')

agencia_png = '../SPEI/agencias.jpeg'
agencia_base64 = base64.b64encode(open(agencia_png, 'rb').read()).decode('ascii')


##############################################################################  DEFINIR Y APLICAR TEMA & AJUSTE DE LAYOUT  ################################################################

#Selecciona el tema 
pio.templates.default = "plotly_white"

# Aplicación
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Img(src='data:image/png;base64,{}'.format(test_base64), style={'height':'auto', 'width':300}),
        html.H3("Diagnóstico", className="display-4"),
        html.Hr(),
        html.P("", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("PIB per cápita", href="/page-1", active="exact"),
                dbc.NavLink("Renta", href="/page-2", active="exact"),
                dbc.NavLink("Ocupación y paro", href="/page-3", active="exact"),
                dbc.NavLink("Población", href="/page-4", active="exact"),
                dbc.NavLink("Cualificación", href="/page-5", active="exact"),
                dbc.NavLink("Infraestructuras y sector publico", href="/page-14", active="exact"),
                dbc.NavLink("Tejido y dinamismo empresarial", href="/page-6", active="exact"),
                dbc.NavLink("Tamaño de las empresas", href="/page-7", active="exact"),
                dbc.NavLink("Instituciones para la colaboración", href="/page-15", active="exact"),
                dbc.NavLink("Internacionalización", href="/page-8", active="exact"),
                dbc.NavLink("Investigación, desarrollo e innovación", href="/page-9", active="exact"),
                dbc.NavLink("Distribución sectorial de la población ocupada", href="/page-10", active="exact"),
                dbc.NavLink("Valor añadido bruto por sector de actividad", href="/page-11", active="exact"),
                dbc.NavLink("Desempeño competitivo", href="/page-12", active="exact"),
                dbc.NavLink("Conclusión", href="/page-13", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
##############################################################################  CARGAR,LIMPIAR Y TRATAR DATAFRAME  ################################################################

# 1 PIB
df1 = pd.read_csv ('../SPEI/PIB per cápita por Territorio Histórico.csv', header = 2, sep=';', encoding='ISO-8859-1') #Cargamos documento
pib11 = pd.DataFrame()
for l in lista:
    pib11 = pib11.append((df1.loc[((df1['ámbitos territoriales'] == l)) & (df1['tipo de medida'] == 'PIB per cápita. Precios corrientes (euros)')])) # Definimos los datos a analizar
pib11 ['Producto interior bruto (PIB) de la C.A. de Euskadi'] = pd.to_numeric(pib11['Producto interior bruto (PIB) de la C.A. de Euskadi']) # Convertimos los datos tipo object a intall

# 2 RENTA
df2 = pd.read_csv ('../SPEI/Renta.csv', header = 1, sep=';', encoding='ISO-8859-1') #Cargamos documento
renta11 = pd.DataFrame()
for l in lista:
    renta11 = renta11.append(df2.loc[(df2['ámbitos territoriales'] == l) & (df2['tipo de renta'] == 'Renta total') & (df2['sexo'] == 'Total')]) # Definimos los datos a analizar
renta11['Renta personal media de la C.A. de Euskadi (euros)'] = pd.to_numeric(renta11['Renta personal media de la C.A. de Euskadi (euros)'])#convertimos a numerico los datos

# 3 OCUPACIÓN
Hoja1 = pd.read_csv('../SPEI/Paro_registrado_desde_1997_pocas.csv', header = 1,sep=';', decimal='.', encoding='ISO-8859-1')            #sep=';', encoding='ISO-8859-1') #Cargamos documento  #Â¡DIV/0!
Hoja1 = Hoja1.rename(columns={'AÃ±o':'Año'})     #para cambiar nombres de columna
Hoja1=Hoja1.drop(labels=[14968], axis=0)         # para cargarme una fila por el index
Hoja1= Hoja1.replace('#Â¡DIV/0!',0)              # PARA REEMPLAZAR
Hoja1['IndiceParo']= pd.to_numeric(Hoja1['IndiceParo'])

paro4 = pd.DataFrame()
paro44 = pd.DataFrame()
paro444 = pd.DataFrame()
paro40 = pd.DataFrame()


for Tp in tA:
  for Ap in nivel:
        paro4 =paro4.append(Hoja1.groupby(['Año','T.H.','Trimestre']).get_group( (Ap,Tp,1)))

paro4=paro4.drop(['Trimestre','Codigo TH','T.H.','Cod. Comarca a 11', 'Descr. Comarca a 11','Cod. Municipio', 'Nombre Municipio','TOTAL PARADOS','IndiceParo', 'Poblacion', 'Pobl. Activa', 'Prim', 'Extrac', 'Manuf', 'Energia', 'ConstrucciÃ³n','Comercio y HostelerÃ\xada', 'Transportes. Inf Comun', 'Seguros y Finanzas Serv Emp', 'Otros Servicios','Sin empleo anterior', 'Directivos',  'TÃ©cnicos y P. CientÃ\xadficos', 'TÃ©cnicos y Prof. de Apoyo',  'Empleados Administrativos', 'Trabajadores Servicios',  'Trabaj. Agric. y Pesca', 'Trabajadores Cualificados', 'Operadores Maquinaria', 'Trabaj. NO Cualificados', 'Fuerzas Armadas','Sin Alfabetizar', 'Estudios Primarios', 'Certificado Escolar', 'ESO', 'EGB','Bachiller', 'FP', 'GRADO MEDIO', 'GRADO SUPERIOR', 'OTROS'], axis = 1)
for h in hA:
    paro444= (paro4.groupby(['Descr. Comarca a 30']).get_group(h))
    paro44 = paro44.append(paro444.groupby(['Año','Descr. Comarca a 30']).sum())

paro44=paro44.reset_index()
paro40 = paro44.melt(id_vars = ['Año','Descr. Comarca a 30'],var_name = 'Sexo')     # Índice de desempleo de las comarcas objetivo de estudio por sexo y edad
paro40 =paro40.groupby(['Año','Descr. Comarca a 30','Sexo']).sum()
# paro40= paro40.sort_values(['Año', 'value'],ascending=False)
paro40=paro40.reset_index()

# 4 POBLACIÓN
df4 = pd.read_csv ('../SPEI/poblacion.csv', header = 1, sep=';', encoding='ISO-8859-1') #Cargamos documento
pob11 = pd.DataFrame()
for l in lista:
    pob11 = pob11.append(df4.loc[(df4['ámbitos territoriales'] == l) & (df4['grupos de países por nacionalidad'] == 'Total')]) # Definimos los datos a analizar
pob11['Población de la C.A. de Euskadi'] = pd.to_numeric(pob11['Población de la C.A. de Euskadi'])

#Definir data frame
pob4 = pd.DataFrame()
#Definir tupla de periodo para corregir etiquetas o pendiente
años_pob = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

#Agregar datos por cada una de las comarcas
#1-Recorrer todas las comarcas
for n_pob4 in lista:
  #Definir el dato de referencia
  pob_referencia2 =df4.loc[(df4['ámbitos territoriales'] == n_pob4) & (df4['periodo']==años_pob[0])&(df4['grupos de países por nacionalidad'] == 'Total')]['Población de la C.A. de Euskadi'].sum()
  #2-Recorrer los periodos
  for a_pob4 in años_pob:
    #Definir los datos de cada periodo
    pob_actual2 = df4.loc[(df4['ámbitos territoriales'] == n_pob4) & (df4['periodo']==a_pob4)&(df4['grupos de países por nacionalidad'] == 'Total')]['Población de la C.A. de Euskadi'].sum()

    pob_actual2= pd.to_numeric(pob_actual2)
    pob_referencia2=pd.to_numeric(pob_referencia2)
    #Calcular porcentaje de crecimiento con respecto al año de referencia
    porcentaje_pob2 = pob_actual2/pob_referencia2
    #Añadir los valores al dataframe
    pob4=pob4.append({'ámbitos territoriales':n_pob4,'periodo':a_pob4,'Población de la C.A. de Euskadi':porcentaje_pob2},ignore_index=True)
      
# Convertir los datos tipo object a int
pob4['Población de la C.A. de Euskadi'] = pd.to_numeric(pob4['Población de la C.A. de Euskadi']) 

# 5 CUALIFICACIÓN
df5 = pd.read_csv ('../SPEI/2cualificacion_Población de 10 y más años de la C.A. de Euskadi por comarca, nivel de instrucción, edad, sexo y periodo.csv', header = 1, sep=';', encoding='ISO-8859-1') #Cargamos documento
cual11 = pd.DataFrame()
for n in nivel1:
  for l in lista:
    cual11 = cual11.append((df5.loc[(df5['comarca'] == l) & (df5['periodo'] == 2020) & (df5['nivel de instrucción'] ==  n)])) # Definimos los datos a analizar
cual11 ['Población de 10 y más años de la C.A. de Euskadi'] = pd.to_numeric(cual11['Población de 10 y más años de la C.A. de Euskadi']) # Convertimos los datos tipo object a int

# 6 Tejido y dinamismo empresarial
df6 = pd.read_csv ('../SPEI/Tejido y dinamismo empresarial.csv', header = 0, sep=';', encoding='ISO-8859-1') #Cargamos documento
evo11 = pd.DataFrame()
for l in lista:
    evo11 = evo11.append(df6.loc[(df6['ámbitos territoriales'] == l) & (df6['actividad (A10)'] == 'Total de actividad')]) # Definimos los datos a analizar
evo11 ['Establecimientos en la C.A. de Euskadi'] = pd.to_numeric(evo11['Establecimientos en la C.A. de Euskadi']) # Convertimos los datos tipo object a intall

# 7 TAMAÑO DE LAS EMPRESAS
df7 = pd.read_csv ('../SPEI/tamaño medio de los establecimientos.csv', header = 0, sep=';', encoding='ISO-8859-1') #Cargamos documento
df7 = df7.melt(id_vars='ámbitos territoriales')
df7.columns = ['ámbitos territoriales','periodo','tamaño']
listas =('Araba/Álava', 'Bizkaia', 'Gipuzkoa','Bidasoa Beherea / Bajo Bidasoa', 'Debabarrena / Bajo Deba','Debagoiena / Alto Deba','Donostialdea','Goierri','Tolosaldea','Urola Kosta','Enkartazioak / Encartaciones', 'Bilbo Handia / Gran Bilbao','Plentzia-Mungia','Gernika-Bermeo','Markina-Ondarroa','Durangaldea / Duranguesado','Arratia-Nerbioi / Arratia-Nervión','Añana','Arabako Errioxa / Rioja Alavesa','Arabako Kantaurialdea / Cantábrica Alavesa','Arabako Lautada / Llanada Alavesa','Arabako Mendialdea / Montaña Alavesa','Gorbeialdea / Estribaciones del Gorbea')
años_emp = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
df7 ['periodo'] = pd.to_numeric(df7['periodo']) # Convertimos los datos tipo object a intall
emple = pd.DataFrame()
ste = pd.DataFrame()
emp111 = pd.DataFrame()
for a in años_emp:
  for l in lista:
    empl=df7.loc[(df7['ámbitos territoriales'] == l) & (df7['periodo'] == a)]['tamaño'].sum()
    ste=df6.loc[(df6['ámbitos territoriales'] == l) & (df6['periodo'] == a) & (df6['actividad (A10)'] == 'Total de actividad')]['Establecimientos en la C.A. de Euskadi'].sum()
    emp111 = emp111.append({'ámbitos territoriales': l,'periodo':a,'Empleados':empl,'Establecimientos':ste}, ignore_index=True)

emp111['Empleados'] = pd.to_numeric(emp111['Empleados'])
emp111['Establecimientos'] = pd.to_numeric(emp111['Establecimientos'])
emp111['Tamaño medio'] = round(emp111['Empleados'] / emp111['Establecimientos'], 3)

# 8 INTERNACIONALIZACIÓN
df8 = pd.read_csv ('../SPEI/exportacion.csv', header = 0, sep=';', encoding='ISO-8859-1') #Cargamos documento
export11 = pd.DataFrame()
for t in th:
    export11 = export11.append(df8.loc[(df8['territorio histórico'] == t) & (df8['CNA-09'] != 'Tot')]) # Definimos los datos a analizar
export11 ['Comercio exterior de la C.A. de Euskadi'] = pd.to_numeric(export11['Comercio exterior de la C.A. de Euskadi']) # Convertimos los datos tipo object a intall

# 9 INNOVACIÓN
df9 = pd.read_csv ('../SPEI/gastos_innovación.csv', header = 1, sep=';', encoding='ISO-8859-1') #Cargamos documento
df9 = df9.melt(id_vars = ['ámbitos territoriales'],var_name = 'periodo')
df9['value']=df9['value'].apply(lambda x: x.replace(',','.'))
# Convertir los datos tipo object a int
df9['value'] = round((pd.to_numeric(df9['value'])),3)



# 10 Distribución sectorial de la población ocupada
df10 = pd.read_csv ('../SPEI/Distribución sectorial de la población ocupada.csv', header = 1, sep=';', encoding='ISO-8859-1') #Cargamos documento
dp11 = pd.DataFrame()
for l in lista:
    dp11 = dp11.append((df10.loc[((df10['ámbitos territoriales'] == l)) & (df10['rama de actividad'] != 'Total')])) # Definimos los datos a analizar
dp11['Población de 16 y más años ocupada de la C.A. de Euskadi'] = pd.to_numeric(dp11['Población de 16 y más años ocupada de la C.A. de Euskadi'])

# 11 Valor añadido bruto por sector de actividad
df11 = pd.read_csv ('../SPEI/Valor añadido bruto por sector de actividad.csv', header = 1, sep=';', encoding='ISO-8859-1') #Cargamos documento
#Remplazar - por 0
df11= df11.replace('-',0)
vab11 = pd.DataFrame()
for l in lista:
    vab11 = vab11.append(df11.loc[(df11['ámbitos territoriales'] == l)&(df11['unidades'] == 'Porcentaje sobre el VAB total del municipio')&(df11['sector de actividad']!='TOTAL')])
vab11['Valor añadido bruto (VAB) de la C.A. de Euskadi '] = pd.to_numeric(vab11['Valor añadido bruto (VAB) de la C.A. de Euskadi ']) # Convertimos los datos tipo object a intall

# 12 ANIMADA
# CARGAR TUPLA DE LOS AÑOS
añosrenta = [2001, 2003, 2006, 2009, 2010, 2011, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
añospib = [1996, 2000, 2005, 2008, 2009, 2010, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
añosgeneral = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
               2013, 2014, 2015, 2016, 2017, 2018, 2019]

# CARGAR LAS TABLAS DESDE DRIVE
df_renta = pd.read_csv('../SPEI/Renta.csv', header=1, sep=';',
                       encoding='ISO-8859-1')  # Cargamos documento
df_PIB = pd.read_csv('../SPEI/PIB per cápita por Territorio Histórico.csv',
                     header=2, sep=';', encoding='ISO-8859-1')  # Cargamos documento
df_PARO = pd.read_csv('../SPEI/Paro_registrado_desde_1997_pocas.csv',
                      header=1, sep=';', decimal='.', encoding='ISO-8859-1')  # Cargamos documento

# Remplazar guiones por 0 en el dataframe
df_PARO = df_PARO.rename(columns={'AÃ±o': 'periodo'})

# Renombrar comarcas de álava
df_PARO = df_PARO.replace('LLANADA ALAVESA', 'Arabako Lautada / Llanada Alavesa')
df_PARO = df_PARO.replace('VALLE DE AIALA', 'Arabako Kantaurialdea / Cantábrica Alavesa')
df_PARO = df_PARO.replace('VITORIA-GASTEIZ', 'Arabako Lautada / Llanada Alavesa')
df_PARO = df_PARO.replace('MONTAÃA ALAVESA', 'Arabako Mendialdea / Montaña Alavesa')
df_PARO = df_PARO.replace('RIOJA ALAVESA', 'Arabako Errioxa / Rioja Alavesa')
df_PARO = df_PARO.replace('VALLES ALAVESES', 'Añana')
df_PARO = df_PARO.replace('ESTRIB. GORBEA', 'Gorbeialdea / Estribaciones del Gorbea')

# Renombrar comarcas de Bizkaia
df_PARO = df_PARO.replace('ENCARTACIONES', 'Enkartazioak / Encartaciones')
df_PARO = df_PARO.replace('MARGEN IZQUIERDA', 'Bilbo Handia / Gran Bilbao')
df_PARO = df_PARO.replace('IBAIZABAL', 'Bilbo Handia / Gran Bilbao')
df_PARO = df_PARO.replace('BILBAO', 'Bilbo Handia / Gran Bilbao')
df_PARO = df_PARO.replace('TXORIERRI', 'Bilbo Handia / Gran Bilbao')
df_PARO = df_PARO.replace('GOBELA', 'Bilbo Handia / Gran Bilbao')
df_PARO = df_PARO.replace('URIBEALDEA', 'Plentzia-Mungia')
df_PARO = df_PARO.replace('BUSTURIALDE', 'Gernika-Bermeo')
df_PARO = df_PARO.replace('LEA - ARTIBAI', 'Markina-Ondarroa')
df_PARO = df_PARO.replace('DURANGUESADO', 'Durangaldea / Duranguesado')
df_PARO = df_PARO.replace('ARRATIA - ZORNOTZA', 'Plentzia-Mungia')
df_PARO = df_PARO.replace('MEDIO NERVION', 'Arratia-Nerbioi / Arratia-Nervión')
df_PARO = df_PARO.replace('URIBEALDEA', 'Arratia-Nerbioi / Arratia-Nervión')

# Renombrar comarcas de Gipuzkoa
df_PARO = df_PARO.replace('BAJO BIDASOA', 'Bidasoa Beherea / Bajo Bidasoa')
df_PARO = df_PARO.replace('BAJO DEBA', 'Debabarrena / Bajo Deba')
df_PARO = df_PARO.replace('ALTO DEBA', 'Debagoiena / Alto Deba')
df_PARO = df_PARO.replace('UROLA GARAIA', 'Goierri')
df_PARO = df_PARO.replace('GOIHERRI', 'Goierri')
df_PARO = df_PARO.replace('UROLA ERDIA', 'Urola Kosta')
df_PARO = df_PARO.replace('UROLA KOSTA', 'Urola Kosta')
df_PARO = df_PARO.replace('TOLOSALDEA', 'Tolosaldea')
df_PARO = df_PARO.replace('DONOSTIALDEA OESTE', 'Donostialdea')
df_PARO = df_PARO.replace('DONOSTIA', 'Donostialdea')
df_PARO = df_PARO.replace('OARSOALDEA', 'Donostialdea')

comarcas = ('Añana', 'Arabako Errioxa / Rioja Alavesa', 'Arabako Kantaurialdea / Cantábrica Alavesa',
            'Arabako Lautada / Llanada Alavesa', 'Arabako Mendialdea / Montaña Alavesa',
            'Gorbeialdea / Estribaciones del Gorbea', 'Enkartazioak / Encartaciones', 'Bilbo Handia / Gran Bilbao',
            'Plentzia-Mungia', 'Gernika-Bermeo', 'Markina-Ondarroa', 'Durangaldea / Duranguesado',
            'Arratia-Nerbioi / Arratia-Nervión', 'Bidasoa Beherea / Bajo Bidasoa', 'Debabarrena / Bajo Deba',
            'Debagoiena / Alto Deba', 'Donostialdea', 'Goierri', 'Tolosaldea', 'Urola Kosta')

# Definir data frame
dd1 = pd.DataFrame()
dd2 = pd.DataFrame()
dd3 = pd.DataFrame()

# Tomar los datos de para cada año
for ad1 in añosgeneral:
    for c1 in comarcas:
        # Tomar los datos del duranguesado
        renta_dur = df_renta.loc[
            (df_renta['ámbitos territoriales'] == c1) & (df_renta['periodo'] == ad1) & (df_renta['sexo'] == 'Total') & (
                        df_renta['tipo de renta'] == 'Renta total')][
            'Renta personal media de la C.A. de Euskadi (euros)'].sum()
        pib_dur = df_PIB.loc[(df_PIB['ámbitos territoriales'] == c1) & (df_PIB['periodo'] == ad1) & (
                    df_PIB['tipo de medida'] == 'PIB per cápita. Precios corrientes (euros)')][
            'Producto interior bruto (PIB) de la C.A. de Euskadi'].sum()
        paro_dur = \
        df_PARO.loc[(df_PARO['Trimestre'] == 1) & (df_PARO['Descr. Comarca a 30'] == c1) & (df_PARO['periodo'] == ad1)][
            'TOTAL PARADOS'].sum()

        # Añadir datos de duranguesado al data frame
        dd1 = dd1.append({'ámbitos territoriales': c1, 'periodo': ad1, 'población parada': paro_dur, 'renta': renta_dur,
                          'PIB': pib_dur}, ignore_index=True)

# convertir las columnas a interpolar en numerico
dd1['renta'] = pd.to_numeric(dd1['renta'])
dd1['PIB'] = pd.to_numeric(dd1['PIB'])

# Cambiar los valores cero por na
dd1[dd1 == 0] = np.nan

for c1 in comarcas:
    # Rellenar los valores na con una interpolación entre el valor anterior y el proximo
    dd3 = dd1.loc[dd1['ámbitos territoriales'] == c1].interpolate(method='linear', axis=0)
    # Combinar las tablas interpoladas de las dos comarcas
    for ad4 in añosgeneral:
        dd2 = dd2.append(dd3.loc[(dd3['periodo'] == ad4)])

# Cambiar los valores na iniciales por 0
dd2 = dd2.fillna(0)
#############################################################################  DEFINIR LAS GRÁFICAS  ################################################################

#1-PIB
@app.callback(
    Output("graph1", "figure"), 
    [Input("mydropdown1", "value")])

def update_line_chart(comarca):
    # Cargar datos

    pib1 = pd.DataFrame()
    pib1 = pib11[pib11['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    años_pib = [1996,2000,2005,2008,2010,2012,2014,2015,2016,2017,2018,2019]
    #Gráfico
    fig = px.line (pib1,x='periodo', y='Producto interior bruto (PIB) de la C.A. de Euskadi', color='ámbitos territoriales', 
    #Definir etiquetas a mostrar
    labels={
    'periodo': 'Año',
    'ámbitos territoriales': 'Ámbito territorial',
    "Producto interior bruto (PIB) de la C.A. de Euskadi": "PIB per cápita"
    }, 
    #Resaltar puntos de datos
    markers=True,
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] 
    #Insertar dato fijo por marcador
    #text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
    )

    fig.update_traces({'line':{'dash':'dash'}}, 
        #textposition = "bottom right"
    )
    fig.update_layout(title="PIB per cápita", xaxis_title = 'Años', yaxis_title = 'PIB per cápita. Precios corrientes (euros)', legend_title_text='Territorio Histórico' , xaxis = dict(tickvals = años_pib), legend=dict(orientation="h",
        yanchor="bottom",y=1,xanchor="left",x=0))
    return fig

#2-RENTA
@app.callback(
    Output("graph2", "figure"), 
    [Input("mydropdown2", "value")])

def update_line_chart(comarca):
    # Cargar datos

    renta1 = pd.DataFrame()
    renta1 = renta11[renta11['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    años_renta = [2001,2003,2006,2009,2011,2013,2014,2015,2016,2017,2018,2019]
    #Gráfico
    figrenta = px.line (renta1,x='periodo', y= 'Renta personal media de la C.A. de Euskadi (euros)', color='ámbitos territoriales', 
    #Definir etiquetas a mostrar
    labels={
    'periodo': 'Año',
    'ámbitos territoriales': 'Ámbito territorial',
    'Renta personal media de la C.A. de Euskadi (euros)': 'Renta per cápita' 
    }, 
    #Resaltar puntos de datos
    markers = True,
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] 
    #Insertar dato fijo por marcador
    #text = "Renta per capita de la C.A. de Euskadi en Euros"
    )
    figrenta.update_traces({'line':{'dash':'dash'}}, 
        #textposition = "bottom right"
        )
    figrenta.update_layout(title="Renta per capita total en euros", xaxis_title = 'Años', yaxis_title = 'Renta per cápita en (euros)', legend_title_text='Ámbitos territoriales' , xaxis = dict(tickvals = años_renta), legend=dict(orientation="h",
        yanchor="bottom",y=0.9,xanchor="left",x=0))
    return figrenta

#3-PARO
@app.callback(
    Output("graph3", "figure"), 
    [Input("mydropdown3", "value")])
    
def update_line_chart(comarca):
    # Cargar datos
    # Cargar datos
    paro1 = pd.DataFrame()
    paro1 = paro40[paro40['Descr. Comarca a 30'].isin(comarca)]  # Definimos los datos a analizar
    # Gráfico
    figparo = px.bar(paro1, x='Sexo', y='value', color='Descr. Comarca a 30', animation_frame ="Año", height = 750, text_auto='.2s',
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] )

    figparo.update_layout(title="Índice de desempleo por sexo y edad", xaxis_title = 'Sexo', yaxis_title = 'Población', legend_title_text='Ámbitos territoriales' , legend=dict(orientation="v",
        yanchor="bottom",y=0,xanchor="left",x=1,), updatemenus=[dict(type='buttons',
                                        showactive=False,
                                        y=0,
                                        x=0,
                                        xanchor='left',
                                        yanchor='top')
                                   ])

    figparo['layout']['sliders'][0]['pad']['t'] = 90
    return figparo

#4-POBLACIÓN
@app.callback(
    Output("graph4", "figure"), 
    [Input("mydropdown4", "value")])
    
def update_line_chart(comarca):
    # Cargar datos

    pob1 = pd.DataFrame()
    pob1 = pob11[pob11['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    años_pob = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    #Gráfico
    figpob = px.line (pob1,x='periodo', y='Población de la C.A. de Euskadi', color='ámbitos territoriales',
    #Definir etiquetas a mostrar
    labels={
    'periodo': 'Año',
    'ámbitos territoriales': 'Ámbito territorial',
    "Población de la C.A. de Euskadi": "Población"
    },
    #Resaltar puntos de datos
    markers=True,
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] 
    #Insertar dato fijo por marcador
    #text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
    )


    figpob.update_traces({'line':{'dash':'dash'}}, 
    #textposition = "bottom right"
    )
    figpob.update_layout(title="Evolución de la población", xaxis_title = 'Años', yaxis_title = 'Población (millones)', legend_title_text='Ámbitos territoriales' , xaxis = dict(tickvals = años_pob),yaxis=dict(dtick=100000), legend=dict(orientation="h",
        yanchor="bottom",y=1,xanchor="left",x=0))
    return figpob

#41 CRECIMIENTO DE LA POBLACIÓN
@app.callback(
    Output("graph41", "figure"), 
    [Input("mydropdown4", "value")])

def update_line_chart(comarca):

    pob5 = pd.DataFrame()
    pob5 = pob4[pob4['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    #Gráfico
    figpob1 = px.line (pob5,x='periodo', y='Población de la C.A. de Euskadi',color='ámbitos territoriales',
    #Definir etiquetas a mostrar
    labels={
    'periodo': 'Año',
    'ámbitos territoriales': 'Ámbito territorial',
    "Población de la C.A. de Euskadi": "Porcentaje de crecimiento"
    }, 
    #Resaltar puntos de datos
    markers=True,
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] 
    #Insertar dato fijo por marcador
    #text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
    )


    figpob1.update_traces({'line':{'dash':'dash'}}, 
        #textposition = "bottom right"
    )
    figpob1.update_layout(showlegend=False,title="Evolución de la población por territorio histórico", xaxis_title = 'Años', yaxis_title = 'Porcentaje de crecimiento', legend_title_text='Ámbitos territoriales' , xaxis = dict(tickvals = años_pob), legend=dict(orientation="v",
        yanchor="bottom",y=0,xanchor="left",x=1))
    
    return figpob1

#5-CUALIFICACIÓN
@app.callback(
    Output("graph5", "figure"), 
    [Input("mydropdown5", "value")])

def update_line_chart(comarca):
    # Cargar datos

    cual1 = pd.DataFrame()
    cual1 = cual11[cual11['comarca'].isin(comarca)] # Definimos los datos a analizar
    años_cual = [1986,1991,1996,2001,2006,2011,2016]
    #Gráfico
    figcual = px.bar(cual1, x='nivel de instrucción', y='Población de 10 y más años de la C.A. de Euskadi', color='comarca',
             title="Nivel de instrucción del último ejercicio disponible para cada sexo año 2020", facet_col='sexo', text_auto='.2s',
             color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] )

    return figcual

#6-TEJIDO Y DINAMISMO EMPRESARIAL
@app.callback(
    Output("graph6", "figure"), 
    [Input("mydropdown6", "value")])
    
def update_line_chart(comarca):
    # Cargar datos

    evo1 = pd.DataFrame()
    evo1 = evo11[evo11['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    años_evo = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    #Gráfico
    figevo = px.line (evo1,x='periodo', y='Establecimientos en la C.A. de Euskadi', color='ámbitos territoriales', 
    #Definir etiquetas a mostrar
    labels={
    'periodo': 'Año',
    'ámbitos territoriales': 'Ámbito territorial',
    "'Establecimientos en la C.A de Euskadi'": "Número de establecimientos"
    }, 
    #Resaltar puntos de datos
    markers=True,
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] 
    #Insertar dato fijo por marcador
    #text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
    )


    figevo.update_traces({'line':{'dash':'dash'}}, 
    #textposition = "bottom right"
    )
    figevo.update_layout(title="Evolución del numero de establecimientos", xaxis_title = 'Años', yaxis_title = 'Número de establecimientos', legend_title_text='Ámbitos territoriales' , xaxis = dict(tickvals = años_evo), legend=dict(orientation="h",
    yanchor="bottom",y=1,xanchor="left",x=0))
    return figevo

#8-TAMAÑO DE LAS EMPRESAS
@app.callback(
    Output("graph7", "figure"), 
    [Input("mydropdown7", "value")])
    
def update_line_chart(comarca):
    # Cargar datos

    emp1 = pd.DataFrame()
    emp1 = emp111[emp111['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    #Gráfico
    figemp = px.line (emp1,x='periodo', y='Tamaño medio', color='ámbitos territoriales',
    #Definir etiquetas a mostrar
    labels={
    'variable': 'Año',
    'ámbitos territoriales': 'Ámbito territorial',
    "value": "Tamaño medio"
    }, 
    #Resaltar puntos de datos
    markers=True,
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] 
    #Insertar dato fijo por marcador
    #text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
    )


    figemp.update_traces({'line':{'dash':'dash'}}, 
    #textposition = "bottom right"
    )
    figemp.update_layout(title="Tamaño medio de los establecimientos", xaxis_title = 'Años', yaxis_title = 'Tamaño medio', legend_title_text='Ámbitos territoriales' , xaxis = dict(tickvals = años_emp), legend=dict(orientation="h",
    yanchor="bottom",y=1,xanchor="left",x=0))
    return figemp

#9-INTERNACIONALIZACIÓN
@app.callback(
    Output("graph8", "figure"), 
    [Input("mydropdown8", "value")])
    
def update_line_chart(comarca):
    export1 = pd.DataFrame()
    export1 = export11[export11['territorio histórico'].isin(comarca)] # Definimos los datos a analizar
    # Cargar datos
    fig_exp = px.line (export1,x='periodo', y='Comercio exterior de la C.A. de Euskadi', color='CNAE009',
    facet_col = 'territorio histórico',#tantos graficos como columnas tengas
    #Definir etiquetas a mostrar
    labels={
    'periodo': 'Año',
    'territorio histórico': 'Ámbito territorial',
    'Comercio exterior de la C.A. de Euskadi': 'Exportaciones'
    }, 
    #Resaltar puntos de datos
    markers = True,
    #Insertar dato fijo por marcador
    #text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
    height=850)

    fig_exp.update_traces({'line':{'dash':'dash'}}, 
    #textposition = "bottom right"
    )
    fig_exp.update_layout(title="Exportaciones", xaxis_title = 'Años', yaxis_title = 'Exportaciones', legend_title_text='CNA-09' , legend=dict(orientation="v",
    yanchor="top",y=-0.5,xanchor="left",x=0))

    fig_exp.update_layout(dict(updatemenus=[
                        dict(
                            type = "buttons",
                            direction = "left",
                            buttons=list([
                                dict(
                                    args=["visible", "legendonly"],
                                    label=" ",
                                    method="restyle"
                                )
                            ]),
                            pad={"r": -105, "t": 10 },
                            showactive=False,
                            x=1,
                            xanchor="right",
                            y=1.1,
                            yanchor="top"
                        ),
                    ]
              ))

    return fig_exp


#INNOVACIÓN
@app.callback(
    Output("graph9", "figure"), 
    [Input("mydropdown9", "value")])
    
def update_line_chart(comarca):
    # Cargar datos
    inn= pd.DataFrame()
    inn = df9[df9['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    años_inn = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
    # Gráfica
    figinn = px.line (inn,x='periodo', y='value', color='ámbitos territoriales',
    #Definir etiquetas a mostrar
    labels={
    'periodo': 'Año',
    'ámbitos territoriales': 'Ámbito territorial',
    "value": "Gastos en innovación"
    }, 
    #Resaltar puntos de datos
    markers=True,
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"] 
    # Insertar dato fijo por marcador
    # text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
    )


    figinn.update_traces({'line':{'dash':'dash'}}, 
        #textposition = "bottom right"
    )
    figinn.update_layout(title="Evolución del gasto en actividades para innovación", xaxis_title = 'Años', yaxis_title = 'Gasto de inovación', legend_title_text='Comarcas' , xaxis = dict(tickvals = años_inn), legend=dict(orientation="v",
        yanchor="bottom",y=0,xanchor="left",x=1))
   
    return figinn


#10-DISTRIBUCIÓN DE LA POBLACIÓN OCUPADA
@app.callback(
    Output("graph10", "figure"), 
    [Input("mydropdown10", "value")])
    
def update_line_chart(comarca):
    # Cargar datos
    años_dp = [1996, 2001, 2006, 2011, 2016]
    dp1 = pd.DataFrame()
    dp1 = dp11[dp11['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    #Gráfico
    figdp = px.bar (dp1,color='ámbitos territoriales', y='Población de 16 y más años ocupada de la C.A. de Euskadi', x='rama de actividad',
    #Definir etiquetas a mostrar
    labels={
    'periodo': 'Año',
    'ámbitos territoriales': 'Ámbito territorial',
    "Población de 16 y más años ocupada de la C.A. de Euskadi": "Población"
    },
    color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"],
    #Resaltar puntos de datos
    #markers=True,
    #Insertar dato fijo por marcador
    #text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
    animation_frame="periodo", height = 750, text_auto='.2s')

    figdp.update_layout(title="Evolución de la población", xaxis_title = 'Rama de actividad', yaxis_title = 'Población', legend_title_text='Ámbitos territoriales' , legend=dict(orientation="v",
        yanchor="bottom",y=0,xanchor="left",x=1), updatemenus=[dict(type='buttons',
                                        showactive=False,
                                        y=-0.4,
                                        x=0,
                                        xanchor='left',
                                        yanchor='top')
                                   ])

    figdp['layout']['sliders'][0]['pad']['t'] = 200

    return figdp

#11-VALOR AÑADIDO BRUTO
@app.callback(
    Output("graph11", "figure"), 
    [Input("mydropdown11", "value")])
    
def update_line_chart(comarca):
    # Cargar datos
    vab1 = pd.DataFrame()
    vab1 = vab11[vab11['ámbitos territoriales'].isin(comarca)] # Definimos los datos a analizar
    años_vab=[1996,2000,2005,2008,2010,2012,2014,2015,2016,2017,2018,2019]
    #Gráfico
    figvab = px.line(vab1, x='periodo', y='Valor añadido bruto (VAB) de la C.A. de Euskadi ', color='sector de actividad',
                  facet_row='ámbitos territoriales',
                  # Definir etiquetas a mostrar
                  labels={
                      'variable': 'Año',
                      'ámbitos territoriales': 'Ámbito territorial',
                      "value": "Tamaño medio"
                  },
                  # Resaltar puntos de datos
                  markers=True,
                  # Insertar dato fijo por marcador
                  # text = "Producto interior bruto (PIB) de la C.A. de Euskadi"
                  color_discrete_sequence=["orange", "purple", "blue", "brown", "red", "green", "pink"], 
                  height=1000)

    figvab.update_traces({'line': {'dash': 'dash'}},
                      # textposition = "bottom right"
                      )
    figvab.update_layout(title="Valor añadido bruto por sector de actividad", xaxis_title='Años', yaxis_title='Porcentaje',
                      legend_title_text='Sector de actividad', xaxis=dict(tickvals=años_vab),
                      legend=dict(orientation="v",
                                  yanchor="top", y=1, xanchor="left", x=1))
        
    return figvab

#13-GRÄFICA ANIMADA
@app.callback(
    Output("graph12", "figure"),
    [Input("mydropdown12", "value")])
def update_line_chart(comarca):
    # Cargar datos
    ani1 = pd.DataFrame()
    ani1 = dd2[dd2['ámbitos territoriales'].isin(comarca)]  # Definimos los datos a analizar
    # Gráfico
    figani = px.scatter(ani1, x='PIB', y='renta', animation_frame='periodo', animation_group='ámbitos territoriales',
                     size='población parada', size_max=80, color='ámbitos territoriales', log_x=True,
                     range_y=[0, 45000], range_x=[10000, 75000], text="población parada",
                     color_discrete_sequence = ["green","red","navy","fuchsia","orange","chocolate","lightskyblue","coral","hotpink","salmon","tomato","saddlebrown","palegreen","olive"])

    figani.update_layout(title="Desempeño competitivo PIB - Renta - Desempleo por año", xaxis_title='PIB',
                         yaxis_title='Renta',
                         legend_title_text='Ámbito territorial',
                         legend=dict(orientation="v",
                                     yanchor="top", y=1, xanchor="left", x=1))

    return figani


##############################################################################  DEFINIR CONTENIDO DE LAS PÁGINAS  ################################################################

index_page = html.Div([
html.H1("Introducción", className="display-4"),
html.Br(),
html.Div('Este estudio se realiza dentro de la asignatura de Sistemas, Política y Economía de la Innovación de la Ingeniería Dual en Innovación de Procesos y Productos IMH, con el propósito de realizar un Diagnóstico de competitividad territorial.'),
html.Br(),
html.Div('Para realizar el análisis se han analizado una serie de indicadores pertenecientes a cuatro grandes ejes que son el desempeño competitivo, las condiciones de los factores, y el contexto para la estrategia y la rivalidad empresarial. Estos indicadores se han analizado a nivel de territorios históricos de Euskadi o a nivel de las comarcas objetivo,  según lo requerido. Las dos comarcas objetivo de estudio son Durangaldea, siendo esta la comarca ”primaria” y el Bajo Bidasoa como la comarca “ secundaria”. '),
html.Br(),
html.Div('Los indicadores analizados son tanto cuantitativos como cualitativos. Los datos con los que se ha realizado el diagnóstico han sido extraídos de las fuentes oficiales de estadística disponibles, como es Eustat, y otras páginas públicas oficiales como es Lanbide, diputación y ayuntamientos. '),
html.Br(),
html.Div('Para tratar los datos se ha usado el lenguaje Python, mediante un documento compartido creado en Colaboratory, el equipo ha podido trabajar de manera simultánea sobre el tratamiento de datos. La redacción del informe se ha realizado de manera semejante mediante Overleaf que es editor de Latex online.')
])
page_1_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown1',
            options = drop,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph1',
    figure = {}),
    html.Div(id='page-1-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])


page_2_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown2',
            options= drop,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph2',
    figure = {}),
    html.Div(id='page-2-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_3_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown3',
            options= dropparo,
        value=['DURANGUESADO', 'BAJO BIDASOA'],
        multi=True
    ),
    dcc.Graph(id = 'graph3',
    figure = {}),
    html.Div(id='page-3-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_4_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown4',
            options= drop,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph4',
    figure = {}),
    dcc.Graph(id = 'graph41',
    figure = {}),
    html.Div(id='page-4-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_5_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown5',
            options= drop,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph5',
    figure = {}),
    html.Div(id='page-5-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_6_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown6',
            options= drop,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph6',
    figure = {}),
    html.Div(id='page-6-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_7_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown7',
            options= drop,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph7',
    figure = {}),
    html.Div(id='page-7-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_8_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown8',
            options= dropth,
        value=['Gipuzkoa','Bizkaia'],
        multi=True
    ),
    dcc.Graph(id = 'graph8',
    figure = {}),
    html.Div(id='page-8-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_9_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown9',
            options= dropinn,
        value=['Durangaldea  /  Duranguesado', 'Bidasoa Beherea  /  Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph9',
    figure = {}),
    html.Div(id='page-9-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_10_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown10',
            options= dropdp,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph10',
    figure = {}),
    html.Div(id='page-10-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_11_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown11',
            options= drop,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa'],
        multi=True
    ),
    dcc.Graph(id = 'graph11',
    figure = {}),
    html.Div(id='page-11-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])

page_12_layout = html.Div([
    html.Label('Elige una opción'),
        dcc.Dropdown(id = 'mydropdown12',
            options= drop,
        value=['Durangaldea / Duranguesado', 'Bidasoa Beherea / Bajo Bidasoa', 'Urola Kosta','Arabako Mendialdea / Montaña Alavesa','Arabako Errioxa / Rioja Alavesa','Gernika-Bermeo'],
        multi=True
    ),
    dcc.Graph(id = 'graph12',
    figure = {}),
    html.Div(id='page-12-content'),
    html.Br(),
    #dcc.Link('Go back to Home', href='/')
])
page_13_layout = html.Div([
html.H3("Conclusión", className="display-4"),
html.Img(src='data:image/png;base64,{}'.format(dafo_base64), style={'height':'auto', 'width':1500}),
html.Div('Demanda Bajo Bidasoa:Comercio y Transporte'),
html.Br(),
html.Div('Sacar partido a la ubicación estratégica desarrollando servicios a compañías de transporte,crear nuevos accesos viarios,impulsar las actuaciones en las redes viarias que transcurren porIrún y realizar mejoras de los accesos a Irún por las carreteras nacionales y autopistas.'),
html.Div('La oferta comercial de Irún es atractiva para los habitantes del otro lado de la frontera.Destacando la zona de Behobia en la que sus comercios trabajan de domingo a domingo.'),
html.Br(),
html.Div('Demanda Duranguesado:Industria-Automoción'),
html.Br(),
html.Div('En el Duranguesado se debe tratar de afectar a la producción de componentes auxiliares de laautomoción, con este fin, sería muy interesante crear un Cluster.'),
html.Div('En este aspecto ACICAE, es un centro de colaboración e investigación para mejorar la colabo-ración en este sector. También se cuenta con un conglomerado importante de empresas que lotrabajan. De modo que para crear un Cluster y fomentar más este campo, solo falta un centroeducativo asociado a esta rama (aunque ACICAE organiza cursos no se puede considerar uncentro educativo) y una implicación activa de la administración pública (hecho que ya se estádando, pues se están concediendo becas para la formación de estudiantes en centros asociados).')
])

page_14_layout = html.Div([
html.H3("Infraestructuras ", className="display-4"),
html.Div('Bajo Bidasoa'),
html.Br(),
html.Div('Infraestructura de enseñanza :'),
html.Div('5 centros de FP (electrónica, telcomunicaciones, informática, mecanizado, logística, administración y diseño ), 1 Facultad de empresariales Mondragon, EOI, conservatorio, escuela arte, centros naútico, buceo. Y hasta el 2020 tuvo escuela de aviación.'),
html.Br(),
html.Div('Infraestructuras tecnológica y de servicios a empresas:'),
html.Div('La universidad de Mondragon cumple la función de fortalecer el tejido empresarial, fomentando la investigación y la transferencia de conocimiento. Carece de centros tecnológicos.'),
html.Br(),
html.Div('Infraestructuras física y de transporte: '),
html.Div('Cuenta con una red completa de transporte con 12 líneas de bus, 3 estaciones de EuskoTren, 1 de ADIF, 1 aeropuerto, 1 puerto deportivo, 1 puerto pesquero, acceso a la N121-A, GI2134, AP8 y  A63.'),
html.Br(),
html.Div('Características naturales: '),
html.Div('Presencia del río bidasoa el cual sirve de límite geográfico entre Hendaye ( Francia) y la comarca del Bajo Bidasoa. Este desembalsa en la Bahía de Txingudi. En la zona costera destaca la presencia del monte Jaizkibel en su punto más alto (S.Enrique), con 547m,  marca el limite occidental de la comarca. En su cara interior se encuentra las Cinco Villas, en donde destaca el pico de las Peñas de Aia con 830m '),
html.Br(),

html.Br(),
html.Div('Duranguesado'),
html.Br(),
html.Div('Infraestructura de enseñanza :'),
html.Div('4 centros de FP (Mecánica, administración, informática, electricidad y electrónica), EOI, conservatorio y centros de educación a personas adultas. Situadas todas en Durango.'),
html.Br(),
html.Div('Infraestructuras tecnológica y de servicios a empresas:'),
html.Div('Se encuentran un centro tecnológico que se encuentra dentro del Consorcio Científico Tecnológico Vasco, llamado Azterlan. Además, el cluster de automoción tiene el AIC (Automotive Intelligence Center) y Gestamp cuenta con GTI (Gestamp Technology Institute).'),
html.Br(),
html.Div('Infraestructuras física y de transporte:'),
html.Div('Cuenta con 8 estaciones de EuskoTren por la que trascurren 3 líneas diferentes, 14 líneas de autobuses (8 líneas de BizkaiBus y 4 líneas de Pesa), acceso a BI-623,BI632,A8,N634,BI3333 y BI4331.'),
html.Br(),
html.Div('Características naturales: '),
html.Div('Las alineaciones montañosas de dirección noroeste-suroeste, localizadas al oeste del río Nervión, forman las Peñas del Duranguesado y Durango. Por ella cruzan dos alineaciones montañosas paralelas la que se ubica más al sur se llama anticlinal y la del norte se le conoce como Crestería del Duranguesado. En la crestería se encuentra Dima, Urkiola y Sierra de Anboto.'),
])

page_15_layout = html.Div([
html.H3("Instituciones para la colaboración", className="display-4"),
html.Img(src='data:image/png;base64,{}'.format(agencia_base64), style={'height':'auto', 'width':500}),
html.Div('Las comarcas de Duranguesado y el Bajo Bidasoa cuentan con dos agencias de desarrollo en las cuales se trabaja de manera activa para promover la creación de empresas, formar a las personas y trabajar en la inserción laboral. En el caso del Behargintza del Duranguesado tiene una componente más social ayudando a las personas más desfavorecidas con programas de prevención de adicciones, recogida de residuos, dinamización de personas mayores, etc.'),
html.Br(),
html.Div('Es destacable también que el Behargintza del Duranguesado solo cubre un 73 % del territorio, según el informe de “Indicadores y análisis de competitividad local en el país vasco”. En cambio Bidasoa Activa cubre el 100 % del territorio en el Bajo Bidasoa.'),
html.Br(),
html.Div('Por otro lado en el bajo bidasoa se cuenta con dos instituciones económicas por cada uno de los territorios que la forman; Irun Ekintzan y Hondarribia Abian. La primera busca solventar los elevados datos de paro de Irún y la segunda impulsa las características endógenas de Hondarribia, como son el comercio local, turismo, actividades náuticas, etc.'),
html.Br(),
html.Div('En el caso de la comarca del duranguesado no cuenta con instituciones económicas de soporte pero si tiene la presencia del cluster de automoción, ACICAE. Con la que se fomenta esta actividad que da trabajo a un gran número de trabajadores de la comarca. En empresas como Gestamp, Batz, Maier,Pierburg, etc.')
])

##############################################################################  LLAMAR A LAS PÁGINAS  ################################################################

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-4':
        return page_4_layout
    elif pathname == '/page-5':
        return page_5_layout
    elif pathname == '/page-6':
        return page_6_layout
    elif pathname == '/page-7':
        return page_7_layout
    elif pathname == '/page-8':
        return page_8_layout
    elif pathname == '/page-9':
        return page_9_layout
    elif pathname == '/page-10':
        return page_10_layout
    elif pathname == '/page-11':
        return page_11_layout
    elif pathname == '/page-12':
        return page_12_layout
    elif pathname == '/page-13':
        return page_13_layout
    elif pathname == '/page-14':
        return page_14_layout
    elif pathname == '/page-15':
        return page_15_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


##############################################################################  LANZAR EL SERVIDOR (127.0.0.1:8050)  ################################################################

if __name__ == "__main__":
    app.run_server(debug = True)
