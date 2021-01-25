#import the necessary libraries:
import os, sys

import pandas as pd 
import numpy as np

import chart_studio.plotly as py 
import cufflinks as cf  
import seaborn as sns
import plotly
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import Scatter, Box
import matplotlib.pyplot as plt
import psutil
import kaleido
# import orca

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

directorio = os.path.dirname(__file__)
for i in range(3):
    directorio = os.path.dirname(directorio)
sys.path.append(directorio)

def get_root_path(N):
    """
    This function gets the root path of a directory to make it reusable for every computer.
    N represents the amount of iterations needed to get the relative path
    """
    path = os.getcwd()
    for i in range(N):
        path = os.getcwd()
        path = os.path.dirname(path)
    sys.path.append(path)

get_root_path(N=3)

#---
'''
#TODO @leosanchezsoler & @Rmolleda
'''
#---
class Plotly_Plot():
    '''
    Father/Mother class

                        ---what it does---
    This class is created with the purpose of visualizing any kind of plot from a Dataframe.
    By working with this class, the program will execute the desired plot just by introducing the desired
    columns.

    Plotly is the only library used on it.
    '''
    def __init__(self, df, x_axis: str, y_axis: str, x_label: str, y_label: str, title: str, color: str, filename: str, z_axis=None, z_label=None, animation_frame=None, animation_group=None, size=None, hover_name=None):
        '''
        df: a pandas.DataFrame with the desired queries.
        x_axis: a string that indicates the values in x axis
        y_axis: a string that indicates the values in y axis
        x_label: a string with x label
        y_label: a string with y label
        title: a string with the plot title
        color: a string with the color value
        filename: a string with the name of the file
        '''
        self.df = df
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.color = color
        self.filename = filename
        ##############
        '''
        These 3 attributes are only used for the motion plots
        animation_frame: the value which will be on the bottom slider
        animation_group: the values which will be grouped in the plot
        size: the values than will delimit the size of the plot
        '''

    def Scatterplot(self):
        '''
        Draws a Scatter plot
        '''
        
        myplot = px.scatter(data_frame=self.df,
            x=self.x_axis,
            y=self.y_axis,
            color=self.color, title=self.title, labels={self.x_axis : self.x_label, self.y_axis :self.y_label})
            
        myplot.update_layout(
                xaxis=dict(showline=True, showgrid=True, showticklabels=True,tickfont=dict(family='Helvetica', size=12)),
                yaxis=dict(showline=True, showticklabels=True, showgrid=True,tickfont=dict(family='Helvetica', size= 12))
            )

        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')
        #myplot.write_image(str(directorio)+ '/group_eda/documentation/static/' + self.filename + '.png')

      
    def Lineplot(self):
        '''
        Draws a Line plot
        '''
        myplot = px.line(data_frame=self.df,
            x=self.x_axis,
            y=self.y_axis,
            color=self.color, title=self.title, labels={self.x_axis : self.x_label, self.y_axis : self.y_label})

        myplot.update_layout(
                xaxis=dict(showline=True, showgrid=True, showticklabels=True, tickfont=dict(family='Helvetica', size=12)),
                    yaxis=dict(showline=True, showticklabels=True, showgrid=True, tickfont=dict(family='Helvetica', size= 12))
            )
        
        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')
    


    def Boxplot(self):
        '''
        Draws a Box plot
        '''

        myplot = px.box(data_frame=self.df,
            x=self.x_axis,
            y=self.y_axis,
            color=self.color, title=self.title, labels={self.x_axis : self.x_label, self.y_axis : self.y_label},
            points='all',
            )
        myplot.update_layout(
                xaxis=dict(showline=True, showgrid=True, showticklabels=True, tickfont=dict(family='Helvetica', size=12)),
                    yaxis=dict(showline=True, showticklabels=True, showgrid=True, tickfont=dict(family='Helvetica', size= 12))
            )

        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')

            
    def Barplot(self):
        '''
        Draws a Bar plot
        '''
        myplot = px.bar(data_frame=self.df,
            x=self.x_axis,
            y=self.y_axis,
            color=self.color, title=self.title, labels={self.x_axis : self.x_label, self.y_axis : self.y_label})

        myplot.update_layout(
                xaxis=dict(showline=True, showgrid=True, showticklabels=True,tickfont=dict(family='Helvetica', size=12)),
                yaxis=dict(showline=True, showticklabels=True, showgrid=True,tickfont=dict(family='Helvetica', size= 12))
            )

        myplot.update_traces(textposition='outside')

        #Sets fontsizes
        myplot.update_layout(uniformtext_minsize=8)
        #sets the angle of xaxis. In this case, countries
        myplot.update_layout(xaxis_tickangle=-45)
        
        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')

        #myplot.write_image(str(directorio)+ '/group_eda/documentation/static/' + self.filename + '.png')


    def Piechart(self):
        '''
        Draws a Piechart
        In this case, write 
        '''
        myplot = px.pie(data_frame=self.df,
            values=self.x_axis,
            names=self.y_axis,
            color=self.color, title=self.title, 
            labels={self.x_axis : self.x_label, self.y_axis : self.y_label})

        #myplot.update_layout(
        #         xaxis=dict(showline=True, showgrid=True, showticklabels=True,tickfont=dict(family='Helvetica', size=12)),
        #             yaxis=dict(showline=True, showticklabels=True, showgrid=True,tickfont=dict(family='Helvetica', size= 12))
        #     )
        
        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')

        #myplot.write_image(str(directorio)+ '/group_eda/documentation/static/' + self.filename + '.png')
    def Scatter3D(self):
        '''
        Draws a 3D Scatter plot by introducing 3 parameters.
        It can be useful to draw tendencies from a specific amount of time with further detail.
        For example, showing how population has changed through years in a country with the monthly record in the
        z_axis
        '''


        myplot = px.scatter_3d(data_frame=self.df, x=self.x_axis, y=self.y_axis, labels={self.x_axis :self.x_label, self.y_axis : self.y_label, self.z_axis: self.z_label})

        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')

        #myplot.write_image(str(directorio)+ '/group_eda/documentation/static/' + self.filename + '.png')

    def Line3D(self):
        '''
        Draws a 3D Line plot by introducing 3 parameters.
        '''
        myplot = px.line_3d(data_frame=self.df, x=self.x_axis, y=self.y_axis, labels={self.x_axis : self.x_label, self.y_axis : self.y_label, self.z_axis: self.z_label})

        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')

        #myplot.write_image(str(directorio)+ '/group_eda/documentation/static/' + self.filename + '.png')

    def MotionScatter(self):
        '''
        Displays a Scatter plot with a slider on the bottom to show progressions/tendencies with motion
        '''

        myplot = px.scatter(data_frame=self.df, x= self.x_axis, y=self.y_axis,
        animation_frame=self.animation_frame, animation_group=self.animation_group,
            size=self.size, color=self.color, hover_name=self.hover_name,
            log_x=True, size_max=55, range_x=[100, 100000],
            range_y=[25, 90])
        
        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')

        #myplot.write_image(str(directorio)+ '/group_eda/documentation/static/' + self.filename + '.png')

    def MotionBar(self):
        '''
        Displays a Bar plot with a slider on the bottom to show progressions/tendencies with motion
        '''
        myplot = px.bar(data_frame=self.df, x= self.x_axis, y=self.y_axis,
        animation_frame=self.animation_frame, animation_group=self.animation_group,
            size=self.size, color=self.color, hover_name=self.hover_name,
            log_x=True, size_max=55,
            range_y=[0, 100000000])

        myplot.write_html(str(directorio)+ '/group_eda/documentation/html/' + self.filename + '.html')

        #myplot.write_image(str(directorio)+ '/group_eda/documentation/static/' + self.filename + '.png')
