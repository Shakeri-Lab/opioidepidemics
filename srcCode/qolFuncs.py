# ------------------QoL functions------------------#

# modules to import
import numpy as np
import shapely.geometry
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
from plotly.subplots import make_subplots
#from dash import Input, Output, State, dcc, html, callback
#import dash_bootstrap_components as dbc

import srcCode.qolDescs as qd

# Mapbox settings
mapbox_token_public = "pk.eyJ1IjoiZXZhbi10bSIsImEiOiJjbDFlYTlncTMwM2J3M2RwbDdjaXc2bW02In0.cxB8jf_1CFeoeVUAuOsYuA"
mapbox_style = "mapbox://styles/evan-tm/cl1ik4lmv003z15ru0ip4isbz"

# VDH OD death data
vdh = pd.read_csv('data/VDH.csv')
# CDC Opioid dispensing data
vaDispense = pd.read_csv('data/vaDispense.csv', dtype={'County FIPS Code': str})
# Geography file
vaGeo = gpd.read_file('data/vaGeo.geojson')
# National prescription and OD death data
nationalData = pd.read_csv('data/nationalData.csv')

# Setting correct geoid type
vaGeo['geoid'] = vaGeo['geoid'].astype(int)

## Returns a plot of the death rates for all opioids in VA
## in: data from VDH, year to plot, drug class
## out: figure representing the data
def plotVDHMap(drug_class, codes = None):
    plotData = vdh[vdh['Drug Class'] == drug_class].copy()
    plotData.rename(columns={'Year of Death':'Year'}, inplace=True)
    if codes:
        plotData = plotData[plotData['Locality'].isin(codes)]
    plotData = plotData[plotData['Death Rate'] != '*']
    plotData['Death Rate'] = plotData['Death Rate'].astype(float)
    plotData = plotData.sort_values('Year')
    # vdh chloropleth
    fig = px.choropleth_mapbox(plotData, 
                               geojson = vaGeo.set_index('geoid').geometry, 
                               animation_frame=plotData.Year,
                               locations = plotData.Locality,
                               color = plotData['Death Rate'],
                               center={"lat": 37.926868, "lon": -78.024902},
                               zoom=6, opacity = 1, 
                               color_continuous_scale='Oranges',
                               range_color=[0.0,45.0])
    fig.update_layout(mapbox_accesstoken=mapbox_token_public, 
                    mapbox_style='light',
                    margin=go.layout.Margin(l=0, r=0,  b=0, t=0),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    autosize=True,
                    font={'size': 16, 'color': "rgb(0,0,0)"})
    #fig.update_traces(hovertemplate=None, hoverinfo = 'skip')
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig["layout"].pop("updatemenus")

    return fig

def plotCDCMap(codes = None):
    global vaDispense

    if codes:
        vaDispense = vaDispense[vaDispense['County FIPS Code'].isin(codes)]
    vaDispense = vaDispense[vaDispense['Opioid Dispensing Rate per 100'] != '–']
    vaDispense['Opioid Dispensing Rate per 100'] = vaDispense['Opioid Dispensing Rate per 100'].astype(float)
    # vdh chloropleth
    fig = px.choropleth_mapbox(vaDispense,
                               geojson = vaGeo.set_index('geoid').geometry,
                               animation_frame = vaDispense.Year,
                               locations = vaDispense['County FIPS Code'],
                               color = vaDispense['Opioid Dispensing Rate per 100'],
                               center={"lat": 37.926868, "lon": -78.024902},
                               zoom=6, opacity = 1,
                               color_continuous_scale='Blues',
                               range_color=[0.0,600.0])
    fig.update_layout(mapbox_accesstoken=mapbox_token_public,
                    mapbox_style='light',
                    margin=go.layout.Margin(l=0, r=0,  b=0, t=0),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    autosize=True,
                    font={'size': 16, 'color': "rgb(0,0,0)"})
    #fig.update_traces(hovertemplate=None, hoverinfo = 'skip')
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig["layout"].pop("updatemenus")

    return fig


def plotUSALineplots():

    global nationalData
    fig = make_subplots(rows=1, cols=2, subplot_titles=['National Opioid Dispensing Rate Per 100 Persons',
                                                        'National Opioid Overdose Deaths Per 100,000 Persons'])
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['Opioid Dispensing Rate Per 100 Persons'],
                mode='lines+markers', name='Dispensing Rate', line=dict(color='blue', width=4)),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['AnyOpioidRate'], 
                mode='lines+markers', name='Any Opioids', line=dict(color='red', width=4)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['HeroinRate'], 
                mode='lines+markers', name='Heroin', line=dict(color='black', width=4)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['NatSemiSynthRate'], 
                mode='lines+markers', name='Natural or Semisynthetic', 
                line=dict(color='green', width=4)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['MethadoneRate'], 
                mode='lines+markers', name='Methadone', line=dict(color='purple', width=4)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['SyntheticRate'], 
                mode='lines+markers', name='Other Synthetic',
                line=dict(color='darkgray', width=4)),
        row=1, col=2
    )
    fig.update_layout(plot_bgcolor = "#e8eaab")
    return fig