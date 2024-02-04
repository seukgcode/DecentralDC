# encoding: utf-8
# Author    : Oasis<2714865936@qq.com>
# Datetime  : 2022/9/7 17:01
# User      : Oasis
# Product   : PyCharm
# Project   : Chart Drawing
# File      : config.py
# explain   : 文件说明

color = dict(
    dark=[],
    light=[],
    origin=[],
    series_1=['#2878B5', '#3D4856', '#A0ACBD', '#926D31', '#CAA062'],
    series_2=['red', 'blue', 'green'],
    series_3=['#8ECFC9', '#FFBE7A', '#FA7F6F', '#82B0D2', '#BEB8DC', '#E7DAD2']
)

font = dict(
    fontsize=16,
    color='black',
    family='Times New Roman',
    weight='light',  # light | normal |bold
    style='italic',
)


legend_dict = dict(
    family='Times New Roman',
    weight='normal',  # light | normal | medium | semibold | bold | heavy | black
    style='normal', # normal | italic | oblique
    size='large',  #'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'
)



tick_params_dict = dict(
    axis='both',
    direction='out',
    color='black',
    labelsize=16,
    width=2.0,
)


line_list = ['-','--',':','-.',(0,(1,1)),(0,(1,5))]
marker_list = ['o','s','d','x','*','^']
size_list = [12] * 10


#tick_params()函数

##借用函数tick_params()可以装修轴上的刻度线和轴标签
#ax.tick_params()
###看一下此函数的一些重要参数
#axis: 可选"x","y","both",默认"both"，分别代表，对x轴操作，对y轴操作，对两个轴都操作。
#direction: 可选 "in","out","inout"代表，刻度线显示在坐标轴里面，坐标轴外边，双边

#length: 刻度线长度
#color: 刻度线颜色
#width： 刻度线宽度
#pad： 刻度线与刻度标签之间的间隔
#bottom, top, left, right四个参数对应四个边框，它们的取值为布尔类型，True 表示显示对应边框上的刻度线，False，代表不显示，默认True
#labelbottom, labeltop, labelleft, labelright,与上面四个对应，代表的是四个边框上的类标的设置，取值为布尔类型，True代表显示对应边框上的类标，False代表不显示。
#labelsize：类标大小的设置参数，可取浮点型数值，也可去"medium","large","small"
#labelrotation：旋转类标一定的角度，与在set_xticklabels()中的参数rotation作用相同。