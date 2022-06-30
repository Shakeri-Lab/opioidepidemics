# ------------------QoL functions------------------#

# modules to import
import numpy as np
import shapely.geometry
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
#from dash import Input, Output, State, dcc, html, callback
#import dash_bootstrap_components as dbc

import srcCode.qolDescs as qd



mapbox_token_public = "pk.eyJ1IjoiZXZhbi10bSIsImEiOiJjbDFlYTlncTMwM2J3M2RwbDdjaXc2bW02In0.cxB8jf_1CFeoeVUAuOsYuA"
mapbox_style = "mapbox://styles/evan-tm/cl1ik4lmv003z15ru0ip4isbz"

vdh = pd.read_csv('data/VDH.csv')
vaDispense = pd.read_csv('data/vaDispense.csv', dtype={'County FIPS Code': str})
vaGeo = gpd.read_file('data/vaGeo.geojson')

vaGeo['geoid'] = vaGeo['geoid'].astype(int)

## Returns a plot of the death rates for all opioids in VA
## in: data from VDH, year to plot, drug class
## out: figure representing the data
def plotVDHMap(year, drug_class, codes = None):
    plotData = vdh.loc[(vdh['Year of Death'] == year) & 
                       (vdh['Drug Class'] == drug_class)]
    if codes:
        plotData = plotData[plotData['Locality'].isin(codes)]
    plotData = plotData[plotData['Death Rate'] != '*']
    plotData['Death Rate'] = plotData['Death Rate'].astype(float)
    # vdh chloropleth
    fig = px.choropleth_mapbox(plotData, 
                               geojson = vaGeo.set_index('geoid').geometry, 
                               locations = plotData.Locality,
                               color = plotData['Death Rate'],
                               center={"lat": 37.926868, "lon": -78.024902},
                               zoom=6, opacity = 1, 
                               color_continuous_scale='Oranges')
    fig.update_layout(mapbox_accesstoken=mapbox_token_public, 
                    mapbox_style='light',
                    margin=go.layout.Margin(l=0, r=0,  b=0, t=0),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    autosize=True,
                    font={'size': 16, 'color': "rgb(255,255,255)"})
    #fig.update_traces(hovertemplate=None, hoverinfo = 'skip')
    fig.update_yaxes(scaleanchor="x", scaleratio=1)

    return fig
def plotCDCMap(year, codes = None):
    plotData = vaDispense.loc[(vaDispense['Year'] == year)]
    if codes:
        plotData = plotData[plotData['County FIPS Code'].isin(codes)]
    plotData = plotData[plotData['Opioid Dispensing Rate per 100'] != '–']
    plotData['Opioid Dispensing Rate per 100'] = plotData['Opioid Dispensing Rate per 100'].astype(float)
    # vdh chloropleth
    fig = px.choropleth_mapbox(plotData,
                               geojson = vaGeo.set_index('geoid').geometry,
                               locations = plotData['County FIPS Code'],
                               color = plotData['Opioid Dispensing Rate per 100'],
                               center={"lat": 37.926868, "lon": -78.024902},
                               zoom=6, opacity = 1,
                               color_continuous_scale='Blues')
    fig.update_layout(mapbox_accesstoken=mapbox_token_public,
                    mapbox_style='light',
                    margin=go.layout.Margin(l=0, r=0,  b=0, t=0),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    autosize=True,
                    font={'size': 16, 'color': "rgb(0,0,0)"})
    #fig.update_traces(hovertemplate=None, hoverinfo = 'skip')
    fig.update_yaxes(scaleanchor="x", scaleratio=1)

    return fig
