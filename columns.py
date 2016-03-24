import pandas
import numpy
import csv

variable_names = ['EP5A_SI_1', 'MV4_123_1', 'VS5A_45_1', 'SA3B_1', 'SP1B_45_1', 'CO4A_SI_1', 'GG3A_123_1', 'RC21_345_1', 'RC19_1', 'MC21A_20_1', 'SP3A_12_1', 'ED4F_1', 'SP4B_12_1', 'VS15A_1', 'CC15A_1', 'CR2A_45_1', 'MC7A_1', 'MC21A_16_1', 'SP5B_45_1', 'VS2A_3_1', 'PC7B_1', 'EP5A_NO_1', 'PR7C_2_1', 'VS5C_123_1', 'CO4A_NO_1', 'SP1D_1', 'MV6E_123_1', 'RC22_345_1', 'ED4G_1', 'MA4_1', 'CV1A_12_1', 'MC2A_1', 'VS3A_3_1', 'CR3_1', 'MV36_1', 'MC21A_17_1', 'SP7B_123_1', 'GG15_1', 'RC11_1', 'MV34_1', 'PC26_1', 'VS5C_45_1', 'SA3D_45_1', 'SP1D_123_1', 'MV6E_45_1', 'CC3_1', 'CO4B_1', 'VS17A_NO_1', 'ED4I_1', 'CC4B_1', 'CV1A_3_1', 'PC5A_1', 'CR1E_1', 'CC4_1', 'CR3B_1', 'MC21A_18_1', 'SP7B_45_1', 'VS2B_123_1', 'SA4A_12_1', 'RC10_1', 'EP1A_12_1', 'SP1D_45_1', 'MV6G_1', 'CO4C_1', 'RC1_1', 'VS6A_1', 'PR13_12_1', 'CC23_1', 'CV1A_45_1', 'SP4C_123_1', 'PC5B_1', 'PC13B_1', 'ED5_1', 'MV15B_PO_1', 'VS17A_SI_1', 'MA3_123_1', 'SP7C_123_1', 'VS2B_45_1', 'MV37_1', 'SP1E_123_1', 'SA4A_3_1', 'VS4A_45_1', 'VS17C_CAL_05_1', 'VS7A_12_1', 'SP4C_45_1', 'CV2B_1', 'RC20_123_1', 'CR4A_3_1', 'MA3_45_1', 'MC21A_3_1', 'EP3A_1', 'ED5B_1', 'CO14B_1', 'SP8B_12_1', 'SP2A_12_1', 'SA4A_45_1', 'DE3_1', 'VS17D_CAL_05_1', 'VS7A_3_1', 'GG10C_1', 'SP4D_123_1', 'CV3_1', 'MV40_123_1', 'DE5_1', 'CR4A_12_1', 'CR4A_45_1', 'MC21A_4_1', 'SP5B_12_1', 'MV14A_12_1', 'ED6B_1', 'MV40_45_1', 'SP8B_3_1', 'MC21A_2_1', 'MC22A_1', 'MV3A_1', 'SP2A_3_1', 'CR1_1', 'CC4C_1', 'CC9C_1', 'PR15_123_1', 'VS7A_45_1', 'SA5_1', 'A2_1', 'MC21A_6_1', 'CC4A_1', 'CV4A_1', 'VS19A_1', 'PC6A_1', 'MG3_1', 'CC9A_1', 'VS16_1', 'MC21A_5_1', 'MV14A_3_1', 'VS3A_45_1', 'ED8B_1', 'VS19A_45_1', 'SP8B_45_1', 'CR6_1', 'SA3D_123_1', 'SP2A_45_1', 'CC5A_12_1', 'GP0B_1', 'VS7C_1', 'CC10_CAR_08_1', 'A2A_1', 'CV4A_12_1', 'VS19A_12_1', 'PC7E_1', 'MG3A_1', 'CR2A_3_1', 'SA13_1', 'PR7A_45_1', 'MV14A_45_1', 'CR1D_1', 'VS3C_123_1', 'SP9B_12_1', 'COM1_1', 'MG1_1', 'ED10_1', 'EP1A_3_1', 'CC5A_3_1', 'GG5B_1', 'VS9_1', 'PC28B_1', 'CV4A_3_1', 'VS19A_3_1', 'VS2A_45_1', 'MG5A_1', 'MV15A_NE_1', 'MC21A_7_1', 'MA17_1', 'SA15_1', 'PC28A_1', 'MV15A_PO_1', 'VS3C_45_1', 'SP9B_3_1', 'VS7H_1', 'SP4B_3_1', 'SP2B_45_1', 'MV43_123_1', 'CC5A_45_1', 'VS4A_12_1', 'PR7C_1_1', 'RC2_1', 'GG3A_45_1', 'CV4A_45_1', 'ED18_1', 'SP6A_12_1', 'MC21A_8_1', 'MC21A_14_1', 'SA16_1', 'ED3C_1', 'CR1F_12_1', 'DE4_1', 'SP7A_12_1', 'SP9B_45_1', 'PR13_3_1', 'VS8A_123_1', 'SP2C_123_1', 'MC21A_15_1', 'PR16_123_1', 'MC8A_1', 'SP4B_45_1', 'CV5A_1', 'MV44_123_1', 'SP6A_3_1', 'PR14_123_1', 'CC19_CAR_05_1', 'MC21A_9_1', 'CR1F_3_1', 'SA19B_123_1', 'RC17_1', 'ED4A_12_1', 'VS8A_45_1', 'SP7A_45_1', 'VS0A_123_1', 'PC15A_1', 'SP1B_3_1', 'VS14_1', 'PR1_1', 'GP5_1', 'GG5B_12_1', 'ED20_1', 'SP6A_45_1', 'MC1A_1', 'MC21A_10_1', 'SP5B_3_1', 'CR1F_45_1', 'SA19B_45_1', 'CO1B_1', 'ED4A_3_1', 'PC1_1', 'VS0A_12_1', 'SP3A_3_1', 'MV42_1', 'PC13A_1', 'MC21A_1_1', 'GG5B_3_1', 'MV4_45_1', 'VS3A_12_1', 'SP6C_123_1', 'MV3B_1_1', 'MC21A_11_1', 'MV15B_NE_1', 'ED19_1', 'ED31_1', 'MA13_1', 'VS4C_123_1', 'SP1A_1', 'CO1B_12_1', 'ED4A_45_1', 'GG5B_45_1', 'PC2_1', 'VS0A_3_1', 'SP3A_45_1', 'PR13_45_1', 'MV4A_12_1', 'EP1A_45_1', 'SP6C_45_1', 'MC3A_1', 'MC21A_12_1', 'MV20_1', 'RC23_345_1', 'CC12_1', 'VS4C_45_1', 'CO1B_3_1', 'SA1A_1', 'ED4B_1', 'PC2A_1', 'VS0A_45_1', 'CC10_1', 'SP3C_123_1', 'PC20C_1', 'VS9A_1', 'MC21A_19_1', 'MV4A_3_1', 'PR7A_12_1', 'SP6D_123_1', 'MC4A_1', 'MC21A_13_1', 'CC1A_1', 'PR2A_1', 'VS10H_1', 'PR7A_3_1', 'VS5A_12_1', 'CO1B_45_1', 'SP1B_12_1', 'ED4A_123_1', 'VS4A_3_1', 'SP3B_123_1', 'PC20D_1', 'MV4B_123_1', 'MV4A_45_1', 'CR2A_12_1', 'MC5A_1', 'VS1E_1', 'SP2B_123_1', 'MG2_1', 'EP4A_1', 'SA2D_123_1', 'VS5A_3_1', 'GG13_1', 'CO3_1', 'MV22_1', 'ED4A2_45_1', 'VS25_1', 'SP3B_45_1', 'PC21_1', 'MV41_1', 'PC7_1', 'MC6A_1', 'RC20_45_1', 'SP7A_3_1', 'VS2A_12_1', 'SP1A2_1', 'PC24_1']


print("Reading File")
#data = pandas.read_csv("output_2.csv", delimiter = ",",dtype=numpy.string_, engine='python' )
data = pandas.read_csv("output_2.csv", delimiter = ",", dtype=numpy.string_ )
print("Finshed Reading File")
n, m = data.shape
jump = 30
i = 0
table = pandas.DataFrame()
iternum = 0

list_num = []
dict_num = {}
for variable in variable_names:
    pos = data.columns.get_loc(variable)
    list_num.append(pos)
    dict_num[pos] = variable
print(list_num)
list_num = sorted(list_num)

while i < n:
    while iternum < len(list_num):
        next_lim = list_num[iternum]
        working_cols = data.iloc[:,next_lim+1]
        extract_cols = data.iloc[:,i:next_lim]
        j = 0
        while j < jump-1:
            working_cols = working_cols + ";" + data.iloc[:,next_lim+j]
            j = j + 1

        df_working_cols = pandas.DataFrame(working_cols)
        df_working_cols.rename(columns={0:dict_num[next_lim][0:-2]}, inplace=True)

        extract_cols = pandas.concat([extract_cols,df_working_cols], axis = 1, join='inner')

        if i == iternum:
            table = extract_cols
        else:
            table = pandas.concat([table,extract_cols], axis = 1, join='inner')
        iternum = iternum + 1
        i = next_lim + jump
    table = pandas.concat([table,data.iloc[:,i:-1]], axis = 1)
    table = pandas.concat([table,pandas.DataFrame(data.iloc[:,-1])], axis = 1)
    i = n
print(table)
print("Writing File")
table.to_csv("output_3.csv",quoting=csv.QUOTE_NONNUMERIC, encoding="utf-8", na_rep = numpy.nan, index = False)
print("End of Program")
