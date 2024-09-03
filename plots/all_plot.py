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
ant_dt = [
    2731.52 / ANT_EXPERT,
	801.41 / ANT_MEDIUM,
    2738.68 / ANT_MEDIUM_EXPERT,	
    732.89 / ANT_MEDIUM_REPLAY
]
ant_hdt = [
    2731.83 / ANT_EXPERT,
    787.23 / ANT_MEDIUM,	
    2171.27 / ANT_MEDIUM_EXPERT,	
    712.61 / ANT_MEDIUM_REPLAY
]
ante_dmnor = [
    2746.57  / ANT_EXPERT,
    821.03  / ANT_MEDIUM,
    2738.41  / ANT_MEDIUM_EXPERT,
    716.85  / ANT_MEDIUM_REPLAY
]
ant_dm = [
    2735.34  / ANT_EXPERT,
    782.97  / ANT_MEDIUM,
    2742.88  / ANT_MEDIUM_EXPERT,
    694.40  / ANT_MEDIUM_REPLAY
]
ant_hdm = [
    2749.20  / ANT_EXPERT,
    820.39  / ANT_MEDIUM,
    2730.01  / ANT_MEDIUM_EXPERT,
    728.20  / ANT_MEDIUM_REPLAY
]
ax1.bar(index, ant_dt, bar_width,
        alpha=opacity,
        color = COLOR_1,
        label = "DT",
        error_kw = error_config)
ax1.bar(index + bar_width, ant_hdt, bar_width,
        alpha=opacity,
        color = COLOR_2,
        label = "HDT",
        error_kw = error_config)
ax1.bar(index + bar_width*2, ante_dmnor, bar_width,
        alpha=opacity,
        color = COLOR_3,
        label = "DM",
        error_kw = error_config)
ax1.bar(index + bar_width*3, ant_dm, bar_width,
        alpha=opacity,
        color = COLOR_4,
        label = "DM+R",
        error_kw = error_config)
ax1.bar(index + bar_width*4, ant_hdm, bar_width,
        alpha=opacity,
        color = COLOR_5,
        label = "HDM",
        error_kw = error_config)
ax1.set_title('Ant')
d_names = ("Exp", "Med", "MedE", "MedR")
ax1.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

# Antmaze
antmaze_dt = [
    0.05, 
    0.18, 
    0.98, 
    0.95
]
antmaze_hdt = [
    0.02,	
    0.12,	
    0.52,	
    0.50
]
antmaze_dmnor = [
    0.08,	
    0.2,	
    0.95,	
    0.92
]
antmaze_dm = [
    0.0,	
    0.1,	
    0.8,	
    0.9
]
antmaze_hdm = [
    0.05,	
    0.15,	
    1.0,	
    1.0
]
ax2.bar(index, antmaze_dt, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax2.bar(index + bar_width, antmaze_hdt, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax2.bar(index + bar_width * 2, antmaze_dmnor, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax2.bar(index + bar_width * 3, antmaze_dm, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax2.bar(index + bar_width * 4, antmaze_hdm, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax2.set_title('AntMaze')
d_names = ("LarD", "MedD", "Uma", "UmaD")
ax2.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

# HalfCheetah
halfcheetah_dt = [
    1530.86 / HALFCHEETAH_EXPERT,
    658.54 / HALFCHEETAH_MEDIUM,
    1572.42 / HALFCHEETAH_MEDIUM_EXPERT,
    1074.72 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah_hdt = [
    1479.88 / HALFCHEETAH_EXPERT,
    669.73 / HALFCHEETAH_MEDIUM,
    1103.51 / HALFCHEETAH_MEDIUM_EXPERT,
    946.68 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah_dmnor = [
    1585.85 / HALFCHEETAH_EXPERT,
    677.84 / HALFCHEETAH_MEDIUM,
    1636.29 / HALFCHEETAH_MEDIUM_EXPERT,
    862.53 / HALFCHEETAH_MEDIUM_REPLAY   
]
halfcheetah_dm = [
    1570.21 / HALFCHEETAH_EXPERT,
    676.78 / HALFCHEETAH_MEDIUM,
    1541.82 / HALFCHEETAH_MEDIUM_EXPERT,
    749.42 / HALFCHEETAH_MEDIUM_REPLAY
]
halfcheetah_hdm = [
    1538.32 / HALFCHEETAH_EXPERT,
    679.03 / HALFCHEETAH_MEDIUM,
    1541.19 / HALFCHEETAH_MEDIUM_EXPERT,
    826.06 / HALFCHEETAH_MEDIUM_REPLAY
]

ax3.bar(index, halfcheetah_dt, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax3.bar(index + bar_width, halfcheetah_hdt, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax3.bar(index + bar_width * 2, halfcheetah_dmnor, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax3.bar(index + bar_width * 3, halfcheetah_dm, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax3.bar(index + bar_width * 4, halfcheetah_hdm, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax3.set_title('HalfCheetah')
d_names = ("Exp", "Med", "MedE", "MedR")
ax3.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

# Hopper
hopper_dt = [
    2234.25 / HOPPER_EXPERT,
    1241.60 / HOPPER_MEDIUM,
    2270.67 / HOPPER_MEDIUM_EXPERT,
    564.70 / HOPPER_MEDIUM_REPLAY
]
hopper_hdt = [
    2072.71 / HOPPER_EXPERT,
    1175.30 / HOPPER_MEDIUM,
    1549.40 / HOPPER_MEDIUM_EXPERT,
    378.57 / HOPPER_MEDIUM_REPLAY
]
hopper_dmnor = [
    2260.68 / HOPPER_EXPERT,
    1383.51 / HOPPER_MEDIUM,
    2026.48 / HOPPER_MEDIUM_EXPERT,
    1199.42 / HOPPER_MEDIUM_REPLAY
]
hopper_dm = [
    2183.71 / HOPPER_EXPERT,
    1299.97 / HOPPER_MEDIUM,
    1776.79 / HOPPER_MEDIUM_EXPERT,
    1065.73 / HOPPER_MEDIUM_REPLAY
]
hopper_hdm = [
    2230.41 / HOPPER_EXPERT,
    1231.19 / HOPPER_MEDIUM,
    1948.04 / HOPPER_MEDIUM_EXPERT,
    770.51 / HOPPER_MEDIUM_REPLAY
]

ax4.bar(index, hopper_dt, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax4.bar(index + bar_width, hopper_hdt, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax4.bar(index + bar_width * 2, hopper_dmnor, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax4.bar(index + bar_width * 3, hopper_dm, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax4.bar(index + bar_width * 4, hopper_hdm, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax4.set_title('Hopper')
d_names = ("Exp", "Med", "MedE", "MedR")
ax4.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

kitchen_dt = [
    2.53 / KITCHEN_COMPLETE,
    2.55 / KITCHEN_MIXED,
    3.00 / KITCHEN_PARTIAL
]
kitchen_hdt = [
    2.70 / KITCHEN_COMPLETE,
    2.28 / KITCHEN_MIXED,
    2.42 / KITCHEN_PARTIAL
]
kitchen_dmnor = [
    2.58 / KITCHEN_COMPLETE,
    2.80 / KITCHEN_MIXED,
    3.02 / KITCHEN_PARTIAL
]
kitchen_dm = [
    2.50 / KITCHEN_COMPLETE,
    2.70 / KITCHEN_MIXED,
    3.00 / KITCHEN_PARTIAL
]
kitchen_hdm = [
    2.20 / KITCHEN_COMPLETE,
    2.65 / KITCHEN_MIXED,
    2.55 / KITCHEN_PARTIAL
]
ax5.bar(np.arange(3), kitchen_dt, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width, kitchen_hdt, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 2, kitchen_dmnor, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 3, kitchen_dm, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax5.bar(np.arange(3) + bar_width * 4, kitchen_hdm, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax5.set_title('Kitchen')
d_names = ("Complete", "Mixed", "Partial")
ax5.set_xticks(_3_RANGES, d_names, color='black', fontsize = FONT_SIZE)

maze2d_dt = [
    103.7 / MAZE2D_LARGE,
    33.72 / MAZE2D_MEDIUM,
    17.17 / MAZE2D_OPEN,
    59.3 / MAZE2D_UMAZE
]
maze2d_hdt = [
    34.1 / MAZE2D_LARGE,
    33.72 / MAZE2D_MEDIUM,
    19.08 / MAZE2D_OPEN,
    37.72 / MAZE2D_UMAZE
]
maze2d3_dmnor = [
    79.65 / MAZE2D_LARGE,
    114.1 / MAZE2D_MEDIUM,
    32.33 / MAZE2D_OPEN,
    110.25 / MAZE2D_UMAZE
]
maze2d_dm = [
    69.9 / MAZE2D_LARGE,
    56.3 / MAZE2D_MEDIUM,
    30.2 / MAZE2D_OPEN,
    86.9 / MAZE2D_UMAZE
]
maze2d_hdm = [
    93.7 / MAZE2D_LARGE,
    145.23 / MAZE2D_MEDIUM,
    26.67 / MAZE2D_OPEN,
    31.13 / MAZE2D_UMAZE
]
ax6.bar(index, maze2d_dt, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax6.bar(index + bar_width, maze2d_hdt, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax6.bar(index + bar_width * 2, maze2d3_dmnor, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax6.bar(index + bar_width * 3, maze2d_dm, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax6.bar(index + bar_width * 4, maze2d_hdm, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax6.set_title('Maze2D')
d_names = ("Lar", "Med", "Open", "Umaze")
ax6.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

walker2d_dt = [
    1867.61 / WALKER2D_EXPERT,
    1081.54 / WALKER2D_MEDIUM,
    1883.23 / WALKER2D_MEDIUM_EXPERT,
    1335.64 / WALKER2D_MEDIUM_REPLAY
]
walker2d_hdt = [
    1869.07 / WALKER2D_EXPERT,
    1106.63 / WALKER2D_MEDIUM,
    1153.5 / WALKER2D_MEDIUM_EXPERT,
    1197.66 / WALKER2D_MEDIUM_REPLAY
]
walker2d3_dmnor = [
    1874.51 / WALKER2D_EXPERT,
    1111.94 / WALKER2D_MEDIUM,
    1871.34 / WALKER2D_MEDIUM_EXPERT,
    1310.88 / WALKER2D_MEDIUM_REPLAY
]
walker2d_dm = [
    1866.81 / WALKER2D_EXPERT,
    1008.24 / WALKER2D_MEDIUM,
    1861.45 / WALKER2D_MEDIUM_EXPERT,
    1302.54 / WALKER2D_MEDIUM_REPLAY
]
walker2d_hdm = [
    1861.86 / WALKER2D_EXPERT,
    1093.42 / WALKER2D_MEDIUM,
    1843.48 / WALKER2D_MEDIUM_EXPERT,
    1237.97 / WALKER2D_MEDIUM_REPLAY
]

ax7.bar(index, walker2d_dt, bar_width,
        alpha=opacity,
        color = COLOR_1,

        error_kw = error_config)
ax7.bar(index + bar_width, walker2d_hdt, bar_width,
        alpha=opacity,
        color = COLOR_2,

        error_kw = error_config)
ax7.bar(index + bar_width * 2, walker2d3_dmnor, bar_width,
        alpha=opacity,
        color = COLOR_3,

        error_kw = error_config)
ax7.bar(index + bar_width * 3, walker2d_dm, bar_width,
        alpha=opacity,
        color = COLOR_4,

        error_kw = error_config)
ax7.bar(index + bar_width * 4, walker2d_hdm, bar_width,
        alpha=opacity,
        color = COLOR_5,

        error_kw = error_config)
ax7.set_title('Walker2D')
d_names = ("Exp", "Med", "MedE", "MedR")
ax7.set_xticks(_4_RANGES, d_names, color='black', fontsize = FONT_SIZE)

handles, labels = ax1.get_legend_handles_labels()
plt.legend(handles, labels, loc=(1.1, 0))

# Show
figure = plt.gcf()
figure.set_size_inches(1920/100, 1080/100 * VERTICAL_SCALE)
plt.savefig('all.pdf', dpi=100)
