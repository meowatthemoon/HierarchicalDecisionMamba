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
    2756.95 / ANT_EXPERT,
	807.15 / ANT_MEDIUM,
    2735.59 / ANT_MEDIUM_EXPERT,	
    685.08 / ANT_MEDIUM_REPLAY
]
ax1.bar(index, ant1, bar_width,
        alpha=opacity,
        color = COLOR_1,
        label = "D 128, L 2, K 20",
        error_kw = error_config)

ant2 = [
    2749.8 / ANT_EXPERT,
    812.47 / ANT_MEDIUM,	
    2746.64 / ANT_MEDIUM_EXPERT,	
    687.93 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width, ant2, bar_width,
        alpha=opacity,
        color = COLOR_2,
        label = "D 128, L 4, K 20",
        error_kw = error_config)
ant3 = [
    2745.23 / ANT_EXPERT,
    797.16 / ANT_MEDIUM,
    2736.97 / ANT_MEDIUM_EXPERT,
    719.62 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*2, ant3, bar_width,
        alpha=opacity,
        color = COLOR_3,
        label = "D 128, L 6, K 10",
        error_kw = error_config)

ant4 = [
    2735.34 / ANT_EXPERT,
    782.97  / ANT_MEDIUM,
    2742.88 / ANT_MEDIUM_EXPERT,
    694.4   / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*3, ant4, bar_width,
        alpha=opacity,
        color = COLOR_4,
        label = "D 128, L 6, K 20",
        error_kw = error_config)

ant5 = [
    2744.13 / ANT_EXPERT,
    839.7 / ANT_MEDIUM,
    2743.46 / ANT_MEDIUM_EXPERT,
    709.62 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*4, ant5, bar_width,
        alpha=opacity,
        color = COLOR_5,
        label = "D 128, L 6, K 60",
        error_kw = error_config)

ant6 = [
    2733.4 / ANT_EXPERT,
    811.74 / ANT_MEDIUM,
    2730.42 / ANT_MEDIUM_EXPERT,
    697.59 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*5, ant6, bar_width,
        alpha=opacity,
        color = COLOR_6,
        label = "D 128, L 8, K 20",
        error_kw = error_config)

ant7 = [
    2747.27 / ANT_EXPERT, 
    831.47 / ANT_MEDIUM,
    2731.55 / ANT_MEDIUM_EXPERT,
    698.45 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*6, ant7, bar_width,
        alpha=opacity,
        color = COLOR_7,
        label = "D 128, L 12, K 20",
        error_kw = error_config)

ant8 = [
    2731.41 / ANT_EXPERT,
    842.39 / ANT_MEDIUM,
    2734.19 / ANT_MEDIUM_EXPERT,
    675.47 / ANT_MEDIUM_REPLAY
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
    0.0, 0.1, 1.0, 0.8
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
    0.0, 0.1, 0.9, 0.7
]
ax2.bar(index + bar_width * 2, antmaze3, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)

antmaze4 = [
    0.0, 0.1, 0.8, 0.9
]
ax2.bar(index + bar_width * 3, antmaze4, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
antmaze5 = [
    0.0, 0.0, 0.9, 0.8
]
ax2.bar(index + bar_width * 4, antmaze5, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)

antmaze6 = [
    0.0, 0.0, 1.0, 0.9
]
ax2.bar(index + bar_width * 5, antmaze6, bar_width,
        alpha=opacity,
        color = COLOR_6,

        error_kw = error_config)

antmaze7 = [
    0.0, 0.3, 1.0, 0.8
]
ax2.bar(index + bar_width * 6, antmaze7, bar_width,
        alpha=opacity,
        color = COLOR_7,

        error_kw = error_config)

antmaze8 = [
    0.0, 0.1, 0.9, 0.8
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
    1509.13 / HALFCHEETAH_EXPERT,
    661.97 / HALFCHEETAH_MEDIUM,
    1610.72 / HALFCHEETAH_MEDIUM_EXPERT,
    674.34 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah2 = [
    1548.93 / HALFCHEETAH_EXPERT,
    663.26 / HALFCHEETAH_MEDIUM,
    1646.08 / HALFCHEETAH_MEDIUM_EXPERT,
    800.93 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah3 = [
    1581.85 / HALFCHEETAH_EXPERT,
    660.67 / HALFCHEETAH_MEDIUM,
    1486.15 / HALFCHEETAH_MEDIUM_EXPERT,
    727.03 / HALFCHEETAH_MEDIUM_REPLAY   
]
halfcheetah4 = [
    1570.21 / HALFCHEETAH_EXPERT,
    676.78 / HALFCHEETAH_MEDIUM,
    1541.82 / HALFCHEETAH_MEDIUM_EXPERT,
    749.42 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah5 = [
    1551.76 / HALFCHEETAH_EXPERT,
    697.03 / HALFCHEETAH_MEDIUM,
    1554.33 / HALFCHEETAH_MEDIUM_EXPERT,
    833.8 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah6 = [
    1509.91 / HALFCHEETAH_EXPERT,
    679.33 / HALFCHEETAH_MEDIUM,
    1619.49 / HALFCHEETAH_MEDIUM_EXPERT,
    888.27 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah7= [
    1557.31 / HALFCHEETAH_EXPERT,
    662.29 / HALFCHEETAH_MEDIUM,
    1515.03 / HALFCHEETAH_MEDIUM_EXPERT,
    914.25 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah8 = [
    1555.83 / HALFCHEETAH_EXPERT,
    670.58 / HALFCHEETAH_MEDIUM,
    1629.78 / HALFCHEETAH_MEDIUM_EXPERT,
    920.06 / HALFCHEETAH_MEDIUM_REPLAY
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
    2241.37 / HOPPER_EXPERT,
    1243.59 / HOPPER_MEDIUM,
    2018.42 / HOPPER_MEDIUM_EXPERT,
    894.24 / HOPPER_MEDIUM_REPLAY
]
hopper2 = [
    2205.45 / HOPPER_EXPERT,
    1202.6 / HOPPER_MEDIUM,
    1747.32 / HOPPER_MEDIUM_EXPERT,
    1037.03 / HOPPER_MEDIUM_REPLAY
]
hopper3 = [
    2267.66 / HOPPER_EXPERT,
    1338.49 / HOPPER_MEDIUM,
    2033.3 / HOPPER_MEDIUM_EXPERT,
    919.44 / HOPPER_MEDIUM_REPLAY
]
hopper4 = [
    2183.71 / HOPPER_EXPERT,
    1299.97 / HOPPER_MEDIUM,
    1776.79 / HOPPER_MEDIUM_EXPERT,
    1065.73 / HOPPER_MEDIUM_REPLAY
]
hopper5 = [
    2240.01 / HOPPER_EXPERT,
    1536.28 / HOPPER_MEDIUM,
    2136.99 / HOPPER_MEDIUM_EXPERT,
    1158.22 / HOPPER_MEDIUM_REPLAY
]
hopper6 = [
    2200.76 / HOPPER_EXPERT,
    1288.08 / HOPPER_MEDIUM,
    1923.58 / HOPPER_MEDIUM_EXPERT,
    906.06 / HOPPER_MEDIUM_REPLAY
]
hopper7 = [
    2204.34 / HOPPER_EXPERT,
    1223.65 / HOPPER_MEDIUM,
    1931.64 / HOPPER_MEDIUM_EXPERT,
    1394.72 / HOPPER_MEDIUM_REPLAY
]
hopper8 = [
    2255.39 / HOPPER_EXPERT,
    1240.58 / HOPPER_MEDIUM,
    2232.73 / HOPPER_MEDIUM_EXPERT,
    1077.1 / HOPPER_MEDIUM_REPLAY
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
    2.8 / KITCHEN_COMPLETE,
    2.7 / KITCHEN_MIXED,
    2.3 / KITCHEN_PARTIAL
]
kitchen2 = [
    2.8 / KITCHEN_COMPLETE,
    2.4 / KITCHEN_MIXED,
    3.0 / KITCHEN_PARTIAL
]
kitchen3 = [
    2.7 / KITCHEN_COMPLETE,
    2.7 / KITCHEN_MIXED,
    2.9 / KITCHEN_PARTIAL
]
kitchen4 = [
    2.5 / KITCHEN_COMPLETE,
    2.7 / KITCHEN_MIXED,
    3.0 / KITCHEN_PARTIAL
]
kitchen5 = [
    2.8 / KITCHEN_COMPLETE,
    2.5 / KITCHEN_MIXED,
    3.0 / KITCHEN_PARTIAL
]
kitchen6 = [
    2.5 / KITCHEN_COMPLETE,
    2.7 / KITCHEN_MIXED,
    3.0 / KITCHEN_PARTIAL
]
kitchen7 = [
    2.8 / KITCHEN_COMPLETE,
    3.0 / KITCHEN_MIXED,
    3.0 / KITCHEN_PARTIAL
]
kitchen8 = [
    2.5 / KITCHEN_COMPLETE,
    2.6 / KITCHEN_MIXED,
    3.0 / KITCHEN_PARTIAL
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
    52.4 / MAZE2D_LARGE,
    62.5 / MAZE2D_MEDIUM,
    29.1 / MAZE2D_OPEN,
    85.3 / MAZE2D_UMAZE
]
maze2d2 = [
    63.1 / MAZE2D_LARGE,
    68.6 / MAZE2D_MEDIUM,
    30.5 / MAZE2D_OPEN,
    88.2 / MAZE2D_UMAZE
]
maze2d3 = [
    61.9 / MAZE2D_LARGE,
    102.3 / MAZE2D_MEDIUM,
    31.6 / MAZE2D_OPEN,
    81.6 / MAZE2D_UMAZE
]
maze2d4 = [
    69.9 / MAZE2D_LARGE,
    56.3 / MAZE2D_MEDIUM,
    30.2 / MAZE2D_OPEN,
    86.9 / MAZE2D_UMAZE
]
maze2d5 = [
    47.1 / MAZE2D_LARGE,
    69.2 / MAZE2D_MEDIUM,
    30.1 / MAZE2D_OPEN,
    65.9 / MAZE2D_UMAZE
]
maze2d6 = [
    60.1 / MAZE2D_LARGE,
    73.8 / MAZE2D_MEDIUM,
    27.9 / MAZE2D_OPEN,
    94.4 / MAZE2D_UMAZE
]
maze2d7 = [
    44.3 / MAZE2D_LARGE,
    70.9 / MAZE2D_MEDIUM,
    32.2 / MAZE2D_OPEN,
    90.9 / MAZE2D_UMAZE
]
maze2d8 = [
    55.4 / MAZE2D_LARGE,
    53.9 / MAZE2D_MEDIUM,
    29.7 / MAZE2D_OPEN,
    85.3 / MAZE2D_UMAZE
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
    1872.34 / WALKER2D_EXPERT,
    1045.51 / WALKER2D_MEDIUM,
    1870.97 / WALKER2D_MEDIUM_EXPERT,
    1299.36 / WALKER2D_MEDIUM_REPLAY
]
walker2d2 = [
    1872.95 / WALKER2D_EXPERT,
    1112.14 / WALKER2D_MEDIUM,
    1876.81 / WALKER2D_MEDIUM_EXPERT,
    1295.37 / WALKER2D_MEDIUM_REPLAY
]
walker2d3 = [
    1870.71 / WALKER2D_EXPERT,
    1047.51 / WALKER2D_MEDIUM,
    1860.44 / WALKER2D_MEDIUM_EXPERT,
    1288.29 / WALKER2D_MEDIUM_REPLAY
]
walker2d4 = [
    1866.81 / WALKER2D_EXPERT,
    1008.24 / WALKER2D_MEDIUM,
    1861.45 / WALKER2D_MEDIUM_EXPERT,
    1302.54 / WALKER2D_MEDIUM_REPLAY
]
walker2d5 = [
    1865.12 / WALKER2D_EXPERT,
    1092.8 / WALKER2D_MEDIUM,
    1870.77 / WALKER2D_MEDIUM_EXPERT,
    1307.33 / WALKER2D_MEDIUM_REPLAY
]
walker2d6 = [
    1857.13 / WALKER2D_EXPERT,
    1117.29 / WALKER2D_MEDIUM,
    1864.3 / WALKER2D_MEDIUM_EXPERT,
    1342.43 / WALKER2D_MEDIUM_REPLAY
]
walker2d7 = [
    1870.73 / WALKER2D_EXPERT,
    1059.91 / WALKER2D_MEDIUM,
    1867.66 / WALKER2D_MEDIUM_EXPERT,
    1276.02 / WALKER2D_MEDIUM_REPLAY
]
walker2d8 = [
    1872.84 / WALKER2D_EXPERT,
    1077.84 / WALKER2D_MEDIUM,
    1868.69 / WALKER2D_MEDIUM_EXPERT,
    1316.05 / WALKER2D_MEDIUM_REPLAY
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
plt.savefig('dm.pdf', dpi=100)