import pandas
import numpy
import csv

dict_num = {46: 'CV1A_12', 76: 'CV1A_3', 106: 'CV1A_45', 139: 'CV2B', 169: 'CV3', 200: 'CV4A', 230: 'CV4A_12', 260: 'CV4A_3', 290: 'CV4A_45', 321: 'CV5A', 366: 'CO1B', 396: 'CO1B_12', 426: 'CO1B_3', 456: 'CO1B_45', 487: 'CO3', 518: 'CO4A_SI', 548: 'CO4A_NO', 582: 'CO4B', 612: 'CO4C', 663: 'CO14B', 708: 'A2', 738: 'A2A', 811: 'ED3C', 849: 'ED4A_12', 879: 'ED4A_3', 909: 'ED4A_45', 940: 'ED4B', 971: 'ED4A_123', 1001: 'ED4A2_45', 1036: 'ED4F', 1066: 'ED4G', 1097: 'ED4I', 1136: 'ED5', 1173: 'ED5B', 1203: 'ED6B', 1234: 'ED8B', 1274: 'ED10', 1315: 'ED18', 1345: 'ED19', 1375: 'ED20', 1416: 'ED31', 1451: 'SA1A', 1508: 'SA2D_123', 1540: 'SA3B', 1572: 'SA3D_123', 1602: 'SA3D_45', 1636: 'SA4A_12', 1666: 'SA4A_3', 1696: 'SA4A_45', 1731: 'SA5', 1772: 'SA13', 1804: 'SA15', 1834: 'SA16', 1869: 'SA19B_123', 1899: 'SA19B_45', 1931: 'SP1A', 1962: 'SP1A2', 1993: 'SP1B_12', 2023: 'SP1B_3', 2053: 'SP1B_45', 2085: 'SP1D', 2115: 'SP1D_123', 2145: 'SP1D_45', 2175: 'SP1E_123', 2206: 'SP2A_12', 2236: 'SP2A_3', 2266: 'SP2A_45', 2298: 'SP2B_123', 2328: 'SP2B_45', 2358: 'SP2C_123', 2391: 'SP3A_12', 2421: 'SP3A_3', 2451: 'SP3A_45', 2482: 'SP3C_123', 2512: 'SP3B_123', 2542: 'SP3B_45', 2576: 'SP4B_12', 2606: 'SP4B_3', 2636: 'SP4B_45', 2667: 'SP4C_123', 2697: 'SP4C_45', 2727: 'SP4D_123', 2760: 'SP5B_12', 2790: 'SP5B_3', 2820: 'SP5B_45', 2853: 'SP6A_12', 2883: 'SP6A_3', 2913: 'SP6A_45', 2944: 'SP6C_123', 2974: 'SP6C_45', 3004: 'SP6D_123', 3037: 'SP7A_12', 3067: 'SP7A_3', 3097: 'SP7A_45', 3128: 'SP7B_123', 3158: 'SP7B_45', 3188: 'SP7C_123', 3224: 'SP8B_12', 3254: 'SP8B_3', 3284: 'SP8B_45', 3316: 'SP9B_12', 3346: 'SP9B_3', 3376: 'SP9B_45', 3413: 'VS0A_123', 3443: 'VS0A_12', 3473: 'VS0A_3', 3503: 'VS0A_45', 3548: 'VS1E', 3580: 'VS2A_12', 3610: 'VS2A_3', 3640: 'VS2A_45', 3671: 'VS2B_123', 3701: 'VS2B_45', 3733: 'VS3A_12', 3763: 'VS3A_3', 3793: 'VS3A_45', 3825: 'VS3C_123', 3855: 'VS3C_45', 3887: 'VS4A_12', 3917: 'VS4A_3', 3947: 'VS4A_45', 3978: 'VS4C_123', 4008: 'VS4C_45', 4039: 'VS5A_12', 4069: 'VS5A_3', 4099: 'VS5A_45', 4130: 'VS5C_123', 4160: 'VS5C_45', 4198: 'VS6A', 4229: 'VS7A_12', 4259: 'VS7A_3', 4289: 'VS7A_45', 4320: 'VS7C', 4372: 'VS7H', 4404: 'VS8A_123', 4434: 'VS8A_45', 4480: 'VS9', 4510: 'VS9A', 4547: 'VS10H', 4580: 'VS14', 4611: 'VS15A', 4642: 'VS16', 4675: 'VS17A_SI', 4705: 'VS17A_NO', 4740: 'VS17C_CAL_05', 4770: 'VS17D_CAL_05', 4809: 'VS19A', 4839: 'VS19A_12', 4869: 'VS19A_3', 4899: 'VS19A_45', 4946: 'VS25', 4976: 'PC1', 5007: 'PC2', 5037: 'PC2A', 5067: 'PC13B', 5097: 'PC13A', 5198: 'PC5A', 5228: 'PC5B', 5259: 'PC6A', 5289: 'PC7', 5320: 'PC7B', 5352: 'PC7E', 5389: 'PC28A', 5419: 'PC28B', 5462: 'PC15A', 5555: 'PC20C', 5585: 'PC20D', 5615: 'PC21', 5660: 'PC24', 5694: 'PC26', 5734: 'RC1', 5765: 'RC2', 5953: 'RC10', 5983: 'RC11', 6029: 'RC17', 6060: 'RC19', 6091: 'RC20_123', 6121: 'RC20_45', 6152: 'RC21_345', 6183: 'RC22_345', 6214: 'RC23_345', 6256: 'DE3', 6286: 'DE4', 6316: 'DE5', 6346: 'CR1', 6383: 'CR1D', 6413: 'CR1E', 6444: 'CR1F_12', 6474: 'CR1F_3', 6504: 'CR1F_45', 6617: 'CR2A_12', 6647: 'CR2A_3', 6677: 'CR2A_45', 6708: 'CR3', 6739: 'CR3B', 6770: 'CR4A_12', 6800: 'CR4A_3', 6830: 'CR4A_45', 6869: 'CR6', 6902: 'COM1', 6943: 'MV3A', 6976: 'MV3B_1', 7007: 'MV4_123', 7037: 'MV4_45', 7068: 'MV4A_12', 7098: 'MV4A_3', 7128: 'MV4A_45', 7159: 'MV4B_123', 7206: 'MV6E_123', 7236: 'MV6E_45', 7267: 'MV6G', 7346: 'MV14A_12', 7376: 'MV14A_3', 7406: 'MV14A_45', 7438: 'MV15A_PO', 7468: 'MV15A_NE', 7528: 'MV15B_PO', 7558: 'MV15B_NE', 7624: 'MV20', 7656: 'MV22', 7741: 'MV34', 7774: 'MV36', 7804: 'MV37', 7850: 'MV40_123', 7880: 'MV40_45', 7910: 'MV41', 7940: 'MV42', 7971: 'MV43_123', 8002: 'MV44_123', 8033: 'EP1A_12', 8063: 'EP1A_3', 8093: 'EP1A_45', 8131: 'EP3A', 8162: 'EP4A', 8193: 'EP5A_SI', 8223: 'EP5A_NO', 8253: 'MA4', 8307: 'MA3_123', 8337: 'MA3_45', 8418: 'MA13', 8459: 'MA17', 8547: 'MC1A', 8577: 'MC2A', 8607: 'MC3A', 8637: 'MC4A', 8667: 'MC5A', 8697: 'MC6A', 8727: 'MC7A', 8757: 'MC8A', 8790: 'MC21A_1', 8820: 'MC21A_2', 8850: 'MC21A_3', 8880: 'MC21A_4', 8910: 'MC21A_5', 8940: 'MC21A_6', 8970: 'MC21A_7', 9000: 'MC21A_8', 9030: 'MC21A_9', 9060: 'MC21A_10', 9090: 'MC21A_11', 9120: 'MC21A_12', 9150: 'MC21A_13', 9180: 'MC21A_14', 9210: 'MC21A_15', 9240: 'MC21A_16', 9270: 'MC21A_17', 9300: 'MC21A_18', 9330: 'MC21A_19', 9360: 'MC21A_20', 9402: 'MC22A', 9439: 'GP0B', 11100: 'GP5', 11135: 'PR1', 11168: 'PR2A', 11688: 'PR7A_12', 11718: 'PR7A_3', 11748: 'PR7A_45', 11779: 'PR7C_1', 11809: 'PR7C_2', 11846: 'PR13_12', 11876: 'PR13_3', 11906: 'PR13_45', 11937: 'PR14_123', 11968: 'PR15_123', 11999: 'PR16_123', 12033: 'GG3A_123', 12063: 'GG3A_45', 12096: 'GG5B', 12126: 'GG5B_12', 12156: 'GG5B_3', 12186: 'GG5B_45', 12230: 'GG10C', 12262: 'GG13', 12294: 'GG15', 12324: 'CC1A', 12358: 'CC3', 12388: 'CC4', 12418: 'CC4A', 12448: 'CC4B', 12478: 'CC4C', 12510: 'CC5A_12', 12540: 'CC5A_3', 12570: 'CC5A_45', 12661: 'CC9C', 12691: 'CC9A', 12721: 'CC10', 12752: 'CC10_CAR_08', 12785: 'CC12', 12820: 'CC15A', 12854: 'CC19_CAR_05', 12886: 'CC23', 12917: 'MG1', 12965: 'MG2', 13003: 'MG3', 13033: 'MG3A', 13064: 'MG5A'}
list_num = [46, 76, 106, 139, 169, 200, 230, 260, 290, 321, 366, 396, 426, 456, 487, 518, 548, 582, 612, 663, 708, 738, 811, 849, 879, 909, 940, 971, 1001, 1036, 1066, 1097, 1136, 1173, 1203, 1234, 1274, 1315, 1345, 1375, 1416, 1451, 1508, 1540, 1572, 1602, 1636, 1666, 1696, 1731, 1772, 1804, 1834, 1869, 1899, 1931, 1962, 1993, 2023, 2053, 2085, 2115, 2145, 2175, 2206, 2236, 2266, 2298, 2328, 2358, 2391, 2421, 2451, 2482, 2512, 2542, 2576, 2606, 2636, 2667, 2697, 2727, 2760, 2790, 2820, 2853, 2883, 2913, 2944, 2974, 3004, 3037, 3067, 3097, 3128, 3158, 3188, 3224, 3254, 3284, 3316, 3346, 3376, 3413, 3443, 3473, 3503, 3548, 3580, 3610, 3640, 3671, 3701, 3733, 3763, 3793, 3825, 3855, 3887, 3917, 3947, 3978, 4008, 4039, 4069, 4099, 4130, 4160, 4198, 4229, 4259, 4289, 4320, 4372, 4404, 4434, 4480, 4510, 4547, 4580, 4611, 4642, 4675, 4705, 4740, 4770, 4809, 4839, 4869, 4899, 4946, 4976, 5007, 5037, 5067, 5097, 5198, 5228, 5259, 5289, 5320, 5352, 5389, 5419, 5462, 5555, 5585, 5615, 5660, 5694, 5734, 5765, 5953, 5983, 6029, 6060, 6091, 6121, 6152, 6183, 6214, 6256, 6286, 6316, 6346, 6383, 6413, 6444, 6474, 6504, 6617, 6647, 6677, 6708, 6739, 6770, 6800, 6830, 6869, 6902, 6943, 6976, 7007, 7037, 7068, 7098, 7128, 7159, 7206, 7236, 7267, 7346, 7376, 7406, 7438, 7468, 7528, 7558, 7624, 7656, 7741, 7774, 7804, 7850, 7880, 7910, 7940, 7971, 8002, 8033, 8063, 8093, 8131, 8162, 8193, 8223, 8253, 8307, 8337, 8418, 8459, 8547, 8577, 8607, 8637, 8667, 8697, 8727, 8757, 8790, 8820, 8850, 8880, 8910, 8940, 8970, 9000, 9030, 9060, 9090, 9120, 9150, 9180, 9210, 9240, 9270, 9300, 9330, 9360, 9402, 9439, 11100, 11135, 11168, 11688, 11718, 11748, 11779, 11809, 11846, 11876, 11906, 11937, 11968, 11999, 12033, 12063, 12096, 12126, 12156, 12186, 12230, 12262, 12294, 12324, 12358, 12388, 12418, 12448, 12478, 12510, 12540, 12570, 12661, 12691, 12721, 12752, 12785, 12820, 12854, 12886, 12917, 12965, 13003, 13033, 13064]

#list_num = [45, 75, 105, 138, 168, 199, 229, 259, 289, 320, 365, 395, 425, 455, 486, 517, 547, 581, 611, 662, 707, 737, 810, 848, 878, 908, 939, 970, 1000, 1035, 1065, 1096, 1135, 1172, 1202, 1233, 1273, 1314, 1344, 1374, 1415, 1450, 1507, 1539, 1571, 1601, 1635, 1665, 1695, 1730, 1771, 1803, 1833, 1868, 1898, 1930, 1961, 1992, 2022, 2052, 2084, 2114, 2144, 2174, 2205, 2235, 2265, 2297, 2327, 2357, 2390, 2420, 2450, 2481, 2511, 2541, 2575, 2605, 2635, 2666, 2696, 2726, 2759, 2789, 2819, 2852, 2882, 2912, 2943, 2973, 3003, 3036, 3066, 3096, 3127, 3157, 3187, 3223, 3253, 3283, 3315, 3345, 3375, 3412, 3442, 3472, 3502, 3547, 3579, 3609, 3639, 3670, 3700, 3732, 3762, 3792, 3824, 3854, 3886, 3916, 3946, 3977, 4007, 4038, 4068, 4098, 4129, 4159, 4197, 4228, 4258, 4288, 4319, 4371, 4403, 4433, 4479, 4509, 4546, 4579, 4610, 4641, 4674, 4704, 4739, 4769, 4808, 4838, 4868, 4898, 4945, 4975, 5006, 5036, 5066, 5096, 5197, 5227, 5258, 5288, 5319, 5351, 5388, 5418, 5461, 5554, 5584, 5614, 5659, 5693, 5733, 5764, 5952, 5982, 6028, 6059, 6090, 6120, 6151, 6182, 6213, 6255, 6285, 6315, 6345, 6382, 6412, 6443, 6473, 6503, 6616, 6646, 6676, 6707, 6738, 6769, 6799, 6829, 6868, 6901, 6942, 6975, 7006, 7036, 7067, 7097, 7127, 7158, 7205, 7235, 7266, 7345, 7375, 7405, 7437, 7467, 7527, 7557, 7623, 7655, 7740, 7773, 7803, 7849, 7879, 7909, 7939, 7970, 8001, 8032, 8062, 8092, 8130, 8161, 8192, 8222, 8252, 8306, 8336, 8417, 8458, 8546, 8576, 8606, 8636, 8666, 8696, 8726, 8756, 8789, 8819, 8849, 8879, 8909, 8939, 8969, 8999, 9029, 9059, 9089, 9119, 9149, 9179, 9209, 9239, 9269, 9299, 9329, 9359, 9401, 9438, 11099, 11134, 11167, 11687, 11717, 11747, 11778, 11808, 11845, 11875, 11905, 11936, 11967, 11998, 12032, 12062, 12095, 12125, 12155, 12185, 12229, 12261, 12293, 12323, 12357, 12387, 12417, 12447, 12477, 12509, 12539, 12569, 12660, 12690, 12720, 12751, 12784, 12819, 12853, 12885, 12916, 12964, 13002, 13032, 13063]
#dict_num = {45: 'CV1A_12', 75: 'CV1A_3', 105: 'CV1A_45', 138: 'CV2B', 168: 'CV3', 199: 'CV4A', 229: 'CV4A_12', 259: 'CV4A_3', 289: 'CV4A_45', 320: 'CV5A', 365: 'CO1B', 395: 'CO1B_12', 425: 'CO1B_3', 455: 'CO1B_45', 486: 'CO3', 517: 'CO4A_SI', 547: 'CO4A_NO', 581: 'CO4B', 611: 'CO4C', 662: 'CO14B', 707: 'A2', 737: 'A2A', 810: 'ED3C', 848: 'ED4A_12', 878: 'ED4A_3', 908: 'ED4A_45', 939: 'ED4B', 970: 'ED4A_123', 1000: 'ED4A2_45', 1035: 'ED4F', 1065: 'ED4G', 1096: 'ED4I', 1135: 'ED5', 1172: 'ED5B', 1202: 'ED6B', 1233: 'ED8B', 1273: 'ED10', 1314: 'ED18', 1344: 'ED19', 1374: 'ED20', 1415: 'ED31', 1450: 'SA1A', 1507: 'SA2D_123', 1539: 'SA3B', 1571: 'SA3D_123', 1601: 'SA3D_45', 1635: 'SA4A_12', 1665: 'SA4A_3', 1695: 'SA4A_45', 1730: 'SA5', 1771: 'SA13', 1803: 'SA15', 1833: 'SA16', 1868: 'SA19B_123', 1898: 'SA19B_45', 1930: 'SP1A', 1961: 'SP1A2', 1992: 'SP1B_12', 2022: 'SP1B_3', 2052: 'SP1B_45', 2084: 'SP1D', 2114: 'SP1D_123', 2144: 'SP1D_45', 2174: 'SP1E_123', 2205: 'SP2A_12', 2235: 'SP2A_3', 2265: 'SP2A_45', 2297: 'SP2B_123', 2327: 'SP2B_45', 2357: 'SP2C_123', 2390: 'SP3A_12', 2420: 'SP3A_3', 2450: 'SP3A_45', 2481: 'SP3C_123', 2511: 'SP3B_123', 2541: 'SP3B_45', 2575: 'SP4B_12', 2605: 'SP4B_3', 2635: 'SP4B_45', 2666: 'SP4C_123', 2696: 'SP4C_45', 2726: 'SP4D_123', 2759: 'SP5B_12', 2789: 'SP5B_3', 2819: 'SP5B_45', 2852: 'SP6A_12', 2882: 'SP6A_3', 2912: 'SP6A_45', 2943: 'SP6C_123', 2973: 'SP6C_45', 3003: 'SP6D_123', 3036: 'SP7A_12', 3066: 'SP7A_3', 3096: 'SP7A_45', 3127: 'SP7B_123', 3157: 'SP7B_45', 3187: 'SP7C_123', 3223: 'SP8B_12', 3253: 'SP8B_3', 3283: 'SP8B_45', 3315: 'SP9B_12', 3345: 'SP9B_3', 3375: 'SP9B_45', 3412: 'VS0A_123', 3442: 'VS0A_12', 3472: 'VS0A_3', 3502: 'VS0A_45', 3547: 'VS1E', 3579: 'VS2A_12', 3609: 'VS2A_3', 3639: 'VS2A_45', 3670: 'VS2B_123', 3700: 'VS2B_45', 3732: 'VS3A_12', 3762: 'VS3A_3', 3792: 'VS3A_45', 3824: 'VS3C_123', 3854: 'VS3C_45', 3886: 'VS4A_12', 3916: 'VS4A_3', 3946: 'VS4A_45', 3977: 'VS4C_123', 4007: 'VS4C_45', 4038: 'VS5A_12', 4068: 'VS5A_3', 4098: 'VS5A_45', 4129: 'VS5C_123', 4159: 'VS5C_45', 4197: 'VS6A', 4228: 'VS7A_12', 4258: 'VS7A_3', 4288: 'VS7A_45', 4319: 'VS7C', 4371: 'VS7H', 4403: 'VS8A_123', 4433: 'VS8A_45', 4479: 'VS9', 4509: 'VS9A', 4546: 'VS10H', 4579: 'VS14', 4610: 'VS15A', 4641: 'VS16', 4674: 'VS17A_SI', 4704: 'VS17A_NO', 4739: 'VS17C_CAL_05', 4769: 'VS17D_CAL_05', 4808: 'VS19A', 4838: 'VS19A_12', 4868: 'VS19A_3', 4898: 'VS19A_45', 4945: 'VS25', 4975: 'PC1', 5006: 'PC2', 5036: 'PC2A', 5066: 'PC13B', 5096: 'PC13A', 5197: 'PC5A', 5227: 'PC5B', 5258: 'PC6A', 5288: 'PC7', 5319: 'PC7B', 5351: 'PC7E', 5388: 'PC28A', 5418: 'PC28B', 5461: 'PC15A', 5554: 'PC20C', 5584: 'PC20D', 5614: 'PC21', 5659: 'PC24', 5693: 'PC26', 5733: 'RC1', 5764: 'RC2', 5952: 'RC10', 5982: 'RC11', 6028: 'RC17', 6059: 'RC19', 6090: 'RC20_123', 6120: 'RC20_45', 6151: 'RC21_345', 6182: 'RC22_345', 6213: 'RC23_345', 6255: 'DE3', 6285: 'DE4', 6315: 'DE5', 6345: 'CR1', 6382: 'CR1D', 6412: 'CR1E', 6443: 'CR1F_12', 6473: 'CR1F_3', 6503: 'CR1F_45', 6616: 'CR2A_12', 6646: 'CR2A_3', 6676: 'CR2A_45', 6707: 'CR3', 6738: 'CR3B', 6769: 'CR4A_12', 6799: 'CR4A_3', 6829: 'CR4A_45', 6868: 'CR6', 6901: 'COM1', 6942: 'MV3A', 6975: 'MV3B_1', 7006: 'MV4_123', 7036: 'MV4_45', 7067: 'MV4A_12', 7097: 'MV4A_3', 7127: 'MV4A_45', 7158: 'MV4B_123', 7205: 'MV6E_123', 7235: 'MV6E_45', 7266: 'MV6G', 7345: 'MV14A_12', 7375: 'MV14A_3', 7405: 'MV14A_45', 7437: 'MV15A_PO', 7467: 'MV15A_NE', 7527: 'MV15B_PO', 7557: 'MV15B_NE', 7623: 'MV20', 7655: 'MV22', 7740: 'MV34', 7773: 'MV36', 7803: 'MV37', 7849: 'MV40_123', 7879: 'MV40_45', 7909: 'MV41', 7939: 'MV42', 7970: 'MV43_123', 8001: 'MV44_123', 8032: 'EP1A_12', 8062: 'EP1A_3', 8092: 'EP1A_45', 8130: 'EP3A', 8161: 'EP4A', 8192: 'EP5A_SI', 8222: 'EP5A_NO', 8252: 'MA4', 8306: 'MA3_123', 8336: 'MA3_45', 8417: 'MA13', 8458: 'MA17', 8546: 'MC1A', 8576: 'MC2A', 8606: 'MC3A', 8636: 'MC4A', 8666: 'MC5A', 8696: 'MC6A', 8726: 'MC7A', 8756: 'MC8A', 8789: 'MC21A_1', 8819: 'MC21A_2', 8849: 'MC21A_3', 8879: 'MC21A_4', 8909: 'MC21A_5', 8939: 'MC21A_6', 8969: 'MC21A_7', 8999: 'MC21A_8', 9029: 'MC21A_9', 9059: 'MC21A_10', 9089: 'MC21A_11', 9119: 'MC21A_12', 9149: 'MC21A_13', 9179: 'MC21A_14', 9209: 'MC21A_15', 9239: 'MC21A_16', 9269: 'MC21A_17', 9299: 'MC21A_18', 9329: 'MC21A_19', 9359: 'MC21A_20', 9401: 'MC22A', 9438: 'GP0B', 11099: 'GP5', 11134: 'PR1', 11167: 'PR2A', 11687: 'PR7A_12', 11717: 'PR7A_3', 11747: 'PR7A_45', 11778: 'PR7C_1', 11808: 'PR7C_2', 11845: 'PR13_12', 11875: 'PR13_3', 11905: 'PR13_45', 11936: 'PR14_123', 11967: 'PR15_123', 11998: 'PR16_123', 12032: 'GG3A_123', 12062: 'GG3A_45', 12095: 'GG5B', 12125: 'GG5B_12', 12155: 'GG5B_3', 12185: 'GG5B_45', 12229: 'GG10C', 12261: 'GG13', 12293: 'GG15', 12323: 'CC1A', 12357: 'CC3', 12387: 'CC4', 12417: 'CC4A', 12447: 'CC4B', 12477: 'CC4C', 12509: 'CC5A_12', 12539: 'CC5A_3', 12569: 'CC5A_45', 12660: 'CC9C', 12690: 'CC9A', 12720: 'CC10', 12751: 'CC10_CAR_08', 12784: 'CC12', 12819: 'CC15A', 12853: 'CC19_CAR_05', 12885: 'CC23', 12916: 'MG1', 12964: 'MG2', 13002: 'MG3', 13032: 'MG3A', 13063: 'MG5A'}

print("Reading File")
#data = pandas.read_csv("output_2.csv", delimiter = ",",dtype=numpy.string_, engine='python' )
data = pandas.read_csv("output_2.csv", delimiter = ",", dtype=numpy.string_ )
print("Finshed Reading File")
n, m = data.shape
jump = 30
i = 0
table = pandas.DataFrame()
iternum = 0
while i < n:
    while iternum < len(list_num):
        next_lim = list_num[iternum]
        print(i)
        print(next_lim)
        print(data.columns.values[i])
        print(data.columns.values[next_lim])
        extract_cols = data.iloc[:,i:next_lim-1]
        working_cols = data.iloc[:,next_lim-1]
        j = 0
        print(data.columns.values[next_lim-1:next_lim+jump-1])
        while j < jump-1:
            working_cols = working_cols + ";" + data.iloc[:,next_lim+j]
            j = j + 1
        print(working_cols)
        print(pandas.DataFrame())
        extract_cols = pandas.concat([extract_cols,pandas.DataFrame(working_cols)], axis = 1, join='inner')
        extract_cols.rename(columns={0:dict_num[next_lim]}, inplace=True)
        if i == 1:
            table = extract_cols
        else:
            table = pandas.concat([table,extract_cols], axis = 1, join='inner')
        iternum = iternum + 1
        i = next_lim + jump-1
    table = pandas.concat([table,data.iloc[:,i:-1]], axis = 1)
    table = pandas.concat([table,pandas.DataFrame(data.iloc[:,-1])], axis = 1)
    i = n
print("Writing File")
table.to_csv("output_3.csv",quoting=csv.QUOTE_NONNUMERIC, encoding="utf-8", na_rep = numpy.nan, index = False)
print("End of Program")
