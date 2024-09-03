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
    2749.01 / ANT_EXPERT,
	821.61 / ANT_MEDIUM,
    2739.15 / ANT_MEDIUM_EXPERT,	
    457.96 / ANT_MEDIUM_REPLAY
]
ax1.bar(index, ant1, bar_width,
        alpha=opacity,
        color = COLOR_1,
        label = "D 128, L 2, K 20",
        error_kw = error_config)

ant2 = [
    2741.63 / ANT_EXPERT,
    805.34 / ANT_MEDIUM,	
    2730.58 / ANT_MEDIUM_EXPERT,	
    565.61 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width, ant2, bar_width,
        alpha=opacity,
        color = COLOR_2,
        label = "D 128, L 4, K 20",
        error_kw = error_config)
ant3 = [
    2742.33 / ANT_EXPERT,
    809.78 / ANT_MEDIUM,
    2733.02 / ANT_MEDIUM_EXPERT,
    571.83 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*2, ant3, bar_width,
        alpha=opacity,
        color = COLOR_3,
        label = "D 128, L 6, K 10",
        error_kw = error_config)

ant4 = [
    2746.57 / ANT_EXPERT,
    821.03 / ANT_MEDIUM,
    2738.41 / ANT_MEDIUM_EXPERT,
    716.85 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*3, ant4, bar_width,
        alpha=opacity,
        color = COLOR_4,
        label = "D 128, L 6, K 20",
        error_kw = error_config)

ant5 = [
    2731.74 / ANT_EXPERT,
    784.6 / ANT_MEDIUM,
    2731.91 / ANT_MEDIUM_EXPERT,
    580.59 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*4, ant5, bar_width,
        alpha=opacity,
        color = COLOR_5,
        label = "D 128, L 6, K 60",
        error_kw = error_config)

ant6 = [
    2746.65 / ANT_EXPERT,
    823.91 / ANT_MEDIUM,
    2738.26 / ANT_MEDIUM_EXPERT,
    487.99 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*5, ant6, bar_width,
        alpha=opacity,
        color = COLOR_6,
        label = "D 128, L 8, K 20",
        error_kw = error_config)

ant7 = [
    2736.43 / ANT_EXPERT, 
    782.97 / ANT_MEDIUM,
    2732.24 / ANT_MEDIUM_EXPERT,
    528.3 / ANT_MEDIUM_REPLAY
]
ax1.bar(index + bar_width*6, ant7, bar_width,
        alpha=opacity,
        color = COLOR_7,
        label = "D 128, L 12, K 20",
        error_kw = error_config)

ant8 = [
    2731.02 / ANT_EXPERT,
    803.85 / ANT_MEDIUM,
    2729.32 / ANT_MEDIUM_EXPERT,
    559.54 / ANT_MEDIUM_REPLAY
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
    0.0,	0.1,	1.0,	0.9
]
ax2.bar(index, antmaze1, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)

antmaze2 = [
    0.0,	0.1,	0.8,	0.9
]
ax2.bar(index + bar_width, antmaze2, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)

antmaze3 = [
    0.0,	0.1,	1.0,	0.8
]
ax2.bar(index + bar_width * 2, antmaze3, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)

antmaze4 = [
    0.08,	
    0.2,	
    0.95,	
    0.92
]
ax2.bar(index + bar_width * 3, antmaze4, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
antmaze5 = [
    0.0,	0.1,	0.9,	0.9
]
ax2.bar(index + bar_width * 4, antmaze5, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)

antmaze6 = [
    0.0,	0.0,	0.9,	1.0
]
ax2.bar(index + bar_width * 5, antmaze6, bar_width,
        alpha=opacity,
        color = COLOR_6,

        error_kw = error_config)

antmaze7 = [
    0.0,	0.0,	0.9,	0.9
]
ax2.bar(index + bar_width * 6, antmaze7, bar_width,
        alpha=opacity,
        color = COLOR_7,

        error_kw = error_config)

antmaze8 = [
    0.0,	0.1,	1.0,	0.8
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
    1572.04 / HALFCHEETAH_EXPERT,
    663.6 / HALFCHEETAH_MEDIUM,
    1572.6 / HALFCHEETAH_MEDIUM_EXPERT,
    828.94 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah2 = [
    1574.81 / HALFCHEETAH_EXPERT,
    671.36 / HALFCHEETAH_MEDIUM,
    1484.11 / HALFCHEETAH_MEDIUM_EXPERT,
    614.42 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah3 = [
    1534.42 / HALFCHEETAH_EXPERT,
    690.87 / HALFCHEETAH_MEDIUM,
    1540.92 / HALFCHEETAH_MEDIUM_EXPERT,
    591.58 / HALFCHEETAH_MEDIUM_REPLAY   
]
halfcheetah4 = [
    1585.85 / HALFCHEETAH_EXPERT,
    677.84 / HALFCHEETAH_MEDIUM,
    1636.29 / HALFCHEETAH_MEDIUM_EXPERT,
    862.53 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah5 = [
    1600.49 / HALFCHEETAH_EXPERT,
    657.52 / HALFCHEETAH_MEDIUM,
    1632.05 / HALFCHEETAH_MEDIUM_EXPERT,
    674.64 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah6 = [
    1475.39 / HALFCHEETAH_EXPERT,
    671.27 / HALFCHEETAH_MEDIUM,
    1570.63 / HALFCHEETAH_MEDIUM_EXPERT,
    679.43 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah7= [
    1608.68 / HALFCHEETAH_EXPERT,
    685.1 / HALFCHEETAH_MEDIUM,
    1604.31 / HALFCHEETAH_MEDIUM_EXPERT,
    741.91 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah8 = [
    1534.89 / HALFCHEETAH_EXPERT,
    666.45 / HALFCHEETAH_MEDIUM,
    1585.99 / HALFCHEETAH_MEDIUM_EXPERT,
    606.74 / HALFCHEETAH_MEDIUM_REPLAY
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
    2088.65 / HOPPER_EXPERT,
    1350.42 / HOPPER_MEDIUM,
    2231.04 / HOPPER_MEDIUM_EXPERT,
    713.82 / HOPPER_MEDIUM_REPLAY
]
hopper2 = [
    2038.83 / HOPPER_EXPERT,
    1178.47 / HOPPER_MEDIUM,
    1582.2 / HOPPER_MEDIUM_EXPERT,
    832.88 / HOPPER_MEDIUM_REPLAY
]
hopper3 = [
    1857.71 / HOPPER_EXPERT,
    1268.18 / HOPPER_MEDIUM,
    1943.28 / HOPPER_MEDIUM_EXPERT,
    823.6 / HOPPER_MEDIUM_REPLAY
]
hopper4 = [
    2260.68 / HOPPER_EXPERT,
    1383.51 / HOPPER_MEDIUM,
    2026.48 / HOPPER_MEDIUM_EXPERT,
    1199.42 / HOPPER_MEDIUM_REPLAY
]
hopper5 = [
    2046.79 / HOPPER_EXPERT,
    1222.32 / HOPPER_MEDIUM,
    1622.79 / HOPPER_MEDIUM_EXPERT,
    539.89 / HOPPER_MEDIUM_REPLAY
]
hopper6 = [
    2268.42 / HOPPER_EXPERT,
    1209.38 / HOPPER_MEDIUM,
    1631.85 / HOPPER_MEDIUM_EXPERT,
    732.74 / HOPPER_MEDIUM_REPLAY
]
hopper7 = [
    2071.23 / HOPPER_EXPERT,
    1246.16 / HOPPER_MEDIUM,
    1723.25 / HOPPER_MEDIUM_EXPERT,
    817.02 / HOPPER_MEDIUM_REPLAY
]
hopper8 = [
    1896.61 / HOPPER_EXPERT,
    1300.73 / HOPPER_MEDIUM,
    1806.63 / HOPPER_MEDIUM_EXPERT,
    671.77 / HOPPER_MEDIUM_REPLAY
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
    3.2 / KITCHEN_COMPLETE,
    2.2 / KITCHEN_MIXED,
    2.3 / KITCHEN_PARTIAL
]
kitchen2 = [
    2.9 / KITCHEN_COMPLETE,
    2.8 / KITCHEN_MIXED,
    2.5 / KITCHEN_PARTIAL
]
kitchen3 = [
    2.7 / KITCHEN_COMPLETE,
    3.0 / KITCHEN_MIXED,
    2.7 / KITCHEN_PARTIAL
]
kitchen4 = [
    2.58 / KITCHEN_COMPLETE,
    2.80 / KITCHEN_MIXED,
    3.02 / KITCHEN_PARTIAL
]
kitchen5 = [
    2.6 / KITCHEN_COMPLETE,
    2.6 / KITCHEN_MIXED,
    2.5 / KITCHEN_PARTIAL
]
kitchen6 = [
    2.6 / KITCHEN_COMPLETE,
    2.4 / KITCHEN_MIXED,
    2.7 / KITCHEN_PARTIAL
]
kitchen7 = [
    2.8 / KITCHEN_COMPLETE,
    2.8 / KITCHEN_MIXED,
    2.2 / KITCHEN_PARTIAL
]
kitchen8 = [
    2.5 / KITCHEN_COMPLETE,
    2.4 / KITCHEN_MIXED,
    2.8 / KITCHEN_PARTIAL
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
    43.9 / MAZE2D_LARGE,
    57.1 / MAZE2D_MEDIUM,
    13.1 / MAZE2D_OPEN,
    47.0 / MAZE2D_UMAZE
]
maze2d2 = [
    51.9 / MAZE2D_LARGE,
    57.4 / MAZE2D_MEDIUM,
    16.0 / MAZE2D_OPEN,
    49.3 / MAZE2D_UMAZE
]
maze2d3 = [
    47.2 / MAZE2D_LARGE,
    64.7 / MAZE2D_MEDIUM,
    19.5 / MAZE2D_OPEN,
    46.2 / MAZE2D_UMAZE
]
maze2d4 = [
    79.65 / MAZE2D_LARGE,
    114.1 / MAZE2D_MEDIUM,
    32.33 / MAZE2D_OPEN,
    110.25 / MAZE2D_UMAZE
]
maze2d5 = [
    50.0 / MAZE2D_LARGE,
    53.4 / MAZE2D_MEDIUM,
    14.0 / MAZE2D_OPEN,
    44.0 / MAZE2D_UMAZE
]
maze2d6 = [
    52.8 / MAZE2D_LARGE,
    54.9 / MAZE2D_MEDIUM,
    19.2 / MAZE2D_OPEN,
    42.5 / MAZE2D_UMAZE
]
maze2d7 = [
    39.6 / MAZE2D_LARGE,
    43.8 / MAZE2D_MEDIUM,
    21.1 / MAZE2D_OPEN,
    43.2 / MAZE2D_UMAZE
]
maze2d8 = [
    32.2 / MAZE2D_LARGE,
    52.3 / MAZE2D_MEDIUM,
    21.0 / MAZE2D_OPEN,
    50.0 / MAZE2D_UMAZE
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
    1869.48 / WALKER2D_EXPERT,
    1048.22 / WALKER2D_MEDIUM,
    1026.26 / WALKER2D_MEDIUM_EXPERT,
    522.2 / WALKER2D_MEDIUM_REPLAY
]
walker2d2 = [
    1873.27 / WALKER2D_EXPERT,
    1002.43 / WALKER2D_MEDIUM,
    1548.88 / WALKER2D_MEDIUM_EXPERT,
    539.83 / WALKER2D_MEDIUM_REPLAY
]
walker2d3 = [
    1881.49 / WALKER2D_EXPERT,
    933.3 / WALKER2D_MEDIUM,
    1169.1 / WALKER2D_MEDIUM_EXPERT,
    532.55 / WALKER2D_MEDIUM_REPLAY
]
walker2d4 = [
    1874.51 / WALKER2D_EXPERT,
    1111.94 / WALKER2D_MEDIUM,
    1871.34 / WALKER2D_MEDIUM_EXPERT,
    1310.88 / WALKER2D_MEDIUM_REPLAY
]
walker2d5 = [
    1874.27 / WALKER2D_EXPERT,
    991.03 / WALKER2D_MEDIUM,
    1074.44 / WALKER2D_MEDIUM_EXPERT,
    764.4 / WALKER2D_MEDIUM_REPLAY
]
walker2d6 = [
    1879.29 / WALKER2D_EXPERT,
    922.94 / WALKER2D_MEDIUM,
    1092.8 / WALKER2D_MEDIUM_EXPERT,
    855.37 / WALKER2D_MEDIUM_REPLAY
]
walker2d7 = [
    1872.52 / WALKER2D_EXPERT,
    953.36 / WALKER2D_MEDIUM,
    936.52 / WALKER2D_MEDIUM_EXPERT,
    681.88 / WALKER2D_MEDIUM_REPLAY
]
walker2d8 = [
    1876.93 / WALKER2D_EXPERT,
    889.9 / WALKER2D_MEDIUM,
    1114.75 / WALKER2D_MEDIUM_EXPERT,
    974.29 / WALKER2D_MEDIUM_REPLAY
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
plt.savefig('dm_nor.pdf', dpi=100)