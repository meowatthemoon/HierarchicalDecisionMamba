import numpy as np
import matplotlib.pyplot as plt
from consts import ANT_EXPERT, ANT_MEDIUM, ANT_MEDIUM_EXPERT, ANT_MEDIUM_REPLAY, COLOR_1, COLOR_2, COLOR_3, COLOR_4, COLOR_5, COLOR_6, COLOR_7, COLOR_8, HALFCHEETAH_EXPERT, HALFCHEETAH_MEDIUM, HALFCHEETAH_MEDIUM_EXPERT, HALFCHEETAH_MEDIUM_REPLAY, HOPPER_EXPERT, HOPPER_MEDIUM, HOPPER_MEDIUM_EXPERT, HOPPER_MEDIUM_REPLAY, KITCHEN_COMPLETE, KITCHEN_MIXED, KITCHEN_PARTIAL, MAZE2D_LARGE, MAZE2D_MEDIUM, MAZE2D_OPEN, MAZE2D_UMAZE, VERTICAL_SCALE, WALKER2D_EXPERT, WALKER2D_MEDIUM, WALKER2D_MEDIUM_EXPERT, WALKER2D_MEDIUM_REPLAY

#"""
FONT_SIZE = 7
_4_RANGES = d_ranges = (0.2, 1.2, 2.2, 3.2)
_3_RANGES = d_ranges = (0.2, 1.2, 2.2)
bar_width = 0.1

opacity = 1.0
error_config = {'ecolor': '0.3'}
index = np.arange(4)
#"""

# Create Subplots 
f, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(1, 7, sharex='col', sharey='row')

# Ant
ant1 = [
    2734.05 / ANT_EXPERT,
	779.14 / ANT_MEDIUM,
    2749.79 / ANT_MEDIUM_EXPERT,	
    562.05 / ANT_MEDIUM_REPLAY
]
ax1.bar(index, ant1, bar_width,
        alpha=opacity,
        color = COLOR_1,
        label = "D 128, L 2, K 20",
        error_kw = error_config)

ant2 = [
    2766.99 / ANT_EXPERT,
    787.82 / ANT_MEDIUM,	
    2723.2 / ANT_MEDIUM_EXPERT,	
    654.53 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width, ant2, bar_width,
        alpha=opacity,
        color = COLOR_2,
        label = "D 128, L 4, K 20",
        error_kw = error_config)
ant3 = [
    2732.41 / ANT_EXPERT,
    794.78 / ANT_MEDIUM,
    2710.65 / ANT_MEDIUM_EXPERT,
    657.81 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*2, ant3, bar_width,
        alpha=opacity,
        color = COLOR_3,
        label = "D 128, L 6, K 10",
        error_kw = error_config)

ant4 = [
    2749.20 / ANT_EXPERT,
    820.39 / ANT_MEDIUM,
    2730.01 / ANT_MEDIUM_EXPERT,
    728.20 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*3, ant4, bar_width,
        alpha=opacity,
        color = COLOR_4,
        label = "D 128, L 6, K 20",
        error_kw = error_config)

ant5 = [
    2741.6 / ANT_EXPERT,
    820.37 / ANT_MEDIUM,
    2737.77 / ANT_MEDIUM_EXPERT,
    659.95 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*4, ant5, bar_width,
        alpha=opacity,
        color = COLOR_5,
        label = "D 128, L 6, K 60",
        error_kw = error_config)

ant6 = [
    2753.42 / ANT_EXPERT,
    795.78 / ANT_MEDIUM,
    2748.58 / ANT_MEDIUM_EXPERT,
    642.59 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*5, ant6, bar_width,
        alpha=opacity,
        color = COLOR_6,
        label = "D 128, L 8, K 20",
        error_kw = error_config)

ant7 = [
    2737.5 / ANT_EXPERT, 
    859.57 / ANT_MEDIUM,
    2727.86 / ANT_MEDIUM_EXPERT,
    729.8 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*6, ant7, bar_width,
        alpha=opacity,
        color = COLOR_7,
        label = "D 128, L 12, K 20",
        error_kw = error_config)

ant8 = [
    2738.74 / ANT_EXPERT,
    809.23 / ANT_MEDIUM,
    2731.72 / ANT_MEDIUM_EXPERT,
    798.73 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*7, ant8, bar_width,
        alpha=opacity,
        color = COLOR_8,
        label = "D 256, L 6, K 20",
        error_kw = error_config)
ax1.set_title('Ant')
d_names = ("Exp", "Med", "MedE", "MedR")
ax1.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

# Antmaze
antmaze1 = [
    0.0, 0.1, 1.0, 1.0
]
ax2.bar(index, antmaze1, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)

antmaze2 = [
    0.0, 0.1, 1.0, 0.9
]
ax2.bar(index + bar_width, antmaze2, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)

antmaze3 = [
    0.0,	0.0,	1.0,	0.8
]
ax2.bar(index + bar_width * 2, antmaze3, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)

antmaze4 = [
    0.05,	
    0.15,	
    1.00,	
    1.00
]
ax2.bar(index + bar_width * 3, antmaze4, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
antmaze5 = [
    0.0,	0.1,	1.0,	0.9
]
ax2.bar(index + bar_width * 4, antmaze5, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)

antmaze6 = [
    0.0,	0.2,	1.0,	1.0
]
ax2.bar(index + bar_width * 5, antmaze6, bar_width,
        alpha=opacity,
        color = COLOR_6,

        error_kw = error_config)

antmaze7 = [
    0.0,	0.2,	1.0,	1.0
]
ax2.bar(index + bar_width * 6, antmaze7, bar_width,
        alpha=opacity,
        color = COLOR_7,

        error_kw = error_config)

antmaze8 = [
    0.0,	0.1,	1.0,	0.9
]
ax2.bar(index + bar_width * 7, antmaze8, bar_width,
        alpha=opacity,
        color = COLOR_8,

        error_kw = error_config)
ax2.set_title('AntMaze')
d_names = ("LarD", "MedD", "Uma", "UmaD")
ax2.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

# HalfCheetah
halfcheetah1 = [
    1495.26 / HALFCHEETAH_EXPERT,
    678.49 / HALFCHEETAH_MEDIUM,
    1642.1 / HALFCHEETAH_MEDIUM_EXPERT,
    856.05 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah2 = [
    1528.72 / HALFCHEETAH_EXPERT,
    669.73 / HALFCHEETAH_MEDIUM,
    1603.04 / HALFCHEETAH_MEDIUM_EXPERT,
    658.37 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah3 = [
    1541.64 / HALFCHEETAH_EXPERT,
    680.66 / HALFCHEETAH_MEDIUM,
    1518.22 / HALFCHEETAH_MEDIUM_EXPERT,
    870.54 / HALFCHEETAH_MEDIUM_REPLAY   
]
halfcheetah4 = [
    1538.32 / HALFCHEETAH_EXPERT,
    679.03 / HALFCHEETAH_MEDIUM,
    1541.19 / HALFCHEETAH_MEDIUM_EXPERT,
    826.06 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah5 = [
    1518.61 / HALFCHEETAH_EXPERT,
    664.82 / HALFCHEETAH_MEDIUM,
    1661.38 / HALFCHEETAH_MEDIUM_EXPERT,
    980.08 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah6 = [
   1546.8 / HALFCHEETAH_EXPERT,
   677.35 / HALFCHEETAH_MEDIUM,
   1510.47 / HALFCHEETAH_MEDIUM_EXPERT,
   846.87 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah7= [
    1569.35 / HALFCHEETAH_EXPERT,
    703.42 / HALFCHEETAH_MEDIUM,
    1520.07 / HALFCHEETAH_MEDIUM_EXPERT,
    934.92 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah8 = [
    1479.55 / HALFCHEETAH_EXPERT,
    664.9 / HALFCHEETAH_MEDIUM,
    1468.85 / HALFCHEETAH_MEDIUM_EXPERT,
    949.47 / HALFCHEETAH_MEDIUM_REPLAY
]
ax3.bar(index, halfcheetah1, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax3.bar(index + bar_width, halfcheetah2, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax3.bar(index + bar_width * 2, halfcheetah3, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax3.bar(index + bar_width * 3, halfcheetah4, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax3.bar(index + bar_width * 4, halfcheetah5, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax3.bar(index + bar_width * 5, halfcheetah6, bar_width,
        alpha=opacity,
        color = COLOR_6,

        error_kw = error_config)
ax3.bar(index + bar_width * 6, halfcheetah7, bar_width,
        alpha=opacity,
        color = COLOR_7,

        error_kw = error_config)
ax3.bar(index + bar_width * 7, halfcheetah8, bar_width,
        alpha=opacity,
        color = COLOR_8,

        error_kw = error_config)
ax3.set_title('HalfCheetah')
d_names = ("Exp", "Med", "MedE", "MedR")
ax3.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

# Hopper
hopper1 = [
    1891.6 / HOPPER_EXPERT,
    1397.88 / HOPPER_MEDIUM,
    1931.43 / HOPPER_MEDIUM_EXPERT,
    832.4 / HOPPER_MEDIUM_REPLAY
]
hopper2 = [
    2036.24 / HOPPER_EXPERT,
    1035.4/ HOPPER_MEDIUM,
    1729.33 / HOPPER_MEDIUM_EXPERT,
    481.89 / HOPPER_MEDIUM_REPLAY
]
hopper3 = [
    2208.83 / HOPPER_EXPERT,
    1239.04/ HOPPER_MEDIUM,
    1835.6 / HOPPER_MEDIUM_EXPERT,
    849.31 / HOPPER_MEDIUM_REPLAY
]
hopper4 = [
    2230.41 / HOPPER_EXPERT,
    1231.19 / HOPPER_MEDIUM,
    1948.04 / HOPPER_MEDIUM_EXPERT,
    770.51 / HOPPER_MEDIUM_REPLAY
]
hopper5 = [
    2197.29 / HOPPER_EXPERT,
    1159.22/ HOPPER_MEDIUM,
    1460.91 / HOPPER_MEDIUM_EXPERT,
    760.1 / HOPPER_MEDIUM_REPLAY
]
hopper6 = [
    2075.5/ HOPPER_EXPERT,
    1179.31/ HOPPER_MEDIUM,
    1066.12 / HOPPER_MEDIUM_EXPERT,
    923.87 / HOPPER_MEDIUM_REPLAY
]
hopper7 = [
    2275.3/ HOPPER_EXPERT,
    1130.55/ HOPPER_MEDIUM,
    1787.79 / HOPPER_MEDIUM_EXPERT,
    917.29 / HOPPER_MEDIUM_REPLAY
]
hopper8 = [
    2151.83/ HOPPER_EXPERT,
    1112.95/ HOPPER_MEDIUM,
    1750.9 / HOPPER_MEDIUM_EXPERT,
    583.49 / HOPPER_MEDIUM_REPLAY
]

ax4.bar(index, hopper1, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax4.bar(index + bar_width, hopper2, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax4.bar(index + bar_width * 2, hopper3, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax4.bar(index + bar_width * 3, hopper4, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax4.bar(index + bar_width * 4, hopper5, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax4.bar(index + bar_width * 5, hopper6, bar_width,
        alpha=opacity,
        color = COLOR_6,

        error_kw = error_config)
ax4.bar(index + bar_width * 6, hopper7, bar_width,
        alpha=opacity,
        color = COLOR_7,

        error_kw = error_config)
ax4.bar(index + bar_width * 7, hopper8, bar_width,
        alpha=opacity,
        color = COLOR_8,

        error_kw = error_config)
ax4.set_title('Hopper')
d_names = ("Exp", "Med", "MedE", "MedR")
ax4.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)


kitchen1 = [
    1.0 / KITCHEN_COMPLETE,
    2.5 / KITCHEN_MIXED,
    1.4 / KITCHEN_PARTIAL
]
kitchen2 = [
    1.2 / KITCHEN_COMPLETE,
    2.3 / KITCHEN_MIXED,
    1.4 / KITCHEN_PARTIAL
]
kitchen3 = [
    1.6 / KITCHEN_COMPLETE,
    2.7 / KITCHEN_MIXED,
    2.0 / KITCHEN_PARTIAL
]
kitchen4 = [
    2.20 / KITCHEN_COMPLETE,
    2.65 / KITCHEN_MIXED,
    2.55 / KITCHEN_PARTIAL
]
kitchen5 = [
    1.3 / KITCHEN_COMPLETE,
    2.7 / KITCHEN_MIXED,
    3.0 / KITCHEN_PARTIAL
]
kitchen6 = [
    1.8 / KITCHEN_COMPLETE,
    1.9 / KITCHEN_MIXED,
    3.1 / KITCHEN_PARTIAL
]
kitchen7 = [
    1.9 / KITCHEN_COMPLETE,
    2.7 / KITCHEN_MIXED,
    1.9 / KITCHEN_PARTIAL
]
kitchen8 = [
    2.4 / KITCHEN_COMPLETE,
    2.4 / KITCHEN_MIXED,
    2.1 / KITCHEN_PARTIAL
]
ax5.bar(np.arange(3), kitchen1, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width, kitchen2, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 2, kitchen3, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 3, kitchen4, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 4, kitchen5, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 5, kitchen6, bar_width,
        alpha=opacity,
        color = COLOR_6,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 6, kitchen7, bar_width,
        alpha=opacity,
        color = COLOR_7,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 7, kitchen8, bar_width,
        alpha=opacity,
        color = COLOR_8,

        error_kw = error_config)
ax5.set_title('Kitchen')
d_names = ("Complete", "Mixed", "Partial")
ax5.set_xticks(_3_RANGES, d_names, color='black', fontsize = FONT_SIZE)

maze2d1 = [
    31.0 / MAZE2D_LARGE,
    141.1 / MAZE2D_MEDIUM,
    23.8 / MAZE2D_OPEN,
    27.3 / MAZE2D_UMAZE
]
maze2d2 = [
    214.6 / MAZE2D_LARGE,
    174.1 / MAZE2D_MEDIUM,
    15.2 / MAZE2D_OPEN,
    21.2 / MAZE2D_UMAZE
]
maze2d3 = [
    79.1 / MAZE2D_LARGE,
    92.3 / MAZE2D_MEDIUM,
    26.9 / MAZE2D_OPEN,
    28.3 / MAZE2D_UMAZE
]
maze2d4 = [
    93.7 / MAZE2D_LARGE,
    145.23 / MAZE2D_MEDIUM,
    26.67 / MAZE2D_OPEN,
    31.13 / MAZE2D_UMAZE
]
maze2d5 = [
    65.9 / MAZE2D_LARGE,
    107.8 / MAZE2D_MEDIUM,
    15.8 / MAZE2D_OPEN,
    26.2 / MAZE2D_UMAZE
]
maze2d6 = [
    89.6 / MAZE2D_LARGE,
    176.6 / MAZE2D_MEDIUM,
    26.6 / MAZE2D_OPEN,
    18.4 / MAZE2D_UMAZE
]
maze2d7 = [
    31.2 / MAZE2D_LARGE,
    178.3 / MAZE2D_MEDIUM,
    17.7 / MAZE2D_OPEN,
    28.7 / MAZE2D_UMAZE
]
maze2d8 = [
    35.8 / MAZE2D_LARGE,
    83.7 / MAZE2D_MEDIUM,
    19.6 / MAZE2D_OPEN,
    23.8 / MAZE2D_UMAZE
]
ax6.bar(index, maze2d1, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax6.bar(index + bar_width, maze2d2, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax6.bar(index + bar_width * 2, maze2d3, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax6.bar(index + bar_width * 3, maze2d4, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax6.bar(index + bar_width * 4, maze2d5, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax6.bar(index + bar_width * 5, maze2d6, bar_width,
        alpha=opacity,
        color = COLOR_6,

        error_kw = error_config)
ax6.bar(index + bar_width * 6, maze2d7, bar_width,
        alpha=opacity,
        color = COLOR_7,

        error_kw = error_config)
ax6.bar(index + bar_width * 7, maze2d8, bar_width,
        alpha=opacity,
        color = COLOR_8,

        error_kw = error_config)
ax6.set_title('Maze2D')
d_names = ("Lar", "Med", "Open", "Umaze")
ax6.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

walker2d1 = [
    1869.22 / WALKER2D_EXPERT,
    1091.66 / WALKER2D_MEDIUM,
    1009.39 / WALKER2D_MEDIUM_EXPERT,
    1238.13 / WALKER2D_MEDIUM_REPLAY
]
walker2d2 = [
    1850.59 / WALKER2D_EXPERT,
    1013.1 / WALKER2D_MEDIUM,
    1855.15 / WALKER2D_MEDIUM_EXPERT,
    1110.72 / WALKER2D_MEDIUM_REPLAY
]
walker2d3 = [
    1838.57 / WALKER2D_EXPERT,
    1001.38 / WALKER2D_MEDIUM,
    1852.7 / WALKER2D_MEDIUM_EXPERT,
    839.52 / WALKER2D_MEDIUM_REPLAY
]
walker2d4 = [
    1861.86 / WALKER2D_EXPERT,
    1093.42 / WALKER2D_MEDIUM,
    1843.48 / WALKER2D_MEDIUM_EXPERT,
    1237.97 / WALKER2D_MEDIUM_REPLAY
]
walker2d5 = [
    1839.9 / WALKER2D_EXPERT,
    1094.66 / WALKER2D_MEDIUM,
    1824.48 / WALKER2D_MEDIUM_EXPERT,
    1244.26 / WALKER2D_MEDIUM_REPLAY
]
walker2d6 = [
    1857.78 / WALKER2D_EXPERT,
    1063.11 / WALKER2D_MEDIUM,
    1825.67 / WALKER2D_MEDIUM_EXPERT,
    746.14 / WALKER2D_MEDIUM_REPLAY
]
walker2d7 = [
    1854.8 / WALKER2D_EXPERT,
    1105.56 / WALKER2D_MEDIUM,
    1845.77 / WALKER2D_MEDIUM_EXPERT,
    986.72 / WALKER2D_MEDIUM_REPLAY
]
walker2d8 = [
    1867.66 / WALKER2D_EXPERT,
    1155.29 / WALKER2D_MEDIUM,
    1812.31 / WALKER2D_MEDIUM_EXPERT,
    1002.05 / WALKER2D_MEDIUM_REPLAY
]
ax7.bar(index, walker2d1, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax7.bar(index + bar_width, walker2d2, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax7.bar(index + bar_width * 2, walker2d3, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax7.bar(index + bar_width * 3, walker2d4, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax7.bar(index + bar_width * 4, walker2d5, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax7.bar(index + bar_width * 5, walker2d6, bar_width,
        alpha=opacity,
        color = COLOR_6,

        error_kw = error_config)
ax7.bar(index + bar_width * 6, walker2d7, bar_width,
        alpha=opacity,
        color = COLOR_7,

        error_kw = error_config)
ax7.bar(index + bar_width * 7, walker2d8, bar_width,
        alpha=opacity,
        color = COLOR_8,

        error_kw = error_config)
ax7.set_title('Walker2D')
d_names = ("Exp", "Med", "MedE", "MedR")
ax7.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

handles, labels = ax1.get_legend_handles_labels()
plt.legend(handles, labels, loc=(1.1, 0))

# Show
figure = plt.gcf()
figure.set_size_inches(1920/100, 1080/100 * VERTICAL_SCALE)
plt.savefig('hdm.pdf', dpi=100)