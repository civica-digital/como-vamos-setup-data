#dependencias
import numpy as np
import pandas as pd
import os
import csv
import difflib
import unicodedata
from fuzzywuzzy import process

print("Loading CSV file")
#Cargar el archivo de datos, accesible mediante 146.148.12.206/output.csv , especificamos que los
#data = pd.read_csv("output_4.csv",delimiter=",", dtype=np.string_, na_values=[" "], encoding="utf-8")
data = pd.read_csv("output_4.csv",delimiter=",", na_values=[" "], encoding="utf-8", dtype=np.string_, )
print("Renombrando Columna de Año")
data.rename(columns={'AO':'AÑO'}, inplace=True)


def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def cleanstring(string):
    string = string.strip()
    string = string.lower()
    string = string.replace(" ","-")
    string = strip_accents(string)
    return string

def cleancolumns(data):
    columns_list = list(data.columns.values)
    nuevas_columnas = []
    for campo in columns_list:
        campo = campo.replace("?","")
        campo = campo.replace(" ","")
        campo = campo.replace(":","_")
        campo = campo.replace("_$","")
        if campo== "" : campo = "row_id"
        nuevas_columnas.append(campo)
    data.columns = nuevas_columnas
    return data

def getclosestelement(name, array):
    if name in array:
        close = name
    try:
        close = process.extractBests(name, array)[0][0]
    except:
        close = difflib.get_close_matches(name, array)[0]
    return close

def get_variable_avail_years(variable,data):
    variableclosest = getclosestelement(variable,data.columns.values)
    filter_data = data[["AÑO",variableclosest]]
    filter_data_sinna = filter_data.dropna(axis=0)
    year_array = np.unique(filter_data_sinna.AÑO)
    min_year = min(year_array)
    max_year = max(year_array)
    return min_year,max_year

def variable_preprocess(header):
    header = str(header)
    suffix_starts=int(len(header)-2)
    suffix_finishes = int(len(header))
    suffix = header[suffix_starts:suffix_finishes]
    variable =header
    variable_fixed = header[0:suffix_starts]
    if suffix== "_*" and variable in preguntas_C:
        variable = variable_fixed
    return variable

def get_variable_prefix(variable):
    prefix = variable[0:2]
    if prefix[0] == "O":
        prefix = 0
    return prefix

def get_variable_dim_mod_topic(variable):
    prefix = get_variable_prefix(variable)
    try:
        prefixclosest = getclosestelement(prefix, prefix_cat_dim_dict.keys())
        dimension = prefix_cat_dim_dict[prefixclosest]["dimension"]
        modulo = prefix_cat_dim_dict[prefixclosest]["modulo"]
    except:
        dimension = np.nan
        modulo = np.nan
    return dimension,modulo

def limpiar_texto(texto):
    texto = texto.replace('"',"'")
    return texto

def detect_variable_type(respuestas):
    cantidad_respuestas = len(respuestas)
    respuestas_1 = ["Muy Malo", "No confía nada", "Muy mala gestión","Completamente en desacuerdo", "Nada", "Muy insatisfecho"]
    if len(respuestas) >= 4 or len(respuestas) <= 8:
        try:
            resp_1 = respuestas["1"]
            if resp_1 in respuestas_1:
                resp_type = "ordinal"
            else:
                resp_type = "categorica"
        except:
            resp_type = "categorica"
    else:
        resp_type = "categorica"
    return resp_type

def generar_linea(variable,data):
    linea = []
    linea.append(variable)
    try:
        prefixprev = getclosestelement(variable,prefix_variables.keys())
        linea.append(limpiar_texto(str(prefix_variables[prefixprev])))
    except: linea.append(np.nan)
    dimension, modulo = get_variable_dim_mod_topic(variable)
    linea.append(dimension)
    linea.append(modulo)
    try:
        respvariable = getclosestelement(variable,prefix_respuestas.keys())
        resp = prefix_respuestas[respvariable]
        linea.append(limpiar_texto(str(resp)))
        linea.append(detect_variable_type(resp))
    except:
        linea.append(np.nan)
        linea.append(np.nan)
    try:
        min_year, max_year = get_variable_avail_years(variable,data)
    except:
        min_year = np.nan
        max_year = np.nan
    linea.append(min_year)
    linea.append(max_year)
    return linea

def create_dictionary(data):
    dictionary_list = []
    headers_bulk = data.columns.values.tolist()
    for header in headers_bulk:
        linea = generar_linea(header,data)
        dictionary_list.append(linea)
    df_dict = pd.DataFrame(dictionary_list, columns=["variable","descripcion","dimension","modulo","respuestas","tipo_respuestas","ano_min","ano_max"])
    return df_dict

def generar_csvs(data):

    print("Bulk")


    datos_bulk_sinna = data.dropna(axis=1,how="all")
    datos_bulk_sinna = cleancolumns(datos_bulk_sinna)
    diccionario_bulk=create_dictionary(datos_bulk_sinna)

    #Archive data

    filename = "output/archivo_encuestas_lote.csv"
    filename_diccionario = "output/diccionario_archivo_encuestas_lote.csv"

    datos_bulk_sinna.to_csv(filename,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)
    diccionario_bulk.to_csv(filename_diccionario,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False )

    for ciudad_key in diccionario_ciudades:

        print(ciudad_key)
        ciudad = diccionario_ciudades[ciudad_key]
        ciudad_clean = cleanstring(ciudad)
        if not os.path.exists("output/"+ciudad_clean+"/subjetivos_archivo"):
            os.makedirs("output/"+ciudad_clean+"/subjetivos_archivo")
        filename_bulk_ciudad ="output/"+ciudad_clean+ "/subjetivos_archivo/archivo_encuestas_" + ciudad_clean+"_lote.csv"
        filename_diccionario_bulk_ciudad = "output/"+ciudad_clean+ "/subjetivos_archivo/diccionario_archivo_encuestas_"+ciudad_clean+"_lote.csv"


        if not os.path.exists("output/"+ciudad_clean):
            os.makedirs("output/"+ciudad_clean)
        datos_bulk_ciudad = data[data['CIUDAD'] == ciudad_key]
        datos_bulk_ciudad_sinna = datos_bulk_ciudad.dropna(axis=1,how="all")
        diccionario_ciudad=create_dictionary(datos_bulk_ciudad_sinna)
        años_datos = np.unique(datos_bulk_ciudad_sinna.AÑO)

        datos_bulk_ciudad_sinna.to_csv(filename_bulk_ciudad,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)
        diccionario_ciudad.to_csv(filename_diccionario_bulk_ciudad,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)


    #data for indices only valid for years before 2008
    dictionary_fail = diccionario_bulk[diccionario_bulk.ano_max.notnull()]
    dictionary_fail= dictionary_fail[dictionary_fail.ano_max != "AÑO"]
    dictionary_fail = dictionary_fail[dictionary_fail["ano_max"].astype(int)<2008]
    datos_bulk_sinna = datos_bulk_sinna.drop(set(dictionary_fail["variable"]),1)
    dictionary_bulk = create_dictionary(datos_bulk_sinna)
    #repeat process for filtered data, this should only be a copy paste of what happens up there for the archive

    filename = "output/encuestas_lote.csv"
    filename_diccionario = "output/diccionario_encuestas_lote.csv"

    datos_bulk_sinna.to_csv(filename,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)
    diccionario_bulk.to_csv(filename_diccionario,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)

    for ciudad_key in diccionario_ciudades:

        print(ciudad_key)
        ciudad = diccionario_ciudades[ciudad_key]
        ciudad_clean = cleanstring(ciudad)
        filename_bulk_ciudad ="output/"+ciudad_clean + "/subjetivos_lote/encuestas_" + ciudad_clean+"_lote.csv"
        filename_diccionario_bulk_ciudad = "output/"+ciudad_clean + "/subjetivos_lote/" + "diccionario_encuestas_"+ciudad_clean+"_lote.csv"


        if not os.path.exists("output/"+ciudad_clean):
            os.makedirs("output/"+ciudad_clean)
        if not os.path.exists("output/"+ciudad_clean+"/subjetivos_lote"):
            os.makedirs("output/"+ciudad_clean+"/subjetivos_lote")
        if not os.path.exists("output/"+ciudad_clean+"/subjetivos_anual"):
            os.makedirs("output/"+ciudad_clean+"/subjetivos_anual")
        datos_bulk_ciudad = data[data['CIUDAD'] == ciudad_key]
        datos_bulk_ciudad_sinna = datos_bulk_ciudad.dropna(axis=1,how="all")
        diccionario_ciudad=create_dictionary(datos_bulk_ciudad_sinna)
        años_datos = np.unique(datos_bulk_ciudad_sinna.AÑO)

        datos_bulk_ciudad_sinna.to_csv(filename_bulk_ciudad,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)
        diccionario_ciudad.to_csv(filename_diccionario_bulk_ciudad,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)

        for año in años_datos:
            print(año)
            filename_año = "output/"+ciudad_clean + "/subjetivos_anual/encuestas_" + ciudad_clean+"_"+   año + ".csv"
            filename_diccionario_año = "output/"+ciudad_clean + "/subjetivos_anual/" + "diccionario_encuestas_"+ciudad_clean+"_"+año+".csv"
            datos_bulk_ciudad_año = datos_bulk_ciudad_sinna[datos_bulk_ciudad_sinna['AÑO'] == año]
            datos_bulk_ciudad_año_sinna = datos_bulk_ciudad_año.dropna(axis=1,how="all")
            diccionario_ciudad_año=create_dictionary(datos_bulk_ciudad_año_sinna)
            datos_bulk_ciudad_año_sinna.to_csv(filename_año,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)
            diccionario_ciudad_año.to_csv(filename_diccionario_año,quoting=csv.QUOTE_ALL, encoding="utf-8", na_rep = np.nan, index = False)
    return "Success"

print("Inicia - cargar diccionarios")
nomenclatura = pd.read_csv("builder/nomeclatura.csv",delimiter=",", dtype=np.string_)
respuestas = pd.read_csv("builder/respuestas.csv",delimiter=",", dtype=np.string_)
variables = pd.read_csv("builder/variables.csv",delimiter=",", dtype=np.string_)

print("Inicia - generar diccionarios")
preguntas_C = ['EP5A_SI_1', 'MV4_123_1', 'VS5A_45_1', 'SA3B_1', 'SP1B_45_1', 'CO4A_SI_1', 'GG3A_123_1', 'RC21_345_1', 'RC19_1', 'MC21A_20_1', 'SP3A_12_1', 'ED4F_1', 'SP4B_12_1', 'VS15A_1', 'CC15A_1', 'CR2A_45_1', 'MC7A_1', 'MC21A_16_1', 'SP5B_45_1', 'VS2A_3_1', 'PC7B_1', 'EP5A_NO_1', 'PR7C_2_1', 'VS5C_123_1', 'CO4A_NO_1', 'SP1D_1', 'MV6E_123_1', 'RC22_345_1', 'ED4G_1', 'MA4_1', 'CV1A_12_1', 'MC2A_1', 'VS3A_3_1', 'CR3_1', 'MV36_1', 'MC21A_17_1', 'SP7B_123_1', 'GG15_1', 'RC11_1', 'MV34_1', 'PC26_1', 'VS5C_45_1', 'SA3D_45_1', 'SP1D_123_1', 'MV6E_45_1', 'CC3_1', 'CO4B_1', 'VS17A_NO_1', 'ED4I_1', 'CC4B_1', 'CV1A_3_1', 'PC5A_1', 'CR1E_1', 'CC4_1', 'CR3B_1', 'MC21A_18_1', 'SP7B_45_1', 'VS2B_123_1', 'SA4A_12_1', 'RC10_1', 'EP1A_12_1', 'SP1D_45_1', 'MV6G_1', 'CO4C_1', 'RC1_1', 'VS6A_1', 'PR13_12_1', 'CC23_1', 'CV1A_45_1', 'SP4C_123_1', 'PC5B_1', 'PC13B_1', 'ED5_1', 'MV15B_PO_1', 'VS17A_SI_1', 'MA3_123_1', 'SP7C_123_1', 'VS2B_45_1', 'MV37_1', 'SP1E_123_1', 'SA4A_3_1', 'VS4A_45_1', 'VS17C_CAL_05_1', 'VS7A_12_1', 'SP4C_45_1', 'CV2B_1', 'RC20_123_1', 'CR4A_3_1', 'MA3_45_1', 'MC21A_3_1', 'EP3A_1', 'ED5B_1', 'CO14B_1', 'SP8B_12_1', 'SP2A_12_1', 'SA4A_45_1', 'DE3_1', 'VS17D_CAL_05_1', 'VS7A_3_1', 'GG10C_1', 'SP4D_123_1', 'CV3_1', 'MV40_123_1', 'DE5_1', 'CR4A_12_1', 'CR4A_45_1', 'MC21A_4_1', 'SP5B_12_1', 'MV14A_12_1', 'ED6B_1', 'MV40_45_1', 'SP8B_3_1', 'MC21A_2_1', 'MC22A_1', 'MV3A_1', 'SP2A_3_1', 'CR1_1', 'CC4C_1', 'CC9C_1', 'PR15_123_1', 'VS7A_45_1', 'SA5_1', 'A2_1', 'MC21A_6_1', 'CC4A_1', 'CV4A_1', 'VS19A_1', 'PC6A_1', 'MG3_1', 'CC9A_1', 'VS16_1', 'MC21A_5_1', 'MV14A_3_1', 'VS3A_45_1', 'ED8B_1', 'VS19A_45_1', 'SP8B_45_1', 'CR6_1', 'SA3D_123_1', 'SP2A_45_1', 'CC5A_12_1', 'GP0B_1', 'VS7C_1', 'CC10_CAR_08_1', 'A2A_1', 'CV4A_12_1', 'VS19A_12_1', 'PC7E_1', 'MG3A_1', 'CR2A_3_1', 'SA13_1', 'PR7A_45_1', 'MV14A_45_1', 'CR1D_1', 'VS3C_123_1', 'SP9B_12_1', 'COM1_1', 'MG1_1', 'ED10_1', 'EP1A_3_1', 'CC5A_3_1', 'GG5B_1', 'VS9_1', 'PC28B_1', 'CV4A_3_1', 'VS19A_3_1', 'VS2A_45_1', 'MG5A_1', 'MV15A_NE_1', 'MC21A_7_1', 'MA17_1', 'SA15_1', 'PC28A_1', 'MV15A_PO_1', 'VS3C_45_1', 'SP9B_3_1', 'VS7H_1', 'SP4B_3_1', 'SP2B_45_1', 'MV43_123_1', 'CC5A_45_1', 'VS4A_12_1', 'PR7C_1_1', 'RC2_1', 'GG3A_45_1', 'CV4A_45_1', 'ED18_1', 'SP6A_12_1', 'MC21A_8_1', 'MC21A_14_1', 'SA16_1', 'ED3C_1', 'CR1F_12_1', 'DE4_1', 'SP7A_12_1', 'SP9B_45_1', 'PR13_3_1', 'VS8A_123_1', 'SP2C_123_1', 'MC21A_15_1', 'PR16_123_1', 'MC8A_1', 'SP4B_45_1', 'CV5A_1', 'MV44_123_1', 'SP6A_3_1', 'PR14_123_1', 'CC19_CAR_05_1', 'MC21A_9_1', 'CR1F_3_1', 'SA19B_123_1', 'RC17_1', 'ED4A_12_1', 'VS8A_45_1', 'SP7A_45_1', 'VS0A_123_1', 'PC15A_1', 'SP1B_3_1', 'VS14_1', 'PR1_1', 'GP5_1', 'GG5B_12_1', 'ED20_1', 'SP6A_45_1', 'MC1A_1', 'MC21A_10_1', 'SP5B_3_1', 'CR1F_45_1', 'SA19B_45_1', 'CO1B_1', 'ED4A_3_1', 'PC1_1', 'VS0A_12_1', 'SP3A_3_1', 'MV42_1', 'PC13A_1', 'MC21A_1_1', 'GG5B_3_1', 'MV4_45_1', 'VS3A_12_1', 'SP6C_123_1', 'MV3B_1_1', 'MC21A_11_1', 'MV15B_NE_1', 'ED19_1', 'ED31_1', 'MA13_1', 'VS4C_123_1', 'SP1A_1', 'CO1B_12_1', 'ED4A_45_1', 'GG5B_45_1', 'PC2_1', 'VS0A_3_1', 'SP3A_45_1', 'PR13_45_1', 'MV4A_12_1', 'EP1A_45_1', 'SP6C_45_1', 'MC3A_1', 'MC21A_12_1', 'MV20_1', 'RC23_345_1', 'CC12_1', 'VS4C_45_1', 'CO1B_3_1', 'SA1A_1', 'ED4B_1', 'PC2A_1', 'VS0A_45_1', 'CC10_1', 'SP3C_123_1', 'PC20C_1', 'VS9A_1', 'MC21A_19_1', 'MV4A_3_1', 'PR7A_12_1', 'SP6D_123_1', 'MC4A_1', 'MC21A_13_1', 'CC1A_1', 'PR2A_1', 'VS10H_1', 'PR7A_3_1', 'VS5A_12_1', 'CO1B_45_1', 'SP1B_12_1', 'ED4A_123_1', 'VS4A_3_1', 'SP3B_123_1', 'PC20D_1', 'MV4B_123_1', 'MV4A_45_1', 'CR2A_12_1', 'MC5A_1', 'VS1E_1', 'SP2B_123_1', 'MG2_1', 'EP4A_1', 'SA2D_123_1', 'VS5A_3_1', 'GG13_1', 'CO3_1', 'MV22_1', 'ED4A2_45_1', 'VS25_1', 'SP3B_45_1', 'PC21_1', 'MV41_1', 'PC7_1', 'MC6A_1', 'RC20_45_1', 'SP7A_3_1', 'VS2A_12_1', 'SP1A2_1', 'PC24_1']
diccionario_ciudades = {'8001': 'Barranquilla', '76892': 'Yumbo', '20001': 'Valledupar', '17001': 'Manizales', '73001': 'Ibagué', '76001': 'Cali','13001': 'Cartagena', '54001': 'Cucuta','68001': 'Bucaramanga Metropolitana','66001': 'Pereira','5001': 'Medellín','11001': 'Bogotá'}
#diccionario_ciudades = {'11001': 'Bogotá'}
prefix_cat_dim_dict = {}
for line in nomenclatura.index:
    prefix_cat_dim_dict[nomenclatura.Nomenclatura[line]] = {"dimension": nomenclatura.Dimension[line], "modulo": nomenclatura.Modulo[line]}

print("Inicia - Cargar Variables")
prefix_variables = {}
for line in variables.index:
    Variable = variables.Nombre[line]
    Variable_Fixed = variable_preprocess(Variable)
    prefix_variables[Variable_Fixed] = variables.Label[line]

print("Inicia - Cargar Respuestas")
prefix_respuestas = {}
for line in respuestas.index:
    Variable = respuestas.Variables[line]
    Variable_Fixed = variable_preprocess(Variable)
    if Variable_Fixed not in prefix_respuestas:
        prefix_respuestas[Variable_Fixed] = {}
    prefix_respuestas[Variable_Fixed][respuestas.id_label[line]] = respuestas.label[line]
print("Inicia - Generar CSVs")
status_csv =generar_csvs(data)
print(status_csv)
