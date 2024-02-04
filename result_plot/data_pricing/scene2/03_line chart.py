# encoding: utf-8
# Author    : Oasis<2714865936@qq.com>
# Datetime  : 2022/9/5 17:00
# User      : Oasis
# Product   : PyCharm
# Project   : Chart Drawing
# File      : 03_line chart.py
# explain   : 文件说明

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from config import legend_dict, tick_params_dict, color
from config import line_list, marker_list

color_list_use = ["#55AF7B","#EB4537", "#555555", "#4286F3", "#FAC230", "#8DD3AF"]

sns.set_theme(context='paper', style='whitegrid', font_scale=1, color_codes=True, rc=None)
sns.set_style('ticks')
sns.set_style({'xtick.color': 'black','ytick.color': 'black','xtick.bottom': True, 'ytick.left': True,'axes.linewidth': 2.5,})

sns.axes_style()#打印axes信息
sns.plotting_context()#打印绘图基本信息




def plot_line(data, 
              x_axis_name, 
              y_axis_name, 
              save_path,
              save_file,
              line_list=line_list,
              marker_list=marker_list,
              x_axis=None,
              y_axis_list=None,
              color_list=color['series_3'],
              markersize_list=None,
              sheet=None,
              figuresize=(9,6),
              show_grid='y',
              main_linewidth=3.0,
              axis_linewidth=1.0,
              label_fontsize=14,
              title_fontsize=18,
              legend_fontsize=15,
              font_family='Times New Roman',
              right_visible = True,
              left_visible = True,
              top_visible = True,
              bottom_visible = True,
              x_lim=None,
              y_lim=None,
              title_text=None,
              legend_font=legend_dict,
              tick_dict = tick_params_dict,
              xlog=False,
              ylog=False,
              save_format='eps',
              dpi_show=800
              ):
    
    
    '''
    
    data: string, 输入数据路径名或者dataframe
    
    x_axis_name: string,x轴的标签
    y_axis_name: string,y轴的标签
    
    save_path: string,保存文件路径
    save_file: string,保存文件命名
    sheet: string or None,如果读入excel，则指定数据所在的sheet页，否则为默认的第一页
    
    
    line_list: list[str] or None,各条线的样式，有'-','--',':','-.'等，可自定义线型，未指定则全部为实线条
    marker_list: list[str] or None,数据点的样式，未指定则全部为实心圆
    color_list: list[str] or None,每条线的颜色,未指定则全部为共色
    
    x_axis: str or None, x轴的columns列名，为None时，是DataFrame第一列列名
    y_axis_list: list[str] or None, y轴的columns列名，为None时，是DataFrame第2列开始的全部列名
    markersize_list: list[int] or None，每个数据点的大小
    sheet:若输入文件为excel，则需要指定单独的sheet，注意每个sheet数据只能画1张图
    figuresize:tuple(int,int),画布比例
    show_grid:string,显示格线，选项有'x','y','both'
    main_linewidth:float,线宽，默认为3.0
    axis_linewidth:float,轴线宽，默认为1.0
    label_fontsize:int or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}, 标签字体大小
    title_fontsize:float,标题字体大小
    legend_fontsize:float,题注字体大小
    font_family:string,字体，默认为'Times New Roman'
    right_visible:bool,右边框是否可见
    left_visible:bool,左边框是否可见
    top_visible:bool,上边框是否可见
    bottom_visible:bool,下边框是否可见
    x_lim:tuple(float,float),坐标轴显示范围
    y_lim:tuple(float,float),坐标轴显示范围
    title_text:string or None,标题内容
    legend_font:dict,图例字典
    tick_dict:dict,参数字典
    xlog:bool,x轴是否为对数尺度
    ylog:bool,y轴是否为对数尺度
    save_format: string,保存文件格式
    dpi_show: int, 分辨率大小，在非eps格式下默认为800
    '''
    #获取数据
    if data.endswith('.csv') or data.endswith('.txt'):
        data = pd.read_csv(data)
    
    elif data.endwith('xlsx'):
        if sheet is not None:
            data = pd.read_excel(data, sheet_name=sheet)
    
    else:
        if isinstance(data, pd.DataFrame()):
            pass
        else:
            raise ValueError
    
    
    
    x_axis = data.columns[0]
    y_axis_list = data.columns[1:]
    
    if figuresize is not None:
        plt.rcParams['figure.figsize']=figuresize
    
    #默认的figsize(6.0,4.0),分辨率为100,图片尺寸为600&400    
    #设置figsize可以在不改变分辨率与尺寸的情况下改变比例
    #eps不要使用dpi
    if line_list == None:
        line_list = ['-'] * 100
        
    
    if markersize_list == None:
        markersize_list = [1] * 100
        
    ax = sns.lineplot()
    ax.grid(axis=show_grid)
    for i in range(len(y_axis_list)):
        y_axis=y_axis_list[i]
        ax.plot(data[x_axis], 
                data[y_axis],
                label = y_axis, 
                linewidth = main_linewidth, 
                marker=marker_list[i], 
                markersize=markersize_list[i], 
                linestyle=line_list[i], 
                color=color_list[i])
    
    
    #可以自定义markerfacecolor, markeredgecolor, markeredgewidth
    #使用color，marker与linestyle设置曲线格式
    
    #边框是否可见
    if not right_visible:
        ax.spines['right'].set_visible(False) #设置右边框是否可见
    
    if not top_visible:
        ax.spines['top'].set_visible(False) #设置上边框是否可见
        
    if not left_visible:
        ax.spines['left'].set_visible(False) #设置左边框是否可见
        
    if not bottom_visible:
        ax.spines['bottom'].set_visible(False) #设置下边框是否可见
    
    
    
    
    #设定坐标轴宽度
    ax.spines['bottom'].set_linewidth(axis_linewidth)
    ax.spines['left'].set_linewidth(axis_linewidth)
    ax.spines['right'].set_linewidth(axis_linewidth)
    ax.spines['top'].set_linewidth(axis_linewidth)
    #可以使用ax.spines[].set_color设置颜色
    
    
    #设置坐标范围
    if x_lim is not None:
        plt.xlim(x_lim)
        #ax.set_xlim(x_lim[0],x_lim[1])功能相同
    
    if y_lim is not None:
        plt.ylim(y_lim)
        #ax.set_ylim(y_lim[0],y_lim[1])功能相同
    
    
    #设置x轴与y轴标签
    ax.set_xlabel(x_axis_name, fontsize = label_fontsize, fontdict={'family': font_family})
    ax.set_ylabel(y_axis_name, fontsize = label_fontsize, fontdict={'family': font_family})
    
    
    
    
    #设置标题相关项
    if title_text is not None:
        ax.set_title(title_text, fontsize = title_fontsize, fontdict={'family': font_family})
    
    
    #title参数
    #fontsize：默认12，可选参数还有['xx-small', 'x-small', 'small', 'medium', 'large','x-large', 'xx-large']
    #backgroundcolor：背景颜色
    #fontweight：字体粗细，可选参数为['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
    #color：字体颜色
    #fontstyle：设置字体类型，可选参数[ 'normal' | 'italic' | 'oblique' ]，italic斜体，oblique倾斜
    #verticalalignment：设置水平对齐方式 ，可选参数 ： 'center' , 'top' , 'bottom' ,'baseline'
    if xlog:
        plt.xscale('log')
    
    if ylog:
        plt.yscale('log')
    
    
    
    ax.tick_params(colors=tick_params_dict['color'], 
                   labelsize=tick_params_dict['labelsize'], 
                   width=tick_params_dict['width'], 
                   axis=tick_params_dict['axis'])
    #可以通过ax.set_xticks 与ax.set_yticks设置x轴与y轴刻度分布情况
    
    if legend_font is not None:
        ax.legend(loc='best', prop=legend_font)
    else:
        ax.legend(loc='best', fontsize = legend_fontsize, )
    #设置图例标题、图例标题字体大小、图例字体大小
    
    
    plt.tight_layout()
    #去除最终结果的白边
    
    os.makedirs(save_path,exist_ok=True)
    if save_format == 'eps':
        plt.savefig(save_path + save_file + '.eps',format='eps', dpi=dpi_show)
    
    elif save_format == 'svg':
        plt.savefig(save_path + save_file + '.svg',format='svg', dpi=dpi_show)
    
    elif save_format == 'pdf':
        plt.savefig(save_path + save_file + '.pdf')
        
    else:
        plt.savefig(save_path + save_file + '.' + save_format, dpi=dpi_show)
        #后面最好跟plt.show(),否则容易出现空白情况
    #plt.savefig(save_path + save_file + '.tif',dpi=600)#后面最好跟plt.show(),否则容易出现空白情况
    plt.show()

plot_line('plot_total_regret1.csv',
          'Round T',
          'value(%)',
          './figures/',
          'Figure_10_scene2_cumulative_regret', 
          label_fontsize=24,
          legend_fontsize=18,
          color_list=color_list_use,
          main_linewidth=1.5, 
          markersize_list=[3] * 10,
          save_format='tif',)


plot_line('plot_regret_ratio1.csv',
          'Round T',
          'value(%)',
          './figures/',
          'Figure_10_scene2_regret_ratio', 
          xlog=True,
          label_fontsize=24,
          legend_fontsize=18,
          color_list=color_list_use,
          main_linewidth=1.5, 
          markersize_list=[3] * 10,
          save_format='tif',)

plot_line('plot_total_regret1.csv',
          'Round T',
          'value(%)',
          './figures/',
          'Figure_10_scene2_cumulative_regret', 
          label_fontsize=24,
          legend_fontsize=18,
          color_list=color_list_use,
          main_linewidth=1.5, 
          markersize_list=[3] * 10,
          save_format='eps',)


plot_line('plot_regret_ratio1.csv',
          'Round T',
          'value(%)',
          './figures/',
          'Figure_10_scene2_regret_ratio', 
          xlog=True,
          label_fontsize=24,
          legend_fontsize=18,
          color_list=color_list_use,
          main_linewidth=1.5, 
          markersize_list=[3] * 10,
          save_format='eps',)